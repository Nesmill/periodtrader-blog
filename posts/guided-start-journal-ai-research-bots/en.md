Five updates released between October 31 and November 5 (versions 1.1.363 to 1.1.367) change the first ten minutes in Period Trader and a lot of what happens after them. There is a new welcome and sign-in, guided tours, a Brokers & exchanges page that connects several crypto accounts at once, a redesigned trade journal, and an AI assistant that can create research bots for you.

Below is what changed, where to find it, and a few things that deliberately did not change.

## A first run that explains itself

The sign-in screen now says what the app is and how it works before it asks for anything. Signing in with Whop is the main button; a licence key is the second path. After you sign in through Whop in your browser, you are sent back to the app and your plan refreshes straight away.

If you have no research bots yet, the Bots tab shows a short welcome instead of an empty list: three steps (**Research**, **Check**, **Trade**) and a get-started checklist that ticks itself off as you go:

1. **Connect a broker or exchange**
2. **Start a research bot**
3. **Take the tour**

The old START HERE card is gone. In its place are guided tours: step-by-step pop-ups that point at each part of the main page, the Broker page and the Chart tab (the chart tour starts the first time you open it). Nothing changes and nothing is traded while you read. Each tour runs once, and you can replay it from the **Tour** button in the header or from Settings.

**New research** now opens a pop-up with four questions:

- **Which market?** Crypto, forex, gold or indices (forex and gold need MetaTrader 5).
- **Candle size**, with a reminder that smaller candles mean more trades and shorter holds.
- **When it finds a strategy that passes**, so you decide up front what the research bot does with a result.
- **Risk per trade**, shown with a money example so the percentage means something.

Everything else sits under **Advanced options**.

On the Free plan, the upgrade box no longer opens by itself at every start. Trying a Pro feature shows a small note instead, and the box opens only when you ask for it, for example from **FREE · Upgrade** at the top.

## Brokers & exchanges: several accounts, one ticket

The Setup page is now **Brokers & exchanges**. It starts with one question, where you want to trade: Bybit, MetaTrader 5 or another exchange. You then see only that part.

You can now connect several crypto exchanges at the same time, one saved account per exchange. The one you select is the default for charts, manual trades, research data and new bots, and every crypto bot records which exchange it trades on. What that means in practice:

- The order ticket has an **Account** picker. A market or pending order goes to the account you picked, and the app refuses an account that is unknown or not connected.
- **New research** and the live bot card have an **Account** picker too.
- Open positions, close-all and the crypto kill switch cover every connected account.
- With no MT5 terminal connected, Charts opens on Bitcoin from your exchange instead of an empty MT5 chart.

### TradFi markets on Bybit and Binance

Both exchanges list perpetual contracts on stocks, ETFs, commodities and forex. They now appear in the chart's market picker, grouped by type with their full names. For Binance, the app reads each contract's real specifications, so stop-loss and take-profit prices round to the correct tick, and it refuses an order before sending it when the contract's trading session is closed.

On Bybit you can also chart and trade **xStocks** (stock tokens on Bybit's spot market) and see option chains in an **Options** tab of the market picker. These orders use a separate ticket that shows a preview you confirm; the app re-reads the price, and a market order whose price moved more than 5% is refused. Research bots and the regular chart ticket stay with perpetual contracts. If an exchange refuses an order because its one-time TradFi terms were not accepted, the app tells you that.

## A new trade journal

The trade journal (version 1.1.365) has a simpler layout:

- One header line with an account picker (one account, and so one currency, at a time; it remembers your choice) and a date picker.
- Three headline cards, **Net**, **Win rate** and **Profit factor**, plus an equity chart.
- A slim ledger: close time, symbol and side, strategy, net result and a review icon. Ticket, gross and fees are in the trade panel that opens beside it.
- A calendar with **Today** and a **Month | Week** switch, and 50 rows per page.

Trades also show up faster. Cached results are refreshed the moment your set of open trades changes, the journal updates on its own (at most every 4 seconds, never while you are editing a note), and crypto bots reconcile with the exchange every 10 seconds instead of every 30.

A few dashboard numbers were wrong and are fixed: Bybit day P&L was always shown as 0 and now sums today's closed trades net of fees, an MT5 account's broker credit is no longer counted as open profit, and the realized banner shows each account separately when they use different currencies.

## Research bots: clearer views and the AI assistant

Research bots now come in four views: **List**, **Large**, **Medium** and **Small**. Since 1.1.363, a card shows every trade of a live deployment (trades, wins and losses, win rate, realized P&L) plus a separate figure since the last reset, and the trade history behind those numbers is kept across saves so the counters no longer drift.

In **All backtests**, the backtest a live bot is running is pinned at the top with a **DEPLOYED** badge, its status and an **Open bot** link, and a **DEPLOYED** filter shows only those rows. This is display only; it changes nothing about execution.

For layered strategies (a base entry plus adds), the chart now draws every add as a numbered dot inside its cycle with the basket's average entry, and forward tests work for layered results too.

The AI assistant, part of Pro, can now create research bots: one at a time, or up to 20 on a single approval card, mixing MT5 and crypto markets. It can also pause, resume or archive many bots at once. The usual rules apply:

> Nothing is sent until you approve the card, and only when live actions are switched on; otherwise approval is a dry run that shows the request that would have been sent.

Creating a research bot starts research. It does not deploy anything to live trading; that still follows your deployment rules and the separate auto-deploy setting. On Free, the card warns you that the plan includes one research bot.

## Safer live execution

Some of the most important changes are invisible until they matter:

- **MT5 protection survives restarts.** After an app restart, a repair step could run before MetaTrader 5 had reported which account was logged in. Trailing stop and take-profit updates for an open trade were then held back until it closed. The app now waits until the account is known.
- **MT5 bot exits close only the bot's own positions**, every leg of a layered basket and nothing else. On a hedging account, a manual position or another bot's position on the same symbol is left alone.
- **MT5 bot plans keep the exact stop-loss and take-profit** that were sent to the broker.
- **Bybit closes are booked correctly** even when the exchange's log repeats a row with its decimals written differently.
- **Notifications do what the settings say.** A ticked box no longer unticks itself, **TEST WEBHOOK** saves the URL before testing it, the app sends the MT5 and risk-guard webhook messages itself, crypto-only setups are no longer told every 15 minutes that MT5 is not connected, and EMA bots now send the **Entry fired** notification. Notifications are still Windows notifications plus your webhook.
- No command windows flash open on start or during an update, and from 1.1.367 the app and installer are digitally signed by Period Trader LLC.

## What did not change

Research still runs on your own PC, and a passing backtest is still a hypothesis to test, not a promise. The guided tours, the new journal and the deployed markers only show you more; none of them place, size or approve trades. If you are new, the welcome checklist above is the quickest way in.
