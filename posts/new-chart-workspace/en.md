Three updates released on October 21 (versions 1.1.356, 1.1.357 and 1.1.358) rebuilt the chart in Period Trader. You can now watch up to four charts at once, set price alerts straight from the price scale, close part of a trade from its tag on the chart, see your backtest and live trades where they happened, and ask the AI assistant to read and mark up the chart you are looking at.

Here is what changed, which parts are in Free and which in Pro, and the safety rules that stayed the same.

## Up to four charts, linked by colour

The chart toolbar has a new **Layout** button with five layouts: one chart, two side by side, two stacked, three (one large plus two) and four in a 2 × 2 grid.

Each chart can join a colour link group: green, blue, orange or purple. Charts in the same group follow each other. By default they share the symbol, the crosshair and the visible date range, and you can also sync the timeframe. Charts that are not linked stay independent.

Any extra chart can pop out into its own window for a second monitor; **Return to main window** puts it back. The main chart always keeps the order ticket and the bot plan, so there is only ever one place where orders are prepared.

A common use: link a higher-timeframe chart and an entry-timeframe chart of the same market, so moving the crosshair on one shows the same moment on the other.

## A market list you can browse

Clicking the symbol name now opens an instrument board: MT5 and Crypto lists with Favorites, All and category tabs, a search box, and sortable columns for price, 24-hour change and volume. Star a row to add it to your favourites, or dock the board on the left of the chart.

Version 1.1.358 added a **Watchlist** next to the MT5 and Crypto lists. A watchlist can mix venues, for example an MT5 forex pair next to a crypto perpetual, and has Gainers and Losers filters. When docked, it shows details for the selected market: the day's change and range, the four forex sessions, a one-hour technical reading (RSI 14, EMA 20/50 and MACD) and this week's calendar events for its currencies. The technical reading describes the indicators; it is not a signal. A missing number shows as a dash with the reason, never a guess. Watchlists are stored on your PC.

## Price alerts that live on the chart

Move the pointer to a price, click the bell beside the price scale, review the alert and press **Save alert**. Saved alerts appear as dashed lines: drag one to move it (Escape cancels the drag) or click it to edit the condition or change its colour. Conditions include above, below, crossing and inside or outside a range.

Since 1.1.358 an alert is drawn on every timeframe of its symbol, and a resizable **Alerts** bar on the right of the chart lists your alerts with pause, remove, a log of past triggers and a shortcut to open each alert's chart.

Delivery options are an in-app notification, a Windows notification and a webhook to a public HTTPS address. Two limits are worth knowing:

- **Your PC checks the alerts.** Period Trader has to be running and connected; the chart window itself can be closed. Nothing is evaluated in the cloud while the PC is off.
- **Alerts never trade.** They do not place orders, deploy a strategy or spend AI credits.

Price alerts are part of Period Trader Pro.

## Managing a trade from the chart

Open positions and pending orders now show as tags on the chart, on the right edge by default (you can move them to the left or middle in chart settings). From a position's tag you can edit the stop loss and take profit, or close 25%, 50%, 75% or the whole position. A partial close follows a few rules:

- It is available for MT5 positions. On crypto venues, a close closes the whole position.
- The size is rounded down to your broker's lot step, and the close is refused if either the part you close or the part that stays open would fall below the broker's minimum lot.
- It is refused while a research bot runs on that symbol, because the bot's own exit expects the size it opened. Close the whole position or stop the bot first.
- The part that stays open keeps its stop loss and take profit unchanged.

Right-clicking the chart opens a menu with buy and sell limit or stop orders at the clicked price, create alert, draw a horizontal line and copy price. An order from this menu is only staged in the ticket: you still review it and confirm it.

The order ticket can also save **presets** for stop loss and take profit. A preset is an amount of money, not a distance: it places the stop where the ticket's size would lose that amount and the target where it would gain the other, around the entry you are composing.

One safety fix shipped in 1.1.357: with one-click trading turned on, switching markets could leave the one-click intent armed, so the next close was confirmed automatically. One-click now applies only to the action it was made for, and a staged ticket always opens its preview.

## Backtest and live trades, drawn where they happened

Version 1.1.358 draws every closed live trade, and every trade of a backtest you choose to show from the Bot plan panel, as a box from entry to exit: green when it made money, red when it lost. Hovering a trade shows a card with the side, the result in percent of price and in money, the entry and exit time, price and reason, the size and the duration. Click to pin the card.

Nothing is recomputed: the boxes come from the stored backtest report and your trade history, and a stop or target the report did not record is not drawn. It makes it easier to see whether a strategy's losses cluster at a certain time of day, or whether live exits look like the backtest's.

## An AI that reads and draws on your chart

The PeriodTrader AI chat now docks beside your charts and stays there in full-screen view. When you ask about the chart, the chat sends what the chart shows along with your message: symbol, timeframe, visible range, last price, your indicators and drawings, and your open positions on that symbol.

It can draw levels, zones, trend lines, order blocks, fair value gaps, break-of-structure marks and risk/reward boxes. These are normal drawings, so you can move, restyle or delete them, and clearing the AI's drawings never removes your own.

It can also prepare an **order card** with side, type, entry, stop loss, take profit, size and risk. The rules are strict:

- Every card carries a stop loss.
- A card that risks more than 5% of the account is refused (you can still size a trade by hand).
- A card expires after three minutes.
- **APPROVE** only stages the order in the chart's ticket and opens the broker preview. Only **CONFIRM** sends it.

The **Education** switch in the chat turns on a mode that keeps answers short and visual: small diagrams, examples drawn on real candles and chart snapshots in the chat. It explains how things work and never tells you to take a specific trade. **Explain with AI** on a calendar event or headline asks the assistant right away. **Ask AI** on a trade box only attaches the trade to the chat; nothing is sent until you press Send.

PeriodTrader AI is part of Pro and uses your AI credits.

## News and the economic calendar on the time axis

Economic releases now appear as flags on the chart's time axis, with dashed lines for upcoming high-impact events. Clicking a flag opens an event card with a countdown and the forecast and previous values. A resizable side panel lists the calendar and recent headlines, filtered by impact or by the current symbol. Spreads can widen and prices can gap around major releases, so seeing them on the chart helps when you review why a trade behaved differently from its backtest.

## Indicator library and smaller changes

- **Indicator library window:** browse by family with search, favourites and live previews computed on the current chart. Since 1.1.358 it also holds your own indicators and strategies, with AI-written descriptions, **Make public** and the Community section inside the same window.
- **Chart settings:** candles, hollow candles, bars, line or area, with your own colours.
- **Accent colour** in Settings > Appearance. Profit and loss colours stay green and red whatever accent you pick.
- Deeper history when you scroll back, your device's time zone by default, sharper rendering, and an instrument list that refreshes when you switch MT5 accounts.

## What did not change

The new chart tools never send an order on their own: an order from the right-click menu or from the AI is only staged until you confirm it, and alerts are read-only. Research bots you deploy keep trading under their own risk guards, as before. Period Trader Free still includes the chart and manual trading on all your brokers and exchanges; PeriodTrader AI and alerts are part of Pro. When an update is available, the dashboard shows a banner with an **UPDATE NOW** button.
