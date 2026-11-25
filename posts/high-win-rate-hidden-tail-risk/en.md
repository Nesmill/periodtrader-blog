A strategy that wins nine trades out of ten sounds safe. It is not, or at least not for that reason. Win rate says how often a strategy is right; it says nothing about how much it loses when it is wrong, and a few large losses can erase hundreds of small wins.

This post shows how a high win rate can hide what traders call tail risk: rare, large losses that a short backtest often never sees. All the numbers below come from hypothetical examples and simulations, not from real trading, except where a source is cited.

## Win rate is only half of the equation

A strategy's expectancy, its average result per trade, needs both halves:

> Expectancy = win rate × average win − loss rate × average loss

The higher the win rate, the larger the average loss a strategy can afford before it stops making money. Here is the break-even point for different win rates:

| Win rate | Largest average loss that still breaks even |
|---|---|
| 40% | 0.67 × the average win |
| 50% | 1.00 × the average win |
| 70% | 2.33 × the average win |
| 90% | 9 × the average win |
| 95% | 19 × the average win |
| 99% | 99 × the average win |

A 90% win rate is not a margin of safety. It is a budget: the strategy may lose at most nine average wins per losing trade. If its losses run bigger than that, every extra trade makes the account smaller, however often it wins.

## A perfect record that loses money

> **Hypothetical strategy T.** It wins 97% of its trades for +1 unit and loses 3% of them for −40 units. Its expectancy is 0.97 × 1 − 0.03 × 40 = **−0.23 units per trade**, and its true profit factor is 0.81. To break even it would need to win 97.6% of the time.

Strategy T loses money in the long run. A backtest will not always say so. We ran 200,000 simulated backtests of strategy T at each length:

| Backtest length | Shows no losing trade at all | Shows a net profit |
|---|---|---|
| 20 trades | 54.4% | 54.4% |
| 50 trades | 21.8% | 55.5% |
| 100 trades | 4.8% | 42.0% |
| 200 trades | 0.2% | 28.1% |
| 500 trades | 0.0% | 26.4% |
| 1,000 trades | 0.0% | 15.3% |

More than half of the 20-trade backtests show a perfect record: no losing trade, a profit factor that cannot even be calculated, and an equity curve that only goes up. Even at 500 trades, about one backtest in four still ends in profit.

The reason is simple arithmetic. To see a 1-in-N event at least once with 95% probability, you need roughly 3 × N trades. Strategy T's big loss comes about once every 33 trades, so a backtest needs close to 100 trades before it is likely to contain one, and many more before it contains enough of them to measure their real frequency. Our earlier post on [how many trades a backtest needs](/blog/how-many-trades-backtest) covers the general sample-size problem; tail risk makes it worse, because the trades that matter most are the rarest ones.

## Martingale: a 99% win rate by design

Some systems produce a high win rate on purpose. The classic is martingale sizing: after every loss, double the next trade so that one win recovers the whole sequence.

> **Hypothetical martingale.** Each trade wins or loses the same amount it risks, with a 49% chance of winning (a fair coin, minus a little for costs). A cycle starts at a stake of 0.5% of the starting balance and doubles after every loss, for at most 7 trades: 0.5%, 1%, 2%, 4%, 8%, 16% and 32%. A win at any step ends the cycle with +0.5%.

The cycle win rate is **99.1%**. The failed cycle, seven losses in a row, happens about once in 111 cycles and loses 127 base stakes: **63.5% of the starting balance**. The expected result per cycle is negative (−0.15 base stakes), because the trades themselves have no edge and doubling cannot create one.

| Cycles played | Chance of at least one failed cycle |
|---|---|
| 50 | 36.3% |
| 100 | 59.4% |
| 250 | 89.5% |
| 500 | 98.9% |
| 1,000 | more than 99.9% |

In 100,000 simulated runs, the median run reached its first failed cycle after 77 wins in a row. By then it was up 38.5% on the starting balance, and the failed cycle took it to 25% below the start. The equity curve before the failure is exactly the kind of curve that convinces people to trade a system.

The same logic applies to grid systems, averaging down without a stop and any rule that increases size after losses. They can be traded with hard limits, but they should be judged by their worst cycle, not by their win rate.

## Real markets go down by the elevator

Tail risk is not just a simulation artifact. Brunnermeier, Nagel and Pedersen studied currency carry trades, which borrow in a low-interest currency to hold a high-interest one. They found that these trades are subject to crash risk: exchange rate moves between high- and low-rate currencies are negatively skewed. As the paper puts it, the finding is "consistent with the saying among traders that exchange rates go up by the stairs and down by the elevator."

A sharper example is the Swiss franc. According to the Swiss National Bank's [2015 annual report](https://snb.ch/public/asset/en/www-snb-ch/publications/communication/annual-report/annrep_2015_komplett/publications0_en/annrep_2015_komplett.en.pdf), a minimum exchange rate of CHF 1.20 per euro was in place from 6 September 2011 to 15 January 2015. On 15 January the SNB [discontinued it](https://snb.ch/public/publication/en/www-snb-ch/publications/communication/press-releases/2015/pre_20150115/publications0_en/pre_20150115.en.pdf), and in the minutes after the announcement the rate fell to an all-time low of CHF 0.85 per euro before settling close to parity that afternoon.

From 1.20 to 0.85 is a 29.2% move, or 3,500 pips, within minutes. A strategy that bought EUR/CHF near the floor would have had more than three years of history in which buying near 1.20 worked. A backtest over those years would have contained zero examples of the floor failing.

A stop-loss does not fully protect against this kind of move. As the SEC's [Investor.gov bulletin on stop orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) explains, "the stop price is not the guaranteed execution price": once triggered, the stop becomes a market order, and the fill "can deviate significantly from the stop price".

## How to spot a hidden tail in a backtest

You cannot see a loss that never happened in your data, but you can look for the conditions that produce one:

- **Compare the worst loss with the average win.** If one losing trade costs 10 or 20 average wins, the win rate is doing all the work, and the next loss decides the result.
- **Check for a hard stop.** A strategy that holds losers until they recover will show a high win rate until the day the market does not recover.
- **Watch the sizing rules.** Anything that adds size after a loss (martingale, recovery cycles, averaging down) turns a normal losing streak into one very large loss.
- **Count the rare events.** If the strategy's big loss could plausibly come once every 50 trades, a backtest with 50 trades proves almost nothing. Aim for about three times that number, and prefer data that includes stress periods: central bank surprises, crashes, gaps over weekends.
- **Read the profit factor carefully.** A profit factor of 3 from 40 trades with only two small losses is weaker evidence than a profit factor of 1.4 built from 300 trades with real losing streaks.
- **Set a ceiling on single losses.** In Period Trader, **Settings → Deployment → Live deployment bar** has a **Maximum single loss** rule: the largest single loss a backtest may show, as a percentage of equity, before it can go live. It cannot see losses that are not in the data, so it works alongside the checks above, not instead of them.

> A high win rate is a description of how a strategy wins, not proof that it wins. Judge it by its worst trades and by how many chances its backtest had to show them.

## Further reading

- Brunnermeier, Nagel and Pedersen (2008), [Carry Trades and Currency Crashes](https://doi.org/10.1086/593088), *NBER Macroeconomics Annual* 23. A free working-paper version is on [NBER](https://www.nber.org/papers/w14473).
- Swiss National Bank (15 January 2015), [Swiss National Bank discontinues minimum exchange rate and lowers interest rate to −0.75%](https://snb.ch/public/publication/en/www-snb-ch/publications/communication/press-releases/2015/pre_20150115/publications0_en/pre_20150115.en.pdf).
- U.S. Securities and Exchange Commission, Investor.gov, [Stop, Stop-Limit, and Trailing Stop Orders – Investor Bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15).
