---
name: lenny-setup
description: Configure your Lenny Wisdom profile — role, company stage, and challenge level. Use on first run or when the user says "change my settings", "update my profile", or "adjust challenge level".
---

# Lenny Setup

Configure your personal profile for the Lenny Wisdom thought partner.

## Instructions

### Check for Existing Profile

First, check if `~/.claude/lenny-wisdom.local.md` already exists.

**If it exists (re-run):**
1. Read the current values from the file
2. Show the user their current settings: name, role, company stage, challenge level
3. Ask: "Which setting would you like to change?" using AskUserQuestion
4. Only update the fields they want to change — don't restart the full flow

**If it does not exist (first run):**
Run the full onboarding flow below.

### Onboarding Flow

Ask the following questions one at a time using AskUserQuestion:

**Question 1: Name**
"What should I call you?"
- Free text input

**Question 2: Role**
"What's your current role?"
- Options: Junior PM, Senior PM, Lead/Staff PM, Director/VP of Product, CPO/Head of Product, Founder/CEO, Other
- This helps calibrate the depth and framing of advice

**Question 3: Company Stage**
"What stage is your company at?"
- Options: Pre-launch / Idea stage, Early stage (pre-PMF), Growth stage (post-PMF, scaling), Mature / Public company, Other
- This helps contextualize frameworks to your situation

**Question 4: Challenge Level**
"How much should I push back on your thinking? (1-5)"
- 1: Exploratory — "Let's explore this together..."
- 2: Gentle probing — "Tell me more about..."
- 3: Warm but direct — "Have you considered...?" (Recommended)
- 4: Significant pushback — "I want to challenge that assumption..."
- 5: Full challenge mode — "What evidence do you have for that?"

### Save Profile

Write the profile to `~/.claude/lenny-wisdom.local.md`:

```markdown
---
name: [user's name]
role: [selected role]
company_stage: [selected stage]
challenge_level: [1-5]
---
```

### Completion Message

After saving:

"You're all set, [name]! Here's what you can do:
- `/lenny-wwld` — Think through a problem with a Socratic thought partner
- `/lenny-ask-guest` — Get a specific guest's perspective
- `/lenny-panel` — Assemble a panel of experts on your question
- `/lenny-feedback` — Get Lenny-lens feedback on a doc or idea
- `/lenny-frameworks` — Browse 55 product frameworks

What would you like to explore first?"
