#!/usr/bin/env python3
"""Build knowledge/graph.json from the knowledge base frontmatter.

Nodes: guests, topics, frameworks, companies (companies with 2+ guests only).
Edges: topic-guest, topic-framework, framework-guest (source), guest-company.

Also writes `topics:` backlinks into guest frontmatter so the graph is
navigable from the files themselves (inverse of each topic's related_guests).

Run from the repo root: python3 scripts/build_graph.py
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
GUESTS_DIR = KNOWLEDGE / "guests"
TOPICS_DIR = KNOWLEDGE / "topics"
FRAMEWORKS_MD = KNOWLEDGE / "frameworks.md"
OUT = KNOWLEDGE / "graph.json"

# Companies must have at least this many guests to become a node.
COMPANY_MIN_GUESTS = 2


def parse_frontmatter(text):
    """Parse simple single-line YAML frontmatter (scalars and inline lists)."""
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if not m:
            continue
        key, raw = m.group(1), m.group(2).strip()
        if raw.startswith("["):
            inner = raw[1:-1]
            if '"' in inner or "'" in inner:
                items = re.findall(r'"([^"]+)"|\'([^\']+)\'', inner)
                fields[key] = [a or b for a, b in items]
            else:
                fields[key] = [s.strip() for s in inner.split(",") if s.strip()]
        else:
            fields[key] = raw.strip("\"'")
    return fields


def norm_name(name):
    """Normalize a person/framework name for fuzzy matching."""
    name = unicodedata.normalize("NFKD", name)
    name = "".join(c for c in name if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def norm_company(name):
    return re.sub(r"\s+", " ", name.strip())


def load_guests():
    guests = {}
    for path in sorted(GUESTS_DIR.glob("*.md")):
        fm = parse_frontmatter(path.read_text())
        slug = path.stem
        guests[slug] = {
            "slug": slug,
            "name": fm.get("name", slug.replace("-", " ").title()),
            "description": fm.get("description", ""),
            "companies": [norm_company(c) for c in fm.get("companies", [])],
            "panel": fm.get("panel", "false") in ("true", True),
        }
    return guests


def load_topics():
    topics = {}
    for path in sorted(TOPICS_DIR.glob("*.md")):
        fm = parse_frontmatter(path.read_text())
        slug = path.stem
        topics[slug] = {
            "slug": slug,
            "name": fm.get("name", slug.replace("-", " ").title()),
            "related_guests": fm.get("related_guests", []),
            "related_frameworks": fm.get("related_frameworks", []),
        }
    return topics


def load_frameworks():
    """Parse frameworks.md: ## Category, ### Name, **Source:** line."""
    frameworks = []
    category = None
    current = None
    for line in FRAMEWORKS_MD.read_text().splitlines():
        if line.startswith("## ") and not line.startswith("### "):
            category = line[3:].strip()
        elif line.startswith("### "):
            current = {"name": line[4:].strip(), "category": category, "source": ""}
            frameworks.append(current)
        elif line.startswith("**Source:**") and current is not None:
            current["source"] = line[len("**Source:**"):].strip()
    return frameworks


def match_framework(name, frameworks_by_norm):
    """Match a topic's related_framework name against frameworks.md entries."""
    n = norm_name(name)
    if n in frameworks_by_norm:
        return frameworks_by_norm[n]
    # Prefix match either direction handles "Sean Ellis PMF Test (40% Rule)"
    for fn, slug in frameworks_by_norm.items():
        if fn.startswith(n) or n.startswith(fn):
            return slug
    # Distinctive-token fallback: "DORA Four Keys" -> "DORA Metrics",
    # "ICE Prioritization" -> "ICE Scoring". Only when the leading token
    # appears in exactly one framework name.
    lead = n.split()[0] if n else ""
    if len(lead) >= 3:
        hits = [slug for fn, slug in frameworks_by_norm.items()
                if lead in fn.split()]
        if len(hits) == 1:
            return hits[0]
    return None


def source_guests(source, guest_names):
    """Best-effort extraction of guest slugs from a framework Source line."""
    # Drop parentheticals ("(Netflix, Chegg)"), then split on separators.
    cleaned = re.sub(r"\([^)]*\)", "", source)
    matches = []
    for part in re.split(r"[/&,]| and ", cleaned):
        n = norm_name(part)
        if n in guest_names:
            matches.append(guest_names[n])
    return matches


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def write_topic_backlinks(guest_topics):
    """Insert/replace a `topics:` field in guest frontmatter."""
    updated = 0
    for slug, topic_slugs in sorted(guest_topics.items()):
        path = GUESTS_DIR / f"{slug}.md"
        text = path.read_text()
        line = "topics: [" + ", ".join(f'"{t}"' for t in sorted(topic_slugs)) + "]"
        if re.search(r"^topics:.*$", text, re.MULTILINE):
            new = re.sub(r"^topics:.*$", line, text, count=1, flags=re.MULTILINE)
        else:
            # Insert before the closing --- of the frontmatter.
            new = re.sub(r"\n---\n", f"\n{line}\n---\n", text, count=1)
        if new != text:
            path.write_text(new)
            updated += 1
    return updated


def main():
    guests = load_guests()
    topics = load_topics()
    frameworks = load_frameworks()

    guest_names = {norm_name(g["name"]): slug for slug, g in guests.items()}
    frameworks_by_norm = {}
    for fw in frameworks:
        fw["slug"] = slugify(fw["name"])
        frameworks_by_norm[norm_name(fw["name"])] = fw["slug"]

    nodes, edges, warnings = [], [], []
    seen_edges = set()

    def add_edge(source, target, kind):
        key = (source, target, kind)
        if key not in seen_edges:
            seen_edges.add(key)
            edges.append({"source": source, "target": target, "kind": kind})

    for slug, g in guests.items():
        nodes.append({
            "id": f"guest:{slug}", "type": "guest", "name": g["name"],
            "file": f"knowledge/guests/{slug}.md", "panel": g["panel"],
        })
    for slug, t in topics.items():
        nodes.append({
            "id": f"topic:{slug}", "type": "topic", "name": t["name"],
            "file": f"knowledge/topics/{slug}.md",
        })
    for fw in frameworks:
        nodes.append({
            "id": f"framework:{fw['slug']}", "type": "framework",
            "name": fw["name"], "category": fw["category"],
            "file": "knowledge/frameworks.md",
        })

    # Topic -> guest and topic -> framework edges.
    guest_topics = {}
    for slug, t in topics.items():
        for g in t["related_guests"]:
            if g in guests:
                add_edge(f"topic:{slug}", f"guest:{g}", "topic-guest")
                guest_topics.setdefault(g, set()).add(slug)
            else:
                warnings.append(f"topic {slug}: unknown guest slug '{g}'")
        for fname in t["related_frameworks"]:
            fslug = match_framework(fname, frameworks_by_norm)
            if fslug:
                add_edge(f"topic:{slug}", f"framework:{fslug}", "topic-framework")
            else:
                warnings.append(f"topic {slug}: unmatched framework '{fname}'")

    # Framework -> source guest edges.
    for fw in frameworks:
        for gslug in source_guests(fw["source"], guest_names):
            add_edge(f"framework:{fw['slug']}", f"guest:{gslug}", "framework-guest")

    # Guest -> company edges (companies with enough guests to be interesting).
    company_guests = {}
    for slug, g in guests.items():
        for c in g["companies"]:
            company_guests.setdefault(c, []).append(slug)
    for company, gslugs in sorted(company_guests.items()):
        if len(gslugs) < COMPANY_MIN_GUESTS:
            continue
        cid = f"company:{slugify(company)}"
        nodes.append({"id": cid, "type": "company", "name": company})
        for gslug in gslugs:
            add_edge(cid, f"guest:{gslug}", "guest-company")

    graph = {
        "meta": {
            "counts": {
                "guests": len(guests), "topics": len(topics),
                "frameworks": len(frameworks),
                "companies": sum(1 for n in nodes if n["type"] == "company"),
                "edges": len(edges),
            },
        },
        "nodes": nodes,
        "edges": edges,
    }
    OUT.write_text(json.dumps(graph, indent=1) + "\n")

    # Mirror the data into docs/ as a JS global so the GitHub Pages viz
    # works without fetch() (file:// safe) and without reaching knowledge/.
    docs = ROOT / "docs"
    docs.mkdir(exist_ok=True)
    (docs / "graph-data.js").write_text(
        "window.GRAPH = " + json.dumps(graph) + ";\n")

    updated = write_topic_backlinks(guest_topics)

    print(f"graph.json: {len(nodes)} nodes, {len(edges)} edges "
          f"({graph['meta']['counts']})")
    print(f"guest frontmatter backlinks written: {updated}")
    if warnings:
        print(f"\n{len(warnings)} warnings:", file=sys.stderr)
        for w in warnings:
            print(f"  - {w}", file=sys.stderr)


if __name__ == "__main__":
    main()
