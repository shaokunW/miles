# Miles — Senior Game Experience Designer

**An English-language Agent Skill for understanding a game, modeling its intended experience, and producing designs a team can execute and evaluate.**

Version: **2.0.0**. Release date: **2026-09-20**.

Miles translates intentions such as “cozy,” “satisfying,” “a real shop,” or “suitable for short visits” into understandable qualities, coherent concepts, element responsibilities, and concrete rules. The developer can express impressions and priorities; Miles supplies the design translation and explains tradeoffs through player situations.

## The V2 core

```text
Understand the game and the current situation
    ↓
Explain condition → mechanism → player consequence → design implication
    ↓
Goal → Experience qualities → Design concept → Functional responsibilities
    ↓
Properties and rules → Implementation acceptance + Experience validation
    ↓
Preserve accepted knowledge, with scope and evidence intact
```

These are flexible working aids. Small questions can use a cause-and-consequence paragraph. A broad opening or external-team handoff receives deeper modeling. A new feature is evaluated through the game's accepted direction; its introduction does not automatically change earlier priorities.

The method applies to different genres and experiences, including demanding decisions, deliberate uncertainty, and tension. Platform, camera, input, audience, visual style, and business model are confirmed or explicitly provisional project conditions.

Start with [SKILL.md](SKILL.md). The detailed [Experience modeling guide](references/experience-modeling.md) explains goal, quality, concept, function, rules, and validation. The [craft-shop example](examples/worked/craft-shop-experience-model.md) and [workstation handoff](examples/worked/workstation-handoff.md) show a complete translation. The [horror example](examples/worked/quiet-horror-experience-model.md) preserves a different intended feeling.

## Project knowledge

```text
Active game project
├── MILES_PROJECT_CONTEXT.md  What the game is and how its intended experience works.
├── MILES_DECISIONS.md        Why consequential choices were made.
└── Conversation / brief     The question, candidates, and details being worked on.
```

The accepted experience model lives inside Project Context. Keep its intended goals and predicted effects explicitly distinguished. Design approval, empirical support, and scope are independent. A passed implementation test leaves a player-feeling hypothesis open.

Game records stay outside the reusable skill directory. Reuse an existing authoritative equivalent rather than creating a second source of truth. File persistence requires an agent with appropriate read/write access; this package supplies no autonomous background memory service.

## Install or upgrade

The package uses the [Agent Skills directory format](https://agentskills.io/specification), with optional metadata in `agents/openai.yaml`. Codex documents repository `.agents/skills` and user `$HOME/.agents/skills` locations in its [official skill guide](https://developers.openai.com/codex/skills/). These pages were checked for this release; see [Sources](references/sources.md) for access details.

### Install from GitHub (recommended)

With Node.js and npm installed, run:

```bash
npx skills add shaokunW/miles -g
```

The [Skills CLI](https://github.com/vercel-labs/skills) downloads Miles from GitHub and lets you choose which supported agents to install it for. `-g` installs it for your user, making it available across projects.

To install only for Codex:

```bash
npx skills add shaokunW/miles -g -a codex
```

For installation in a single game repository, run this from that repository's root and omit `-g`:

```bash
npx skills add shaokunW/miles -a codex
```

To list the available skill without installing it:

```bash
npx skills add shaokunW/miles --list
```

The skill's invocation name is `miles-game-experience-designer`; `miles` is the GitHub repository name.

### Fresh manual installation

Extract the archive. Place its single `miles-game-experience-designer` folder in either:

```text
~/.agents/skills/miles-game-experience-designer/
```

or, for a repository-scoped installation:

```text
your-game/.agents/skills/miles-game-experience-designer/
```

Use one intended active copy so duplicate skill names do not create ambiguity. Other hosts may use different discovery mechanisms. The archive is a skill directory, with no plugin manifest or bundled installer. The GitHub installation above uses the external Skills CLI.

### Existing V1 / V1.1 installation

Back up local modifications, replace the installed reusable skill folder deliberately, and preserve the active game's context and decision files. Keep backups outside skill-discovery directories. Avoid copying the new folder inside the old one as another nested directory.

Read [MIGRATION.md](MIGRATION.md). Existing accepted project knowledge remains valid within its scope. The templates are for empty records; the initializer refuses existing records. Upgrade requires no automatic rewrite, new database, or separate experience-model authority.

## Invoke

In a host supporting explicit `$` skill invocation:

```text
$miles-game-experience-designer

Help design the trial opening of this game. Read the active project's
context and vision first. Establish or reuse a connected understanding,
then translate the intended experience into a concrete player flow.
Explain the relevant causes, tradeoffs, implementation requirements,
and a way to test what the player learns and feels.
```

Other useful requests:

```text
Miles, I want this space to feel like a shop I care about. I have little
design experience. Propose an understandable interpretation, then show
how it changes the camera, decoration, equipment cues, UI, and rhythm.
```

```text
Miles, turn the accepted direction into a brief for an external team.
Specify the named slice, state behavior, visual roles, adjustable values,
recovery cases, implementation acceptance, and experience validation.
```

```text
Miles, review this tactical HUD. Preserve difficult decisions while
checking whether the player can understand available actions and results.
```

## Optional initialization

Python **3.10+**, standard library only. Run from the installed skill directory using the actual, already existing game root:

```bash
python3 scripts/init_project.py \
  --project-root /path/to/game \
  --project-id my-game \
  --project-name "My Game" \
  --dry-run
```

Review the paths. Run the same command without `--dry-run` only when empty record creation is intended. The initializer creates two blank templates with identity metadata; it infers no gameplay facts. It refuses existing Miles records and recognized legacy records, unsafe roots, and direct writes inside the skill. An explicit migration is required for existing files.

An optional [repository instruction snippet](templates/AGENTS_SNIPPET.md) can be adapted to the actual repository's instructions and record paths. It grants no extra authority.

## Package map

| Area | Contents |
|---|---|
| `SKILL.md` | Role, core workflow, knowledge rules, and on-demand routing. |
| `references/` | Project understanding, experience modeling, visual/space design, interaction, onboarding, pacing, handoff, evidence, foundations, sources. |
| `examples/classics/` | Six source-bounded case analyses retained from V1.1. |
| `examples/worked/` | Fictional discovery, complete experience models, handoff, expansion, lifecycle, and tactical review. |
| `templates/` | Two persistent records and optional brief, handoff, playtest, and repository templates. |
| `scripts/` | Safe empty-record initialization and package-specific structural validation. |
| `tests/` | Deterministic script and package-integrity tests. |
| `evals/` | Behavioral scenarios for a real host/model evaluation. |

Sources are linked with attribution and inspection limits. The package redistributes no third-party game assets, book text, slides, or recordings. The Goal/Quality/Concept/Function workflow and worked designs are original adaptations, with references used as design lenses.

## Validation

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

The validator checks package paths, metadata conventions, local Markdown file links, template fields, and evaluation records. It uses a deliberately narrow parser for this package, not a general YAML or Markdown implementation. It performs no network request, player study, or agent execution.

See [VALIDATION.md](VALIDATION.md) for checks actually run. See [evals/README.md](evals/README.md) for behavioral testing. Included scenarios are test specifications; they become evidence only after execution and review.
