# Implementation handoff

Use when the work will be built by another developer, artist, external team, or agent. The handoff lets them reproduce the important experience relationships without inventing the unresolved core design.

## State the delivery level

**Exploration:** alternatives or foundations remain open; build studies that help choose.

**Prototype-ready:** the hypothesis, minimal behavior, provisional settings, and test setup are sufficient to build a disposable experiment.

**Implementation-ready:** the named slice has settled behavior, necessary assets and interfaces, applicable constraints, edge cases, and acceptance cases. Unresolved wider project questions stay outside the slice or become explicit blockers.

These labels describe the work's readiness. Design approval and empirical support remain separate fields.

## Keep the goal trace visible

Open with the player situation, intended outcome, relevant quality/concept, and the responsibility the feature fulfills. Link existing Project Context rather than copying its entire contents.

A contractor should understand why a rule matters. “Clear the workstation cue on completion” preserves the distinction between active work and completed work. A single rationale can justify multiple implementation requirements.

## Describe observable behavior

Specify starting state, trigger, guards, available input, immediate response, persistent consequence, and next state. Include unavailable behavior, cancel, repeated input, partial completion, interruption, and resume where applicable.

Use the project's real names when known. Keep invented schema and routes clearly proposed. Align with repository architecture only after the experience behavior is grounded. An existing page carrier is a constraint or implementation option; it leaves the design purpose to be established.

For resources and ownership, state who owns the item, when it changes state, which operation is authoritative, and how interrupted or repeated actions preserve integrity. Avoid promising automatic persistence without an implementation contract.

## Invariants and adjustable properties

An **invariant** is an accepted relationship the implementation must preserve within the specified scope. Examples: a completed transaction credits once; a sold object loses active ownership; an idle object lacks a ready-state cue.

A **parameter** is an intentionally adjustable property. Include name, units/type, initial value or approved token, allowed cases, tuning purpose, and status. An unresolved value essential for implementation is a blocker. A prototype can use an explicit provisional default.

A **creative freedom** is an area where variation is allowed while preserving the agreed function and checks. For example: the exact decorative pattern may vary, provided the reserved task symbol and legibility conditions remain distinct.

These fields prevent both accidental under-specification and unnecessary micromanagement.

## Art, content, and engineering responsibilities

State which existing assets are reused, which variants or copies must be produced, and which state data the view consumes. Define collaboration boundaries through delivered behavior, without inventing team members or schedules.

Provide relevant screenshots or prototypes only when available. Name missing evidence explicitly. For a visual artifact request, use the host's appropriate image/design tools when available. A written specification can remain a complete deliverable when images are outside scope.

## Acceptance: reproducible implementation checks

Write Given / When / Then cases that can be performed on the delivered build. Include normal flow, denial, interruption, and repeated input where consequential. Define pass/fail against the specified behavior.

Examples:

- Given the station is idle, when service mode renders, then the ready-state cue is absent.
- Given the station is ready, when the player selects it twice during one transition, then exactly one task is opened and the result is applied once.
- Given a visit is interrupted after an authoritative completion, when the saved state is restored, then the completed work remains complete and its reward remains singular.

The last two cases require the project to provide the relevant transition and persistence contract. Mark any missing contract before describing the handoff as implementation-ready.

## Validation: the experience question

State what the implementation is expected to help players understand or feel, how the test will be run, and what would change the design. Use a task that avoids naming the desired input. Observe assistance, wrong interpretations, recovery, and player accounts.

A player can finish a task while misunderstanding the broader system. A visually compliant asset can still obscure an action. Keep implementation results and player findings separate in reporting.

## Ready-to-build review

Read the handoff as an external team would. Can they identify the scope, states, dependencies, required assets, adjustable values, acceptance cases, and owner of unresolved decisions? Can they explain which experience would be harmed by breaking an invariant?

Use the [handoff template](../templates/IMPLEMENTATION_HANDOFF.md). The [worked workstation slice](../examples/worked/workstation-handoff.md) demonstrates a narrowly scoped implementation-ready proposal with explicit fictional assumptions.
