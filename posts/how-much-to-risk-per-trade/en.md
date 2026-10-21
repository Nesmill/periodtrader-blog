Two traders can run the exact same strategy, with the same entries, exits and edge, and end up in completely different places. One grows the account steadily. The other spends most of the year in a deep drawdown or blows the account up. The only difference is how much each one risks per trade.

This post shows why position sizing matters as much as the strategy itself, using a hypothetical simulation: how fixed-fractional sizing works, how normal losing streaks turn into drawdowns, what the Kelly criterion says about the "optimal" bet, and why the safe answer is usually much smaller than the optimal one.

## Fixed-fractional sizing in one formula

Fixed-fractional sizing means every trade risks the same percentage of your **current** equity. "Risk" here is what you lose if the stop is hit, not the size of the position:

> Position size = (equity × risk %) ÷ (stop distance × value per unit of price movement)

A hypothetical example: a $10,000 account risking 1% has $100 at stake. If the stop on EURUSD is 25 pips away and one standard lot is worth about $10 per pip, the position is $100 ÷ (25 × $10) = 0.40 lots. Move the stop to 50 pips and the position halves to 0.20 lots, while the dollar risk stays at $100.

Two consequences follow:

- **The stop decides the size, not the other way round.** You pick the stop where the trade idea is wrong, then let the formula tell you how big the position can be.
- **Size shrinks after losses and grows after wins.** Each loss is a percentage of a smaller balance, so in theory a string of stop-outs never takes the account to zero. In practice, gaps and slippage can make a single loss bigger than planned.

## Losing streaks are not rare events

To make the numbers concrete, take a hypothetical strategy that wins 40% of its trades, earns 2R on winners (twice the amount risked) and loses 1R on losers. Its expectancy is 0.40 × 2 − 0.60 × 1 = **+0.2R per trade**, and its breakeven win rate at a 2:1 reward-to-risk ratio is 100 ÷ (1 + 2) = 33.3%. It is a genuinely profitable strategy on paper.

It still loses most of its trades. Over 500 trades, our calculation gives a 97% chance of at least one streak of 8 or more losses in a row, a 71% chance of a streak of 10 or more, and a 35% chance of 12 or more. In the simulated runs, the median longest losing streak was 11 trades.

Here is what ten straight losses do at different risk levels:

| Risk per trade | After 5 losses | After 10 losses | Gain needed to recover from 10 losses |
|---|---|---|---|
| 0.5% | -2.5% | -4.9% | +5.1% |
| 1% | -4.9% | -9.6% | +10.6% |
| 2% | -9.6% | -18.3% | +22.4% |
| 5% | -22.6% | -40.1% | +67.0% |
| 10% | -41.0% | -65.1% | +186.8% |

The last column is the asymmetry that makes large risk so expensive: a 10% drawdown needs an 11.1% gain to recover, a 50% drawdown needs 100%, and a 75% drawdown needs 300%.

## Same edge, different risk: a Monte Carlo

> **Hypothetical simulation.** 20,000 random sequences of 500 trades from the strategy above (40% win rate, +2R / −1R, independent trades). Every risk level trades the **same** 20,000 sequences, so the only thing that changes is the size of each bet.

Risk of ruin usually means the chance of losing so much that you can no longer continue. As a stand-in for that point, the third column counts runs that fell 50% or more from a peak at some stage, a hole that needs a 100% gain to climb out of.

| Risk per trade | Median max drawdown | Runs with a 50%+ drawdown | Runs ending below the start | Median ending equity |
|---|---|---|---|---|
| 0.5% | 7.9% | 0% | 0.1% | 1.63× |
| 1% | 15.4% | under 0.1% | 0.2% | 2.57× |
| 2% | 29.2% | 2.0% | 0.2% | 5.95× |
| 5% | 60.8% | 84.5% | 0.9% | 39.4× |
| 10% | 88.7% | 100% | 6.5% | 128.5× |
| 20% | 99.9% | 100% | 48.0% | 1.42× |

Three things stand out:

- **Drawdown scales with risk almost one for one at first.** Doubling from 1% to 2% roughly doubled the typical worst drawdown, from about 15% to about 29%.
- **More risk stops paying.** Median growth rises with risk up to 10% per trade, then collapses: at 20%, the median run ends at just 1.42× its start, less than the 1% row, and nearly half of all runs lose money, with the same +0.2R edge on every trade.
- **The big growth numbers are not tradable.** The 10% row only works if you sit through a median drawdown of almost 89%. Few people would keep trading through that, and an account on leverage can hit a margin stop-out long before.

These figures come from an edge that is fixed and known in advance. Real trading never gives you that, which matters more than anything in the table.

## The Kelly criterion, and why traders bet less

In a 1956 paper in the *Bell System Technical Journal*, John L. Kelly Jr. worked out the bet size that maximizes the long-run growth rate of capital. For a trade that wins with probability *p* and pays *b* times the amount risked, the Kelly fraction is *p* − (1 − *p*) ÷ *b*. MacLean, Thorp and Ziemba summarize it as the edge divided by the odds. For our strategy that is 0.40 − 0.60 ÷ 2 = **10%**, exactly the row with the highest growth and the 89% median drawdown.

The same authors are blunt about the downside: the Kelly criterion "can be very risky in the short term", and in their continuous-time analysis, betting twice the Kelly amount brings the long-run growth rate down to roughly zero. Our 20% row (twice Kelly) shows the same thing. Their conclusion is that long-term growth investors "should bet Kelly or less".

Betting less costs surprisingly little growth. In a blackjack example they cite (a 2% advantage), betting half the Kelly fraction kept about 75% of the growth rate while raising the chance of doubling before halving from 67% to 89%.

### The real problem: you don't know your edge

Kelly assumes you know *p* and *b*. A trader only has estimates, usually from a backtest, and [backtests tend to overstate edges](/blog/why-perfect-backtests-overfit). We reran the simulation with a true win rate of 35% instead of 40%. The strategy is still profitable on paper (+0.05R per trade), but sized at 10% as if the win rate were 40%:

- the median run ended at **0.10×** its starting equity, and 78.5% of runs lost money;
- the same mistake at 1% risk ended at a median **1.22×**, with 27% of runs below the start and a median max drawdown of 24.7%.

Small risk is not just more comfortable. It also leaves room for being wrong about the edge. MacLean, Thorp and Ziemba make the same point: because growth is so sensitive to errors in the estimated mean, "to be on the safe side, the size of the wagers should be reduced."

## What the formula leaves out

- **Costs.** Spread, commission and slippage come on top of the stop. A market that gaps over a weekend can fill a stop well beyond its level.
- **Minimum trade size.** On a hypothetical $500 account, 1% is $5. If the smallest size the broker accepts loses $10 at your stop, you are really risking 2%, double what you chose.
- **Correlated positions.** Three long-dollar trades at 1% each behave more like one 3% bet when the dollar moves.
- **Several strategies at once.** Total open risk adds up across bots and accounts.

Period Trader handles the sizing and minimum-size parts of this for MT5 bots: it sizes each order from the stop that will actually rest at the broker, so a stop-out costs roughly the percentage of equity you selected (1% by default). When the broker's smallest tradable size forces more risk than that, the order still goes ahead, and the bot card flags it with an OVER badge showing the real percentage.

## A practical checklist

- **Size from the stop.** Decide where the idea is wrong, then compute the position.
- **Fix the risk percentage before the trade**, and don't raise it to win back a loss.
- **Plan for the streak.** In our hypothetical, the chance of a streak of 10 or more losses within 500 trades was about 71%. Know what that does to your account at your chosen risk.
- **If you use Kelly, use a fraction of a conservative estimate**, never the full number from a backtest.
- **Count total open risk**, including correlated positions and every running strategy.
- **Check real risk on small accounts** against the broker's minimum size.

> **Key takeaway:** the edge decides whether a strategy can make money. The size of each bet decides whether you are still trading when it does.

## Further reading

- J. L. Kelly Jr. (1956), [A New Interpretation of Information Rate](https://doi.org/10.1002/j.1538-7305.1956.tb03809.x), *Bell System Technical Journal* 35(4).
- MacLean, Thorp and Ziemba (2010), [Long-term capital growth: the good and bad properties of the Kelly and fractional Kelly capital growth criteria](https://doi.org/10.1080/14697688.2010.506108), *Quantitative Finance* 10(7). A free earlier version, [Good and bad properties of the Kelly criterion](https://www.stat.berkeley.edu/~aldous/157/Papers/Good%5FBad%5FKelly.pdf), is hosted by UC Berkeley.
