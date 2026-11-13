Two updates released on November 9 and 11 (versions 1.1.368 and 1.1.369) change how research bots get from a good backtest to a proven setup, and what may happen in between. The biggest addition is the live trial: a small, capped way for a well-checked setup to trade real money before it is fully proven. Around it, research got stricter about costs and luck, gained 68 strategies and learned from other installs.

Here is what changed, how each piece works, and where the limits are.

## Live trials: real money, small size, clear limits

Until now a research setup had to become a **Champion** before it could go live. On fast candles that can take weeks, because proof comes one closed paper trade at a time. A live trial is the step in between. A setup is **ready** for one only when all of this is true:

- It is **Promising**: it made money after fees on unseen days, the part of the data it was never tuned on, with a statistical score of at least 1.0.
- It is **Steady** (explained below) and did not turn out to be a fluke on similar markets.
- Its paper test has not dropped it, and the bot has no champion or live deployment of its own.
- Fewer than three trials are running across your bots, and this setup never had a trial before.
- The market is crypto. MetaTrader 5 markets are off for trials unless you switch them on.

A trial uses the normal deployment path at **0.1% risk per trade**. It stops and closes its position when its realized plus open loss since the start reaches **1% of the account** it started with, when its paper test drops the setup, or when a different setup becomes the bot's champion. If the setup itself becomes the champion, it keeps trading at the trial size until you change it. After a stopped trial, that bot waits six hours before another setup may start one.

> A trial starts by itself only when auto-deploy is on. Otherwise the card shows **Live trial ready** and a **Start live trial** button, and a confirmation names the risk per trade and the loss cap before anything starts.

The five numbers (risk per trade, loss cap, maximum trials, minimum score and the MT5 switch) are in **Settings > Deployment**. Risk per trade can go from 0.1% to 1%.

Keep two things in mind. A live trial is not a champion; the app says so, and the setup is still being tested. And the 1% cap is a rule the app enforces by closing the position, not a guarantee: in a fast or gapping market the loss can end up larger.

## Faster proof, without a lower bar

### Promising setups and paper tests (1.1.368)

A run that made money on unseen data but has too few trades to rule out luck is now marked **Promising** and shown early, instead of disappearing. It then starts a paper test by itself: it trades new candles with no real money. It becomes a champion once its unseen-data result and its paper trades together clear the luck bar.

### Five paper tests per bot and similar markets (1.1.369)

Each research bot now paper-tests up to **five setups at once**, at most two of the same strategy. A paper test is judged only at checkpoints, every five closed paper trades, against a bar of at least 2.2. That is deliberate: re-checking a test every few minutes lets a setup with no edge pass simply by waiting long enough. Tests that are clearly not working are dropped early, which frees the slot for the next setup.

Promising setups are also checked on **similar markets**: the same settings run on up to eight comparable markets over the same unseen calendar days, with the setup's own market left out and same-day trades counted once. Holding up there can confirm a champion in minutes, because it needs no new candles. Losing there does not drop the paper test, since an edge can belong to one market, but the setup moves to the back of the queue.

Each card shows an estimate of the **days left to proof**, so a setup that trades too rarely to prove anything in time is easy to spot.

### Research that respects costs

- **Fee-aware search.** Settings whose take-profit is less than four round-trip trading costs away, or whose stop is less than 1.5 round-trip costs away, are no longer backtested: fees would take most of every trade. The rule adapts by itself to each market and candle size, so on 1-hour or 4-hour candles almost nothing is skipped.
- **Steady or Unsteady.** Each Promising setup is re-run with every setting one step lower and higher. If 40% or fewer of those neighbours are profitable, it is marked **Unsteady** and waits behind the others.
- **Losing streaks.** A streak of more than six losing trades, or a win rate under 35%, now costs ranking points.

What counts as a champion did not change with these filters.

### A longer window (1.1.368)

Research can use 180-day and 365-day windows, picking 365 days for 1-hour and 4-hour candles and 180 for 30-minute and faster, until you choose. The unseen test is a quarter of the window, between 30 and 90 days, and the luck bar stops rising at 2.0.

## 68 new strategies with plain names

Version 1.1.368 adds 68 strategies across trend, momentum, Smart Money, volume and funding-rate ideas, so research can now try more than 100, and every one can use layered entries. **All strategies** is the default; strategies measured as dead on a market are skipped, and a **Shortlist** option is the fastest start. Older strategies got plain names (for example Band Snapback, Quiet Pullback, Daily Range Breakout, Trend Turn and Dip Ladder), and existing bots and reports keep working under the new names.

The AI chat (Pro) can list and explain every strategy and create research bots with any of them, layered ones included, with the usual approval card.

## Collective learning: what is shared and what is not

Research now learns, from every backtest it runs, which setting values tend to work for each strategy, market and candle size. Installs also share an anonymous map of that evidence, so each one can search more efficiently. According to the app's notice, it shares aggregate strategy results and the settings of setups that tested well, and never keys, logins, balances, trades or your code.

Three safeguards matter here:

- A part of the map only steers research once at least three installs contribute to it.
- At least a quarter of each batch of new settings stays fully random.
- A setup suggested by another install is re-tested on your own data, but it can never become a champion from that alone, only through new paper trades. Its "unseen days" might not be unseen at all from another install's point of view.

Collective learning is on by default. The first-run notice has a **Turn off** button, and the switch lives in Settings. While it is on, the app also sends a periodic check-in with only its version number, so active installs can be counted.

## Cleaner screens and a What's new window

Research cards, the **Details** window and Settings now use shorter text; resting the pointer on a term opens a short explanation. The Research Review window was redesigned with a plain-language verdict, a **Road to champion**, a **Luck meter** and a backtest funnel. The best backtest has its own **Deploy** button, and **All backtests** shows as cards. The risk guard and the account strip (balance, equity, day P&L) are explained in plain words.

After every update, a window now explains what changed. You can reopen it from **Settings > Updates**, or ask the AI chat "what's new?".

## Exchanges: Bitunix in, three out

**Bitunix** is now a supported exchange for USDT perpetuals. Connect it in **Brokers & exchanges**; your Bitunix account must use One-way position mode. **MEXC, Coinbase International and Kraken Futures** are no longer supported.

Bybit's order history no longer lists cancelled, rejected and deactivated orders unless they are requested by status (see [Bybit's API documentation](https://bybit-exchange.github.io/docs/v5/order/order-list)). The app now asks for them explicitly, so Bybit trade history keeps working.

## Fixes and what did not change

- Paper tests that stopped counting new candles restart and keep their trades, and research no longer starves them of resources.
- Strategies from the library now work in paper tests.
- Research Review shows updates without pressing Ctrl+F5.

Research still runs on your own PC. A champion, a Promising setup or a live trial is still a hypothesis under test, not a promise of profit, and auto-deploy remains a separate switch you control.
