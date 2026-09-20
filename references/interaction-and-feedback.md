# Interaction, feedback, and attention

Use this guide for controls, world interactions, HUDs, menus, signs, and action feedback.

## Begin with the established language

Read the project's interaction vocabulary and state expressions. Identify what already means selectable, ready, locked, dangerous, completed, or newly available. Introduce a new convention when it creates a justified improvement, with a plan for teaching and consistency.

Describe each control as a contract:

> In [state], [signal] communicates [available action]. [Input] produces [immediate response] and [consequence]. [Alternative input or failure] produces [recoverable result].

This contract is useful across touch, mouse, controller, keyboard, and mixed-input projects. Derive input-specific details from the actual platform and access requirements.

## Design attention for this situation

Identify the player's current task and which information is needed now, later, or on request. Assess competing salience, spatial association, occlusion, contrast, text legibility, motion, and consistency using the actual artifact.

A single primary action can help a tightly guided beat. Exploration or strategy may require several simultaneously legible options. Select the hierarchy that supports the intended decision.

World presentation, NPC behavior, animation, audio, haptics, HUD, and text each have different strengths. Consider perceptibility, localization, camera limits, interruption, and available production resources before choosing a channel.

## Layer the response

Separate acknowledgment of input from confirmation of outcome. The first helps the player know the action registered; the second helps them understand the resulting state. For a networked or delayed action, distinguish pending, successful, and failed states using the project's conventions.

Make rewards attributable. A number changing somewhere else may need a local explanation or a clear connection to the affected resource. Match the strength of feedback to consequence and repetition: a dramatic first achievement and a frequent collection action can need different treatments.

Specify invalid input and reversal. Let players inspect costs before consequential purchases where appropriate. Prevent repeated input from unintentionally creating repeated transactions. Include cancel, back, and interrupted states in the handoff.

## Accessible communication

Microsoft's XAG 103 calls for alternative channels for essential visual and audio information and warns against color-only communication. Its guidance is a reference for review, not a certification of a design. See [REF-08](sources.md#ref-08). 

Apply the principle to this project: pair a color with a shape or label, make essential audio available visually, and retain relevant cues when an optional feedback channel is disabled. Check readability and operation with the game's actual settings and input modes. State untested accessibility questions honestly.

## Useful tradeoff questions

Does the clearer cue reveal a puzzle answer or simply reveal an available action? Does stronger feedback interrupt repeated play? Does an extra confirmation prevent a costly error or burden a harmless action? Does a compact layout preserve accurate interaction on the target device?

A good recommendation states which tradeoff matters and how the prototype will test it. Conceptual reference: [Norman and Nielsen](foundations.md). Counterexample to “clarity removes difficulty”: [Into the Breach](../examples/classics/into-the-breach.md).

## V2: function before presentation

For each signal, identify the responsibility it serves: object identity, interaction capability, current state, consequence, atmosphere, or personal expression. Describe its role in the actual mode. Then choose properties and channels that serve the accepted experience concept.

Review camera, world, and UI together using [Visual and spatial language](visual-spatial-language.md). Trace important choices through [Experience modeling](experience-modeling.md); preserve alternative channels for essential information and deliberate ambiguity where it serves the game.
