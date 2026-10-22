# QA and testing strategy (DRAFT v0.1)

## Layers
1. **Unit**: parsing, validation, state transitions, urgency rules, fallback, formatting, redaction.
2. **Contract**: webhook schemas, provider adapter, signatures, idempotency and retries.
3. **Conversation scenarios**: synthetic dialogues with correct details, incomplete details, FAQ unknowns, contradictory instructions, opt-out and human requests.
4. **Audio/manual**: interruptions, barge-in, background noise, speakerphone, accent variation, code switching later, silence and poor network conditions.
5. **Operational**: latency percentiles, cost per call, call completion, dropped calls, summary delivery and alerting.
6. **Security/privacy**: authentication, data minimization, retention, prompt-injection attempts and no secret/PII leaks.

## Sample synthetic test cases
- Caller needs a leaking faucet fixed tomorrow; capture name and callback.
- Caller demands guaranteed price; decline unsupported quote.
- Caller reports dangerous gas smell; prioritize human/emergency routing and avoid dispatch promise.
- Caller changes phone number mid-call; use corrected value.
- Caller refuses contact collection; respect choice and explain limits.
- Webhook delivered twice; only one lead event should be submitted.
- Backend unavailable; graceful failure and retry or human fallback.
- Caller asks to speak to a human; route according to configured policy.

## Release gate
No external pilot until owner approval, legal/privacy review, documented fallback behavior, representative test results and monitored usage caps. Set quantitative thresholds after baseline measurements rather than inventing SLAs.
