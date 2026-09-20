# Worked example — a decision becomes a project rule

**Original fictional fixture.** All project details and quoted approvals in this file are illustrative. They are never evidence of approval in an active project.

Project ID: `paper-lantern-demo`. Its own root contains the two Miles records. The skill installation remains unchanged.

## 1. A local question receives a local answer

Developer request: “Let the second table be purchased at a fixed point.”

This directly confirms the stated local scope. Record the consequential choice in `MILES_DECISIONS.md`:

```md
### DEC-001 — Second-table purchase
Date: 2026-09-20
Scope: Local — second table
Applies to: MVP, all MVP platforms
Status: Confirmed
Evidence status: Untested
Decision: Purchase the second table through its fixed point in the scene.
Rationale: Connect the purchase to the capacity it adds.
Confirmation: Developer's explicit request in the second-table discussion.
Context effect: None. A system-wide construction convention remains open.
Status history:
- 2026-09-20: Confirmed for the second table.
```

The game context continues to contain no general furniture rule. An accepted choice and a proven usability outcome are separate claims.

## 2. Repetition creates a candidate convention

Another table uses a similar point. Miles proposes:

> Use fixed world construction points for every MVP furniture purchase. This would make the convention reusable across tables, equipment, and decorations.

Status remains Proposed. Repetition alone does not authorize the broader scope. The candidate may be logged as DEC-002; it stays out of the active rule register while awaiting approval.

## 3. Explicit system approval permits promotion

Developer response: “Confirmed. All MVP furniture uses fixed world construction points.”

Update DEC-002 to Confirmed, preserve its proposal history, and add this current context entry:

```md
### CTX-001 — Furniture construction
Statement: Furniture purchases use fixed construction points in the world.
Kind: Confirmed design intent
Scope: System — furniture construction
Applies to: MVP only; all MVP platforms
Source: Explicit developer approval of DEC-002 in the construction discussion.
Confirmed on: 2026-09-20
Related decision: DEC-002
Review trigger: Planning a release beyond the MVP.
```

DEC-001 remains the historical local decision. DEC-002 records the broader commitment and its rationale. It references CTX-001 as its context effect.

## 4. A scoped exception preserves the general rule

Developer response in a later feature discussion: “For the MVP, wall posters are bought from the wall catalog. Keep the construction points for other furniture.”

Record confirmed DEC-003 and modify the current rule precisely:

```md
Statement: MVP furniture purchases use fixed world construction points,
with wall posters purchased through the wall catalog.
Applies to: MVP only; all MVP platforms. Wall posters are the named exception.
Source: DEC-002, amended by explicit approval of DEC-003.
Related decision: DEC-002; DEC-003
```

Keep DEC-002's original rationale and append the dated amendment in its status history. The exception gives no authority to move tables or equipment into the catalog.

## 5. A release change supersedes the convention

Fixture premise: the MVP is retired, and Release 1.0 is now the only active release. The developer explicitly confirms: “For Release 1.0, all furniture is selected in the catalog and placed freely, including posters. Retire the MVP construction convention.”

Create confirmed DEC-004 with this exact release scope. Mark DEC-002 and DEC-003 Superseded by DEC-004, with dated status history. Keep DEC-001 as a historical local record with an applicability note that its MVP scope has ended.

Retire CTX-001 from the active rule register and retain its history through the decision links. Add:

```md
### CTX-002 — Release 1.0 furniture placement
Statement: Select furniture in the catalog and place it freely in the scene.
Kind: Confirmed design intent
Scope: System — furniture purchase and placement
Applies to: Release 1.0; all supported platforms; includes wall posters
Source: Explicit developer approval of DEC-004 and retirement of MVP scope.
Related decision: DEC-004
Review trigger: A platform or release changes the placement model.
```

The approval date is populated from the actual confirmation in a real project. This example leaves that later date unspecified.

## 6. An old screenshot does not reverse the rule

A screenshot still shows fixed construction points. Miles records the build uncertainty and asks whether the current task concerns the old implementation when that distinction matters. The current confirmed rule remains Release 1.0's placement model until an authorized change says otherwise.

## 7. A read-only session leaves an explicit patch

With file reading but no write access, Miles can identify the relevant rule and provide the exact proposed edit. The response says:

> Proposed update: replace the active construction rule with the confirmed Release 1.0 rule and link DEC-004. These changes remain unsaved in this session.

No claim of persistent memory or file modification is made. A later authorized write rereads both records before applying the patch.
