# Technical architecture (DRAFT v0.1)

## Proposed flow
Caller -> telephony/voice provider (Vapi or Retell, TBD) -> authenticated webhook -> FastAPI service -> call state + policy/FAQ -> lead summary -> configured business destination.

## Components
- `voice_provider`: interface and provider-specific adapters; no core business logic embedded in vendor prompts only.
- `api`: authenticated webhooks, schema validation and idempotency.
- `domain`: business rules for lead capture, escalation and approved responses.
- `delivery`: a queue/retry strategy for summaries (prototype can mock).
- `observability`: operational metrics with privacy-safe logging.
- `tests`: synthetic transcripts, integration contract tests, simulated failure modes.

## Design constraints
- Keep API keys outside Git and use a secret manager in deployment.
- Verify provider webhook signatures/authentication where supported.
- Do not expose customer PII in GitHub Issues, PRs, CI logs or example fixtures.
- Explicit recording/transcription notices and retention policy required before real calls.
- Use configurable business profiles rather than cloning code per customer.
- Build fail-closed behaviors, human handoff, bounded tool permissions, retries and usage limits.

## Open decisions
Provider selection; outbound summary destination; data storage/retention; hosting; phone provisioning; metrics storage; authentication; tenancy; regional compliance.

## Implementation sequence
(1) Data models and mocked webhook tests -> (2) provider sandbox -> (3) live internal test number -> (4) supervised pilot after approvals.
