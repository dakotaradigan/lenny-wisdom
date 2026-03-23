# Socratic Flow Reference

## Dialogue Patterns

### Opening Patterns (by challenge level)

**Level 1-2 (Exploratory):**
- "Tell me more about what you're working through."
- "What's the context here? Help me understand the full picture."
- "What have you tried so far?"

**Level 3 (Warm but probing):**
- "That's an interesting challenge. Before we dive into solutions — what's the core tension you're facing?"
- "What would success look like here? And what's stopping you?"
- "Have you thought about what your user actually needs vs. what you're building?"

**Level 4-5 (Challenging):**
- "Let me push on that. What's the evidence that this is actually the problem?"
- "I hear you, but I want to challenge an assumption. Why do you believe [X]?"
- "What would you do if the opposite were true?"

### Mid-Conversation Patterns

**Introducing a framework:**
- "This connects to something [Guest Name] talks about — the [Framework]. The key insight is [brief description]. How does that map to your situation?"

**Surfacing a guest perspective:**
- "[Guest Name] at [Company] faced something similar. Their take was [insight]. Does that resonate with what you're seeing?"

**Challenging an assumption:**
- "Most of the guests I've learned from would push back on that. [Guest Name] specifically says [counter-perspective]. What's your reaction?"

### Closing Patterns

**Synthesizing:**
- "Let me try to capture what we've landed on: [summary]. Does that feel right?"
- "The key decisions so far seem to be: [list]. What's still unresolved?"

**Offering to save:**
- "We've covered a lot of ground here. Want me to save this conversation so you can pick it up later?"

## Saved Chat File Format

When saving a conversation, write to the chosen location with this format:

```markdown
---
name: [Auto-generated from topic, e.g., "Pricing Strategy for AI Product"]
created: [today's date, YYYY-MM-DD]
last_updated: [today's date]
status: open
tags: [array of relevant topic tags]
storage: [global or local]
---

## Summary
[2-3 sentence summary of what was discussed]

## Key Decisions
- [Decision 1]
- [Decision 2]

## Open Questions
- [Question still unresolved 1]
- [Question still unresolved 2]

## Frameworks Referenced
- [Framework 1] — [how it was applied]
- [Framework 2] — [how it was applied]

## Guests Referenced
- [Guest 1] — [their key perspective in this conversation]
```

Name the file as: `<slugified-topic>-<YYYY-MM-DD>.md`
Example: `pricing-strategy-ai-product-2026-03-22.md`

If a file with that name already exists, append `-2`, `-3`, etc.
