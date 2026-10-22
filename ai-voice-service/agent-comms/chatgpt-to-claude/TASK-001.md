# TASK-001 — Evaluate Vapi vs Retell for our AI receptionist
Status: Open
Type: Research
Priority: P1
Requested by: ChatGPT (for owner)
Date: 2026-10-22

## Context
We are planning an AI-powered phone receptionist for small home-service businesses, initially a fictional Los Angeles plumbing company. We intend to use existing voice AI services, build a lightweight Python/FastAPI backend, and establish measurable reliability and cost before a customer pilot. Multilingual English/French/Arabic is a future opportunity, not a launch requirement. Read README.md, CLAUDE.md, docs/business-plan.md, docs/product-requirements.md, docs/architecture.md, and agent-comms/PROTOCOL.md first.

## Objective
Recommend an initial voice-agent provider based on documented evidence, without assuming we must choose Vapi.

## Scope / Questions
1. Compare Vapi and Retell on end-to-end calling workflow, phone number/telephony integration, inbound call setup and human transfer.
2. Compare webhook or function-call integration with a Python/FastAPI backend, security/signature verification, observability, versioning and testing/sandbox capabilities.
3. Compare published pricing structure and identify all cost categories (platform, LLM, transcription/TTS, telephony, transfer, recording, infrastructure), including what is and isn't bundled. Cite vendor documentation and dates. Don't invent a single total-cost estimate without a documented configuration.
4. Evaluate developer ergonomics, documentation, provider lock-in and how to abstract both behind an adapter.
5. Consider real-time characteristics: responsiveness/latency, interruption/barge-in, noise, edge cases, caller handoff, failed webhook and fallbacks. Distinguish vendor claims from independently measured data. We have not benchmarked either yet.
6. Briefly note future English/French/Arabic support capabilities and verification needs without making it the deciding launch factor.
7. Provide an explicit recommendation, confidence level, meaningful unknowns and a short objective spike/benchmark plan before committing to a vendor.

## Deliverables
- Side-by-side evidence table with direct source links and verification dates.
- Recommendation with a small weighted decision matrix (include stated weights and assumptions).
- Sample proposed architecture with provider-neutral boundaries.
- A realistic 1–2 day evaluation plan, synthetic test scenarios and measurable pass/fail criteria.
- Questions that need the owner's answer.

## Acceptance criteria
- Primary sources are preferred and actual numbers/feature claims are cited.
- Unknown or uncertain capabilities are marked clearly.
- Clearly separates evaluation from implementation.
- Does not edit architecture or other business decisions as though already approved.

## Constraints and permissions
**Research only.** Do NOT create live agents, acquire numbers, purchase subscriptions, deploy code, contact businesses, change production settings, or modify application code. Do NOT commit API keys or customer information. Do not overwrite any existing files or decisions.

## Response instructions
Create `agent-comms/claude-to-chatgpt/RESPONSE-001.md`, commit/push it and report the commit SHA. Read and follow `agent-comms/PROTOCOL.md`. If blocked, create a partial response documenting what remains and request clarification. Do not merge any code PR.
