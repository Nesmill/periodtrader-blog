A strategy can have a real edge before costs and still lose money after them. Spread, commission and slippage are charged on every trade, win or lose, and they are easy to underestimate in a backtest because they look tiny next to the price.

This post shows how to measure trading costs in the unit that matters, the amount risked per trade, using a hypothetical example and a simulation. The short version: the same costs that barely touch a slow strategy can wipe out a fast one.

## Three costs, one bill

Every round trip, from entry to exit, pays some combination of:

- **Spread.** The gap between the bid and the ask. A market buy fills at the ask and a market sell at the bid, so a trade that enters and exits at market pays roughly one full spread per round trip.
- **Commission.** On many forex and CFD accounts, a fixed amount per lot. On crypto exchanges, usually a percentage of the position's notional value (the taker fee, for orders that fill immediately).
- **Slippage.** The difference between the price you expected and the price you got. Stop-loss orders are especially exposed: as the SEC's Investor.gov explains, the stop price "is not the guaranteed execution price". It is a trigger that turns the stop into a market order, and the fill "can deviate significantly from the stop price".

Overnight financing (swap) is a fourth cost, left aside here.

For the rest of the post we use one hypothetical cost assumption on a EURUSD-like pair where one pip is worth $10 per standard lot: a 0.6-pip average spread, a $7 round-trip commission per lot (0.7 pips) and 0.2 pips of average slippage, for **1.5 pips per round trip**.

## Measure costs in R, not in pips

What matters is not the 1.5 pips but the cost relative to what the trade risks. If R is the amount you lose when the stop is hit, the cost of a round trip in R is:

> Cost in R = round-trip cost ÷ stop distance

With fixed-fractional sizing, this has a concrete dollar meaning. A hypothetical $10,000 account risking 1% has $100 at stake on every trade. A tighter stop means a bigger position, and a bigger position pays more spread and commission:

| Stop | Position for $100 of risk | Cost per round trip | Cost in R |
|---|---|---|---|
| 5 pips | 2.00 lots | $30.00 | 0.30R |
| 10 pips | 1.00 lot | $15.00 | 0.15R |
| 20 pips | 0.50 lots | $7.50 | 0.075R |
| 50 pips | 0.20 lots | $3.00 | 0.03R |
| 100 pips | 0.10 lots | $1.50 | 0.015R |

The risk is $100 in every row, but the 5-pip stop pays twenty times the cost of the 100-pip stop, because its position is twenty times larger.

## What costs do to expectancy

Now take a hypothetical strategy that wins 45% of its trades, targets 1.5 times its stop and loses 1R when stopped out. Before costs, its expectancy is 0.45 × 1.5 − 0.55 × 1 = **+0.125R per trade**, its profit factor is 1.23 and it breaks even at a 40% win rate.

Costs hit winners and losers alike: each win nets 1.5R minus the cost and each loss costs 1R plus the cost, so net expectancy is the gross expectancy minus the cost in R. We assume the same statistics in R at every stop size, to isolate the effect of costs:

| Stop | Net expectancy | Breakeven win rate | Net profit factor | Gross edge paid in costs |
|---|---|---|---|---|
| No costs | +0.125R | 40.0% | 1.23 | 0% |
| 5 pips | −0.175R | 52.0% | 0.76 | 240% |
| 10 pips | −0.025R | 46.0% | 0.96 | 120% |
| 20 pips | +0.050R | 43.0% | 1.08 | 60% |
| 50 pips | +0.095R | 41.2% | 1.17 | 24% |
| 100 pips | +0.110R | 40.6% | 1.20 | 12% |

With costs included, the breakeven win rate becomes (1 + cost in R) ÷ (1 + reward-to-risk ratio). At a 5-pip stop it needs a 52% win rate just to break even, and it wins 45%: same signals, losing strategy.

### Same signals, 500 trades

> **Hypothetical simulation.** 20,000 random sequences of 500 trades from the strategy above, sized at 1% of current equity per trade. Every stop size trades the **same** 20,000 sequences, so only the costs change.

| Stop | Runs ending below the start | Median ending equity | Median max drawdown |
|---|---|---|---|
| No costs | 1.7% | 1.80× | 15.6% |
| 5 pips | 99.9% | 0.40× | 62.8% |
| 10 pips | 72.4% | 0.85× | 32.3% |
| 20 pips | 22.4% | 1.24× | 21.4% |
| 50 pips | 6.0% | 1.55× | 17.5% |
| 100 pips | 3.3% | 1.67× | 16.6% |

Without costs, under 2% of the runs ended below where they started. With a 1.5-pip cost and a 5-pip stop, almost every run did, and the median run lost 60% of its equity.

## The more you trade, the bigger the edge has to be

Costs are paid per trade, so they grow with turnover. In the example above, the 5-pip version pays 30R in costs every 100 trades against a gross edge of 12.5R. The 100-pip version pays 1.5R.

Research on real portfolios points the same way. Barber and Odean studied 66,465 US households at a large discount broker from 1991 to 1996. The households that traded most earned a net 11.4% a year, against 17.9% for the market and 18.5% for those that traded least, with very similar gross returns. In their words, "it is the cost of trading and the frequency of trading, not portfolio selections," that explain the poor results. Costs were far higher then: in their data, the average round trip above $1,000 cost about 3% in commissions and 1% in spread. The mechanism has not changed.

Novy-Marx and Velikov tested a large set of published stock-market anomalies after trading costs. Most strategies with one-sided monthly turnover below 50% kept statistically significant returns after costs, at least when designed to reduce trading, but "few of the strategies with higher turnover do". Costs also reduced statistical significance in every case, "increasing concerns related to data snooping", the same problem behind [overfit backtests](/blog/why-perfect-backtests-overfit).

## Costs are not a constant

A simple backtest charges one fixed cost per trade. Real costs move:

- **Spreads widen when liquidity thins.** A 2017 BIS report on foreign exchange liquidity notes that algorithmic market makers often respond to stress by "widening prices before ceasing to quote them altogether". In the flash event of 7 October 2016, sterling fell 9% against the dollar in early Asian hours, and executed stop-loss orders helped exhaust the limited liquidity on the main spot platform.
- **Stops slip in fast markets and gaps.** A stop that becomes a market order fills at the next available price, which after a weekend gap or a major data release can be well past the stop.
- **A quoted spread is not an average spread.** One checked at a quiet moment can understate what a strategy pays across the hours it trades.

A tight stop magnifies every extra fraction of a pip, so these swings hurt short-term strategies most.

## How to put costs into a backtest

- **Use your own broker's numbers**: the average spread over several days, the commission per lot for a round trip, or the exchange's taker fee, not the best case from a marketing page.
- **Convert costs into R** for your typical stop. If costs eat a large share of the expected edge per trade, the strategy has little room for error.
- **Charge costs on every trade**, winners and losers, and add a slippage allowance on stop exits.
- **Stress-test at twice the cost.** In our example, the 20-pip version stays positive at 1.5 pips (+0.05R) but turns negative at 3 pips (−0.025R), while the 50-pip version keeps +0.065R.
- **Compare live fills with the backtest.** If real spreads and slippage run higher than assumed, rerun the research with the real figures.

Period Trader prices these costs into its research. For MT5, each backtest charges the spread measured from your connected account's recent quotes plus your broker's round-trip commission per lot (the figure you enter in SETUP, or one measured from your own settled deals), and crypto backtests charge the exchange's taker fee. A research bot whose backtests ran without those costs is flagged COSTS NOT PRICED.

> **Key takeaway:** judge a strategy by its edge after costs, measured in R. The tighter the stop and the more often it trades, the bigger that edge has to be.

## Further reading

- B. M. Barber and T. Odean (2000), [Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors](https://doi.org/10.1111/0022-1082.00226), *Journal of Finance* 55(2). A [free copy](https://faculty.haas.berkeley.edu/odean/papers/returns/individual_investor_performance_final.pdf) is hosted by UC Berkeley.
- R. Novy-Marx and M. Velikov (2016), [A Taxonomy of Anomalies and Their Trading Costs](https://doi.org/10.1093/rfs/hhv063), *Review of Financial Studies* 29(1). The quotes above are from the free 2014 [NBER working paper](https://www.nber.org/papers/w20721).
- U.S. Securities and Exchange Commission, Investor.gov: [Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15).
- Bank for International Settlements (2017), [Foreign exchange liquidity in the Americas](https://www.bis.org/publications/paper-90-foreign-exchange-liquidity-americas.pdf), BIS Papers No 90.
