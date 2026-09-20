# Miles — Senior Game Experience Designer

**A reusable, English-language Agent Skill for player-centered game design and project continuity.**

Miles understands a game's established context, analyzes the player's experience, recommends concrete designs, and keeps confirmed project knowledge separate from current proposals. The skill adapts to the game's audience, genre, platform, creative intent, and production constraints.

Version: **1.0.0**. Reference review date: **2026-09-20**.

## What Miles can help with

Use Miles for onboarding and tutorials, player journeys, world and UI interaction, feedback, progression, pacing, game-experience reviews, and consequential design choices. Give it an idea, screenshot, video, feature, flow, system, or observed player problem.

A typical response leads with a recommendation, explains the relevant player flow and tradeoff, and proposes a useful test. Larger assignments can produce a design brief and handoff. Small questions stay small.

## The knowledge model

```text
Active game project
├── MILES_PROJECT_CONTEXT.md  What this game currently is.
├── MILES_DECISIONS.md        Why important choices were made.
└── Current task / brief     What we are solving today.
```

**Project Context** contains confirmed, scoped facts and intended rules. **Design Decisions** record meaningful choices, rationale, approval status, and evidence. **Current Design Context** contains today's situation and working assumptions.

A local proposal stays local. Explicit approval can confirm it. A confirmed, reusable rule can enter project context within its exact release and system scope. History remains available when rules change.

Game memory belongs to the active game, outside this reusable skill folder. It is ordinary project-file persistence, available when the agent reads those files. The package supplies no separate database, background service, or automatic model memory.

## Install

This package follows the [Agent Skills format](https://agentskills.io/specification). The optional Codex integration follows [OpenAI's skill documentation](https://developers.openai.com/codex/skills/), checked on the date above.

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

### Manual installation for Codex

Download and extract the repository or release archive, then rename the extracted folder to `miles-game-experience-designer`. Alternatively, clone it with that folder name:

```bash
git clone https://github.com/shaokunW/miles.git miles-game-experience-designer
```

For one game repository, run the following from the directory containing the `miles-game-experience-designer` folder:

```bash
mkdir -p /path/to/game/.agents/skills
cp -R miles-game-experience-designer /path/to/game/.agents/skills/
```

Use the active game's actual path. For an existing installation, review and replace the skill directory deliberately; retain the game's context files. Avoid nesting a second copy inside the existing skill directory.

For a user-wide installation instead:

```bash
mkdir -p "$HOME/.agents/skills"
cp -R miles-game-experience-designer "$HOME/.agents/skills/"
```

Choose the repository or user installation that fits your workflow. The included `agents/openai.yaml` provides optional display metadata. Other Agent Skills hosts have their own discovery and installation procedures; follow that host's instructions.

### Initialize project records, optionally

Miles can use existing authoritative records. For a new project, this optional Python 3.10+ standard-library script creates only two empty templates. Run from the installed skill directory:

```bash
python3 scripts/init_project.py \
  --project-root /path/to/game \
  --project-id my-game \
  --project-name "My Game" \
  --dry-run

python3 scripts/init_project.py \
  --project-root /path/to/game \
  --project-id my-game \
  --project-name "My Game"
```

The root must already exist. Review the dry run before creating records. The tool refuses existing Miles files, recognized legacy context filenames, a skill installation as the project root, and ambiguous unsafe path cases. It never overwrites a record or copies the example game's facts. Repeated initialization is intentionally refused; use and maintain the existing files instead.

For existing authoritative filenames, use them directly and record their path mapping. The initializer deliberately leaves migration to an explicit project decision.

An optional [repository instruction snippet](templates/AGENTS_SNIPPET.md) can be added to existing agent instructions after review. It grants no additional permissions.

## Invoke

In a host supporting explicit skill invocation:

```text
$miles-game-experience-designer
Review this onboarding flow. Read the active game's context first.
Focus on what a new player understands, attempts, and expects next.
Recommend the smallest useful change and a way to test it.
```

Other example requests:

```text
Miles, the player completes the first order and then hesitates.
Diagnose the transition using the current build and project rules.
```

```text
Miles, review this tactical HUD. Preserve the difficulty of the decisions
while making available actions and known consequences clearer.
```

```text
Miles, we have confirmed that all furniture purchases use fixed world
points for the MVP. Record the system rule with that release scope.
```

```text
Miles, compare two ways to introduce automation. Tell me what meaningful
responsibility remains with the player in each option.
```

The bundled content is English. Miles responds in the conversation's language unless instructed otherwise; project documentation follows the repository's language convention.

## Project contents

| Location | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Role, workflow, memory rules, response style, and on-demand routing. |
| [agents/openai.yaml](agents/openai.yaml) | Optional Codex skill UI metadata. |
| [references](references/foundations.md) | Seven focused guides plus a source registry. |
| [examples](examples/README.md) | Six classic reference cases and three complete original worked examples. |
| [templates](templates/MILES_PROJECT_CONTEXT.md) | Context, decision log, design brief, playtest plan, and repository snippet. |
| [scripts/init_project.py](scripts/init_project.py) | Safe, explicit creation of blank project records. |
| [scripts/validate_skill.py](scripts/validate_skill.py) | Package-specific structural and local-link checks. |
| [tests/test_init_project.py](tests/test_init_project.py) | Initializer and validator unit tests. |
| [evals](evals/README.md) | Behavioral evaluation prompts, fixtures, and acceptance criteria. |
| [CHANGELOG.md](CHANGELOG.md) | Package changes. |

Progressive disclosure keeps the role instructions focused. Miles loads only the relevant guide, case, or template for the current task.

## Reference library

The conceptual cards cover MDA, Don Norman, Jesse Schell, Raph Koster, Tracy Fullerton, Nielsen's interface heuristics, Valve's empirical playtesting, and Microsoft's accessibility guidance. Each card includes when to use it, original working questions, and a boundary.

The classic cases cover Super Mario Bros., Portal, Breath of the Wild, Journey, Into the Breach, and Factorio. Each separates the sourced description, Miles's interpretation, a possible application, and a test. Book overviews and talk abstracts are explicitly labeled; the package makes no claim that the full books or recordings were inspected.

See the [source registry](references/sources.md) for original links, authors, and evidence limits. Sources and games retain their respective rights. No third-party source files or game assets are redistributed.

## Validate locally

From this skill directory:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
```

The validator checks this package's metadata, required paths, Markdown local-file links, template fields, and evaluation records. It performs no network requests and does not execute an agent. It is a package-specific checker, not a substitute for a host's own validator.

The unit tests exercise file safety and repeat-run behavior using temporary directories. The [validation record](VALIDATION.md) reports the local checks completed for this release. The separate [behavioral evaluation guide](evals/README.md) explains how to test Miles in an actual host and inspect resulting project changes. Structural validation is distinct from demonstrated agent performance.

## Deliberate boundaries

Confirmed design intent remains distinguishable from implementation and from measured outcomes. Simulated player thoughts remain hypotheses. Creative challenge, meaningful uncertainty, and satisfying stopping points remain part of design.

A static screenshot does not establish timing or behavior. An iconic game's success does not prove a transferred pattern. File access and permissions determine whether context can actually be saved. These boundaries are included in the acceptance scenarios.
