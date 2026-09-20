# Project context and decision memory

Use this guide for initialization, conflicting records, promotion, scope changes, and persistent writes.

## Project ownership

Identify the active game root using the task, repository instructions, and existing project documentation. A repository can contain several games. A reusable skill can be installed globally. Neither fact makes the skill directory a valid home for game memory.

Default records at the active game root:

- `MILES_PROJECT_CONTEXT.md`: current established conditions, accepted intentions and experience model, scoped rules, and evidence links.
- `MILES_DECISIONS.md`: significant choices and status history.

When a project already declares equivalent authoritative files, use those paths and record the mapping. Avoid silently creating competing records. Keep the two Miles files together so their relative links remain valid.

Read relevant sections and linked decisions before asking for facts. Older decisions provide rationale; the current context supplies active scope. Examples and templates are instructional fixtures, never evidence about a real project.

## Project facts and a shared understanding

At first engagement or a material direction change, use [project-understanding.md](project-understanding.md) to synthesize the game. The existence of this file or a successful code read supplies no automatic readiness verdict.

Preserve an accepted, connected summary of the world, player role, intended audience, core experience, supporting loops, and important priorities in Project Context. Reference the confirmed entries it draws on. Keep unknowns visible; unaccepted interpretations remain in the current brief. Accepted model rationale can persist with its causal predictions explicitly labeled as hypotheses. Reuse established authority and avoid asking the developer to confirm the same facts again.

## What earns a place in context

A candidate needs explicit confirmation, continuing relevance, and a clear scope. Useful entries include platform commitments, player assumptions the developer has adopted, creative pillars, core loops, system meaning, and interaction conventions.

Record the *kind* of knowledge accurately:

| Kind | Example | Meaning |
|---|---|---|
| Confirmed constraint | The MVP supports touch input. | A project commitment. |
| Confirmed design intent | Construction uses fixed world points in the MVP. | An accepted rule; implementation may lag. |
| Observed implementation | Build 42 exposes a drag handle. | An inspected, version-specific fact. |
| Research finding | In study P-03, 3 of 6 participants tried the locked gate. | A bounded observation with method and sample. |
| Hypothesis | The gate may look like the next objective. | Candidate explanations stay in the current brief; accepted design rationale may link the hypothesis with its research status intact. |

Prefer durable constraints and intended language in current context. Link build inventories and research records where details change quickly. Label adopted audience assumptions as project intent, with a research status; confirmation by a developer does not turn them into measured audience facts.

An entry should have an ID, statement, applicability, source, confirmation date, and related decision when applicable. Include a review trigger when expiry or a release boundary matters. Unknown values remain explicit. Store only a minimal set of open questions in context, separated from confirmed entries.

## Independent dimensions

**Scope:** Local / System / Product. Scope describes reach, not importance or approval.

**Status:** Proposed / Confirmed / Rejected / Superseded. Status describes a choice's lifecycle.

**Evidence:** Untested / Qualitative evidence / Quantitative evidence / Mixed / Inconclusive. Evidence describes support for an expected outcome, not authorization.

**Applicability:** Release, feature, platform, mode, audience, or date boundary. Carry this boundary through every copy of a rule.

Examples: a confirmed local layout can remain in the log; a proposed product-wide rule stays out of confirmed context; a confirmed MVP-wide system rule remains limited to the MVP.

## Confirmation and promotion

Explicit approval of an unambiguous recommendation confirms its stated scope. When several options are on the table, an ambiguous acknowledgment leaves the selection unresolved. Existing authoritative records can establish confirmation when their authority and active scope are clear.

Promote only the reusable rule that was accepted. Approval to put the second table at a fixed point covers that table. Approval that every MVP furniture purchase uses fixed points covers the named furniture system and release.

Repeated local choices are a reason to propose a reusable rule. Ask for confirmation of that rule before promoting it. A high change cost is useful evidence of importance, not a mandatory condition of persistence.

## Reconciliation

Separate three questions: what was intended, what is implemented, and what should now be adopted.

A screenshot that conflicts with a rule may show an older build, an implementation defect, or an intentional change. Record the observation and clarify the discrepancy only as needed for the task. A newer timestamp by itself establishes no authority.

An explicit authorized correction can replace earlier context. For consequential conflicts between current authorities, expose the conflict and obtain the smallest required resolution. Continue with unaffected design work where possible.

For a confirmed exception, retain the general rule and name the exception's narrow scope. For a replacement, update current context and mark the previous decision Superseded with the new decision ID. Preserve the original rationale and a dated status-history entry.

## Safe write procedure

1. Check project identity, applicable instructions, and write authorization.
2. Reread the target section; reconcile any intervening edits.
3. Prepare a minimal change with exact scope, provenance, and decision IDs.
4. Update current context and decision history consistently. Preserve unrelated content.
5. Read back the changed records and check references and status.
6. Report the meaningful update, or provide an unsaved patch when writes are unavailable.

Use the filesystem's safe-write facilities when available. This Markdown convention supplies no database transaction or concurrency lock across files. Recheck both files after a partial failure and repair only the authorized changes.

The initializer creates empty templates and project identity metadata. It neither interprets conversations nor promotes rules. It refuses existing target files and recognized legacy context files so the designer can resolve ownership deliberately.

See the complete [lifecycle example](../examples/worked/context-lifecycle.md) for a local decision, scoped promotion, exception, and replacement.

## Persist an experience model without inflating its evidence

The accepted model belongs inside the existing Project Context. Preserve player goals, concrete quality definitions, organizing concepts, element responsibilities, and reusable property/rule relationships. Link the decision and its exact scope. A useful rationale explains how a condition affects the experience so future choices can be derived.

“Make work feel manageable” can be a confirmed intent. “Pending-work cues help players choose their next action” remains a causal hypothesis. “Four of six observed participants independently found the station in test T-01” would be a scoped finding only after such a test actually occurs. These meanings remain separate in an accepted model.

Use one authoritative record per rule; cross-reference rather than copying changing statements into several tables. Candidate concepts remain in the current brief or proposed decisions until accepted. A brief model can be plain prose with source and status; identifiers are useful when dependencies grow.

When viewport, audience, creative priorities, or timing rules change, trace the affected concepts, functions, rules, and tests. Preserve unaffected knowledge and record which decision changed. See [Experience modeling](experience-modeling.md) and [Migration](../MIGRATION.md).
