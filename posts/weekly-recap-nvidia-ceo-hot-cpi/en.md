Last week (November 9–13, 2026) the S&P 500 posted its first winning week since early October, but big moves hid underneath. Nvidia's chief executive resigned and its stock fell for a sixth straight week, October inflation came in hotter than expected, Treasury yields and the dollar jumped, and bitcoin fell below $70,000, then kept falling over the weekend.

Below: what changed, why systematic traders should care, and what is still open.

## The week in numbers

| Market | Close, Fri Nov 13 | Change vs. Fri Nov 6 |
|---|---|---|
| S&P 500 | 7,561.67 | +2.5% |
| Nasdaq Composite | 25,136.27 | +2.3% |
| Dow Jones Industrial Average | 52,347.55 | +2.1% |
| Nvidia (NVDA) | $162.85 | -12.7% |
| US 2-year Treasury yield | 4.88% | +37 bp |
| US 10-year Treasury yield | 5.15% | +29 bp |
| US Dollar Index | 103.41 | +1.1% |
| EUR/USD | 1.1050 | -1.6% |
| USD/JPY | 159.88 | +1.5% |
| Brent crude, January futures | $95.84 | -2.5% |
| Bitcoin (USD) | $68,249 | -9.9% |
| Nikkei 225 (Japan) | 61,142.35 | +6.5% |

Data: AP (US indices), US Treasury (yields), Yahoo Finance daily data (Nvidia, Brent settlement, currencies, dollar index, Nikkei; bitcoin at the UTC daily close). We computed the percentages.

## 1. Nvidia loses its CEO, the index shrugs

On Thursday, Nvidia's board announced that Jensen Huang, who co-founded the company 33 years ago, had resigned as president, CEO and board member, effective immediately. CFO Colette Kress became interim CEO while keeping her finance role, and former Synopsys CEO Harvey C. Jones became the board's first-ever chair. The resignation came days after Huang disclosed an affair in a note to employees on Sunday and the board opened an investigation, CNBC reported.

The stock fell 4.3% on Monday and kept sliding on Tuesday. On Thursday it dropped as much as 14% after the open, then recovered to close down 4.3%. On Friday it lost another 2.0% and closed below $4 trillion of market value for the first time since July 2025, according to CNBC. For the week it lost 12.7%, its sixth straight weekly decline and its longest losing streak since 2012.

Meanwhile, the S&P 500 jumped 2.3% on Monday, its best day since April, and on Wednesday CoreWeave's stronger-than-expected results lifted tech stocks and pulled the index within 2.6% of its October record (AP).

### Why systematic traders care

- **Key-person news is gap risk.** The biggest headlines landed on a Sunday and before Thursday's open. A stop order does not protect you from the opening price: if trading resumes far below your stop, the order fills at the next available price. Backtests that fill every stop exactly at its level understate this. Our post on [trading costs](/blog/trading-costs-spread-commission-slippage) covers slippage.
- **A stock and its index can split.** Nvidia fell 12.7% while the S&P 500 rose 2.5%; a week earlier, they fell together. That is why [correlation decides your real risk](/blog/strategy-correlation-portfolio-risk) across several strategies.
- **Another gap is scheduled.** Nvidia reports quarterly results on Tuesday after the close.

## 2. Hot inflation, a hawkish Fed and higher yields

US consumer prices rose 0.4% in October, above the 0.3% economists expected, and core CPI, which excludes food and energy, rose 0.3% against a 0.2% forecast, the Bureau of Labor Statistics reported Tuesday (CNBC, CNN). The BLS did not publish a year-over-year rate, because last year's government shutdown stopped it from collecting October 2025 data; economists cited by CNN put the annual rate near 4%.

Hours before the release, Fed Governor Christopher Waller said in London that a half-point hike should be on the table at the December 8–9 meeting if core CPI came in around 0.3%. After the data, CME FedWatch showed a quarter-point hike fully priced in and the odds of a half-point move at 13.6%, up from around zero, CNBC reported.

Bonds sold off. In Treasury data, the 2-year yield rose 17 basis points on Tuesday alone and ended the week at 4.88%, up 37 bp. The 10-year yield rose 29 bp to 5.15%.

### Why systematic traders care

A scheduled release can reprice a whole market in minutes. If your strategy trades on CPI days, check what its backtest assumed about spreads and fills right after 8:30 a.m. ET; live spreads around releases are often wider than the average spread a backtest uses.

## 3. The dollar's best week since September, the yen near 160

The US Dollar Index climbed to about 103.4 on Friday, its highest level since April 2025, and posted its biggest weekly gain since September, according to Reuters via CNBC; CoinDesk also noted the 19-month high.

The yen weakened to about 159.9 per dollar, close to the 160 mark. Japan's Finance Minister Satsuki Katayama said on Friday that the government would respond appropriately to currency volatility, and traders stayed alert for possible intervention (CNBC).

### Why systematic traders care

An official intervention has no scheduled time. If it comes, a USD/JPY strategy can face a sharp move against it at any hour, with spreads widening as it happens. Also note that one factor drove most of the week: EUR/USD, GBP/USD and USD/JPY all moved in the dollar's favor, and gold, priced in dollars, fell 4.6% (Yahoo Finance data). Three "different" currency strategies can be one bet on the dollar.

## 4. Oil: one post moves Brent 3%

January Brent fell 5.8% on Monday, after President Donald Trump said on Sunday that fresh attacks on Iran were highly unlikely as talks progressed (AP, CNBC). On Thursday the tone reversed. Trump wrote on social media, "We don't need a deal with Iran," and redirected Vice President JD Vance to domestic issues (The Guardian, NBC News). Brent settled up 3.3% at $95.82 that day, CNBC reported. For the week, January Brent lost 2.5%.

### Why systematic traders care

Monday's drop and Thursday's jump came from opposite statements, days apart, with no calendar warning. Trend and breakout strategies can be whipsawed in that kind of market: a breakout entered on one headline can hit its stop on the next. Check how an oil backtest behaved in past headline-driven weeks, not just on average.

## 5. Crypto: below $70,000, then a weekend flush

On Friday bitcoin fell below $70,000 for the first time since August. Over 24 hours, $1.64 billion of leveraged crypto positions were liquidated, 88.7% of them longs, according to CoinGlass data cited by CoinDesk. US spot bitcoin ETFs had net outflows on every day of the week, totaling $1.065 billion (Farside data via crypto.news).

The selling did not stop when stock markets closed. Bitcoin dropped about 8% after Friday's US close, CoinDesk reported, and on Sunday it touched about $62,100, its lowest since July 14 (CoinDesk, The Business Times). Weekend liquidations totaled about $2 billion, mostly longs. It was bitcoin's sixth straight weekly loss.

### Why systematic traders care

Crypto trades 24/7. If your crypto bot takes its cues from stocks, or you hedge crypto with stock positions, nothing on the stock side can react between Friday's close and Monday's open. Leverage makes this worse: in Yahoo Finance data, bitcoin's UTC close fell 15.3% from November 6 to November 14. As a hypothetical illustration, at 10x leverage a move of about 10% against a position is enough to wipe out its margin, before fees and funding.

## The week ahead: what is still uncertain

- **Nvidia earnings, Tuesday November 17** at about 1:20 p.m. PT, its first report under the interim CEO.
- **Fed minutes, Wednesday November 18** at 2:00 p.m. ET, for the October 27–28 meeting. A December hike is priced in; its size is still debated.
- **Anthropic IPO.** The AI company plans to price its shares on November 18 and start trading on the Nasdaq on November 19 under the ticker ANT, with a range of $70 to $78 a share.
- **US–Iran.** No deal in sight; new attacks on shipping would move oil quickly.

Spreads often widen and prices can gap around events like these.

## Sources

- AP via WTOP, index closes: [Nov 9](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-monday-11-9-2026/), [Nov 11](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-wednesday-11-11-2026/), [Nov 12](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-thursday-11-12-2026/), [Nov 13](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-friday-11-13-2026/)
- [Nvidia: CEO transition](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)
- CNBC, Nvidia: [Nov 12](https://www.cnbc.com/2026/11/12/nvidia-nvda-jensen-huang-second-affair.html), [Nov 13](https://www.cnbc.com/2026/11/13/nvidia-nvda-stock-jensen-huang-transition.html)
- [CNBC: October CPI](https://www.cnbc.com/2026/11/10/cpi-inflation-report-october-2026.html)
- [CNN: October CPI](https://edition.cnn.com/2026/11/10/business/us-inflation-cpi-consumer-prices-october)
- [US Treasury: yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611)
- [CNBC (Reuters): dollar and yen](https://www.cnbc.com/2026/11/13/dollar-near-19-month-high-on-fed-hike-bets-yen-tests-160.html)
- [CNBC: oil and Iran](https://www.cnbc.com/2026/11/12/oil-prices-jump-after-trump-says-no-iran-deal-needed-weve-got-their-strait.html)
- [The Guardian: Iran deal](https://www.theguardian.com/us-news/2026/nov/12/trump-jd-vance-iran-war)
- [NBC News: Iran deal](https://www.nbcnews.com/politics/donald-trump/us-doesnt-need-peace-deal-iran-vance-corruption-trump-rcna609027)
- CoinDesk, bitcoin: [Nov 13](https://www.coindesk.com/markets/2026/11/13/bitcoin-hits-12-week-low-as-dollar-rallies-on-interest-rate-outlook-liquidations-top-usd1-6-billion), [Nov 14](https://www.coindesk.com/markets/2026/11/14/bitcoin-drifts-back-to-usd65-000-deep-value-zone-says-analyst), [Nov 16](https://www.coindesk.com/markets/2026/11/16/bitcoin-slips-to-usd64-000-after-usd2-billion-weekend-flush)
- [crypto.news: ETF flows](https://crypto.news/weekly-crypto-etf-outflows-bitcoin-ethereum-november-13/)
- [The Business Times: bitcoin](https://www.businesstimes.com.sg/wealth/crypto-alternative-assets/bitcoin-hits-four-month-low-sell-wipes-out-us2-billion-crypto-bets)
- [Federal Reserve: November calendar](https://www.federalreserve.gov/newsevents/2026-november.htm)
- [CNBC: Anthropic IPO](https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html)
- [Yahoo Finance: Anthropic IPO date](https://finance.yahoo.com/technology/article/anthropic-ipo-claude-maker-to-begin-trading-on-thursday-nov-19-173550865.html)
- Yahoo Finance data: [NVDA](https://finance.yahoo.com/quote/NVDA/history/), [Brent](https://finance.yahoo.com/quote/BZF27.NYM/history/), [BTC](https://finance.yahoo.com/quote/BTC-USD/history/), [DXY](https://finance.yahoo.com/quote/DX-Y.NYB/history/), [Nikkei](https://finance.yahoo.com/quote/%5EN225/history/), [EUR/USD](https://finance.yahoo.com/quote/EURUSD%3DX/history/), [GBP/USD](https://finance.yahoo.com/quote/GBPUSD%3DX/history/), [USD/JPY](https://finance.yahoo.com/quote/JPY%3DX/history/) and [gold](https://finance.yahoo.com/quote/GC%3DF/history/)
