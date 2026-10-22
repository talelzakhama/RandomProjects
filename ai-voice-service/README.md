# AI Voice Service for Small Businesses

**Status:** Planning / pre-MVP. All dates, prices and technology choices are provisional.

## Mission
Launch a repeatable AI-powered phone receptionist service for small businesses, beginning with a narrow Los Angeles home-services use case. Expand to English/French/Arabic and additional markets (including Tunisia and Qatar) **after** validating the first product.

## Initial product
A voice agent that receives a call, explains that it is an AI assistant, answers approved FAQs, collects contact/service information, detects urgent requests, and delivers a structured lead summary. For v1 it **does not** promise prices, dispatch technicians, or book appointments.

## Proposed stack (decision pending)
- Voice orchestration: evaluate **Vapi vs Retell** through a short hands-on comparison.
- Backend: Python 3.12+ / FastAPI; vendor adapter to reduce lock-in.
- Testing: pytest, simulated call transcripts and manual audio scenarios.
- Repo: GitHub. Claude Code implements on feature branches; ChatGPT helps plan and review.
- Database: defer until justified; minimize retained personal data.
- Hosting: choose after prototype; Replit is optional.

## Roadmap
1. **Validate** target niche, user pain, willingness to pay, competitor alternatives.
2. **Prototype** one receptionist for a fictional LA plumbing company.
3. **Harden** consent, security, handoff, monitoring, latency, tests and cost controls.
4. **Pilot** with a consenting business on limited calls, review failure cases.
5. **Productize** reusable onboarding/configuration, support and recurring billing.
6. **Expand** only after repeatability; study language quality and local law in each market.

## Getting started
- Read [the draft plan](docs/business-plan.md), [product requirements](docs/product-requirements.md), [architecture](docs/architecture.md), and [test strategy](docs/testing-strategy.md).
- Review [the decisions](docs/decisions.md) before choosing providers or pricing.
- For Claude Code, see [CLAUDE.md](CLAUDE.md).
- Track work in [the roadmap](docs/roadmap.md).
- **Do not commit secrets, customer recordings/transcripts, phone numbers, or production personal data.**

## First milestone
An internally testable call flow plus written evidence that at least a few real businesses have the stated problem. No production deployment before legal/operational review.
