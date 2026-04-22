# Startup Validator

A Claude skill that takes a raw business idea through a 7-phase validation and launch planning pipeline.

## Phases

1. **Idea Validation** - Market demand, competition, risk scoring, GO/PIVOT/STOP verdict
2. **Niche Discovery** - 10 niche variations scored and ranked
3. **Pain Point Research** - Customer frustrations mapped and prioritized
4. **Lean Business Plan** - One-page plan with unit economics
5. **MVP Design** - Minimum viable product spec with tech stack and 7-day build timeline
6. **Customer Acquisition** - 4-week plan to get first 50-100 customers organically
7. **Monetization** - Pricing, conversion optimization, revenue milestones

## Installation

Drop the `SKILL.md` file into your Claude skills directory:

```bash
mkdir -p ~/.claude/skills/startup-validator
cp SKILL.md ~/.claude/skills/startup-validator/
```

## Packaging for Customers

```bash
uv run scripts/package.py
```

Produces a versioned zip file in `dist/` ready for customer delivery.

## Triggers

Say any of these to activate: "validate my idea", "startup plan", "business idea", "should I build this", "MVP plan", "how to launch", "find my niche", "get first customers"

## Community

Built something with this? Share it in the [Build With AI](https://skool.com/buildwithai/about) community.
