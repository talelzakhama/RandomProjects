# Product requirements (DRAFT v0.1)

## Persona
Small Los Angeles plumbing business that misses calls during jobs or after hours.

## v1 user journey
1. Caller reaches the number.
2. Agent identifies itself as an AI assistant, states the business it represents and provides appropriate notice.
3. Agent asks what service is needed and the approximate service area.
4. Agent collects contact name and callback number with consent; confirms key details.
5. Agent classifies urgency without making safety-critical assertions or promising dispatch.
6. Agent explains next steps accurately, ends politely.
7. System sends a **minimal** structured summary to a designated business inbox/dashboard, with safe retries.

## Must have
- Approved FAQ responses with safe unknown-answer behavior.
- Structured lead: name, callback number, category, approximate area, urgency flag, brief notes, timestamp.
- Human escalation/fallback for emergencies, unclear intent, caller requests or system failures.
- Basic abuse/rate limits, request authentication, minimal retention, configurable business hours.
- Synthetic demo mode before any live caller data.
- Observability: event counts, latency, error rate, handoff rate and cost per call with privacy-preserving logs.

## Not in v1
- Appointment booking or calendar writes.
- Payment collection.
- Price quotes and service guarantees.
- Emergency dispatch or medical/legal advice.
- Multilingual production commitments.
- Full customer-facing dashboard.

## Acceptance criteria (provisional)
- Lead extraction works on at least 20 synthetic test conversations including negative cases.
- Unsupported questions trigger safe deferral; no fabricated quote/appointment.
- Caller interruption, silence, accents, noise and repeated corrections are tested.
- Human fallback can be triggered in test.
- Service detects duplicate events and retries without duplicate delivery.
- Production gate requires explicit legal/privacy, security and business-owner approval.
