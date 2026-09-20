# Decisions, handoffs, and validation

Use this guide for a meaningful tradeoff, a design specification, or an experiment.

## A compact decision brief

State the problem, the current evidence, the intended player behavior and feeling, relevant constraints, and the scope of today's choice. Include the learning or gameplay challenge the design should preserve.

For consequential alternatives, compare only differences that could change the decision. Useful dimensions include clarity, agency, emotional fit, access, production cost, repeat-play cost, consistency, and reversibility. Qualitative comparisons are sufficient when numerical weights would be invented.

Recommend one direction and state the deciding reason, principal cost, uncertainty, and condition for revisiting it. Record approval status separately from confidence in the outcome.

## A usable handoff

Describe eligibility, states, perceptible signals, inputs, transitions, consequences, completion, cancellation, errors, interruption, and recovery. Include relevant copy or layout constraints when requested.

Flag engineering dependencies rather than assuming them: transaction guarantees, save boundaries, concurrent tasks, timing sources, network failure, and accessibility settings. Distinguish design requirements from one possible implementation.

For an external-team specification, follow [Implementation handoff](implementation-handoff.md) and its separate acceptance/experience tracks.

Use [DESIGN_BRIEF.md](../templates/DESIGN_BRIEF.md) when the work benefits from a durable brief. A small UI question usually needs a much smaller answer.

## A testable hypothesis

Write a prediction that could be contradicted:

> If the construction point communicates a purchasable table before selection, eligible new players should identify expansion without being told where to tap.

Then state the evidence that would change the recommendation. For example: repeated attempts to serve another customer instead may indicate a competing intention rather than an unreadable construction point.

## Pick the test to match the question

| Question | Useful approach | Boundary |
|---|---|---|
| Can the player discover and use this control? | Task observation with a representative prototype. | Successful use does not establish enjoyment. |
| What does the player believe happened? | Brief neutral questions after relevant behavior. | An explanation can differ from actual behavior. |
| Does the interaction support the intended feeling? | Play plus contextual, open-ended accounts. | Inferred emotion from clicks alone is weak evidence. |
| Does the pattern improve a population outcome? | Suitable comparative measurement or experiment. | A few observed sessions cannot establish a retention lift. |
| Does the rule hold across states? | State-based review and implementation tests. | Logic coverage leaves perceptual usability open. |

Valve's published playtesting approach frames iteration empirically and discusses both observation and measurement. This skill borrows that stance while keeping each test bounded to its actual method. See [REF-07](sources.md#ref-07).

## Observe with minimal coaching

Recruit for the relevant audience and prior knowledge. Describe a task goal without disclosing the desired input. Record assistance so coached and independent completion remain distinguishable.

Decide whether to use concurrent think-aloud. It can reveal interpretation while also changing attention and pacing; a short retrospective question may better preserve some experiences. Keep collected information minimal and obtain appropriate participant permission.

Record the build, task, segment, sample, relevant settings, observed behavior, and alternative explanations. Treat small-sample findings as opportunities to diagnose and refine. Choose sample size and quantitative analysis for the particular claim rather than applying a universal magic number.

## Instrument with definitions

For each event, define its trigger, uniqueness or repeat behavior, eligibility, and relevant build/variant. Define the denominator and observation window for a rate. Avoid collecting personal data that the design question does not require.

Separate a proposed target from a baseline and an observed result. Report uncertainty and concurrent changes. Completion time, errors, perceived competence, fun, return behavior, and revenue answer different questions.

## Close the loop

An experiment can support, weaken, or leave a hypothesis unresolved. Record the result with its limits, revise the recommendation when warranted, and obtain confirmation for consequential rule changes. Preserve the original decision's rationale and link the new evidence.

Use [PLAYTEST_PLAN.md](../templates/PLAYTEST_PLAN.md) for a reusable test record. Behavioral acceptance tests for Miles itself live in [evals](../evals/README.md).

## V2: tie a decision to an experience model

Reference the applicable goal, defined quality, organizing concept, and functional responsibility. Explain the condition-to-mechanism-to-consequence link that justifies the rule. A decision can support several goals while imposing a cost on another; retain that tension in its rationale.

Report two independent outcomes. Implementation acceptance says whether the specified states and behavior are correct. Experience validation says what was observed and reported by the tested players under the recorded conditions. Correct implementation leaves the experience hypothesis open until examined. A successful session supports only conclusions warranted by its method and sample.
