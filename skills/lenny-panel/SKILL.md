---
name: lenny-panel
description: Assemble a panel of relevant experts from Lenny's top 50 guests to debate your question, showing where they converge and diverge. Use when the user wants "multiple perspectives", "expert panel", or "what do the experts think".
---

# Expert Panel

Assemble a panel of Lenny's most insightful guests to weigh in on your question, showing where they agree and where they disagree.

## Instructions

### Step 1: Understand the Question

If the user's question is vague, ask one clarifying question before assembling the panel.

### Step 2: Find Relevant Panelists

1. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/guest-index.md`
2. Filter to rows where `Panel` = `yes` (top ~50 curated guests)
3. Match relevant panelists by scanning the Expertise column against the user's question
4. Select the most relevant subset (organically sized — typically 5-10 guests)

### Step 3: Present the Panel

For each panelist, show:
- **Name** and brief role/company context (1 line)
- Why they're on this panel (what expertise they bring)

Ask: "Want to adjust the panel, or shall we dive in?"

### Step 4: Present Perspectives

Open only the matched guest profile files from `${CLAUDE_PLUGIN_ROOT}/knowledge/guests/`.

Present the panel discussion in two sections:

**CONVERGENCE** — Where the panelists agree:
- Identify 2-4 points of consensus across the panel
- Attribute each point to the guests who hold that view
- These represent high-confidence signals

**DIVERGENCE** — Where the panelists disagree:
- Identify 2-3 points of meaningful disagreement
- Frame each as "[Guest A] vs [Guest B]" with their respective positions
- Explain WHY they diverge (different contexts, different priorities)
- These are where the user's specific context matters most

### Step 5: Engage the User

Ask: "Which perspective resonates most with your situation? Or which disagreement do you want to explore?"

When the user drills into a divergence:
- Expand on both sides with more detail from each guest's profile
- Ask probing questions to help the user figure out which side applies to them
- Don't pick a winner — help the user decide based on their context

### Step 6: Offer Expansion

After the core discussion:
"Want to hear from anyone else? [X] more panel guests have expertise in this area."

List the remaining panel-eligible guests who matched but weren't included in the initial panel.

For detailed panel synthesis patterns, see [panel-flow-reference.md](panel-flow-reference.md).
