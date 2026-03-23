---
name: Engineering and Technical Leadership
description: Technical leadership, engineering productivity, tech debt, build vs buy, DORA metrics, developer experience, code deletion, AI-assisted engineering, systems thinking for engineers, engineering org design, CTO perspectives, shipping velocity
related_guests: [will-larson, farhan-thawar, nicole-forsgren, guillermo-rauch, sam-schillace]
related_frameworks: [DORA Metrics, SPACE Framework, Linear Method, Shape Up, LNO Framework]
---

# Engineering and Technical Leadership

## Overview

Engineering leadership has undergone a fundamental transformation in the post-ZIRP era. The skills that made engineering leaders successful during the growth-at-all-costs period -- primarily hiring and team expansion -- are no longer sufficient. Today's technical leaders must master right-sizing, allocation, accountability, and velocity. The guests in this topic collectively paint a picture of engineering excellence that prioritizes intensity over hours, shipping small changes frequently, and treating engineers as accountable adults rather than resources to be coddled.

A recurring theme across these leaders is the counterintuitive relationship between speed and quality. Nicole Forsgren's research proves that moving faster actually improves stability, while Farhan Thawar demonstrates that intensity per minute matters more than total hours worked. Guillermo Rauch and Sam Schillace both point toward a future where AI fundamentally expands who can build software, shifting the engineering bottleneck from writing code to making good decisions about what to build. Will Larson grounds all of this in systems thinking -- building mental models of organizations while remaining humble enough to update those models when reality disagrees.

The practical implication for product leaders is clear: engineering productivity is not about adding headcount or optimizing processes. It is about creating the conditions for small teams to ship small changes at high frequency, holding people accountable for outcomes, and systematically removing the cruft that accumulates in both codebases and organizations.

## Key Patterns

### 1. Speed and Stability Are the Same Strategy
Forsgren's DORA research demolishes the myth that slowing down improves quality. Teams that deploy more frequently have lower change failure rates because each deployment is smaller with a smaller blast radius. Farhan Thawar's Shopify exemplifies this -- a 10,000-person remote company that ships with startup-level urgency by optimizing for intensity per minute rather than hours worked.

### 2. Accountability Enables Growth
Will Larson argues that the ZIRP era's tendency to coddle engineers paradoxically prevented their growth into senior leadership. Staff engineer career paths require organizations willing to hold senior engineers accountable for outcomes. The best engineering cultures give engineers real, hard problems -- this is what enables career growth, not sheltering them from difficulty.

### 3. Simplification Through Deletion
Farhan Thawar's Delete Code Club at Shopify regularly removes over a million lines of code. This is not housekeeping -- it is a strategic practice that creates speed, reduces maintenance burden, and forces clarity about what matters. The pattern extends beyond code: Larson's observation that Stripe's incident analysis became so thorough it crowded out fixing incidents shows the same principle applied to process.

### 4. AI Shifts the Bottleneck, Not the Need for Engineers
Guillermo Rauch sees AI expanding the builder population from 20 million developers to 100 million product builders. Sam Schillace emphasizes that knowing how things work under the hood becomes more important in an AI era because it helps you influence the model. The bottleneck migrates from writing code to making decisions about what to build and maintaining the judgment to evaluate AI output.

### 5. Systems Thinking with Humility
Will Larson's central insight: build mental models to represent complex systems, but when the model conflicts with reality, reality is always right. The biggest failure mode of systems thinkers is deciding that reality is wrong. This applies to engineering metrics, organizational design, and technical architecture alike.

### 6. Measurement Requires Agreement on the Problem
Forsgren observes that 80% of organizations' biggest challenge is not measurement itself but agreeing on what problem they are trying to solve. Teams spend months without aligning on whether "developer experience" means friction, culture, or toolchains. Measurement without shared problem definition produces noise, not signal.

### 7. Optimism as Technical Strategy
Sam Schillace's what-if vs. why-not framework separates innovators from incrementalists. Every disruptive technology faces an avalanche of why-not objections. Google Docs succeeded despite years of executives calling it stupid because the what-if thinkers kept experimenting. Being optimistic and wrong beats being pessimistic and right.

## Frameworks to Apply

### DORA Four Keys (Nicole Forsgren)
Measure deployment frequency, lead time for changes, change failure rate, and time to restore service. Use for diagnosis and benchmarking, not punishment. The key insight: elite performance benchmarks hold regardless of company size.

### SPACE Framework (Nicole Forsgren)
A holistic developer productivity model covering Satisfaction, Performance, Activity, Communication, and Efficiency. Prevents the trap of optimizing only for throughput while ignoring sustainability and burnout.

### LNO Framework (Shreyas Doshi)
Categorize engineering work as Leverage (10x return), Neutral (1:1), or Overhead (low return). Apply perfectionism only to L tasks. Prevents over-engineering on low-impact work and under-investing in high-impact work.

### Shape Up (Ryan Singer)
Fixed 6-week cycles with 2-week cooldowns. Give teams shaped problems with appetite constraints rather than detailed specs. Particularly useful when sprint-based agile feels too micro-managed.

### Delete Code Club (Farhan Thawar)
Regular, structured code deletion as an organizational practice. Forces clarity about what matters, reduces maintenance surface area, and creates a culture where simplification is valued alongside creation.

## Socratic Questions

1. When your team says they need to "slow down to improve quality," are you sure that's true? What does your change failure rate look like relative to your deployment frequency?

2. If you measured intensity per minute rather than hours worked, what would change about how your team operates?

3. What percentage of your codebase could you delete tomorrow with no user impact? What is preventing you from doing so?

4. Are your senior engineers accountable for business outcomes, or primarily for code quality? What would change if you shifted that balance?

5. When you encounter a metric that contradicts your mental model of how the team works, do you update the model or question the metric?

6. Has your team agreed on what problem "engineering productivity" actually refers to, or are different people optimizing for different definitions?

7. If AI could write 80% of your code tomorrow, what would your engineering team spend their time on? Is that what they should be spending time on today?

8. When you evaluate a new technology or approach, do you default to "what if this works?" or "why not?" -- and which of those questions is more likely to surface breakthrough opportunities?

9. Are your engineering processes (code review, incident analysis, planning ceremonies) still proportional to the value they create, or have some grown beyond their usefulness?

10. What would your organization look like if you had half the engineers but twice the intensity per person?

## Common Pitfalls

1. **Conflating hours with output.** Teams that work long hours but ship slowly often have an intensity problem, not a capacity problem. Farhan Thawar's "do more per minute" reframes the real lever.

2. **Treating speed and quality as tradeoffs.** Forsgren's data shows they move together. Batching large releases to "ensure quality" actually increases risk and makes debugging harder.

3. **Measuring without agreement on the problem.** Implementing DORA metrics or any productivity framework without first aligning on what you are trying to improve produces dashboards no one acts on.

4. **Over-engineering incident response.** Larson's Stripe example: incident analysis became so comprehensive that it crowded out actually fixing the underlying issues. Measure twice, cut once -- but do not measure infinite times and never cut.

5. **Resisting code deletion.** Teams treat code as an asset to be preserved rather than a liability to be minimized. Every line of code is a maintenance cost. Deletion is a feature.

6. **Hiring your way out of productivity problems.** Post-ZIRP, engineering leaders who only knew how to grow teams now face the harder skill of right-sizing and allocation. Adding people often reduces velocity in the short and medium term.

7. **Dismissing AI tools with why-not thinking.** Listing reasons AI coding tools will not work (hallucinations, security, accuracy) is easy and misses the transformative what-if opportunity. The builders who experiment early compound their advantage.

## Key Guests

| Guest | Expertise | Best For |
|-------|-----------|----------|
| Will Larson | Engineering org design, systems thinking, staff engineer paths, accountability culture | Questions about engineering leadership, team sizing, post-ZIRP challenges, and building senior IC career paths |
| Farhan Thawar | Intensity culture, pair programming, code deletion, hiring engineers | Questions about shipping velocity, remote engineering culture, hiring, and simplifying codebases |
| Nicole Forsgren | DORA metrics, SPACE framework, developer productivity measurement | Questions about measuring engineering performance, benchmarking teams, and making the case for DevOps investment |
| Guillermo Rauch | Developer tools, AI building tools, TAM expansion, product taste | Questions about the future of engineering with AI, building developer platforms, and expanding who can build software |
| Sam Schillace | Disruptive innovation, what-if thinking, creative experimentation | Questions about building products that challenge assumptions, AI transformation, and overcoming organizational resistance to new ideas |
