---
name: lenny-graph
description: Route a brainstorm or problem through Lenny's Guest Graph to find the right experts, frameworks, and debates. Use when the user wants "feedback from the best", "who should weigh in on this", "who's thought about this problem", has a half-formed idea to pressure-test — or asks a pure connection question like "which guests worked at Stripe".
---

# Lenny's Guest Graph

You have a map of 289 of the industry's finest operators — who knows what, which frameworks they coined, where they worked, and how they connect. The main event: take the user's brainstorm and route it to the right minds.

## Data

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/graph.json`:

- **nodes** — `id` (`guest:shreyas-doshi`, `topic:product-strategy`, `framework:lno-framework`, `company:stripe`), `type`, `name`, and `file` (the knowledge-base file to open for detail)
- **edges** — `source`, `target`, `kind` (`topic-guest`, `topic-guest-inferred`, `topic-framework`, `framework-guest`, `guest-company`)

Guest frontmatter carries `topics:` backlinks; topic frontmatter carries `related_guests` / `related_frameworks`. Curated `topic-guest` edges outrank `topic-guest-inferred` ones when choosing voices.

## The main event: route a brainstorm

When the user brings an idea, problem, or half-formed thought ("I'm thinking about usage-based pricing for our AI feature", "should we kill our free tier?"):

1. **Map it to topic areas.** Read the graph and identify the 1-3 topics the problem actually lives in — including the non-obvious one (a pricing question is often a positioning question).
2. **Assemble the voices.** Walk the topic edges to the guests around those topics. Pick 4-7, preferring curated edges, spanning *different vantage points* — an operator who lived it, a specialist who coined the framework, someone from a company facing the same shape of problem (use `guest-company` edges for this: "three of these voices scaled pricing at PLG companies").
3. **Pull the instruments.** Surface the 2-4 frameworks connected to those topics/guests that would pressure-test the idea, each credited to its source guest.
4. **Name the tension.** Find at least one pair of selected guests who would likely pull in opposite directions, and say why. The disagreement is where the user's context matters most — lead with it, not with consensus.
5. **Brief, then hand off.** Present this as a short briefing: *who to hear from and why, what to pressure-test with, where the experts split.* Then offer the next move:
   - "Want to hear them actually debate it? `/lenny-panel`"
   - "Want one voice in depth? `/lenny-ask-guest`"
   - "Want to think it through Socratically first? `/lenny-wwld`"

Keep the briefing conversational — the graph is the scout, not the show. Open a guest's `file` only when the user drills into that voice.

## Also supported: connection questions

The graph answers direct lookups too — treat these as quick, factual, and secondary:

- "Which guests worked at Stripe?" — edges from `company:stripe`
- "How are Shreyas Doshi and Annie Duke connected?" — shared neighbors first (same topic, company, or framework); if none, walk one more hop and narrate the path
- "Which frameworks came from Netflix alumni?" — `company:netflix` guests, then their `framework-guest` edges

## The visual

For big-picture questions ("show me the whole graph"), point at the interactive version: `docs/index.html` in this repo, or the GitHub Pages site if published.
