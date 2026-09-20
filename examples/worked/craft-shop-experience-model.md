# Worked example: from “a cozy shop” to a design model

**Original fictional project. All project facts, acceptance, values, and decisions below are invented for demonstration. Player effects are hypotheses; no playtest was conducted. Keep this fixture outside the active game's confirmed context.**

## Input and established fixture context

The developer says: “Make the opening feel like a cozy shop I can actually run. The decor and equipment should look good together. I have little design experience; give the team something usable.”

Assume the fictional project already establishes:

- A portrait craft-shop game with a visible owner, customers, fixed oblique camera, and tap input.
- Customers choose and assemble a craft; the owner handles finishing, delivery, and resetting a station.
- Personal creations may later be kept, sold, or displayed. Their opening timing remains open.
- The opening's priority is understanding the service role; personal expression supports the longer-term shop identity.
- The prototype uses a 360 × 800 logical viewport and one active service station. These are fixture-specific conditions.

Audience session pattern, grip, and precise color preferences remain open. Target players are people interested in running a small craft shop; this is adopted positioning rather than a demographic finding.

## 1. Miles supplies an understandable interpretation

> “I read this as a small place you can care for: work has a clear purpose, the room shows your taste, and completing service gives you a moment to appreciate what changed. For the opening, I would emphasize being a capable host, then offer a personal choice at the recovery point. That keeps service as the first success while giving the space a reason to become yours.”

The developer can react to that scene. They need no vocabulary about formal experience qualities. If the intention is a lively high-pressure shop, the concept and rhythm can be revised before specifying a tutorial or layout.

## 2. Goal and qualities

**G-01 — Capable host:** after the first service cycle, the player understands what the owner handles and can start another cycle independently.

**G-02 — Personal place:** the player can recognize a visible consequence of a personal choice across visits. This is a supporting goal with an open introduction time.

| Quality | Meaning in this project | Representative manifestation | Tension and check |
|---|---|---|---|
| Understandable work | A player can identify pending service and understand the effect of finishing it. | A ready workstation announces its state; completion settles the cue. | Competes with constant ambient motion. Observe selection and ask what changed. |
| Manageable activity | The player can choose the next task and reach a recovery point. | An order ends in a stable state before the next optional commitment. | Competes with continuous urgency. Observe return/interruption and ask what felt imposed. |
| Personal presence | Prior choices stay recognizable in the room. | A chosen piece remains visible during later service. | Competes with scene density and asset cost. Check recognition and meaning, leaving indifference possible. |

These goals and qualities are proposed translations within the fixture. Approval would establish design intent; their effect remains untested.

## 3. Organizing concept

**C-01 — “Work asks for care; the room remembers your choices.”**

Representative moment: the customer leaves a finished arrangement. A small finishing symbol appears at the relevant station. The player completes service and the station returns to its everyday appearance. After closing that loop, the player can continue service or spend a moment on the room. A displayed creation remains visible later without demanding repeated action.

This concept guides several decisions: state-based attention, a legible completion beat, persistent expression, and a distinction between active work and optional opportunities. It leaves the precise palette and display-inventory carrier open until their requirements are established.

The player's intended conceptual model is: “Customers make the arrangement. I finish and deliver their work. Clearing the station prepares it for another customer. My own creations remain mine until I sell or give them away.”

## 4. How the conditions affect design

| Condition | Mechanism in this scene | Possible experience effect | Design response and uncertainty |
|---|---|---|---|
| Portrait viewport with the stated camera | Limited simultaneous lateral coverage. | The customer and active station may become visually disconnected. | Test their composition together. An off-screen cue is a candidate if framing cannot preserve awareness. |
| Tap input and visible owner | Tapping an object may imply movement, interaction, or selection. | Players may form inconsistent expectations if identical taps change meaning silently. | Reuse the established tap-to-approach/operate contract and show its current state. Confirm actual behavior before choosing new UI. |
| Decor and equipment share a material family | Visual coherence can reduce distinctions if states rely only on object color. | Ready work may blend into ordinary scenery. | Separate object identity from readiness cues. Investigate scene interpretation at target size. |
| Sequential owner service | Arrival bursts can create outstanding tasks. | Busy periods may feel engaging or unmanageable. | Tune arrival patterns and concurrency alongside action effort and delay consequences. |
| Personal objects persist | Choices remain perceptible during later play. | Players may experience continuity or merely visual clutter. | Offer a restrained display opportunity and investigate recognition and personal meaning. |

## 5. Functional responsibilities and concrete rules

| Element / mode | Responsibility | Rule/property proposal | Experience link |
|---|---|---|---|
| Camera in service mode | Keep the current work and its source understandable. | Prototype the customer, station, and delivery destination together at the fixture viewport. Preserve an accessible method to discover any task outside view. | G-01; understandable work. |
| Floor/rug in service mode | Group the work zone and express room character. | Use a stable decorative treatment; reserve the service symbol and ready-state outline for actual pending work. | C-01; expression plus hierarchy. |
| Rug in editing mode | Support deliberate rearrangement. | Selection handles appear only in the editing mode. Exiting editing restores service-state presentation. | Personal presence and mode clarity. |
| Workstation in service mode | Process work and communicate readiness. | Distinguish idle, ready, busy, blocked, and complete through the state contract. Readiness has a recognizable symbol plus text; completion removes the pending cue. | G-01. |
| Growth entry | Make future opportunity available. | Use a stable optional entry after the service loop; interrupt active service only for a separately accepted reason. | Manageable activity. |
| Player creation | Preserve identity and ownership. | Keep the item on cancel; display changes location; sale changes ownership after a confirmed transaction. Keep customer work tied to delivery. | G-02; coherent consequences. |
| Arrival controller | Create activity and recovery. | In the prototype, use named service phases and an explicit recovery state. Advance from recovery through the player's chosen continuation. | Manageable activity; opening scope only. |

The arrival rule is scoped to this proposed opening. Normal business may use a different pattern after the first independent cycle.

## 6. Art and UI direction the team can investigate

Prepare a single furnished scene in service mode and editing mode. Establish a shared material family for room objects, preserve readable silhouettes, and provide a separate task-state symbol. Review environment, characters, equipment, and UI in one composition.

The initial color task is to produce contextual studies within these roles: environment foundation, object materials, characters/creations, and active-state accents. Exact color tokens are an art-direction decision after comparing these studies. The brief does not assert a universal color-to-emotion mapping. Essential information also uses shape, icon, or text. [REF-08](../../references/sources.md#ref-08)

Allowed freedom: pattern, incidental decorative detail, and material treatment within the selected study. Protected relationships: active work remains identifiable, edit affordances are mode-specific, and personal pieces remain recognizable without becoming false task signals.

See the [workstation handoff](workstation-handoff.md) for a narrower prototype slice with exact states and checks.

## 7. The opening follows the model

Proposed sequence: see the customer role → carry out owner finishing/delivery → reset the station → see a stable completed order → independently choose another service cycle or explore an optional personal-space opportunity.

This sequence derives from the established service priority. Making a personal creation before opening remains an alternative if the priority changes. Adding the capability to sell/display creations alone leaves that sequence unchanged until the additional opening cost and experience benefit are considered.

Learning check: on a later, slightly varied service opportunity, remove step-by-step prompts and observe whether the player identifies their responsibility. Correct prompt-following and independent understanding are recorded separately.

## 8. Pacing configuration for the experiment

Use named events and gates before guessing economy-wide timing. For this opening prototype:

| Property | Proposed value / unit | Why it is explicit |
|---|---|---|
| Maximum active customer orders | 1 order | Isolates role learning in the opening only. |
| Arrival after first reset | Wait for player continuation | Creates a recovery point to examine. |
| Later arrival pattern | Outside this experiment | Broader business pressure requires separate design. |
| Hint delay / service durations | Reuse verified prototype values and record them before testing | Isolates this change from simultaneous timing changes. |
| Interrupted opening | Restore the authoritative service state | Keeps understanding and resources consistent. |

This is prototype-ready after the reused timing and persistence contracts are recorded. A production team should flag any missing dependencies. The quality “manageable activity” can later be tested with several active tasks; the one-order value has no product-wide authority.

## 9. Two validation tracks

**Implementation acceptance**

A-01: idle station lacks the ready cue; ready station shows the agreed symbol/text; completion removes it.

A-02: editing mode alone exposes decor selection handles; switching back preserves actual work state.

A-03: the opening recovery phase admits no new order until the continuation action.

A-04: interrupt/reload preserves ownership, accepted work completion, and the current task, under the agreed save contract.

**Experience validation**

Recruit for the adopted target interest, record prior experience, device settings, and the actual sample. Ask the player to get the shop ready for another customer without revealing the desired input. Observe missed states, decorative-object attempts, assistance, recovery, and the next independent action.

Neutral follow-up: “What were you responsible for?” “How did you decide what to do next?” “Was there a point where you felt ready to stop or continue?” “Which changes in this room, if any, feel connected to your choices?”

Revise if the state cue is technically correct yet players repeatedly misread who performs the craft, if recovery feels like waiting without agency, or if personal objects create false work signals. Treat these as different diagnoses; avoid solving all of them by increasing brightness or shortening time.

No results are reported. Small qualitative sessions can identify these problems; a broader retention claim needs its own suitable measurement.

## 10. Knowledge disposition

With explicit approval, preserve the goals, quality definitions, concept, service role, and accepted reusable state-language rules in Project Context. Preserve hypotheses and research status. Record the opening's recovery rule with its opening-only scope in Decisions. Keep numeric settings, alternative color studies, and unresolved personal-creation timing local until their scope warrants promotion.
