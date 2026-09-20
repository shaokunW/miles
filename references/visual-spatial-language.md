# Visual and spatial language

Use when evaluating orientation, camera, UI/world composition, palette, decoration, functional equipment, density, or the feeling of a space. Begin with the accepted experience goal and current player situation. The proposed relationships below require project-specific review and testing.

## Inspect the actual viewing conditions

Record what is known: platform, viewport dimensions and aspect ratios, orientation, camera/projection, zoom, safe areas, UI scale, input, text language, and accessibility settings. Distinguish logical design coordinates from rendered pixels. Observe the relevant play mode and representative clutter.

Orientation describes a viewport condition. Grip, reach, environment, and duration need separate evidence or explicitly adopted assumptions. Ask what falls outside the frame, what becomes occluded, and which actions remain discoverable during camera movement.

## Give the scene a functional hierarchy

Identify the player's current intention and the states that could require a change of plan. Assign roles to background, orientation landmarks, functional objects, active demands, optional opportunities, and personal expression.

Compare the world and UI together. Multiple strong signals can compete even when they belong to different layers. Camera framing, silhouette, placement, icons, labels, sound, and motion can cooperate; channel choice depends on visibility, access, atmosphere, and implementation cost.

Protect clarity at points where the player needs informed control. Preserve deliberate ambiguity in exploration or mystery when it serves the experience and leaves the required controls usable.

## Distinguish identity, capability, state, and mode

A machine's recognizable form says what it is. A signifier can suggest an available interaction. A state cue says whether a particular action is available now. Mode determines how the same object behaves.

For each relevant object, specify:

| Field | Example responsibility |
|---|---|
| Identity | Recognizable workstation silhouette or material family. |
| Capability | Indicates where processing is performed. |
| State | Idle, ready, in use, blocked, complete. |
| Mode | Service interaction during business; selection handles during editing. |
| Response | Accepted input changes the correct state and provides feedback. |
| Recovery | Interruption restores a coherent task and understandable presentation. |

Decoration can have information, spatial, narrative, and expressive functions. It can participate in a visual hierarchy without becoming visually empty. Decide whether it is interactive in the current mode and communicate that consistently.

## Design color by role

Separate three questions: what atmosphere is intended, what information color communicates, and how strongly an element attracts attention relative to its surroundings.

Define a palette's roles with representative in-context studies: environment, materials, characters, important objects, state accents, and text/icon contrast. Describe relationships using hue, value, saturation, area, shape, and motion as useful. Reuse approved design tokens when available.

Treat emotional associations as context-dependent hypotheses. “Warm colors create coziness” leaves culture, lighting, contrast, scene content, personal associations, and play events unexplained. Show a candidate scene and investigate its actual reception.

Color may reinforce meaning alongside shape, icon, label, position, or another appropriate channel. Essential information needs such alternatives. Test with the applicable accessibility settings and intended players; simulation filters provide a preliminary check. [REF-08](sources.md#ref-08)

An art change can pass its palette specification while leaving recognition or feeling unresolved. Keep those acceptance and research tracks separate.

## Specify assets as a system

A useful art/UI handoff includes a representative composition at target size; object and material roles; state/mode matrix; required static and animated variants; copy; safe-area and scaling rules; important occlusion cases; and permitted variation.

Separate functional invariants from creative freedom. For example, an artist can vary rug patterns while preserving the service cue's distinctive symbol and readable task area. Select actual colors after reviewing the composition. Unapproved hexadecimal values remain candidate tokens.

## Review the intended relationships

Check empty, typical, and dense scenes; both default and optional modes; disabled or unavailable states; camera edges; relevant aspect ratios; and input obscuration. Use the actual build or clearly labeled static mockups. A screenshot establishes appearance at one moment; timing and transitions require other evidence.

For research, ask a participant to pursue a natural goal. Observe initial interpretation, mistaken selections, and recovery. Follow with neutral questions about what seemed actionable and why. Keep motion/eye-attention claims bounded to the measurement actually performed.

See the [shop model](../examples/worked/craft-shop-experience-model.md) and [workstation handoff](../examples/worked/workstation-handoff.md) for a complete translation.
