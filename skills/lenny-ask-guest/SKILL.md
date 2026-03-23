---
name: lenny-ask-guest
description: Get a specific podcast guest's perspective on your question. Use when the user asks "what would [guest] say", "ask Shreyas about", or wants a named expert's viewpoint.
---

# Ask a Guest

Route your question to a specific Lenny podcast guest and get their perspective based on their frameworks, ideas, and philosophy.

## Instructions

### Step 1: Identify the Guest

Parse the user's request for a guest name. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/guest-index.md` and search the Guest column.

**If exact match found:** Open that guest's profile file.

**If no exact match but close matches exist (fuzzy matching):**
- Try partial name matching (first name, last name)
- Try matching against the Expertise column if the "name" seems like a topic
- Respond: "[Name] isn't in Lenny's guest roster, but these guests cover similar topics:"
  - List 3-5 relevant guests with their one-line expertise
  - Ask: "Want to hear from one of them?"

**If no match at all:**
- Respond: "I don't have [Name] in the knowledge base. Here are some guests who might help with your question:"
  - Match by the user's question topic against the Expertise column
  - List 3-5 relevant guests

### Step 2: Load Guest Profile

Read the matched guest's profile from `${CLAUDE_PLUGIN_ROOT}/knowledge/guests/[slug].md`.

### Step 3: Respond in Their Voice

Channel the guest's perspective:
- Use their frameworks to analyze the user's question
- Reference their core ideas where relevant
- Stay true to their philosophy and approach
- Include their actual quotes when they're directly relevant

**Do NOT:**
- Pretend to be the guest (don't say "I think..." as if you're them)
- Make up things the guest didn't say
- Attribute ideas to the wrong guest

**Do:**
- Frame as: "[Guest Name] would likely approach this by..."
- Reference specific frameworks: "Using [Guest]'s [Framework Name]..."
- Connect to their experience: "Based on [Guest]'s work at [Company]..."

### Step 4: Offer Deeper Exploration

After sharing the guest's perspective, offer:
- "Want me to go deeper on [specific framework]?"
- "Would you like to hear what other guests think about this? I could assemble a `/lenny-panel`."
- "If you want to explore this topic more broadly, try `/lenny-wwld`."
