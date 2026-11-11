Four trading bots that each risk 1% per trade look like four small, separate risks. Whether they really are depends on one number most traders never measure: how closely the strategies' results move together. In our hypothetical simulation, four strategies with identical edges and identical 1% sizing went from a median drawdown of 17% to 38% purely because their results became more correlated.

## Four 1% bets are not always four small risks

Correlation measures how two series move together, on a scale from −1 to +1. At 0, one strategy's result tells you nothing about the other's. At +1, they win and lose together, so two strategies are really one strategy traded twice as large.

What matters for risk is the correlation of the strategies' **results** (their trade-by-trade or day-by-day profit and loss), not just of the prices they trade. Overlap hides in ordinary setups:

- **Same market, different settings.** A 15-minute and a 1-hour trend strategy on gold can easily enter the same move.
- **A shared currency.** EURUSD and GBPUSD are both quoted against the US dollar, so a broad dollar move pushes both in the same direction.
- **One asset class.** Many crypto coins tend to rise and fall with Bitcoin.
- **Across asset classes.** An IMF study found that the correlation between Bitcoin and S&P 500 returns was 0.01 in 2017–19 and 0.36 in 2020–21.

## How much diversification do you actually get?

Portfolio theory has used this arithmetic since Harry Markowitz's 1952 paper: the risk of a combination depends on the correlations between its parts, not only on their individual sizes. Take N strategies with the same size of swing, each risking the same amount, and a pairwise correlation ρ between their results:

> Combined swing = one strategy's swing × √(N + N × (N − 1) × ρ)
>
> Effective independent bets = N ÷ (1 + (N − 1) × ρ)

| Strategies | ρ = 0 | ρ = 0.3 | ρ = 0.6 | ρ = 0.9 |
|---|---|---|---|---|
| 2 | 2.00 | 1.54 | 1.25 | 1.05 |
| 4 | 4.00 | 2.11 | 1.43 | 1.08 |
| 10 | 10.00 | 2.70 | 1.56 | 1.10 |

The table shows effective independent bets. Ten strategies with a correlation of 0.3 give you the diversification of fewer than three independent ones. As you add more strategies, the effective number never passes 1 ÷ ρ, which is 3.3 at ρ = 0.3. Adding a fifth or tenth similar bot mostly adds size, not diversification.

## A hypothetical simulation: same edge, different correlation

> **Hypothetical simulation.** Four strategies, each with a 40% win rate, +2R on winners and −1R on losers (expectancy +0.2R per trade). Each strategy takes one trade per period and risks 1% of current equity on it, for 250 periods, 20,000 times. The only thing that changes between rows is how correlated the four strategies' results are.

| Correlation of results | All four lose in the same period | Median max drawdown | 95th percentile max drawdown | Chance of a drawdown above 20% |
|---|---|---|---|---|
| 0.00 | 12.9% | 16.9% | 27.1% | 28.0% |
| 0.19 | 22.6% | 23.5% | 37.2% | 73.6% |
| 0.41 | 32.9% | 29.9% | 46.6% | 94.6% |
| 0.71 | 47.0% | 37.8% | 57.7% | 99.6% |

Every row has the same edge and the same 1% per trade. Yet the period where all four strategies lose at once (a 4% hit) goes from about one period in eight to almost one in two, and the typical worst drawdown more than doubles.

For comparison, we ran a single strategy with the same edge on the same horizon at different risk levels. At 2% per trade, its median max drawdown was 24.3%. At 3%, 34.9%. At 4%, 44.1%. So four bots at 1% with a correlation of just 0.19 drew down roughly like one bot at 2%, and four bots with a correlation of 0.71 landed between one bot at 3% and one at 4%.

> **Key takeaway:** total risk is not the risk per bot times the number of bots, and it is not the risk per bot either. Correlation decides where between the two you end up.

## Correlation is not a constant

A correlation estimated from a backtest is an average over the period you tested. The problem is that correlations tend to rise exactly when you need them low.

- **Longin and Solnik (2001)** studied the correlation of international equity markets and found that "correlation increases in bear markets, but not in bull markets."
- **Ang and Chen (2002)** found that correlations between US equity portfolios and the US market during joint down moves were on average 11.6% higher than a normal distribution implies, while upside correlations were not distinguishable from it. Their conclusion: diversification "may be overstated" if you ignore this.
- The **IMF** figures above show a correlation that barely existed before 2020 appearing within a couple of years.

Longin and Solnik also add a warning: if you simply split history into calm and volatile days and compare correlations, you can see a higher correlation in volatile periods even when the true correlation never changed. In their example, a constant correlation of 0.50 showed up as 0.21 on small-move days and 0.62 on large-move days. Measuring correlation needs care in both directions.

### What a calm backtest misses

We reran the four-strategy simulation with a regime switch. Most of the time the strategies were almost unrelated, but twice in each 250-period run there was a 20-period stress block where their results became highly correlated (0.71).

| Scenario | Correlation you would measure | Median max drawdown | 95th percentile max drawdown | Chance of a drawdown above 20% |
|---|---|---|---|---|
| What the calm periods suggest | 0.06 | 19.3% | 30.3% | 44.1% |
| What actually happened, with stress blocks | 0.06 calm / 0.71 stress | 24.0% | 38.7% | 74.3% |

The stress blocks were only 16% of the periods, but they moved the typical drawdown up by almost five percentage points and the bad-case drawdown by more than eight. A backtest window that happened to miss a stress episode would have measured the 0.06 and planned for the first row.

## How to measure correlation between your strategies

1. **Use results, not prices.** Build a daily profit-and-loss series for each strategy (in R or in % of equity) over the same dates, with flat days counted as zero.
2. **Include stress periods.** Make sure the window contains at least one sharp sell-off or volatility spike for the markets you trade. A sample from a single calm regime will understate the correlation.
3. **Look at the worst days, not just the coefficient.** Count how often several strategies lost on the same day, and how large the combined loss was. That number translates directly into drawdown.
4. **Treat the estimate as noisy.** A correlation from a few dozen trades is as uncertain as any other backtest statistic; see our post on [how many trades a backtest needs](/blog/how-many-trades-backtest).

## A practical checklist

- **Add up total open risk** across every running strategy, and assume highly correlated strategies are one larger position.
- **Size the book for the day everything loses together.** If four bots at 1% can all be stopped out in the same session, your real single-day risk is about 4%, before gaps and slippage.
- **Diversify by what drives the result**, not by the number of bots: different markets, different signal logic, different holding periods.
- **Recheck correlations after big market events**, since a relationship measured in a calm year may not hold in the next stressed one.
- **Use platform limits as a ceiling, not as a correlation check.** In Period Trader, Settings has a *Default risk per trade* for new deployments and a *Maximum live deployments* cap on how many bots run at once. Both bound size and count; neither knows whether your bots are trading the same idea. That judgment is yours.

For how per-trade risk turns into drawdowns for a single strategy, see [how much to risk per trade](/blog/how-much-to-risk-per-trade).

## Further reading

- Markowitz, H. (1952). "Portfolio Selection." *The Journal of Finance*, 7(1), 77–91. [DOI 10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)
- Longin, F. and Solnik, B. (2001). "Extreme Correlation of International Equity Markets." *The Journal of Finance*, 56(2), 649–676. [DOI 10.1111/0022-1082.00340](https://doi.org/10.1111/0022-1082.00340)
- Ang, A. and Chen, J. (2002). "Asymmetric Correlations of Equity Portfolios." *Journal of Financial Economics*. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X02000685) · [author PDF](https://business.columbia.edu/sites/default/files-efs/pubfiles/1516/corr.pdf)
- Adrian, T., Iyer, T. and Qureshi, M. S. (2022). "Crypto Prices Move More in Sync With Stocks, Posing New Risks." [IMF Blog](https://www.imf.org/en/blogs/articles/2022/01/11/crypto-prices-move-more-in-sync-with-stocks-posing-new-risks)
