# Worked example: quiet tension in a survey game

**Original fictional example. All project conditions and decisions are illustrative. No playtest results are claimed.**

Input: “Make this abandoned observatory feel unsettling, but let players understand their equipment.”

Assumed context: single-player first-person exploration on desktop with mouse/keyboard; players survey rooms using a signal meter; the current build has controllable movement and an explicit calibration operation. The creative goal is uncertainty about the environment while retaining understandable control of the tool. These are fixture conditions, separate from the shop example.

## Goal and qualities

**Goal:** players choose to investigate an ambiguous signal while understanding the cost and reliability of their own measurement action.

**Uneasy anticipation:** incomplete environmental evidence gives the player a question that feels worth investigating. Observe approaches, retreats, and accounts of what they expected.

**Instrumental confidence:** the player can explain whether the meter is calibrated and whether a reading succeeded. Observe calibration use and ask what information the instrument supplied.

These qualities can conflict if every control is made obscure or every mystery is explained through UI. Their boundaries define the design.

## Concept

**“Trust the instrument's operation; investigate what its readings might mean.”**

Representative moment: the calibrated meter records a valid reading, yet its pattern changes near a sealed room. The player understands that the device worked and chooses how to interpret the result. The world supplies several clues without revealing a guaranteed explanation.

The intended player model is: “Calibration determines reading reliability. A successful reading gives evidence, and I decide what it suggests about the room.”

## Functions, rules, and consequences

| Element | Responsibility | Proposed rule | Hypothesis / tension |
|---|---|---|---|
| Meter status UI | Make tool state understandable. | Distinguish uncalibrated, sampling, valid, and failed using symbol plus label. | Supports control understanding while preserving environmental ambiguity. |
| Environmental clue | Invite interpretation. | Present a signal pattern with more than one plausible in-world explanation. | May encourage curiosity; could instead seem arbitrary without supporting clues. |
| Audio | Support atmosphere and signal presence. | Essential reading status also has an appropriate visual channel. | Maintains the task information when audio is unavailable. |
| Room lighting and materials | Establish setting and spatial orientation. | Review navigation landmarks separately from ambiguous narrative details. | Supports movement while reserving uncertainty for the fiction. |
| Sampling cadence | Create anticipation. | Use a provisional sampling interval with a clear progress indication and cancel behavior. | Waiting may create tension or mere irritation; test within the full scene. |

Desktop input does not prove genre expertise or a preferred difficulty. A desaturated palette alone leaves the emotional hypothesis unresolved. The unsettling experience depends on world evidence, timing, interpretation, agency, and player expectations together.

## Acceptance and experience validation

Acceptance: each meter state has the specified cue; cancellation ends sampling without a valid result; a failed reading is distinguishable from a completed reading; required status survives muted audio. These remain unexecuted cases.

Experience test: give the player an exploration goal without identifying the sealed room. Observe whether they use the meter coherently, what they investigate, and how they recover from failure. Ask what they trusted, what remained uncertain, and what they expected from the room. Separate intended apprehension from confusion about controls.

If players understand the tool but ignore the room, examine the clue's meaning and motivation. If they approach repeatedly because they think calibration failed, repair the state language before increasing ambiguity. If every interpretation becomes obvious, revisit the environmental evidence while preserving the agreed control model.

## Scope and memory

With approval, preserve the distinction between reliable tool operation and ambiguous environmental meaning as a scoped experience principle. Retain predicted effects as hypotheses. Keep sampling intervals and room-specific clue placement local until reusable rules are explicitly accepted.

This example uses the same Miles method to preserve tension and ambiguity. “Comfortable,” “fast,” and “one obvious next action” have no automatic product-wide priority.
