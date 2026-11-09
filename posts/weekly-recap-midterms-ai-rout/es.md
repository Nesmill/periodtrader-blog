La semana pasada (2 al 6 de noviembre de 2026) los mercados se movieron con fuerza alrededor de las elecciones de medio término en EE. UU. Las acciones tuvieron el miércoles su mejor día en meses y el jueves el peor desde abril de 2025 por la venta masiva de acciones de inteligencia artificial, y el desplome llegó a Asia, donde Corea del Sur detuvo la bolsa. Mientras tanto, el empleo en EE. UU. superó lo previsto, el Banco de Inglaterra subió las tasas y el Brent tuvo su mayor caída semanal desde abril.

Aquí tienes qué cambió, por qué importa al trader sistemático y qué sigue abierto.

## La semana en números

| Mercado | Cierre, viernes 6 nov | Cambio vs. viernes 30 oct |
|---|---|---|
| S&P 500 | 7,376.86 | -2.7% |
| Nasdaq Composite | 24,579.42 | -3.4% |
| Dow Jones Industrial Average | 51,285.73 | -0.9% |
| Rendimiento del Tesoro de EE. UU. a 10 años | 4.86% | -8 pb |
| Brent, futuros de enero | $98.32 | -13.3% |
| WTI, futuros de diciembre | $90.83 | -12.8% |
| EUR/USD | 1.1228 | +0.4% |
| GBP/USD | 1.3456 | +0.6% |
| USD/JPY | 157.50 | -0.2% |
| Bitcoin (USD) | $75,747 | -1.9% |
| Kospi (Corea del Sur) | 5,059.69 | -11.7% |
| Nikkei 225 (Japón) | 57,434.77 | -9.3% |

Datos: AP (índices de EE. UU.), Tesoro de EE. UU. (rendimientos) y datos diarios de Yahoo Finance (liquidaciones de futuros, divisas, índices asiáticos; bitcoin al cierre diario en UTC). Los porcentajes los calculamos nosotros.

## 1. Elecciones: un rally de alivio y luego un desplome de la IA

Los demócratas ganaron el control de la Cámara de Representantes y del Senado en las elecciones del martes. El miércoles el S&P 500 subió 1.6% y el Dow saltó unos 1,570 puntos, o 3%, su mayor ganancia del año, informó CBS News.

El jueves el ánimo cambió. El S&P 500 cayó 4.4% hasta 7,353.73, su peor día desde el choque arancelario del "Día de la Liberación" en abril de 2025, y el Nasdaq Composite bajó 5.5% y quedó 11.9% por debajo de su récord de octubre, lo que lo coloca en corrección (AP). El detonante fue la apuesta por la IA: los inversionistas temieron que las nuevas mayorías frenen la construcción de centros de datos de IA, que los votantes asocian con facturas eléctricas más altas. Nvidia cayó 9.3% y AMD 17.3%.

Según CNBC, ese día las "Siete Magníficas" perdieron más de $1 billón (un millón de millones) de valor de mercado, y cayeron los 11 sectores del S&P 500; el de tecnología de la información bajó 7.3%, su peor día desde marzo de 2020.

El viernes la tecnología recuperó parte de lo perdido: el Nasdaq subió 1.1% y el S&P 500 0.3%, mientras el Dow cedió 0.5%.

### Por qué le importa al trader sistemático

La volatilidad puede cambiar de régimen en una sola sesión. En los datos de Yahoo Finance, el VIX cerró en 16.61 el miércoles y en 28.18 el jueves, un salto de 70%. Una estrategia con distancias fijas de stop y objetivo de pronto ve movimientos mucho mayores en relación con esos niveles, así que los stops se tocan más a menudo. Calcular el tamaño de la posición según el riesgo, y no con un número fijo de contratos o acciones, mantiene la pérdida por operación cerca del porcentaje previsto cuando los rangos se amplían. Nuestro artículo sobre [cuánto arriesgar por operación](/blog/how-much-to-risk-per-trade) explica las cuentas.

La concentración también importa: cuando unas pocas acciones de chips pesan tanto en el índice, una estrategia sobre el índice y otra sobre acciones tecnológicas pueden ser la misma apuesta.

## 2. Asia: una pausa en Seúl y un mercado bajista en Tokio

Asia recibió el golpe el viernes. A las 9:03 a. m. en Seúl, la Bolsa de Corea activó un cortacircuitos de primer nivel en el Kospi después de que el índice cayera 8.52% hasta 4,924.61, y suspendió la negociación durante 20 minutos (Yonhap, Korea JoongAng Daily). Fue la undécima pausa de ese tipo en el índice este año. El Kospi cerró con una baja de cerca de 6%, en 5,059.69, y perdió 11.7% en la semana.

El Nikkei 225 de Japón cayó 5.96% hasta 57,434.77, más de 20% por debajo de su máximo de junio, la definición habitual de mercado bajista, informó CNBC.

### Por qué le importa al trader sistemático

Una pausa no es solo un gap. Según las reglas de la Bolsa de Corea, tal como las describe JoongAng Daily, durante esos 20 minutos no se aceptan órdenes nuevas; solo cancelaciones. Luego la negociación se reanuda con una subasta de precio único de 10 minutos. Un bot que opere en ese mercado verá órdenes rechazadas y un único precio de reapertura en lugar de cotizaciones continuas. Asegúrate de que tu estrategia maneje las órdenes rechazadas sin reintentar en bucle, y de que su backtest no suponga ejecuciones a precios que nunca se negociaron.

## 3. Empleo, rendimientos y un alza del Banco de Inglaterra

### Las nóminas de EE. UU. superan lo previsto

Las nóminas no agrícolas aumentaron en 165,000 en octubre, frente a 59,000 esperadas en un sondeo de Dow Jones, y la tasa de desempleo bajó a 4.1% desde 4.2%, informó CNBC. El titular de KPMG dijo que los avances "aseguran" una subida de tasas en diciembre. Tras el dato, CME FedWatch situó en 76.8% la probabilidad de un alza de un cuarto de punto de la Fed en la reunión del 8 y 9 de diciembre.

Aun así, los bonos del Tesoro subieron. En los datos diarios del Tesoro, el rendimiento a 10 años bajó de 4.94% a 4.86% en la semana, y el jueves AP señaló que esa baja podía indicar que los inversionistas buscaban refugio mientras caían las acciones.

### Banco de Inglaterra

El jueves el Banco de Inglaterra subió su tasa de referencia un cuarto de punto, a 4%, su primer aumento desde agosto de 2023. La votación fue de 8 a 1; Catherine Mann quería un alza de medio punto. El banco espera que la inflación británica, de 3.5% en septiembre, suba a cerca de 5% a mediados del próximo año por los precios de la energía. El gobernador Andrew Bailey dijo que, si no se resuelve el conflicto en Oriente Medio, es poco probable que esta sea la última subida. La próxima decisión es el 17 de diciembre.

### Por qué le importa al trader sistemático

Una mayor probabilidad de alzas normalmente subiría los rendimientos, pero el de 10 años bajó, probablemente porque los inversionistas buscaron refugio durante la caída de las acciones. Prueba las estrategias que operan datos macro con la reacción real de los precios, no con la que "debería" haber ocurrido.

## 4. Petróleo: la mayor caída semanal del Brent desde abril

El Brent de enero cayó 8.7% el miércoles porque los inversionistas apostaron a que el resultado electoral podría empujar a Washington a terminar la guerra con Irán, informó CNBC. El viernes liquidó en $98.32. Irán habría enviado una propuesta nuclear a Washington a través de Catar, pero los ataques a petroleros en el estrecho de Ormuz continuaron.

### El cambio de contrato, otra vez

CNBC informó una caída semanal de "más de 16%" para el Brent. Esa cifra compara el precio de enero del viernes con el contrato de diciembre, que venció el 30 de octubre en $117.64. Comparando el mismo contrato, el Brent de enero bajó de $113.43 a $98.32: 13.3%. Unos 3 puntos porcentuales de la cifra del titular vienen del cambio de contrato que explicamos [la semana pasada](/blog/weekly-recap-big-tech-binance-hack). Si tu fuente de datos usa un contrato continuo, verifica si está ajustado hacia atrás, o tu backtest registrará un movimiento que ninguna posición real en futuros vivió.

## 5. Cripto: liquidaciones y salidas de los ETF

El bitcoin llegó a $81,080 el miércoles y luego cayó junto con la tecnología. El cierre diario en UTC pasó de $80,405 el miércoles a $75,942 el jueves, una baja de 5.6%. Se liquidaron más de $1,000 millones en apuestas apalancadas en cripto, informó CoinDesk. En la semana, el bitcoin perdió 1.9%.

Los ETF de bitcoin al contado en EE. UU. tuvieron salidas netas de $1,280 millones, su peor semana desde finales de junio y suficiente para dejar en negativo sus flujos de 2026, según The Block (datos de SoSoValue) y los datos de Farside citados por crypto.news.

### Por qué le importa al trader sistemático

El jueves el bitcoin cayó más o menos lo mismo que el Nasdaq. Un bot de cripto y una estrategia sobre el Nasdaq quizá no sean tan independientes como parecen. Las cascadas de liquidaciones también hacen que, en días como el jueves, las órdenes stop en cripto puedan ejecutarse lejos de su precio de activación.

## La semana que viene: lo que sigue sin resolverse

- **IPC de octubre en EE. UU., martes 10 de noviembre** a las 8:30 a. m. (hora del Este), una de las últimas lecturas de inflación antes de la reunión de la Fed del 8 y 9 de diciembre.
- **Día de los Veteranos, miércoles 11 de noviembre.** Las bolsas de acciones de EE. UU. abren, pero SIFMA recomienda un cierre total para la negociación de bonos en dólares.
- **EE. UU. e Irán.** Siguen las conversaciones a través de Catar, y los ataques en Ormuz no se han detenido.

En eventos como estos, los spreads suelen ampliarse y los precios pueden abrir con gaps.

## Fuentes

- [AP vía WTOP: cierres del 6 nov](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-friday-11-6-2026), [5 nov](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-thursday-11-5-2026) y [4 nov](https://wtop.com/national/2026/11/how-major-us-stock-indexes-fared-wednesday-11-4-2026)
- [AP vía AZFamily, 5 nov: venta de IA](https://azfamily.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs)
- [CNBC, 5 nov: estadísticas de la caída](https://www.cnbc.com/2026/11/05/stock-market-selloff-ai-fears.html)
- [CNBC, 6 nov: mercados en vivo](https://www.cnbc.com/2026/11/05/stock-market-today-live-updates.html)
- [CBS News, 4 nov: resultado electoral y rally del Dow](https://www.cbsnews.com/news/stock-market-soar-democrats-take-control-of-congress)
- [Yonhap, 6 nov: pausa del Kospi](https://en.yna.co.kr/view/AEN20261106002100320)
- [Korea JoongAng Daily, 6 nov: cortacircuitos](https://www.koreajoongangdaily.com/business/kospi-tracks-us-stocks-to-tank-nearly-9-after-opening-triggering-circuit-breaker/12959005)
- [CNBC, 6 nov: empleo de octubre](https://www.cnbc.com/2026/11/06/jobs-report-october-2026.html)
- [KPMG, 6 nov: informe de empleo](https://kpmg.com/us/en/articles/2026/october-2026-jobs-report.html)
- [Tesoro de EE. UU.: curva diaria de rendimientos](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611)
- [Banco de Inglaterra: decisión de noviembre](https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026)
- [The Guardian, 5 nov: alza del BoE](https://www.theguardian.com/business/2026/nov/05/bank-of-england-raises-interest-rates-first-increase-for-more-than-three-years)
- [Central Banking, 5 nov: primera alza desde 2023](https://centralbanking.com/central-banks/monetary-policy/monetary-policy-decisions/7977775/bank-of-england-makes-first-rate-hike-since-2023)
- [CNBC, 6 nov: petróleo](https://www.cnbc.com/2026/11/06/oil-price-today-brent-wti.html)
- [CNBC TV18, 6 nov: caída semanal del petróleo](https://cnbctv18.com/market/commodities/crude-oil-prices-brent-biggest-weekly-loss-since-april-us-iran-war-de-escalation-strait-of-hormuz-west-asia-20028438.htm)
- [CoinDesk, 5 nov: bitcoin y liquidaciones](https://www.coindesk.com/markets/2026/11/05/bitcoin-crypto-stocks-caught-in-ai-trade-meltdown-but-wintermute-trader-sees-glass-half-full)
- [The Block, 7 nov: salidas de ETF](https://www.theblock.co/news/markets/2026-11-07-bitcoin-etfs-flip-negative-for-2026-after-1-28-billion-outflow-week-worst-since-june-435984)
- [crypto.news: flujos de ETF según Farside](https://crypto.news/bitcoin-ether-etfs-weekly-outflows-blackrock-november)
- [BLS: calendario del IPC](https://www.bls.gov/news.release/cpi.htm)
- [SIFMA: cierre por el Día de los Veteranos](https://sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026)
- [Yahoo Finance: Brent ene 2027](https://finance.yahoo.com/quote/BZF27.NYM/history/), [WTI dic 2026](https://finance.yahoo.com/quote/CLZ26.NYM/history/), [bitcoin](https://finance.yahoo.com/quote/BTC-USD/history/), [VIX](https://finance.yahoo.com/quote/%5EVIX/history/), [Kospi](https://finance.yahoo.com/quote/%5EKS11/history/), [Nikkei](https://finance.yahoo.com/quote/%5EN225/history/), [EUR/USD](https://finance.yahoo.com/quote/EURUSD%3DX/history/), [GBP/USD](https://finance.yahoo.com/quote/GBPUSD%3DX/history/) y [USD/JPY](https://finance.yahoo.com/quote/JPY%3DX/history/)
