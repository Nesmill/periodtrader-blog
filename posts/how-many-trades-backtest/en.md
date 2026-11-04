A backtest with 40 trades and a 60% win rate looks like evidence. Statistically, it is closer to a coin that landed heads 24 times out of 40: interesting, but not proof of anything. Every number a backtest reports (win rate, expectancy, profit factor) is an estimate from a sample, and small samples produce wide, noisy estimates.

This post shows how wide that noise is at different trade counts, how often pure luck passes for an edge, and a simple formula for estimating how many trades a strategy needs before its results mean something. All numbers come from a hypothetical simulation, not from real trading.

## A backtest is a sample, not a measurement

Think of a strategy as having a "true" win rate and a "true" expectancy: the values you would see if it could trade the same market conditions forever. A backtest never sees forever. It sees one stretch of history, and the trades in that stretch are a random draw from what the strategy could have done.

Two strategies with the same true edge will produce different backtests, just as two people flipping the same fair coin 40 times will get different counts. The question is not "what did the backtest show?" but "how far from the truth could this result be, given how few trades it has?"

That distance is called **sampling error**, and it shrinks with the square root of the number of trades. To cut the error in half you need four times as many trades, not twice as many.

## How wide is the uncertainty?

Take a hypothetical strategy that wins 40% of the time, makes 2R on winners (twice the amount risked) and loses 1R on losers. Its true expectancy is 0.40 × 2 − 0.60 × 1 = **+0.20R per trade**, and it breaks even at a 33.3% win rate. Each trade's result swings a lot around that average: the standard deviation is about 1.47R per trade.

Suppose a backtest shows exactly those numbers. Here is the 95% confidence range around them at different sample sizes (the win-rate range uses the Wilson interval recommended by the [NIST/SEMATECH e-Handbook](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm); the expectancy range uses the normal approximation):

| Trades | Win rate 95% range | Expectancy 95% range |
|---|---|---|
| 20 | 21.9% to 61.3% | −0.44R to +0.84R |
| 50 | 27.6% to 53.8% | −0.21R to +0.61R |
| 100 | 30.9% to 49.8% | −0.09R to +0.49R |
| 300 | 34.6% to 45.6% | +0.03R to +0.37R |
| 1,000 | 37.0% to 43.1% | +0.11R to +0.29R |

At 20, 50 and even 100 trades, the range still includes negative expectancy. The win-rate range at 100 trades runs from below the 33.3% breakeven to almost 50%. Only around 300 trades does the whole range sit above zero, and even then the strategy could plausibly be worth anywhere from barely positive to nearly twice the estimate.

> A backtest's win rate and expectancy come with an error bar. With fewer than about 100 trades, that error bar is usually wider than the edge you are trying to measure.

## When luck looks like an edge

Confidence ranges are abstract, so we also simulated the problem directly.

> **Hypothetical simulation.** Strategy A is the one above: a real +0.20R edge. Strategy Z has no edge at all: it wins 40% of the time at +1.5R / −1R, so its true expectancy is exactly zero. For each trade count we ran 100,000 independent backtests of each strategy, with independent trades and no costs.

| Trades | A (real edge) shows a loss | Z (no edge) shows profit factor ≥ 1.3 | Z (no edge) shows expectancy ≥ +0.20R |
|---|---|---|---|
| 20 | 24.8% | 24.3% | 24.3% |
| 50 | 15.7% | 15.5% | 15.5% |
| 100 | 9.1% | 9.3% | 6.4% |
| 300 | 0.8% | 1.1% | 0.3% |
| 1,000 | <0.1% | <0.1% | <0.1% |

Read the 20-trade row carefully. A genuinely profitable strategy showed a losing backtest about one time in four. A strategy with zero edge looked at least as good as the profitable one, also about one time in four. With 20 trades, the backtest is close to useless at telling them apart.

It gets worse once you run many backtests. We also tested 50 zero-edge variants on 50 trades each and kept the best one, 20,000 times over. The winner's profit factor was at least 1.3 in more than 99.9% of runs, with a median of 1.91, even though none of the variants had any edge. That is the overfitting problem from our post on [why near-perfect backtests are usually overfit](/blog/why-perfect-backtests-overfit): small samples and many trials multiply each other.

## How many trades is enough?

A practical way to judge a backtest is the ratio between its average trade and the uncertainty of that average, a t-statistic:

**t = expectancy ÷ (standard deviation per trade ÷ √trades)**

Rearranged, it tells you roughly how many trades you need to reach a given t:

**trades ≈ (t × standard deviation ÷ expectancy)²**

A t of 2 roughly corresponds to the classic 5% significance level (two-sided). The table uses the same 2R / 1R payoff as above with different true win rates:

| Win rate | Expectancy | Trades for t = 2 | Trades for t = 3 |
|---|---|---|---|
| 35.0% | +0.05R | 3,277 | 7,372 |
| 36.7% | +0.10R | 835 | 1,878 |
| 40.0% | +0.20R | 216 | 486 |
| 43.3% | +0.30R | 99 | 222 |

Two things stand out. First, small edges need enormous samples: halving the expectancy roughly quadruples the trades required. Second, the payoff shape matters too. Holding expectancy at +0.20R, a strategy that wins 60% at 1R / 1R needs about 97 trades for t = 2, while one that wins 24% at 4R / 1R needs about 457, because rare large winners make each trade's result much noisier.

### Why t = 2 is often too low

The 5% threshold assumes you ran one test. In a 2016 paper in *The Review of Financial Studies*, Campbell Harvey, Yan Liu and Heqing Zhu counted hundreds of published return factors and argued that, after accounting for how many had been tried, a new factor should clear a t-statistic above 3.0, and that a t-statistic of 2.0 "is no longer appropriate". Their subject was academic research, but the logic applies to anyone who tries many strategy variants: the more you search, the higher the bar. At t = 3, our +0.20R strategy needs close to 500 trades.

## Not every trade counts as one

The formulas above assume every trade is an independent bet. Real trades often are not:

- **Clusters.** A strategy that opens five positions in the same hour, on the same news, has placed closer to one bet than five.
- **Correlated symbols.** Long EUR/USD and long GBP/USD at the same time are largely the same trade on the US dollar.
- **One regime.** 400 trades taken during a single trending year tell you how the strategy behaves in that kind of market, not in a range or a crash.

We reran Strategy A with 300 trades grouped into 60 clusters of five, where every trade in a cluster shares the same outcome. Counted naively, 300 trades give a t of 2.36. Counted as the 60 independent bets they really are, t falls to 1.05. In the simulation, the share of backtests showing a loss rose from under 1% with 300 independent trades to 11.6% with 60 clusters of five.

The same issue affects return ratios. In "The Statistics of Sharpe Ratios" (*Financial Analysts Journal*, 2002), Andrew Lo showed that ignoring serial correlation in monthly returns could overstate a hedge fund's annual Sharpe ratio by as much as 65%. Dependence between results makes a track record look more reliable than it is.

## A practical checklist

- **Read every backtest metric as a range**, not a point. A 55% win rate on 60 trades is consistent with a true win rate anywhere from about 42% to 67%.
- **Estimate the trades you need before testing.** Use the formula with a conservative guess of the edge. If the answer is far more trades than your data can produce, test on more symbols, a longer history or a different timeframe, or accept that the result will stay uncertain.
- **Raise the bar with the number of variants tried.** One idea tested once can live with t = 2. A sweep of hundreds of combinations needs more.
- **Count independent bets, not fills.** Group trades that open together or on correlated instruments, and make sure the sample spans more than one market regime.
- **Keep unseen data for the final check.** Period Trader's research holdout, for example, will not pass a backtest unless it has at least 15 trades on data kept apart from the search and at least 40 trades overall. Those are floors, not proof; your own minimum-trades rule can be stricter.
- **Treat early live results the same way.** Ten live trades say very little about whether a strategy still works, in either direction.

## Further reading

- Harvey, C. R., Liu, Y. and Zhu, H. (2016). "… and the Cross-Section of Expected Returns." *The Review of Financial Studies*, 29(1), 5–68. [DOI 10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059) · [author PDF](https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF)
- Lo, A. W. (2002). "The Statistics of Sharpe Ratios." *Financial Analysts Journal*, 58(4), 36–52. [DOI 10.2469/faj.v58.n4.2453](https://doi.org/10.2469/faj.v58.n4.2453)
- NIST/SEMATECH e-Handbook of Statistical Methods, [7.2.4.1 Confidence intervals for a proportion](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm)
