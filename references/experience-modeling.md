# Experience modeling

Use this guide when the developer says “make it feel good,” “cozy,” “professional,” “busy,” “immersive,” “suitable for this platform,” or asks for a cross-system design. The method is an original Miles working convention. Its vocabulary draws on the design lenses in [Foundations](foundations.md); the sequence carries no claim of universal scientific validity.

## The responsibility I own

I turn an intention into an experience the developer can picture, a concept the team can share, and decisions they can implement. I propose the translation from available project evidence. The developer can evaluate a concrete scene without first learning design terminology.

Begin with the original intention and its scope. Use a brief scenario to expose the meaning:

> “For this opening, I interpret ‘a cozy shop’ as a place where work stays understandable and your own choices leave a visible mark. You finish an order, see the counter settle, and choose whether to make something for your wall. This would place a pause between guided service and optional expression.”

This is a candidate interpretation. Show the cost or an alternative when the difference would matter. Keep established answers intact.

## 1. Conditions and causal impact

“Affects the work” means a condition changes a relevant possibility, constraint, priority, or test. Explain the mechanism in this particular design.

| Condition | Mechanism | Possible player consequence | Implication / check |
|---|---|---|---|
| Portrait viewport at the present camera scale | Side-by-side space has limited on-screen coverage. | A waiting station may be outside view. | Compare layout, framing, navigation, and off-screen status in the target viewport. |
| Arrival bursts while the owner serves sequentially | Work can accumulate faster than the owner resolves it during the burst. | Urgency may rise; prioritization may become meaningful or overwhelming. | Test arrival pattern, outstanding work, service effort, and consequences together. |
| Decor and ready equipment share the same animated ring | A learned cue refers to two different action states in the same mode. | Players may try scenery or overlook work. | Separate state language or clarify mode; inspect mistaken selections. |
| A player-created object persists in the shop | A later visit contains a recognizable consequence of an earlier choice. | Some players may experience ownership or continuity. | Check recognition and ask what, if anything, the object means to them. |
| Sound may be unavailable in the play setting | An audio-only state change loses its channel. | A player may miss the change. | Add an appropriate visible or other accessible cue; test the setting. |

These are hypotheses and design examples. Their effect depends on the build, player, situation, and competing signals.

Use a counterfactual: “If this condition changed, what would we design or test differently?” Also keep structurally important unknowns visible during discovery, even when their impact is still being investigated.

Distinguish a condition's effect on behavior from affective experience: mood, feeling, or emotional response. Explain each relationship explicitly; the same condition can influence both.

## 2. Goal: the intended player outcome

Describe who, at what point, should understand, do, or experience what. Separate experience goals, learning goals, production constraints, and commercial objectives.

“Player can complete another order independently” is a learning goal. “Player feels capable of caring for the shop” is an experience goal. “Ship two workstations this release” is scope. “Increase repeat sessions” is a business hypothesis or objective. Keep their dependencies visible.

A project can combine management, making, expression, discovery, or companionship. Establish their roles and where priorities change across the journey. Avoid forcing a single permanent motivation for every player or moment.

## 3. Experience qualities: give the feeling usable characteristics

Define a small set relevant to this work. The number is a communication choice. A useful quality card contains:

- **Name and meaning:** ordinary language and a project-specific definition.
- **Manifestation:** a scene or behavior that could express it.
- **Tension:** another valuable quality or constraint it can compete with.
- **Evidence:** what to observe and what to ask the player.

Example:

**Manageable activity:** the player can identify pending work, choose a next action, and reach a recovery point. This can coexist with demanding periods. It competes with continuous urgency. Observe task recognition and recovery; ask what felt under their control and what felt imposed.

**Personal presence:** prior choices remain recognizable in the space. It competes with visual clutter and content cost. Observe recognition and voluntary use; ask which changes, if any, feel connected to their choices.

**Curiosity:** the player can form a worthwhile question and see an approachable way to investigate it. It can coexist with uncertainty. Observe self-directed exploration and ask what they expected to discover.

A behavior is evidence relevant to a quality. It does not uniquely identify an internal feeling: lingering could reflect enjoyment, confusion, distraction, or a technical delay.

## 4. Design concept: coordinate several decisions

A concept is a proposed organizing idea. Write a plain sentence, illustrate one player moment, and explain which choices it guides.

Example: “Work asks for attention when it needs care; personal choices remain visible between tasks.”

Consequences could include state-based workstation cues, a clean completion beat, persistent personal objects, and lower-priority growth entries during active work. These choices share a rationale. A competing high-pressure concept would coordinate cues and pacing differently.

A concept should earn its place by resolving real choices. Test it against at least two relevant decisions, especially one tradeoff. A poetic name alone leaves the design incomplete. One concept can support several qualities; one quality may require several systems. Use links and prose when a single linear table hides those relationships.

The **designer's concept** organizes the work. The **player's conceptual model** is their understanding of roles, possibilities, rules, and consequences. For example: “The customer creates the pattern; I process and deliver it; clearing the station lets service continue.” Show how the world and interface teach that model. [REF-02](sources.md#ref-02)

## 5. Function: assign responsibilities

An element can serve several responsibilities:

| Responsibility | Example question |
|---|---|
| Gameplay | What action, resource conversion, or meaningful choice does it enable? |
| Informational | What state, possibility, or consequence does it communicate? |
| Spatial | How does it frame, separate, connect, or orient the play space? |
| Expressive / narrative | What identity, history, taste, or world meaning does it carry? |
| Emotional / social | What experience or relationship is it intended to support? |
| Temporal | How does it create anticipation, intensity, transition, or rest? |

Give each element a primary role in the current mode and relevant secondary roles. A rug can organize a work zone and express taste. A workstation can transform an item and reveal task status. A trophy can carry a memory. Gameplay bonuses are optional, project-dependent responsibilities.

Look for missing responsibilities, needless duplication, and conflicting signals. Specify how responsibilities change by mode: a decoration may become selectable in editing while remaining stable scenery during service.

## 6. Properties and rules: make the design buildable

Choose the smallest variables that can materially change the intended experience:

- Spatial: framing, scale, placement, occlusion, navigation, grouping, density, touch or pointer targets.
- Perceptual: shape, value relationships, color roles, texture frequency, material, motion, text, sound, haptics.
- Behavioral: state, trigger, available input, consequence, ownership, failure, cancellation, repeat action, recovery.
- Temporal/economic: arrival patterns, service effort, concurrent demands, consequences of delay, resource changes, recovery periods.

Describe relations before specifying unnecessary absolute values. “Current work has a distinct static state symbol while ordinary decor remains unmarked in service mode” is testable. “Make it attractive” leaves the implementer to invent its function.

Use exact values when required for a prototype or implementation. Include units, defaults, bounds or allowed cases, current source/status, and a reason for tuning. Establish the viewport and coordinate system before giving pixel requirements. Preserve existing project tokens where appropriate.

## 7. Trace one decision all the way through

A compact trace:

> **Goal:** feel capable during the first service cycle. **Quality:** understandable work. **Concept:** pending care announces itself. **Function:** a workstation communicates whether it needs action. **Rule:** readiness shows a shape-and-text marker; completion clears it; decoration lacks that service-state marker. **Hypothesis:** players can locate the next job without trying multiple decorative objects. **Acceptance:** each specified state produces the correct marker. **Experience check:** observe unguided selection in a furnished scene and ask what the marker means.

Mark source and confidence at each consequential link. A confirmed hardware condition can support an untested player hypothesis. An accepted concept can coexist with provisional timing.

## 8. Validate in both directions

Forward review: Do these rules plausibly serve the goal, under the named conditions?

Backward review: For each consequential rule, which responsibility or constraint justifies it? An orphan detail may be unnecessary or reveal a missing goal. A goal without any supporting responsibility needs more design.

**Implementation acceptance** tests reproducible state and behavior. **Experience validation** observes intended players and gathers neutral accounts. Technical conformance, completion, emotional response, and business behavior answer different questions.

State an observation that would weaken the current explanation and what you would revise. Inspect competing explanations before changing an accepted creative priority. Use proportional prototypes and iteration. [REF-05](sources.md#ref-05), [REF-10](sources.md#ref-10)

## 9. Persist the accepted model

In the existing Project Context, retain accepted goals, defined qualities, concepts, reusable responsibilities/rules, and their causal rationale. Keep interpretation and evidence status explicit. Reference important decisions and actual research records. Store detailed feature alternatives in the current brief.

When a condition changes, follow the dependencies to affected rules, tests, and decisions. Preserve unrelated commitments. A new ability to display a creation may affect ownership and space; its tutorial placement requires a separate decision.

## Minimum useful outputs

A small question may need one cause-and-consequence paragraph. An ambiguous cross-system request needs a connected model and a concrete scenario. A handoff needs states, rules, acceptance, and test questions. Use the [brief](../templates/DESIGN_BRIEF.md) and [handoff](../templates/IMPLEMENTATION_HANDOFF.md) only to the depth required.
