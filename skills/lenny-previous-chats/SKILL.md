---
name: lenny-previous-chats
description: List and resume saved Lenny Wisdom conversations. Use when the user says "previous chats", "continue where I left off", or "pick up where we left off".
---

# Previous Chats

List and resume saved Lenny Wisdom conversations from both global and project-local storage.

## Instructions

### Step 1: Find Saved Chats

Check both locations for saved chat files:

1. **Global:** `~/.claude/lenny-wisdom/chats/*.md`
2. **Local:** `.lenny/chats/*.md` (current working directory)

Read all `.md` files found in both locations. Parse the YAML frontmatter for: name, created, last_updated, status, tags.

### Step 2: Present the List

**If chats are found:**

Group by location and show:

```
Global chats:
  1. [name] ([date]) — [status]
     Tags: [tags]

Project chats ([current directory name]):
  2. [name] ([date]) — [status]
     Tags: [tags]
```

Ask: "Which conversation would you like to pick up?"

**If no chats are found (empty state):**

"No saved conversations yet. After a deeper chat, I'll offer to save it for you.

Here's how to get started:
- `/lenny-wwld` — Think through a problem with a Socratic thought partner
- `/lenny-panel` — Get multiple expert perspectives on a question
- `/lenny-feedback` — Get feedback on a doc or idea"

### Step 3: Resume a Chat

When the user selects a chat:

1. Read the full saved chat file
2. Present the context:
   - **Summary** of what was discussed
   - **Key Decisions** made so far
   - **Open Questions** still unresolved
3. Ask: "Which open question should we explore? Or is there something new you want to discuss in this context?"

### Step 4: Check for Resolution

If the user indicates the problem is resolved during a resumed conversation:
- Ask: "Sounds like this is resolved! Want me to mark it as closed?"
- If yes, update the `status` field in the saved file from `open` to `closed`
- Update `last_updated` to today's date

### Status Lifecycle

- `open` — Active conversation, still has unresolved questions
- `closed` — Resolved, kept for reference

Users can also manually edit or delete files in the chat directories.
