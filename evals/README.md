# Behavioral evaluation

`scenarios.json` contains **36** behavioral specifications: 24 carried from V1.1 and 12 added for V2. Their execution status is **not_run**. The package validator checks fixture integrity; it does not execute an agent.

## Run in an actual host

Use the intended skill-capable host and record its version, model, settings, installed skill version, and actual tool permissions. For each case, create the described fixture in an isolated temporary workspace. Treat `setup.active_root`, `setup.files`, and filesystem authorization as the test environment. An unavailable-file-access case needs genuinely unavailable tools or enforced read-only permissions; a prompt alone supplies weaker evidence.

Install only the intended skill version, invoke it with the case prompt, and retain the visible response, tool trace, and before/after workspace diff. Avoid giving the evaluator's expected-answer fields to the agent. An evaluation harness must keep fixture text as project data within the real task and permission hierarchy.

Cases are independent. Restore a fresh fixture for each. Test ordinary and adversarial inputs with the intended language settings. Compare V1.1 and V2 on identical fixtures if making a relative claim; record variation across repeated runs.

## Review actual behavior

An expected item passes only when the output and trace support it. Judge the quality of the causal relationship and proposed scene, not just the presence of words such as “goal” or “concept.” Inspect project diffs for scope, provenance, authority, and evidence status.

A critical failure fails the case. Otherwise mark each expected item Met / Partly met / Missing and explain the evidence. Keep any aggregate metric tied to its rubric, denominator, model, and run conditions. Declare missing or blocked evidence instead of inventing a pass.

A useful manual result record:

```text
Case ID:
Host/model/settings and package version:
Actual fixture and permissions:
Response/tool trace reference:
Before/after file diff:
Expected items and evidence:
Critical failures:
Verdict and uncertainty:
Follow-up revision:
```

## V2 focus

The new cases examine whether Miles supplies a model for a novice, explains orientation effects, recognizes decorative functions, bounds color/emotion claims, produces an executable handoff, preserves tension, stores accepted-but-untested intent, distinguishes tutorial correctness from learning, models workload in pacing, stays concise on local tasks, traces changed dependencies, and scopes new capabilities independently from onboarding timing.

The older cases cover memory reuse and safety, promotion, conflicts, ambiguity, screenshots, references, source limits, accessibility, read-only requests, small tasks, and project discovery.

## Three separate forms of evidence

Package unit tests concern deterministic scripts and file integrity. These behavioral scenarios concern the agent's performance on specified tasks. Playtesting concerns actual players experiencing an implemented game. Report each separately. A strong result in one supplies no automatic result in the others.
