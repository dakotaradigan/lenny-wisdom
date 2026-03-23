---
name: lenny-frameworks
description: Browse and explore named product frameworks from Lenny's podcast and newsletter. Use when the user asks about "frameworks", "models", "playbooks", or wants to find the right framework for a situation.
---

# Lenny Frameworks

Browse and explore 55 named product frameworks from Lenny's podcast and newsletter, organized by category.

## Instructions

### Browsing Mode

When the user says "show me frameworks" or wants to browse:

1. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/frameworks.md`
2. Present the categories with framework counts:

   **Growth** (12 frameworks) — North Star Metric, Racecar Growth, Adjacent User Theory...
   **Strategy** (10) — DHM Model, Positioning, JTBD, PR/FAQ...
   **Prioritization** (5) — LNO, RICE, ICE, Opportunity Solution Tree...
   **Product-Market Fit** (2) — Sean Ellis Test, Superhuman PMF Engine
   **Leadership** (6) — Radical Candor, Give Away Your Legos, Magic Loop...
   **Decision-Making** (5) — Pre-mortem, One-Way/Two-Way Doors, Five Whys...
   **Communication** (4) — Concentric Circles, What/So What/Now What...
   **Pricing** (3) — Willingness to Pay, Leaders/Fillers/Killers...
   **Execution** (5) — OKRs, Shape Up, DORA Metrics...
   **Productivity** (3) — Indistractable, 10-Minute Rule, Timeboxing...

3. Ask: "Which category interests you? Or describe your situation and I'll recommend the right frameworks."

### Search Mode

When the user describes a situation (e.g., "I need to prioritize my roadmap"):

1. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/frameworks.md`
2. Identify the 2-4 most relevant frameworks for their situation
3. For each, share:
   - Framework name and source guest
   - How it works (key steps)
   - How it applies to their specific situation
4. Ask: "Want me to walk you through applying one of these?"

### Deep Dive Mode

When the user asks about a specific framework:

1. Find it in `${CLAUDE_PLUGIN_ROOT}/knowledge/frameworks.md`
2. Share the full description, steps, and when to use it
3. Read the source guest's profile from `${CLAUDE_PLUGIN_ROOT}/knowledge/guests/` for additional context
4. Offer: "Want to see how this framework applies to your current situation? Try `/lenny-wwld` with your specific challenge."
