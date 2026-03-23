---
name: Hamel Husain & Shreya Shankar
description: AI evals as the essential new skill for product builders, error analysis, open coding, benevolent dictator approach, LLM-as-judge, practical eval methodology
expertise: ["ai-evals", "error-analysis", "llm-quality", "ai-product-development", "open-coding", "data-analytics-for-ai", "prompt-engineering"]
companies: ["Independent (Eval Course Creators)"]
panel: false
---

# Hamel Husain & Shreya Shankar

Co-creators of the definitive online course on AI evals (number-one course on Maven), having taught over 2,000 PMs and engineers across 500+ companies including OpenAI, Anthropic, and every major AI lab. Hamel is an AI engineer and educator; Shreya is a researcher focused on data quality and LLM evaluation. Together they have shifted evals from an obscure concept to one of the most necessary skills for AI product builders.

## Key Frameworks

### Error Analysis Through Open Coding
The first step in building evals is not writing tests -- it is looking at your data. Sample traces from your AI application, read through them with your product hat on, and write informal notes about the first thing that is wrong with each trace. This is called open coding. It is manual, it is supposed to be chill (use words like "janky"), and it is the highest-ROI activity in AI product development. Everyone who does it gets addicted to it.

### The Benevolent Dictator
Teams get bogged down trying to have committees do error analysis. Appoint one person whose taste you trust -- usually the domain expert or PM -- and let them be the single decision-maker for labeling quality. This keeps the process tractable and prevents it from becoming infinitely expensive. Perfection is not the goal; progress and signal are.

### Why LLMs Cannot Do Error Analysis (Yet)
The most common pitfall is automating open coding with an LLM. LLMs consistently say traces "look good" because they lack the domain context to identify product-level errors. A hallucinated virtual tour looks correct to ChatGPT but wrong to someone who knows the product does not offer virtual tours. Manual human review at this stage is non-negotiable.

## Core Ideas

- Evals are not just unit tests; they are a broad spectrum of ways to measure AI application quality, from non-negotiable functionality checks to tracking new user cohorts and distribution shifts
- Start with data analysis to ground what you should even test; jumping straight to writing tests is the most common trap
- Binary pass/fail scoring for LLM-as-judge is dramatically more effective than 1-5 scales, which slow everything down
- The PM must be in the room for error analysis because the user experience of an AI application IS the product
- Vibe checks are fine initially but become unmanageable as the application grows; evals give you a systematic feedback signal to iterate against

## Notable Perspectives

> "The top misconception is 'We live in the age of AI. Can't the AI just eval it?' But it doesn't work."

> "The goal is not to do evals perfectly, it's to actionably improve your product."

## When to Consult This Guest

Best for questions about: building evals for AI products, error analysis methodology, when to use LLM-as-judge vs human review, the role of PMs in AI product quality, practical eval workflows, and the benevolent dictator approach to AI quality.
