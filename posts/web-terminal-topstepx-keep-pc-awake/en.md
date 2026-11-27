Two updates shipped since our last product post. Version 1.1.379 turns the Browser tab into the **Web terminal**, with a live dashboard and order ticket for platforms PeriodTrader has a script for, starting with TopstepX. Version 1.1.380 keeps your PC from going to sleep while bots, open trades or research are running, and fixes a rare freeze. Here is what changed and why it matters.

## The Web terminal (1.1.379, Pro)

The Browser tab let you open a trading platform's website inside the app and work in it with the AI. It is now called **WEB TERMINAL**, and for a platform with a script it no longer shows you the raw website first. The platform runs hidden, and you get a PeriodTrader dashboard instead.

### A live dashboard for TopstepX

TopstepX is the first platform with a script included in the app. Its dashboard shows, updated every second:

- balance, max loss limit and the room left before it;
- realized and unrealized P&L, and the daily loss against its limit;
- tabs for your positions, orders, trades and accounts.

On a prop account, hitting the max loss limit usually ends the account, so the room left before it sits at the top instead of somewhere on the firm's page.

The real website does not disappear. It stays visible as a small live window in the corner, and one click opens it full size if you want to use the site itself. A **DASHBOARD / WEBSITE** switch moves between the two. If you are signed out, the site opens full size so you can sign in on the platform's own page; PeriodTrader never sees your password, and the dashboard comes back by itself once you are in.

### Trading from our ticket

The dashboard has its own order ticket: **BUY MARKET**, **SELL MARKET**, **CLOSE POSITION**, **REVERSE**, **CANCEL ORDERS** and **FLATTEN ALL**. Two safeguards come with it:

- Every order asks you to confirm before anything is sent.
- **Test only** walks through every step of an order and stops before the order button, so you can watch exactly what the script would do without trading.

Behind the ticket, the app types and clicks inside the platform's hidden page the way a person would. That is why a working script matters: it describes which fields to read and which buttons to press, and pressing the order button is always a separate, marked step that needs your confirmation in the dashboard.

## Platform scripts, built once by the AI

What about a platform PeriodTrader does not know yet? The first time you use it, the AI does a **first run**: it reads your account, positions and order ticket, fills a test order up to the order button without ever pressing it, and saves what it did as a script.

The script is checked on the live page before it is saved, and testing never sends an order. From then on the dashboard runs from the script, which is much faster than the AI and needs no AI turn for each action. If a platform changes its page, **Fix with AI** or **Rebuild with AI** repairs the script the same way.

A few details worth knowing:

- **Scripts are data, not code.** A script lists fields, tables and steps such as "click", "fill" or "wait"; it cannot run programs on your PC.
- **Shared for review.** New scripts are shared with PeriodTrader so other users can get them. Every shared script is held for review because it can place orders, and a script that contains anything private, such as account numbers, e-mail addresses or money amounts, is not shared at all.
- **Ready-made for everyone.** Once a script is approved, any user who opens that platform without one gets it installed automatically, and approved scripts also ship with the next update. Your own script always takes priority over a shared one.

The Web terminal is a Pro feature, and the first run uses the AI, which draws on your shared AI credits. After that, day-to-day use of a script does not need the AI.

## Keep this PC awake (1.1.380)

If you leave a PC running bots overnight, Windows can put it to sleep after a period of inactivity. A sleeping PC pauses the app: bots stop watching the market, research stops and broker connections drop. The stops and targets already at your broker or exchange stay in place, but nothing in the app manages the trade until the PC wakes up.

PeriodTrader now asks Windows to stay awake while it has work to do:

- a live bot or auto-deployment is running;
- an MT5 or crypto position is open;
- a research bot is running and not paused.

When none of that is true, the request is released and Windows sleeps as usual. The screen can still turn off; only the system stays awake. The setting is **Keep this PC awake while bots or research are running** in **Settings → General**, on by default, with a status line that tells you whether it is idle or active right now.

Two limits to keep in mind. On battery, Windows may still put the PC to sleep. And this only blocks automatic sleep while the PC is idle: Microsoft's documentation notes that this mechanism [cannot prevent the user from putting the computer to sleep](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate), so choosing Sleep, shutting down or a laptop set to sleep when its lid closes still works as before. If your bots need to run while you are away, check your Windows power settings too.

## A freeze fix (1.1.380)

In 1.1.379 the app could, rarely, freeze and stop updating bots, trailing stops and the risk guard. It happened when the account check for deposits and withdrawals ran at the same moment the app was syncing a stop-loss: each waited for the other. That check now runs in the background and can no longer block the app. Orders already at the broker kept their stop-loss and take-profit throughout.

> If you are still on 1.1.379, update to 1.1.380. Auto-update installs it at a safe moment, when every open trade has its stop resting at the broker.

## Research and the rest of 1.1.379

### Start over

The research bot menu has a new **Start over…** option. It rebuilds the bot with every setting it was created with, as if you had just created it: the run count goes back to 0 and the search starts fresh, while its past runs stay in the history. If the bot has a live deployment, that bot keeps trading as it is and stays on the same card; your deployment rules decide when a new champion replaces it.

### Research skips settings that change nothing

Some strategies set their own stop and target and ignore part of the shared grid, so research could spend hundreds of backtests on settings that produced identical results. Each single-strategy research bot now checks this once, shortly after it starts: it changes one setting at a time and holds any setting that makes no difference at a single value. Searches finish sooner and the backtests go to settings that matter.

### Smaller changes

- **Recovery research bots** no longer show a best result from older backtests that stopped early at their first loss cap; the card shows the real best over the whole test period.
- **Lighter while researching:** the app uses less processor and memory while research runs.
- **Chart trade panel:** after a trade from the panel is filled, its stop-loss and take-profit switch off so they stop showing on the chart. A refused order keeps them.
- **Structured Earn analytics:** total earned, return, average per position, daily pace, best result, a growth chart, a by-pair table and a sortable list of every position, at the top of the tab.
- **Alert sounds:** choose from 10 sounds, set the volume or turn sound off in **Settings → Notification / Reporting**, with a **Test sound** button.
- **Community:** sharing to and installing from Community works again for signed-in users.

None of these changes how your strategies trade. They are about seeing your account clearly, keeping the app running when you step away and spending research time where it counts.
