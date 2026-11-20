Nine updates since our last product post (versions 1.1.370 to 1.1.378) put much more of a trade's life on the chart: you can trail the stop of any open trade, remove or move a stop-loss with one confirmation, close part of a position and see where a trade breaks even after costs. Around that, strategies the AI writes for you can now go live, research can test against prop-firm rules, and a new Heatmap shows every market at once.

## Managing an open trade from the chart

### Your trades next to your bots (1.1.373)

Manual orders from the chart were blocked while a bot had a trade open. Now only a symbol that already has an open position waits, so your trade never mixes with a bot's. Your manual trades stay yours: no bot counts, closes or takes over a position you opened by hand.

### A trailing stop on any trade (1.1.374)

Press **TRAIL** on an open trade, manual or a bot's, and choose:

- the distance, in price, pips, percent or ATR (1.1.377 adds points and ticks);
- when it starts: right away, after some profit, at an R multiple or at a price;
- a minimum step, a breakeven move, and whether it follows every tick or only closed candles.

It moves the real stop-loss at your broker or exchange, and only ever closer to the price: it never removes or loosens a stop. It works on MetaTrader 5 and every connected crypto exchange except Binance, which has no safe way to replace a stop in one step.

On a bot's trade, your trailing takes over that trade's stop and the bot's own trailing pauses for it; the bot keeps its take-profit and exit signals. You can instead let both run, and the tighter stop wins. Remove yours and the bot trails again.

### Remove, move or split the exits (1.1.375 to 1.1.378)

- **✕ on a line** removes that stop-loss or take-profit. You see a preview first, nothing is sent until you press **CONFIRM**, and the confirmation warns that a trade without a stop has no loss limit. A bot's stop-loss has no ✕: bots always keep one at the broker.
- **✎ on the stop-loss** opens a small pop-up to move it or change the trailing. A gold **TL** tag marks a running trailing stop.
- **Dragging** a stop-loss or take-profit now moves the line at once and shows *Applying…* until the exchange confirms.
- **Several take-profits** on one Bybit trade, each closing part of the position. You can drag each one or cancel it with its x.
- **Partial close** of 25%, 50% or 75% on MetaTrader 5 and Bybit, from the positions menu or by right-clicking the trade. The size is rounded down to the venue's step, and it is refused if either part would fall below the minimum.
- **Add to a Bybit position** you opened yourself: a same-side order averages the entry and keeps your stop-loss and take-profit unless you change them.

The AI chat (Pro) can set, move or remove stops and targets too, and you approve every change.

### Units that mean what they say (1.1.377)

Stops, targets and trailing distances can now be set in points, pips, ticks, price, percent or ATR, everywhere from strategies and backtests to open trades. A 30-point stop is exactly 30 points on every candle.

### Break-even after costs (1.1.376)

A violet **BE** line marks the price where closing the trade would leave zero after its costs. On MetaTrader 5 that includes commission both ways, swap so far and the spread; on crypto, the exchange fee both ways, but not funding.

## Your own strategies, live (1.1.371)

Strategies the AI chat writes for you used to be research-only. They now research, paper-test and deploy live like built-in ones, on MetaTrader 5 and crypto, including auto-deploy and live trials. A few rules keep that honest:

- The AI test-runs the code before saving it, and research sweeps the strategy over its own settings.
- A live bot runs the exact code that was tested. If you edit the strategy after deploying, the bot opens no new trades until you redeploy it.
- Exits, the broker stop-loss and take-profit and the account guards are the same as for built-in strategies. Layered entries and Recovery mode stay built-in only.

## Prop-account research (1.1.370 to 1.1.377)

You can add a Topstep account, answer a few questions about it and backtest a strategy as that account, with a pass or fail against the firm's rules. Research bots can also run on a prop account, so every backtest trades by those rules.

Version 1.1.377 adds **rolling starts**: when a setup passes, the same settings start again from different days of the window, and the card shows "passes from X of Y start days", plus which rule failed the rest. Setups that pass from more start days rank higher, because a pass that depends on one lucky start date is weak evidence.

## Recovery mode, with hard limits (1.1.370)

Recovery mode is an advanced option on **New research**. After a losing trade, the next trades in the same cycle are larger, so that one win can recover the cycle's loss. That is exactly why its worst case matters: a run of losses grows the size at every step.

The app does not hide that. **AI recommended** picks settings from your balance, the instrument's minimum size, spread and volatility, and shows the worst case if every step loses. Each cycle has a hard loss limit the app enforces (10% of the balance by default, 50% at most), and you can add a maximum trade size and a daily loss limit. As with any stop, a gap or a fast market can still push a loss past the plan. A live Recovery bot only starts when you deploy it and confirm; live trials and automatic switching never use it.

> Treat Recovery as a risk setting you choose knowingly, not as a way to avoid losses. Backtest the worst case first.

## Browser tab and your own AI (1.1.370, 1.1.371)

- **Browser tab (Pro):** open a trading platform's website inside the app, stay signed in and let the AI read the page and work in it. Anything that could place an order or move money asks for your approval first.
- **Connect your own AI:** use AI apps such as Claude Desktop, ChatGPT, Cursor or VS Code with Period Trader. You can trust a connection once so routine requests skip the approval card, but real-money actions still need your explicit OK.
- **AI level:** choose Low, Medium or High next to the chat box. Higher levels use more of the shared weekly AI credits per question.

## See more, wait less

- **Heatmap (1.1.378):** every MetaTrader 5 and crypto market colored by today's change and sized by volume, with presets such as Top gainers, Metals or CFD indices. Zoom in on a tile for the day's range and a small candle chart, or click it to open the chart.
- **Pop-out windows (1.1.378):** open any section in its own window.
- **Trade journal (1.1.377):** a clearer trade chart, the best and worst move while the trade was open (MFE/MAE), and on MetaTrader 5 the initial risk and R.
- **Light mode (1.1.371):** uses less CPU and memory on smaller PCs. Live bots, stops and risk never change.

## Updates and safety fixes

**Auto-update (1.1.372)** installs new versions at a safe moment: every open trade has its stop resting at the broker or exchange, no order is in progress, no Recovery cycle is mid-way, and a candle has just closed. A countdown lets you postpone, and installers are checked against the Period Trader LLC signature first.

Other fixes worth knowing:

- Live bots now judge only closed candles, the same as the backtest (1.1.370).
- A **missed-stop safety net**, on by default, closes a bot's position if price stays past its stop while the venue still shows it open (1.1.370).
- Auto-deployed MetaTrader 5 bots follow their trailing again, and a bot whose signal comes right after a restart waits up to three minutes for MetaTrader 5 instead of losing the entry (1.1.377).

Research still runs on your own PC, and every new control above is a tool for managing risk, not a promise about results.
