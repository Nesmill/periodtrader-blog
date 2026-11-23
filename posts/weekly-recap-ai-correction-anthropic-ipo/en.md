Last week (November 16–20, 2026) the AI selloff turned into a full correction. The S&P 500 lost 8.6%, its worst week since April 2025, and the Nasdaq Composite fell 10% and erased its gain for the year. Nvidia beat its earnings forecasts and still lost 23%, Anthropic completed the largest IPO on record and faded on day two, Treasury yields fell back below 5%, and bitcoin dropped below $57,000.

Below: what changed, why systematic traders should care, and what is still open.

## The week in numbers

| Market | Close, Fri Nov 20 | Change vs. Fri Nov 13 |
|---|---|---|
| S&P 500 | 6,910.39 | -8.6% |
| Nasdaq Composite | 22,617.73 | -10.0% |
| Dow Jones Industrial Average | 48,147.33 | -8.0% |
| Cboe Volatility Index (VIX) | 35.89 | +86% |
| Nvidia (NVDA) | $125.53 | -22.9% |
| Anthropic (ANT) | $88.91 | IPO price $83 |
| US 2-year Treasury yield | 4.63% | -25 bp |
| US 10-year Treasury yield | 4.92% | -23 bp |
| US Dollar Index | 103.81 | +0.4% |
| USD/JPY | 159.71 | -0.1% |
| Gold futures | $3,515.40 | -9.5% |
| Brent crude, January futures | $92.57 | -3.4% |
| Bitcoin (USD) | $58,799 | -13.8% |
| Nikkei 225 (Japan) | 56,436.65 | -7.7% |

Data: AP (US indices), US Treasury (yields), Yahoo Finance daily data (VIX, stocks, currencies, futures, Nikkei; bitcoin at the UTC daily close). We computed the percentages.

## 1. The S&P 500 enters a correction

The S&P 500 fell on all five days, and on Friday it dropped 3.7% to close more than 10% below its October 6 record, the usual definition of a correction. It was the index's seventh straight daily loss (AP, Reuters). The Dow also closed in correction territory. The Nasdaq Composite lost 5.3% on Friday alone and had its worst week since March 2020, according to Reuters.

The VIX, which measures expected S&P 500 swings, closed at 35.89, up from 19.30 a week earlier and its highest close since April 2025. On Friday it briefly touched 40 (Bloomberg).

Part of the selling was rule-based. The S&P 500 traded below its 200-day moving average on Tuesday and broke it decisively on Thursday, which CNBC said turned trend-following funds (CTAs) into automatic sellers. Goldman Sachs estimated that CTAs sold $57 billion of US stocks over the past month and turned net short, and that its models see up to $80.6 billion more selling in the coming week if prices keep falling (Bloomberg).

### Why systematic traders care

- **Trend rules are a crowd.** When thousands of funds watch the same moving average, a break can trigger a wave of selling at once. If your strategy uses a widely watched level, expect fills to be worse right when it triggers.
- **Volatility changes position size.** A VIX near 36 means daily ranges are much wider than in October. With fixed-fractional sizing, a wider stop means a smaller position for the same risk; our guide on [how much to risk per trade](/blog/how-much-to-risk-per-trade) shows the math.
- **A losing week is not automatically a broken strategy.** Check whether your drawdown is within what the backtest showed before you switch anything off. We covered that in [broken strategy or drawdown](/blog/strategy-broken-or-drawdown).

## 2. Nvidia: a beat, then a 23% weekly loss

On Tuesday after the close, Nvidia reported fiscal third-quarter revenue of $115.8 billion, up 103% from a year earlier, its first report since CEO Jensen Huang resigned. Revenue beat the $109.1 billion analysts expected and guidance of $130 billion for the next quarter topped the $125.1 billion consensus, according to LSEG data cited by CNBC. On the earnings call, board chair Harvey Jones said the board does not intend to reinstate Huang. The stock fell 2.9% on Wednesday.

On Friday, Reuters reported, citing two people briefed on the matter, that SEC enforcement staff are examining potential accounting issues at Nvidia. The SEC declined to comment, and an SEC inquiry is not a finding of wrongdoing (24/7 Wall St. via Yahoo Finance, Decrypt). Nvidia fell 14.0% that day to $125.53, its seventh straight daily loss, and ended the week down 22.9%.

### Why systematic traders care

- **Good numbers do not guarantee a rising price.** A strategy that buys "earnings beats" can lose when the market is reacting to something else, here leadership and a regulatory probe.
- **Intraday headlines move prices too.** The SEC report hit during trading hours. Stops do fill in that case, but in a fast market they fill at the next available price, which can be well past the stop. Our post on [trading costs](/blog/trading-costs-spread-commission-slippage) covers slippage.

## 3. Anthropic's record IPO fades on day two

Anthropic priced its IPO on Wednesday at $83 a share, above its $70–78 range, and raised $81.3 billion, the largest IPO on record (CNBC, Reuters). After the underwriters bought their full option of extra shares, gross proceeds reached about $93.5 billion, Anthropic said in its closing announcement.

The stock opened at $111.50 on Thursday, reached $115.10 and closed at $97.17, 17.1% above the offer price. On Friday it fell 8.5% to $88.91. Many investors had hoped the listing would act as a "clearing event" for AI stocks, Goldman traders wrote, according to Bloomberg; instead, the selling spread.

### Why systematic traders care

A new listing has no price history to backtest, and its first sessions are among its most volatile: on day one, ANT traded between $92.72 and $115.10. Any rule built on a few days of data is a guess, not a tested strategy. Our post on [how many trades you need](/blog/how-many-trades-backtest) explains why.

## 4. Fed minutes say hikes, the bond market says safety

The minutes of the Fed's October 27–28 meeting, released Wednesday, said almost all participants judged that further rate increases would likely be appropriate. A couple noted that a hike of more than 25 basis points could be considered in December if inflation data were unfavorable. Most participants also observed that AI-related debt had grown rapidly through "complex and opaque financing structures" (Federal Reserve, CNBC).

Then the stock selloff sent investors into Treasuries. The 10-year yield fell 23 basis points to 4.92% and the 2-year fell 25 bp to 4.63%, according to Treasury data. A quarter-point December hike stayed about 92% priced in on Friday (CNBC), but by Monday CME FedWatch showed no chance of a half-point move, down from about 10% roughly ten days earlier, CoinDesk reported.

### Why systematic traders care

Correlations shifted under stress. Bonds rallied as stocks fell, but gold futures lost 9.5% in the same week, instead of acting as a haven. If two of your strategies "hedge" each other, check how they behaved together in stressed weeks, not just on average; see [correlation decides your real risk](/blog/strategy-correlation-portfolio-risk).

## 5. Bitcoin falls below $57,000

Bitcoin fell below $60,000 on Friday (Reuters) and later below $57,000, its lowest level since September 2024, according to CoinDesk. CoinGlass data cited by CoinDesk showed $2.40 billion of leveraged crypto positions liquidated in 24 hours. US spot bitcoin ETFs had $1.79 billion of net outflows in the week, the most in 21 weeks (Crypto Briefing). In Yahoo Finance data, bitcoin's UTC close fell 13.8% for the week, and it touched about $55,150 on Saturday (UTC) before closing above $61,000 on Sunday.

### Why systematic traders care

Liquidations feed on themselves: forced selling pushes the price lower, which liquidates the next layer of leveraged longs. That is when crypto spreads widen and stops slip. If you trade crypto with leverage, size positions so a cascade like this cannot wipe out your margin.

## The week ahead: what is still uncertain

- **PCE inflation, Wednesday November 25** at 8:30 a.m. ET (BEA), the Fed's preferred gauge, a week after the hot CPI.
- **Thanksgiving:** US stock markets close on Thursday November 26 and close early, at 1 p.m. ET, on Friday. Thin holiday trading can mean wider spreads and sharper moves.
- **Nvidia:** Huang is set for closed-door interviews with three House committees on December 1 (CNBC).
- **Fed, December 8–9:** a quarter-point hike is priced in; the size is still debated.

## Sources

- AP via WTOP, index closes: [Nov 16](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-monday-11-16-2026/), [Nov 18](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-wednesday-11-18-2026/), [Nov 19](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-thursday-11-19-2026/), [Nov 20](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-friday-11-20-2026/)
- [Reuters via Yahoo Finance: Nov 20 close](https://finance.yahoo.com/news/wall-st-futures-slip-anthropic-104746137.html)
- [Investopedia: Nov 20](https://investopedia.com/stock-market-today-dow-jones-s-and-p-500-nasdaq-11202026-12266027)
- CNBC: [selloff](https://cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html), [Nvidia](https://www.cnbc.com/2026/11/18/nvidia-stock-earnings.html), [Anthropic IPO](https://www.cnbc.com/2026/11/18/anthropic-ipo-ai-offering-price.html), [ANT debut](https://www.cnbc.com/2026/11/19/anthropic-ipo-ant-live-updates.html), [Fed minutes](https://cnbc.com/amp/2026/11/18/fed-minutes-october-2026.html), [yields](https://www.cnbc.com/2026/11/20/treasury-yields-bonds-inflation.html)
- Bloomberg via Yahoo Finance: [Goldman, CTAs](https://finance.yahoo.com/markets/stocks/articles/goldman-says-stock-selloff-legs-212055157.html), [VIX](https://finance.yahoo.com/markets/options/articles/vix-hits-highest-level-since-212233067.html)
- [Nvidia: Q3 FY2027 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Third-Quarter-Fiscal-2027/default.aspx)
- SEC report: [24/7 Wall St. via Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/nvidia-stock-plunges-12-reuters-201702082.html), [Decrypt](https://decrypt.co/383744/nvidia-shares-sink-52-week-low-sec-probing-accounting)
- [Anthropic: IPO closing](https://www.anthropic.com/news/ipo-close)
- [Reuters via Euronext: IPO pricing](https://live.euronext.com/en/financial-news/anthropic-raises-record-81-billion-ipo-15-trillion-valuation)
- [Federal Reserve: October minutes](https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm)
- [US Treasury: yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611)
- CoinDesk: [bitcoin, Nov 21](https://www.coindesk.com/markets/2026/11/21/bitcoin-tanks-below-usd57-000-for-the-first-time-in-two-years-and-its-not-alone), [Fed bets, Nov 23](https://www.coindesk.com/markets/2026/11/23/market-rout-kills-50-basis-points-december-fed-rate-hike-bets)
- [Crypto Briefing: ETF flows](https://cryptobriefing.com/bitcoin-etf-outflows-blackrock-ibit-weekly/)
- [BEA: release schedule](https://www.bea.gov/news/schedule/full)
- [Yahoo Finance: holiday hours](https://finance.yahoo.com/markets/stocks/articles/stock-market-open-thanksgiving-black-110415213.html)
- Yahoo Finance data: [NVDA](https://finance.yahoo.com/quote/NVDA/history/), [ANT](https://finance.yahoo.com/quote/ANT/history/), [VIX](https://finance.yahoo.com/quote/%5EVIX/history/), [BTC](https://finance.yahoo.com/quote/BTC-USD/history/), [DXY](https://finance.yahoo.com/quote/DX-Y.NYB/history/), [USD/JPY](https://finance.yahoo.com/quote/JPY%3DX/history/), [gold](https://finance.yahoo.com/quote/GC%3DF/history/), [Brent](https://finance.yahoo.com/quote/BZF27.NYM/history/) and [Nikkei](https://finance.yahoo.com/quote/%5EN225/history/)
