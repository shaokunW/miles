# Player-experience diagnosis

Use this guide for a feature, flow, screenshot, video, or reported experience problem.

## Establish an evidence boundary

Record what the artifact contains and what remains unavailable. A still image can support claims about visible elements, hierarchy, wording, and apparent spatial relationships. It cannot establish transition timing, response latency, off-screen controls, or what a real player understood.

A video supports observations within its recording interval and build. A developer report is attributed testimony. Telemetry supports the events actually defined and captured. Keep conflicting sources visible.

Use four compact labels where ambiguity matters: **Observed**, **Confirmed**, **Hypothesis**, **Proposed**. Routine recommendations need readable prose, not a label on every sentence.

## Describe the player at this moment

Use relevant experience, learned controls, motivation, play setting, and access needs. A segment such as “new to management games; has completed the first order” is more useful than an invented name and personality.

Identify the player's current intention as well as the designer's desired behavior. A player trying to deliver an order may ignore an upgrade prompt that seems secondary.

## Walk through consequential beats

| Beat component | Working question |
|---|---|
| State | Where is the player, what is available, and what do they already know? |
| Signal | What perceptible change could attract relevant attention? |
| Interpretation | What meaning might this player infer using learned conventions? |
| Intent | What result would make an action worthwhile? |
| Action | What is the likely attempt, including a plausible mistaken attempt? |
| Response | What immediate change follows the input? |
| Feedback | How does the player connect the action with its consequence? |
| Next intent | What can they reasonably pursue, pause, or return to? |

A walkthrough is a hypothesis generator. Write “a new player may interpret…” rather than reporting an imagined participant as evidence.

## Find the earliest consequential mismatch

An apparent motivation problem can begin with poor comprehension; an apparent comprehension problem can begin with a hidden signal. Trace the dependency before adding rewards or more instructions.

Use this compact diagnosis:

> At [state], [observed feature] may cause [interpretation or action], interfering with [experience goal]. Evidence: [artifact or finding]. Uncertainty: [unknown].

Rank a small number of issues by their relationship to the current objective, possible consequence, and evidence strength. A single blocked progression path can justify investigation even when its frequency is unknown.

## Preserve creative difficulty

Classify the uncertainty the experience intends to preserve. Players may be asked to discover a destination, infer a puzzle rule, time a jump, or sacrifice one tactical advantage for another. Clarify the controls and consequence information required to engage with that challenge fairly.

A puzzle's solution can remain hidden while its available controls stay understandable. A frightening scene can remain unpredictable while pause, subtitles, and essential interactions remain accessible.

## Review beyond success

Inspect mistaken inputs, failure feedback, cancellation, insufficient resources, interruption, repeat use, and returning after a break. Include the point where a player can leave satisfied. Confirm that assistance fades according to evidence of understanding, while help remains recoverable.

For a screenshot review, the useful deliverable is usually: observed hierarchy, primary hypothesis, annotated change description, and the missing interaction to test. Provide precise annotations only when the tools and target artifact support them.

Conceptual background: [Norman, MDA, and usability lenses](foundations.md). Concrete contrast: [tactical UI review](../examples/worked/tactical-ui-review.md).
