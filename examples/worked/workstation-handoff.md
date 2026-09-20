# Worked handoff: a workstation that announces pending care

**Original fictional prototype. Values are proposed settings; no assets, game code, or player results are claimed to exist. This specification applies to an isolated prototype slice.**

Project: the fictional [craft-shop example](craft-shop-experience-model.md).
Delivery level: **Prototype-ready**.
Approval: Proposed.
Experience evidence: Untested.

## Purpose and included scope

Help a first-time player find pending owner work while the furnished room retains its everyday character. The station's responsibility is to communicate service state and accept the correct selection. This supports understandable work under the concept “Work asks for care; the room remembers your choices.”

Build one station-state presenter and its selection behavior in a test scene. Include a non-interactive decorative object and a simulated editing mode. Exclude processing gameplay, save-system implementation, customer scheduling, economy, inventory, and complete game navigation.

The harness supplies authoritative station state, mode, selection eligibility, a static world projection, and an acknowledgment/failure response to selection. Those input names are proposed test interfaces. The real repository may supply equivalent contracts.

## Behavior contract

| State in service mode | Visible treatment | Selection behavior | Next state |
|---|---|---|---|
| Idle | Base object; no task-state marker. | Optional base selection response is outside this slice; emit no work intent. | Set by harness. |
| Ready | Static work icon plus “Ready to finish” label. | Emit one work intent per activation; disable repeats while awaiting acknowledgment. | Pending. |
| Pending | Keep task identity; replace label with “Opening…”. | Additional input emits no extra work intent. | Busy on acknowledgment; Ready with “Try again” on failure. |
| Busy | Static progress-status icon plus “Finishing”. | Emit no new work intent. | Set by harness. |
| Blocked | Distinct warning icon plus supplied plain-language reason. | Emit one inspect-reason intent per activation. | Set by harness. |
| Complete | Show “Finished” briefly, then stable base appearance. | Emit no work intent. | Base appearance while state stays complete. |

Decor carries no service-state marker or work intent in service mode. In editing mode, decor becomes selectable with an edit handle; the station emits selection-only intents and suppresses service input. Return to service mode renders the current authoritative service state.

The Ready prompt and state labels use shape/icon plus text. State identification remains available with sound and motion disabled. [REF-08](../../references/sources.md#ref-08)

## Presentation and parameters

Coordinate system: logical prototype units, target viewport 360 × 800; render scaling maps the logical canvas into the test viewport. These values serve this fixture only.

| Parameter | Proposed default | Function / allowed adjustment |
|---|---|---|
| `marker_anchor` | Projected top-center of the station, offset 12 units upward | Tie status to its source; adjust for silhouette and occlusion. |
| `label_font_size` | 16 logical units | Starting readability setting; test real-device appearance. |
| `marker_icon_size` | 20 × 20 logical units | Starting symbol size; preserve distinction between work and warning icons. |
| `selection_region` | Station projection expanded to at least 48 × 48 logical units | Prototype activation area; resolve any overlap explicitly. This is a candidate size rather than a cited universal standard. |
| `completion_hold_ms` | 800 ms | Temporary transition feedback; completion also has a stable absence of pending work. |
| `pending_timeout_ms` | 3000 ms | Test-harness failure timeout; returns to Ready and enables retry. Real integration must use the game's operation result contract. |
| `motion_enabled` | False | Static baseline for the experiment. |
| `audio_required` | False | All necessary information is available visually in this slice. |

Required assets: base station shape, decorative object, distinguishable work/warning/status symbols, plain text labels, and edit handle. Prototype geometric placeholders are acceptable. A production art package needs its own approved style tokens and export requirements.

In this fixture the station is fully visible. Off-screen behavior is excluded and requires a separate decision before extending this slice to off-screen tasks.

## Invariants and failure handling

The presenter reflects the supplied work state. Only a valid Ready activation emits a work intent. A pending request suppresses duplicates until its acknowledgment, failure, or timeout. Editing changes selection behavior without changing authoritative work state.

On a harness reset or simulated resume, clear view-local pending timers and render the newly supplied authoritative state. The presenter has no authority to grant rewards or restore inventory. The real game's operation and persistence contracts remain dependencies for production integration.

State changes cancel incompatible completion/pending timers. A complete-to-ready transition immediately replaces the completion cue with the ready cue. Input cancellation before activation emits no intent.

Creative freedom: incidental prop detail and base material studies. Protect marker identity, state transitions, label legibility, and decor/work separation.

## Implementation acceptance

| ID | Given / When | Then |
|---|---|---|
| A-01 | Idle state renders in service mode. | Base station only; zero pending-work cues. |
| A-02 | Ready state renders with sound and motion disabled. | Work icon and readable ready label remain. |
| A-03 | Ready is activated twice before acknowledgment. | Exactly one work intent; Pending presentation follows the first. |
| A-04 | Pending receives failure or times out. | Ready with retry label; one new activation can emit one intent. |
| A-05 | Busy changes to Complete. | Completion label appears for the configured duration, then ordinary appearance; no new work intent. |
| A-06 | Complete changes to Ready before its timer finishes. | Ready cue remains visible after the old timer would have expired. |
| A-07 | Switch to editing, select decor, then return to service. | Selection-only intent in editing; decor has no service marker on return. |
| A-08 | Simulated resume supplies Busy while the view was Pending. | Busy presentation; prior view-local timer cannot restore Ready. |
| A-09 | Pointer/touch is canceled before activation. | Zero selection or work intents. |

All cases: **Pending execution**. Passing these cases establishes prototype contract conformance only.

## Experience validation

Task: “A customer has work ready. Continue helping them.” Show a furnished scene with the station and decoration, keeping the solution undisclosed. Record the actual test audience, device, prior experience, and any assistance.

Observe first selected object, repeated mistaken attempts, whether the label explains the owner's responsibility, and recovery after a simulated failure. Ask afterward: “What did you think needed doing?” “How did you know?”

Hypothesis: state-based cues help players identify the correct pending service while leaving ordinary decor interpretable as part of the room. Alternative explanation: the player selects the station because it is alone or because of prior familiarity. Vary representative clutter and prior experience before making a broader claim.

Revision signals: players perceive “Ready” as customer readiness to begin their own craft; the label occludes the work; decoration draws repeated false selections; retry leaves players uncertain whether the previous action happened. Each would justify a different change.

The prototype leaves overall coziness and long-term ownership untested. Those require play that includes the broader room and repeated visits.
