Last week (November 2–6, 2026) markets swung hard around the US midterm elections. Stocks had their best day in months on Wednesday, then their worst since April 2025 on Thursday as AI stocks sold off, and the rout spread to Asia, where South Korea halted trading. Meanwhile, US hiring beat forecasts, the Bank of England raised rates and Brent crude had its biggest weekly fall since April.

Below: what changed, why it matters for systematic traders, and what is still open.

## The week in numbers

| Market | Close, Fri Nov 6 | Change vs. Fri Oct 30 |
|---|---|---|
| S&P 500 | 7,376.86 | -2.7% |
| Nasdaq Composite | 24,579.42 | -3.4% |
| Dow Jones Industrial Average | 51,285.73 | -0.9% |
| US 10-year Treasury yield | 4.86% | -8 bp |
| Brent crude, January futures | $98.32 | -13.3% |
| WTI crude, December futures | $90.83 | -12.8% |
| EUR/USD | 1.1228 | +0.4% |
| GBP/USD | 1.3456 | +0.6% |
| USD/JPY | 157.50 | -0.2% |
| Bitcoin (USD) | $75,747 | -1.9% |
| Kospi (South Korea) | 5,059.69 | -11.7% |
| Nikkei 225 (Japan) | 57,434.77 | -9.3% |

Data: AP (US indices), US Treasury (yields), Yahoo Finance daily data (futures settlements, currencies, Asian indices; bitcoin at the UTC daily close). We computed the percentages.

## 1. Midterms: a relief rally, then an AI rout

Democrats won control of both the House and the Senate in Tuesday's midterm elections. On Wednesday, the S&P 500 rose 1.6% and the Dow jumped about 1,570 points, or 3%, its biggest gain of the year, CBS News reported.

The mood flipped on Thursday. The S&P 500 fell 4.4% to 7,353.73, its worst day since the April 2025 "Liberation Day" tariff shock, and the Nasdaq Composite dropped 5.5%, ending 11.9% below its October record, which puts it in a correction (AP). The trigger was the AI trade: investors worried that the new majorities could slow the construction of AI data centers, which voters link to higher power bills. Nvidia fell 9.3% and AMD 17.3%.

According to CNBC, the "Magnificent Seven" lost more than $1 trillion of market value that day, and all 11 S&P 500 sectors fell, with information technology down 7.3%, its worst day since March 2020.

On Friday, tech stocks recovered part of the drop: the Nasdaq rose 1.1% and the S&P 500 0.3%, while the Dow slipped 0.5%.

### Why systematic traders care

Volatility can change regime in one session. In Yahoo Finance data, the VIX closed at 16.61 on Wednesday and 28.18 on Thursday, a 70% jump. A strategy with fixed stop and target distances suddenly sees moves that are much larger relative to those levels, so stops get hit more often. Sizing positions by risk, not by a fixed number of contracts or shares, keeps the loss per trade near the planned percentage when ranges widen. Our post on [how much to risk per trade](/blog/how-much-to-risk-per-trade) covers the math.

Concentration matters too: when a few chip stocks carry so much index weight, an index strategy and a tech-stock strategy can be the same bet.

## 2. Asia: a trading halt in Seoul and a bear market in Tokyo

Asia took the hit on Friday. At 9:03 a.m. in Seoul, the Korea Exchange triggered a first-level circuit breaker on the Kospi after the index fell 8.52% to 4,924.61, halting trading for 20 minutes (Yonhap, Korea JoongAng Daily). It was the 11th such halt on the index this year. The Kospi closed down about 6% at 5,059.69 and lost 11.7% over the week.

Japan's Nikkei 225 fell 5.96% to 57,434.77, more than 20% below its June peak, the usual definition of a bear market, CNBC reported.

### Why systematic traders care

A halt is not just a gap. Under Korea Exchange rules, as JoongAng Daily describes them, no new orders are accepted during the 20 minutes; only cancellations. Trading then restarts with a 10-minute single-price auction. A bot running on that market will see rejected orders and one reopening price instead of a continuous feed. Make sure your strategy handles rejected orders without retrying in a loop, and that its backtest does not assume fills at prices that never traded.

## 3. Jobs, yields and a Bank of England hike

### US payrolls beat forecasts

Nonfarm payrolls rose by 165,000 in October, compared with 59,000 expected in a Dow Jones poll, and the unemployment rate fell to 4.1% from 4.2%, CNBC reported. KPMG's headline said the gains "lock in" a December rate hike. After the release, CME FedWatch put the odds of a quarter-point Fed hike at the December 8–9 meeting at 76.8%.

Treasuries rallied anyway. In the Treasury's daily data, the 10-year yield fell from 4.94% to 4.86% over the week, and on Thursday AP said the drop in yields could signal investors seeking safety as stocks fell.

### Bank of England

On Thursday the Bank of England raised Bank Rate by a quarter point to 4%, its first increase since August 2023. The vote was 8–1; Catherine Mann wanted a half-point hike. The Bank expects UK inflation, 3.5% in September, to rise to around 5% by the middle of next year because of energy prices. Governor Andrew Bailey said that unless the Middle East conflict is resolved, this hike is unlikely to be the last. The next decision is on December 17.

### Why systematic traders care

Higher hike odds would normally lift yields, yet the 10-year fell, likely as investors sought safety during the stock sell-off. Test macro-release strategies on how prices actually reacted, not on how they "should" have.

## 4. Oil: Brent's biggest weekly fall since April

January Brent fell 8.7% on Wednesday as investors bet the election result could push Washington toward ending the war with Iran, CNBC reported. It settled Friday at $98.32. Iran reportedly sent a nuclear proposal to Washington through Qatar, but attacks on tankers in the Strait of Hormuz continued.

### The roll, again

CNBC reported a weekly drop of "more than 16%" for Brent. That figure compares Friday's January price with the December contract, which expired on October 30 at $117.64. Comparing the same contract, January Brent fell from $113.43 to $98.32: 13.3%. About 3 percentage points of the headline figure come from the contract change we covered [last week](/blog/weekly-recap-big-tech-binance-hack). If your data feed uses a continuous contract, check whether it is back-adjusted, or your backtest will record a move that no single futures position experienced.

## 5. Crypto: liquidations and ETF outflows

Bitcoin reached $81,080 on Wednesday, then fell with tech stocks. The UTC daily close went from $80,405 on Wednesday to $75,942 on Thursday, down 5.6%. More than $1 billion of leveraged crypto bets were liquidated, CoinDesk reported. For the week, bitcoin lost 1.9%.

US spot bitcoin ETFs had $1.28 billion of net outflows, their worst week since late June and enough to turn their 2026 flows negative, according to The Block (SoSoValue data) and Farside data cited by crypto.news.

### Why systematic traders care

On Thursday bitcoin fell about as much as the Nasdaq. A crypto bot and a Nasdaq strategy may not be as independent as they look. Liquidation cascades also mean that stop orders in crypto can fill far from their trigger price on days like Thursday.

## The week ahead: what is still uncertain

- **US CPI for October, Tuesday November 10** at 8:30 a.m. ET, one of the last inflation readings before the Fed's December 8–9 meeting.
- **Veterans Day, Wednesday November 11.** US stock exchanges are open, but SIFMA recommends a full close for US dollar bond trading.
- **US–Iran.** Talks through Qatar continue, and Hormuz attacks have not stopped.

Spreads often widen and prices can gap around events like these.

## Sources

- [AP via WTOP: index closes Nov 6](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-friday-11-6-2026), [Nov 5](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-thursday-11-5-2026) and [Nov 4](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-wednesday-11-4-2026)
- [AP via AZFamily, Nov 5: AI sell-off](https://azfamily.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs)
- [CNBC, Nov 5: sell-off statistics](https://www.cnbc.com/2026/11/05/stock-market-selloff-ai-fears.html)
- [CNBC, Nov 6: markets live](https://www.cnbc.com/2026/11/05/stock-market-today-live-updates.html)
- [CBS News, Nov 4: election result and Dow rally](https://www.cbsnews.com/news/stock-market-soar-democrats-take-control-of-congress)
- [Yonhap, Nov 6: Kospi halt](https://en.yna.co.kr/view/AEN20261106002100320)
- [Korea JoongAng Daily, Nov 6: circuit breaker](https://www.koreajoongangdaily.com/business/kospi-tracks-us-stocks-to-tank-nearly-9-after-opening-triggering-circuit-breaker/12959005)
- [CNBC, Nov 6: October jobs](https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html)
- [KPMG, Nov 6: jobs report](https://kpmg.com/us/en/articles/2026/october-2026-jobs-report.html)
- [US Treasury: daily par yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611)
- [Bank of England: November decision](https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026)
- [The Guardian, Nov 5: BoE hike](https://www.theguardian.com/business/2026/nov/05/bank-of-england-raises-interest-rates-first-increase-for-more-than-three-years)
- [Central Banking, Nov 5: first hike since 2023](https://centralbanking.com/central-banks/monetary-policy/monetary-policy-decisions/7977775/bank-of-england-makes-first-rate-hike-since-2023)
- [CNBC, Nov 6: oil](https://www.cnbc.com/2026/11/06/oil-price-today-brent-wti.html)
- [CNBC TV18, Nov 6: weekly oil fall](https://cnbctv18.com/market/commodities/crude-oil-prices-brent-biggest-weekly-loss-since-april-us-iran-war-de-escalation-strait-of-hormuz-west-asia-20028438.htm)
- [CoinDesk, Nov 5: bitcoin and liquidations](https://www.coindesk.com/markets/2026/11/05/bitcoin-crypto-stocks-caught-in-ai-trade-meltdown-but-wintermute-trader-sees-glass-half-full)
- [The Block, Nov 7: ETF outflows](https://www.theblock.co/news/markets/2026-11-07-bitcoin-etfs-flip-negative-for-2026-after-1-28-billion-outflow-week-worst-since-june-435984)
- [crypto.news: Farside ETF flows](https://crypto.news/bitcoin-ether-etfs-weekly-outflows-blackrock-november)
- [BLS: CPI release schedule](https://www.bls.gov/news.release/cpi.htm)
- [SIFMA: Veterans Day close](https://sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026)
- [Yahoo Finance: Brent Jan 2027](https://finance.yahoo.com/quote/BZF27.NYM/history/), [WTI Dec 2026](https://finance.yahoo.com/quote/CLZ26.NYM/history/), [bitcoin](https://finance.yahoo.com/quote/BTC-USD/history/), [VIX](https://finance.yahoo.com/quote/%5EVIX/history/), [Kospi](https://finance.yahoo.com/quote/%5EKS11/history/), [Nikkei](https://finance.yahoo.com/quote/%5EN225/history/), [EUR/USD](https://finance.yahoo.com/quote/EURUSD%3DX/history/), [GBP/USD](https://finance.yahoo.com/quote/GBPUSD%3DX/history/) and [USD/JPY](https://finance.yahoo.com/quote/JPY%3DX/history/)
