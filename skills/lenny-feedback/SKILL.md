---
name: lenny-feedback
description: Review a PRD, strategy doc, or product idea through the lens of Lenny's collected wisdom. Use when the user says "review my doc", "give me feedback on", "critique this", or pastes a document.
---

# Lenny Feedback

Review product documents, strategy decks, and ideas through the lens of Lenny's collected wisdom — frameworks, guest perspectives, and common pitfalls.

## Instructions

### Step 1: Receive the Document

Accept input in two ways:
- **Inline paste:** User pastes the content directly in the conversation
- **File path:** User provides a path to a file (read it with the Read tool)

**Length handling:**
- **Very short (<100 words):** Ask 2-3 clarifying questions before reviewing. "This is a bit brief for a thorough review. Can you tell me: What's the goal? Who's the audience? What decision does this support?"
- **Normal (100-5000 words):** Review directly.
- **Very long (>5000 words):** If pasted inline, suggest providing a file path instead. Focus on structure, strategy, and big-picture issues rather than line-by-line feedback.

### Step 2: Identify Relevant Frameworks

1. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/topic-index.md` to find matching topics
2. Read `${CLAUDE_PLUGIN_ROOT}/knowledge/frameworks.md` to find applicable frameworks
3. Open matched topic files for common pitfalls and patterns

### Step 3: Review Against Criteria

For the detailed critique checklist, see [review-criteria-reference.md](review-criteria-reference.md).

Structure your feedback in these sections:

**What's Strong**
- 2-3 things the document does well
- Always lead with strengths — be warm and encouraging

**What's Missing**
- Gaps that frameworks suggest should be addressed
- Missing perspectives or stakeholders
- Untested assumptions

**What to Sharpen**
- Areas that could be clearer, more specific, or more actionable
- Metrics that should be defined
- Positioning that could be tighter

**Frameworks to Consider**
- 2-3 frameworks from the knowledge base that would strengthen this document
- Brief explanation of how each applies

### Step 4: Offer Next Steps

"Would you like me to:
- Deep-dive on any of these points?
- Assemble a `/lenny-panel` to get expert perspectives on a specific aspect?
- Help you apply one of the frameworks I mentioned?"
