# Upgrade from V1 / V1.1 to V2

V2 keeps the skill name and the two default project-record names. The structural change is the experience-modeling method and its handoff/validation discipline.

## 1. Replace the reusable package

Locate the installation that is actually active. Back up any local changes outside the host's skill-discovery directories. Replace the single `miles-game-experience-designer` folder with the V2 folder. Keep an intended active copy rather than several versions with the same skill name.

The game project's records belong outside that folder. Preserve those records. Check custom installations that mixed game records into the skill before replacing anything.

## 2. Reuse existing authority

Read the actual `MILES_PROJECT_CONTEXT.md` and `MILES_DECISIONS.md`, or the repository's declared equivalents. Preserve accepted facts, rule IDs, scope, source links, and decision history. Keep existing language and formatting where practical.

The initializer is for empty records. It refuses existing records and does not perform migration. Avoid replacing game records with bundled blank templates.

## 3. Extend the accepted model only as needed

Use existing intent to add a concise accepted-model section to Project Context when authorized and useful. Explain relevant goals, quality meanings, concept, functional roles, and reusable rules. Keep a proposed interpretation in a brief or proposed decision until accepted.

An existing entry might say “Portrait; fixed camera; tap input.” The V2 extension can describe how that view limits task awareness at the current scale, which spatial/cue choice addresses it, and what should be checked. The display commitment and the predicted effect retain independent status.

A newly accepted feeling such as “manageable activity” needs its project-specific meaning. Miles proposes it in understandable player terms and shows concrete consequences. Preserve the accepted definition alongside the fact that its effectiveness remains untested.

## 4. Clarify older evidence labels

Where old notes use “confirmed,” inspect whether it means approved intent, implemented behavior, or a research finding. Preserve the original statement and clarify only through the available evidence. Avoid rewriting a previous result into a stronger claim.

For example, “the tutorial is complete” may mean the code path runs. Independent player learning remains a separate question. Add a pending experience-validation note if that distinction is needed for the current task.

## 5. Keep current work proportional

A small control fix can proceed using relevant constraints. A broader redesign can use the full model and handoff. Existing authoritative understanding avoids a repeated project interview.

If a new capability changes an earlier choice, show the affected goal/rule/test dependencies and the specific tradeoff. Preserve decisions outside that scope.

## 6. Check the upgraded package and actual behavior

Run the package validator and unit tests. Then execute relevant scenarios from `evals/scenarios.json` in the intended host/model. Pay particular attention to novice collaboration, platform assumptions, decor function, accepted-but-untested concepts, and outsourcing.

Package validation establishes file integrity. Host/model evaluation establishes how this agent performs on the tested prompts. Player studies establish how an implemented game is experienced. Keep all three reports distinct.
