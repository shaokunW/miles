# Worked example — the first shop expansion

**Original fictional fixture.** The project, rules, numbers, approval states, and tests below are invented for this example. They supply no facts about the active project.

## Request

> When should the second table appear, and how should the player buy it?

## Relevant confirmed context in this fixture

Project: Paper Lantern Shop. Portrait touch game. The player runs a small craft shop and moves the visible owner by tapping destinations. The introduction has one primary actionable location at a time. A first order teaches service, finishing, payment, and cleanup. Expansion should express increased shop capacity.

The project has no confirmed construction rule covering every furniture item. This assignment concerns the second table only.

## Current design context

Player stage: first order and cleanup completed; ordinary service can now repeat.

Learned knowledge: selecting a world object initiates its relevant interaction, customers occupy tables, and payment adds coins.

Design objective: let the player recognize that earned money can increase capacity, while leaving another order available.

Prototype assumptions: the player has 125 coins; the second table costs 100. These are illustrative tuning values, not a proposed universal economy. The prototype can inspect and revalidate balance before purchase.

## Diagnosis

A silent construction marker may fail to connect the completed order with expansion. A forced purchase, however, would prevent us from observing whether the player independently values the new capacity.

Both statements are hypotheses. The fixture contains no player study.

## Recommendation

Reveal a fixed construction point after the full first-order introduction ends. Let the player inspect the second table and choose whether to purchase it now. Show the added seating capacity in the scene immediately after a successful purchase.

Use the established world-object interaction. Selecting the point opens a small anchored purchase panel showing the table, its capacity benefit, cost, and Buy / Close actions. Tapping the point alone never spends currency.

Alternative considered: force the purchase as the next tutorial step. It makes the action easier to guarantee, but confounds independent understanding with compliance. Choose the optional reveal for this learning goal.

## Player-experience hypothesis

| Beat | Signal and action | Intended interpretation / experience |
|---|---|---|
| First order ends | Payment and cleanup finish; the original table returns to a usable state. | “I completed a service cycle.” |
| Capacity opportunity appears | An empty table footprint gains the established interaction cue and a table silhouette. | “This space can become another table.” |
| Player selects the point | An anchored panel shows capacity and cost. | “My earnings can make the shop larger.” |
| Player buys | The cost is charged once and the table appears. | “My choice changed the shop.” |
| Player continues or pauses | Normal service remains available; the new table can receive customers under existing rules. | “I can use this capacity when I continue.” |

These are intended meanings to test, not observed player thoughts.

## State and transition contract

Eligibility: `introComplete && !table2Owned`. Here `introComplete` includes the first order's cleanup, not payment alone.

| State | Presentation | Input / condition | Transition |
|---|---|---|---|
| Hidden | No second-table purchase cue. | Introduction completes. | Available. |
| Available | Table footprint and established interaction cue. | Select footprint. | Inspecting. |
| Inspecting | Capacity benefit, current price, Buy, Close. | Close or tap away. | Available, with no charge. |
| Inspecting, insufficient coins | Price and missing amount; ordinary service remains available. | Buy attempt. | Stay; explain shortfall without charging. |
| Inspecting, eligible | Confirmed purchase action. | Buy. | Revalidate ownership and balance, then commit. |
| Purchase committed | Table present; balance updated. | Repeated input or reopening. | Owned; no additional charge. |
| Owned | Standard table interaction language. | Select table. | Existing table behavior. |

The design requires an authoritative purchase result. The engineering implementation must determine its transaction and save mechanism. Treat duplicate input and stale balance as explicit test cases.

## Recovery and access

After leaving the panel, the player can complete another order and return. When balance changes while the panel is open, refresh affordability and revalidate at commit. An interrupted presentation reconstructs from saved ownership and balance; animation completion never determines ownership.

Use shape or text alongside highlight color. Respect the existing sound, motion, and input settings. Keep the information readable on the target screen without covering the object it explains.

## Smallest useful validation

Recruit players matching the fixture's novice audience. Start immediately after the first-order introduction. Say, “Continue running the shop,” without mentioning the table.

Observe whether they notice the opportunity, inspect it, understand the capacity benefit, and choose what to do. Declining to buy can be a valid choice. Ask afterward what the footprint offered and what buying would change.

Revise the cue if players consistently interpret it as decoration. Revise the benefit presentation if they identify a purchase but cannot explain its purpose. Revisit the timing if the opportunity repeatedly interrupts a more urgent intention.

Optional events, defined before collection: `expansion_revealed` once per eligible player state; `expansion_inspected` on a closed-to-open panel transition; `expansion_purchased` once on authoritative ownership change. An inspection rate uses unique eligible players shown the reveal as its denominator and a declared observation window. The example claims no target or observed rate.

## Knowledge disposition

Current status: **Proposed**. Scope: **Local — second table**. Evidence: **Untested**.

Explicit acceptance can create a local decision entry with the exact reveal and purchase behavior. It creates no product-wide requirement for fixed construction points. A later proposal that all MVP furniture follows this convention needs separate confirmation and a scoped context entry.
