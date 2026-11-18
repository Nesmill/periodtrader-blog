Every strategy eventually hits a losing stretch, and the hardest question in systematic trading is what it means. Stop too early and you abandon a working system at the bottom of a normal drawdown; stop too late and you keep paying for an edge that is gone. In our hypothetical simulation, a strategy with a genuine edge still had a run of 10 or more losses in a row in 70% of its 500-trade histories.

This post looks at why edges stop working, what a normal drawdown looks like in numbers, and how four common "stop" rules perform when we know the right answer.

## Why a working strategy can stop working

There are three different reasons a strategy starts losing, and they call for different responses.

### 1. The market changed regime

Markets move between states: trending and ranging, calm and volatile. Economists model this explicitly. James Hamilton's 1989 paper in *Econometrica* proposed a widely used way of modeling "changes in regime", where the same series switches between states with different behaviour.

A trend-following strategy and a mean-reversion strategy make money in different regimes, so either one can lose for months simply because the market is in the other state. Momentum gives a well-documented example. Kent Daniel and Tobias Moskowitz found that momentum crashes occur "in panic states, following market declines and when market volatility is high", as the market rebounds. From March to May 2009, the stocks with the worst past returns rose 163% while the past winners gained only 8%, a brutal period for any strategy that bought winners and sold losers.

### 2. The edge decayed

Some edges shrink for good because other traders find them. David McLean and Jeffrey Pontiff studied 97 published stock-return predictors and found that portfolio returns were 26% lower out-of-sample and 58% lower after publication. The pattern was still there, but much weaker.

Andrew Lo's Adaptive Markets Hypothesis offers a middle view: strategies "wax and wane", performing well in some environments and poorly in others, and may decline for a time and later return to profitability.

### 3. There was never an edge

The third possibility is the uncomfortable one: the backtest was [overfit](/blog/why-perfect-backtests-overfit) or [too short to prove anything](/blog/how-many-trades-backtest), and live trading is simply revealing it.

> A losing stretch does not tell you which of the three is happening. That is why the decision to stop has to be made with numbers, ideally before the drawdown starts.

## What a normal drawdown looks like

Take a hypothetical strategy that wins 40% of its trades, makes 2R on winners (twice the amount risked) and loses 1R on losers. Its expectancy is **+0.20R per trade**: a real, healthy edge. We simulated 20,000 independent histories of 500 trades each:

| What we measured (healthy strategy) | Result |
|---|---|
| Chance that a given 20-trade stretch loses money | 25.0% |
| Chance that a given 50-trade stretch loses money | 15.6% |
| Chance that a given 100-trade stretch loses money | 9.1% |
| Histories with at least one losing 50-trade stretch | 98.9% |
| Longest losing streak (median / worst 5%) | 11 / 16 trades |
| Longest time without a new equity high (median / worst 5%) | 93 / 219 trades |
| Maximum drawdown (median / worst 5%) | 16R / 28R |

The first three rows are exact binomial probabilities; the rest come from the simulation. Read the table as a warning about intuition. A strategy that is profitable on average will, in almost every 500-trade history, have at least one 50-trade stretch that loses money, and the typical history spends 93 trades without making a new high. At 1% risk per trade, a 16R drawdown is roughly a 15% decline in the account.

> Losing streaks and flat months are part of a working strategy, not proof that it is broken.

## Four stop rules, tested where we know the answer

To compare rules fairly, we built a second scenario: the same strategy trades 200 healthy trades, then its edge breaks. Its win rate drops to 30%, so expectancy becomes **−0.10R per trade**. A good rule should rarely fire on the healthy strategy and should catch the broken one quickly. We ran each rule on 5,000 healthy 500-trade histories and 5,000 break scenarios:

| Stop rule | Healthy strategy stopped within 500 trades | Median trades after the break before it fires |
|---|---|---|
| 10 losses in a row | 70.2% | 78 |
| Last 50 trades net negative | 98.6% | 30 |
| Drawdown deeper than 28R | 4.8% | 150 |
| CUSUM on results in R | 6.0% | 140 |

The two intuitive rules look fast, but they are fast because they fire on almost everything. They stopped the healthy strategy in most histories, and in the break scenario they had often already fired during the 200 healthy trades (38% of runs for the streak rule, 80% for the 50-trade rule).

The two calibrated rules rarely stop a healthy strategy (about 5% of the time, by design), but they need a median of 140 to 150 trades after the break to fire. At −0.10R per trade, a 140-trade delay costs about 14R on average, roughly 13% of the account at 1% risk per trade.

That trade-off is not a flaw in any particular rule. When a strategy's results swing by more than 1R per trade and the edge you are monitoring is a fraction of 1R, telling "unlucky" from "broken" takes many trades. No rule is both fast and reliable.

### How CUSUM works

CUSUM (cumulative sum) comes from industrial quality control, introduced by E. S. Page in 1954. In trading terms:

1. Choose a reference level halfway between what you expect (+0.20R) and what you would call broken (−0.10R): here +0.05R.
2. After each trade, add the amount by which the result fell short of that reference, and reset the running total to zero whenever it would go negative.
3. Stop when the total crosses a threshold chosen so that a healthy strategy rarely reaches it. In our simulation, a threshold of 33R produced a 6% false-alarm rate over 500 trades.

It is close to a drawdown measured against the profit the strategy should have made, which is why it reacted slightly faster than the plain drawdown rule here.

## How to decide before the drawdown

- **Write the stop rule before going live.** Base it on the backtest's own distribution of drawdowns and losing streaks, as in the table above, not on how the losses feel at the time.
- **Measure in R, not money.** It keeps the rule valid when position size or account balance changes.
- **Know your strategy's regime.** Split the backtest into trending and ranging periods, or calm and volatile ones, and see where the profit came from. A drawdown that arrives in a regime the backtest says is bad is useful information; a drawdown in the strategy's best regime deserves more suspicion.
- **Check execution before blaming the edge.** Wider spreads or more slippage can quietly erase an edge; see [how trading costs eat a strategy's edge](/blog/trading-costs-spread-commission-slippage).
- **Don't refit to the latest losses.** Tuning parameters until the recent drawdown disappears is just overfitting on a smaller sample. Re-test on fresh, unseen data instead.
- **Consider cutting size instead of choosing all or nothing.** Reducing risk while the evidence builds limits the cost of a broken edge without giving up a healthy one.

In Period Trader, when you set up a research bot on a single strategy, a **Market fit** line reads the last year of the chosen market's candles and says whether its moves tend to keep going or snap back, labelled a good, fair or poor fit for that strategy's style. It describes the past year, so treat it as a starting point: regimes can change, which is the point of this post.

## Further reading

- Hamilton, J. D. (1989), [A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle](https://doi.org/10.2307/1912559), *Econometrica* 57(2).
- Page, E. S. (1954), [Continuous Inspection Schemes](https://doi.org/10.1093/biomet/41.1-2.100), *Biometrika* 41(1-2).
- Lo, A. W. (2004), [The Adaptive Markets Hypothesis](https://doi.org/10.3905/jpm.2004.442611), *Journal of Portfolio Management* 30(5). A [free copy](https://web.mit.edu/Alo/www/Papers/JPM2004_Pub.pdf) is hosted by MIT.
- McLean, R. D. and Pontiff, J. (2016), [Does Academic Research Destroy Stock Return Predictability?](https://doi.org/10.1111/jofi.12365), *Journal of Finance* 71(1).
- Daniel, K. and Moskowitz, T. J. (2016), [Momentum Crashes](https://doi.org/10.1016/j.jfineco.2015.12.002), *Journal of Financial Economics* 122(2), open access.
