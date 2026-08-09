---
name: lenny-graph
description: Explore connections in Lenny's Guest Graph — how guests, topics, frameworks, and companies relate. Use when the user asks "who's connected to", "which guests worked at", "who else covers this topic", or wants to navigate the knowledge base by relationships.
---

# Lenny's Guest Graph

Navigate the knowledge base as a graph: guests, topics, frameworks, and the companies that connect them.

## Data

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/graph.json`. It contains:

- **nodes** — `id` (e.g. `guest:shreyas-doshi`, `topic:product-strategy`, `framework:lno-framework`, `company:stripe`), `type`, `name`, and `file` (the knowledge-base file to open for detail)
- **edges** — `source`, `target`, `kind` (`topic-guest`, `topic-framework`, `framework-guest`, `guest-company`)

Guest frontmatter also carries `topics:` backlinks, and topic frontmatter carries `related_guests` / `related_frameworks` — use whichever direction is cheaper for the question.

## Instructions

### Answering connection questions

1. Read `graph.json` and collect the edges touching the entity in question
2. Group connections by type (topics, frameworks, companies, guests one hop away)
3. Present the neighborhood conversationally, not as a data dump — lead with the most interesting connections
4. For any node the user wants to go deeper on, open its `file` from the knowledge base

Typical questions this answers:

- "Which guests worked at Stripe?" — edges from `company:stripe`
- "Who else covers pricing?" — neighbors of `topic:pricing-and-monetization`
- "How are Shreyas Doshi and Annie Duke connected?" — find shared neighbors (both link to `topic:systems-thinking-and-mental-models` and the Pre-mortem framework)
- "Which frameworks came out of Netflix alumni?" — guests with a `company:netflix` edge, then their `framework-guest` edges

### Two-hop paths

For "how is X related to Y" questions, look for shared neighbors first (same topic, same company, same framework). If none, walk one more hop and narrate the path: "Shreyas and Kim Scott don't overlap directly, but both connect to Leadership & Management through..."

### Suggesting the visual

When a question is really about the big picture ("show me the whole graph", "what does the knowledge base look like"), point the user at the interactive version: `docs/index.html` in this repo, or the GitHub Pages site if published.

### Handing off

When the user lands on a guest or framework they want to actually use:
- "Want [Guest]'s full perspective on your question? Try `/lenny-ask-guest`."
- "Want to hear several of these connected guests debate it? Try `/lenny-panel`."
