Four updates released between October 23 and October 28 (versions 1.1.359 to 1.1.362) change what you can see between "my research bot found something" and "this strategy trades live". You can now read every approval check behind a backtest, keep promising candidates on a watchlist, test them on new candles without placing orders, and give each research bot its own deployment rules.

Here is what changed, how each piece works, and what none of it does.

## Why a backtest isn't approved, check by check

A research bot only names a champion when a backtest passes every check, and on a hard market that can take tens of thousands of backtests. Until then, the bot's card shows its best backtest so far with an equity curve, labelled **Best so far · not yet approved**, and a **Why not yet:** line with the first check it failed.

Version 1.1.360 adds the full picture. In a research bot's **All backtests** list, every row now has a **CHECKS / WATCH** button next to **DETAILS**, and the best backtest's curve has **ALL APPROVAL CHECKS / WATCH**. Either one opens a Research review with a single table: each check, the backtest's actual value, the requirement, and a status of **Pass**, **Not passed** or **Not evaluated**.

The checks come in three groups:

- **Research quality:** the quality grade, research eligibility and walk-forward validation.
- **Unseen data (holdout):** the saved verdict on data kept apart from the search, a statistical score against the threshold saved with that evaluation, at least 15 holdout trades and 40 trades overall, a positive holdout net result, a holdout profit factor of at least 1.10, known trading costs, and an average win at least three times the average round-trip cost.
- **Your deployment rules:** minimum trades, a positive return after costs, maximum drawdown, minimum profit factor, maximum single loss and, if you require one, a trading style.

Each row says where its number comes from: recorded with the backtest, a saved evaluation, your bot's current rules, or a fixed default that an older backtest may not have recorded. Three items are listed as **Not evaluated** on purpose, because they are only checked when you deploy: live cost pricing, account and execution safety, and the Decision AI check. Opening the review spends no AI credits.

Three rules from the dialog are worth repeating:

> The holdout score is not a profit percentage or a probability. Missing evidence is not a pass. A "recorded champion" label is historical, not permission to trade now.

Below the table you can expand every recorded rejection reason, the exact parameters and costs the backtest used, and its recorded metrics and validation.

## A watchlist for promising candidates

**Watch this candidate** saves the backtest and freezes a copy of it, so it stays readable even after older results are cleaned up. **SAVED / RETAINED / WATCHLIST**, next to **All backtests**, lists three kinds of results together: the ones you saved, the ones you are watching, and the ones the app keeps automatically.

Since 1.1.360 each research bot keeps the complete original results of its best 100 backtests, plus protected results. Older results whose trades were never saved can still show as unavailable; they are not rebuilt and passed off as the original.

None of this approves anything. As the list itself puts it: saving is not approval.

## Forward tests that never place an order

A backtest, even one with an unseen holdout, still uses the past. Version 1.1.360 lets you see how a candidate behaves on candles that did not exist when you picked it.

Once a backtest is on your watchlist, **Start order-free forward test** freezes its exact configuration and the app's backtest engine, then runs the strategy on each new closed candle:

- **Only candles that open after you start count.** Earlier history is used only to warm up indicators.
- **It reads closed candles from the app's verified candle cache.** If no new candle has arrived, the test waits; nothing is filled in.
- **Costs are the ones recorded with the backtest.** A backtest with missing or zero recorded costs is refused, so you never get a cost-free simulation.
- **Simulated equity counts closed trades only,** after those costs. A trade still open at the latest candle is not counted as a closed one.
- **It runs while Period Trader is open,** checking active tests in the background, and you can press **Refresh evidence** at any time. **Stop evaluation** ends a test and **Export evidence** saves its full record as a JSON file.

Some limits are deliberate. Up to 20 forward tests can run at once. They support the built-in strategies; custom strategies and layered setups are refused with a message instead of being swapped for something similar. If you switch the trading account, or the app's engine changes (for example after an update), the test keeps its evidence but cannot continue, and you start a new one. Earlier observations are never rewritten.

Most importantly, a forward test sends no orders and does not approve, deploy or change the saved holdout verdict. It is extra evidence, not a gate.

## Ask PeriodTrader AI about a research bot

**Ask PeriodTrader AI** in the review attaches the backtest to the chat with a suggested question, for example to explain every check that passed, failed or was not evaluated. Nothing is sent until you press Send. The assistant can read a bot's recorded parameters, validation evidence, saved trade history and forward tests. These research tools are read-only: reading them changes nothing, starts no test and deploys nothing. PeriodTrader AI is part of Pro and uses your AI credits.

## Deployment rules per research bot

Version 1.1.359 lets each research bot follow the global deployment rules (Settings → Deployment) or its own. Open the bot's menu → **Deployment rules…** and choose **Use the global rules** or **Use this bot's own rules**: minimum trades, minimum profit factor, maximum drawdown, maximum single loss, and a trading style you prefer or require. **Use recommended** fills in suggested values, and the New research form offers the same choice when you create a bot.

A risky choice shows warnings and asks for a second click (**Save anyway**); the decision stays yours. A stricter rule re-grades the bot's stored backtests at once, and if the champion no longer passes, the best stored backtest that does takes its place. A looser rule applies from the next backtests on. The AI assistant can only tighten a bot's rules; anything looser needs your approval. Changes are listed in the bot's change history.

## Deploying a backtest that isn't a champion

Automatic deployment still only takes an approved champion. You can now deploy another backtest yourself with **DEPLOY THIS BACKTEST…**. The app first lists every check it fails and warns that it can place real orders when its strategy signals; it only goes live if you confirm. Auto-deploy and the AI never give that confirmation.

The hard safety checks still apply: pricing, exchange keys, leverage limits, your plan, open positions and bot limits. A backtest whose trade record is missing or incomplete has to be re-run first; the app offers to do that (about a minute) and deploy the new result.

## When a search is taking long

When a research bot has run more than 15,000 backtests without an approved champion, its card shows **Taking long**, the count, and a higher timeframe that may find more (for example 1H or 4H for a 15-minute bot). **Ask AI why** opens the chat for a plain explanation. Nothing changes by itself: trying another timeframe means creating a new research bot.

## Live trades and charts

Versions 1.1.361 and 1.1.362 focus on live accuracy. Deployments keep the correct entry candle, the stop loss and take profit drawn on the chart stay aligned with the protection your broker or exchange confirmed, and current trades get clearer chart markers and lot labels. Backtest equity and drawdown charts, the messages when data is missing or a curve is being rebuilt, and the journal were improved too. Existing strategy risk settings and your original trading history are preserved.

## Smaller changes

- **Back to research:** opening a saved backtest on the chart marks it **Backtest preview · read only**, with its trades on the chart and its original parameters and saved metrics in the Bot plan. Order fields stay disabled, and **Back to research** returns you to where you were.
- **Indicators:** 30 more analytical studies in the indicator library.
- **Connections:** setup offers MetaTrader 5, Binance, Bybit, MEXC and OKX. Saved connections are kept.
- **Sign-in:** after updating to 1.1.359 or later, sign in with Whop once. Your plan, broker connections and settings stay as they were.

## What did not change

Reviewing, watching, saving and forward testing are read-only: none of them places an order, approves a backtest or deploys a bot. Automatic deployment keeps its normal checks, and live bots keep trading under their own risk guards. When an update is available, the dashboard shows an **UPDATE NOW** button.
