# Worked example — a tactical interface review

**Original fictional fixture.** No screenshot or player study is bundled. The visible details below are explicitly supplied observations for the exercise.

## Established project context

A desktop turn-based rescue game uses mouse and keyboard. Its player promise is difficult rescue tradeoffs with understandable consequences. Selecting a unit previews its available actions. Some enemy behaviors are deliberately hidden until scouted.

## Supplied artifact description

The review concerns a still image. The selected rescue action shows a destination outline. Revealed hazards appear as red circles. A narrow side panel lists actions, but the supplied description does not establish how hazard timing or damage details are displayed during interaction.

User request: “Make this easier to understand without making the strategy easier.”

## Example Miles response

**Keep the rescue tradeoff. Strengthen the preview of revealed consequences.**

The supplied image shows destinations and hazard areas, but it leaves their order of resolution unclear. I would first check the existing hover and selection states; the still image alone cannot show whether that information is already available.

My main hypothesis is that players may see where a hazard is located while misreading when it resolves. Add a compact resolution-order marker to revealed hazards and show the selected move's affected units in the action preview. Retain hidden information for unscouted behavior, as the current rules require.

The player flow becomes: select a unit → inspect an action → read the known consequences and explicit unknowns → choose the rescue tradeoff → confirm → see those consequences resolve.

The cost is additional visual information. Prefer displaying details on the selected action and inspect state, with a clear route to inspect again. Pair hazard color with a distinguishable symbol. Avoid introducing a suggested best move; choosing between consequences is the intended challenge.

To test this, ask players to predict the result before committing a move, then compare that prediction with the actual outcome. If they predict correctly but still deliberate over whom to rescue, the interface may be supporting the intended strategy. Repeatedly incorrect timing predictions would point to a communication problem.

This is a **local proposal** for action previews. The existing rule about hidden enemy behavior remains unchanged. No persistent project update has been confirmed.

## Why this is a useful acceptance example

The response checks the evidence boundary, uses the established input model, preserves creative intent, names an uncertainty, provides a concrete intervention, and proposes a test. It remains applicable to a genre and platform very different from the shop fixture.

Reference connection: the [Into the Breach case](../classics/into-the-breach.md) motivates a clarity-versus-choice question. It supplies no proof that this fictional preview will succeed.
