La semana pasada (19 al 23 de octubre de 2026) los mercados se movieron entre dos temores: que el auge del gasto en inteligencia artificial choque con un muro de financiamiento y que la guerra con Irán vuelva a encenderse. Las tecnológicas tuvieron su peor día desde junio, el rendimiento del Tesoro a 10 años su mayor caída diaria desde marzo de 2023 y el Brent subió por tercera semana seguida.

Aquí tienes qué cambió, por qué importa si operas de forma sistemática y qué sigue en el aire antes de una semana cargada de bancos centrales y resultados de grandes tecnológicas.

## La semana en números

| Mercado | Cierre, viernes 23 oct | Cambio vs. viernes 16 oct |
|---|---|---|
| S&P 500 | 7,623.68 | -0.5% |
| Nasdaq Composite | 25,955.34 | -0.7% |
| Dow Jones Industrial Average | 52,215.16 | +0.4% |
| Russell 2000 | 2,775.90 | +2.0% |
| Rendimiento del Tesoro de EE. UU. a 10 años | 5.00% | -9 pb |
| Brent, futuros de diciembre | $116.72 | +6.2% |
| EUR/USD | 1.1221 | +0.1% |
| USD/JPY | 156.49 | -1.0% |
| Bitcoin (USD) | $81,074 | -0.5% |

Datos: AP (índices), Tesoro de EE. UU. (rendimiento), CNBC (liquidación del Brent) y datos diarios de Yahoo Finance (divisas; bitcoin al cierre diario en UTC). Los porcentajes los calculamos nosotros.

## 1. Acciones de IA: el peor día del Nasdaq desde junio

El jueves 22 de octubre, el Nasdaq Composite cayó 2.6% hasta 26,008.86, su peor sesión desde junio, y el S&P 500 perdió 1.21%, su peor día desde julio, mientras el Dow cerraba ligeramente al alza. Meta bajó cerca de 7% tras elevar su previsión de inversión en capital, pese a que sus ingresos superaron lo esperado. Nvidia cayó cerca de 4%, AMD más de 8% y CoreWeave, proveedor de nube para IA, 10%. Según Reuters, el índice de semiconductores de Filadelfia se hundió 6.7%, su mayor caída diaria desde junio.

La preocupación no es la demanda, sino el dinero. Jensen Huang, CEO de Nvidia, dijo a CNBC que la demanda de nubes especializadas en IA está "por las nubes", pero que el capital escasea. Un analista citado por CBS News señaló que el gasto en IA supera el flujo de caja operativo, así que las empresas dependen de los mercados de deuda y de acciones.

La caída fue concentrada: en la semana el Nasdaq perdió 0.7%, mientras el Dow ganó 0.4% y el Russell 2000, de empresas pequeñas, subió 2%. El viernes el patrón se invirtió: los chips rebotaron y el Dow cayó 1.2% al extenderse las ventas a otros sectores.

### Por qué le importa al trader sistemático

La misma estrategia en un índice del Nasdaq y en el Dow tuvo semanas muy distintas, aunque ambos sean "acciones de EE. UU.". Y el jueves las acciones ligadas a la IA cayeron juntas: así una canasta de cinco nombres de IA termina comportándose como una sola posición grande.

## 2. Bonos del Tesoro: el de 10 años baja de 5% y luego rebota

Según los datos diarios del Tesoro de EE. UU., el rendimiento a 10 años pasó de 5.13% el miércoles a 4.96% el jueves: 17 puntos básicos en una sesión. CNBC y Reuters coincidieron en que fue la mayor baja diaria desde el 10 de marzo de 2023, y lo llevó por debajo de 5% por primera vez desde el 23 de septiembre. El viernes volvió a 5.00%, con una baja semanal de 9 puntos básicos.

Lo interesante es la dirección. A inicios de mes, el petróleo y la inflación habían llevado los rendimientos a 10 y 30 años a sus niveles más altos en más de dos décadas. El jueves, en cambio, los inversionistas compraron bonos mientras caían las acciones. "Por primera vez en un tiempo, los bonos del Tesoro están funcionando como refugio", dijo a CNBC un gestor de renta fija.

### Por qué le importa al trader sistemático

La relación entre acciones y bonos no es fija. Si tu portafolio o tu cobertura asume que los bonos suben cuando las acciones caen, revisa cómo se comportó esa relación en el período de tu backtest: este mes cambió en cuestión de semanas.

## 3. Petróleo: el Brent sube 6% por el temor a nuevos ataques contra Irán

Los futuros del Brent subieron 4% el jueves hasta $113.17 y otro 3.1% el viernes hasta $116.72, la liquidación más alta desde el 29 de abril, según CNBC. En la semana ganó 6.2%, su tercera alza semanal seguida. El WTI liquidó el viernes en $103.27, con un alza semanal de cerca de 2%.

El detonante fue un reporte de The New York Times sobre planes de EE. UU. e Israel para nuevos ataques contra Irán después de las elecciones de medio término, y el comentario de Trump el miércoles de que no estaban negociando con Teherán y de que algo pasaría "bastante pronto". Además, siguieron los ataques de los hutíes contra Arabia Saudita. Hasta la mañana del lunes no se habían reportado nuevos ataques contra Irán; el domingo, Trump dijo a Fox News que "se acerca el momento de decidir" entre un acuerdo y reanudar los ataques, mientras mediadores de Catar visitaban Teherán. Los últimos ataques confirmados de EE. UU. contra Irán fueron el 1 de septiembre, según CNBC.

### Una trampa de roll en tu gráfico del Brent

El Brent de diciembre deja de negociarse el viernes 30 de octubre: según las reglas de ICE, un contrato vence el último día hábil del segundo mes antes de la entrega. El viernes, diciembre liquidó en $116.72 y enero, el contrato siguiente, cerró en $111.70 según Yahoo Finance: una diferencia de $5.02, o 4.3%.

El lunes hacia las 9:05 a. m. (hora de Nueva York), el Brent de diciembre cotizaba cerca de $115.30, alrededor de 1.2% por debajo del viernes. Pero un gráfico continuo que ya había pasado a enero mostraba unos $110.30: en apariencia, una caída de 5.5% desde $116.72. La mayor parte de esa "caída" es el cambio de contrato, no el mercado.

Si haces backtest u operas con futuros continuos o CFD del Brent, revisa cómo manejan el roll tus datos y tu bróker. Un salto de roll sin ajustar puede disparar stops y señales que nunca ocurrieron en un contrato negociable.

## 4. Cripto: los flujos de los ETF van y vienen y bitcoin se acerca a $80,000

En los ETF de bitcoin al contado de EE. UU., las entradas de los primeros días se revirtieron el jueves con unos $635 millones de salidas netas, el mayor retiro diario desde el 25 de junio según datos de SoSoValue citados por Cointelegraph. El rastreador de Decrypt lo situó en $635.6 millones, casi 60% de los cerca de $1,070 millones captados en las tres sesiones anteriores.

El precio se movió menos que los flujos. Bitcoin cerró el viernes en $81,074, 0.5% menos que una semana antes, tras tocar unos $84,800 el miércoles. El fin de semana bajó hasta un cierre dominical de $80,024, cerca de 5.7% por debajo de ese máximo.

### Por qué le importa al trader sistemático

Cripto cotiza el fin de semana, cuando acciones, bonos y futuros están cerrados; con una decisión sobre Irán pendiente, bitcoin fue uno de los pocos mercados que podían reaccionar en tiempo real. Eso sí, la liquidez es menor: según Yahoo Finance, el volumen de bitcoin del domingo fue cerca de la mitad del volumen del viernes. Conviene revisar el backtest de una estrategia cripto separando fines de semana y días laborables.

## 5. Forex: el yen se fortalece mientras bajan los rendimientos de EE. UU.

El USD/JPY abrió la semana en 157.79 y llegó a 158.68 el 20 de octubre, según MUFG Research. Cuando el apetito por riesgo se enfrió el jueves, el par perforó 157, el mínimo del mes, y cayó por debajo de 156.50 temprano el viernes antes de recuperarse hacia 157. Según Yahoo Finance, perdió cerca de 1.0% en la semana. El EUR/USD terminó prácticamente sin cambios, alrededor de 1.12.

### Por qué le importa al trader sistemático

El USD/JPY suele seguir la diferencia de tasas entre EE. UU. y Japón, así que un movimiento grande en los bonos del Tesoro puede llegar al yen en cuestión de horas. Con la Fed y el Banco de Japón decidiendo esta semana, una estrategia en yenes enfrenta dos decisiones de tasas en unos dos días.

## La semana que viene: lo que sigue en duda

- **Fed, miércoles 28 de octubre (2:00 p. m., hora de Nueva York).** El rango objetivo está en 3.75% a 4.00% desde la subida de septiembre. Los precios de CME FedWatch citados por Trading Economics daban cerca de 9% de probabilidad a una subida esta semana y más de 80% a una en diciembre, y pueden cambiar rápido.
- **Microsoft y Alphabet (miércoles después del cierre) y Amazon (jueves después del cierre).** Sus planes de inversión están en el centro del debate sobre el financiamiento de la IA.
- **BCE el jueves 29 de octubre y Banco de Japón el 29 y 30 de octubre.**
- **Irán.** Sigue abierto si continúan las conversaciones o se reanudan los ataques, con las elecciones de medio término de EE. UU. el 3 de noviembre.

El spread suele ampliarse y el precio puede abrir con gaps alrededor de decisiones así. El gráfico de Period Trader marca los datos económicos como banderas en el eje de tiempo, con líneas discontinuas para los próximos eventos de alto impacto, así ves cuándo un bot está a punto de operar en medio de uno. Si la volatilidad está cambiando la distancia de tus stops, nuestra guía sobre [cuánto arriesgar por operación](/blog/how-much-to-risk-per-trade) explica cómo mantener constante el riesgo.

## Fuentes

- [CNBC, 22 oct: Nasdaq](https://www.cnbc.com/2026/10/21/stock-market-today-live-updates.html)
- [CBS News, 22 oct: gasto en IA](https://www.cbsnews.com/news/nasdaq-ai-spending-debt-investors-concerns-stocks/)
- [Reuters vía The Globe and Mail, 22 oct](https://www.theglobeandmail.com/investing/markets/inside-the-market/market-news/article-premarket-global-stocks-fall-bonds-gain-as-meta-dents-tech-optimism/)
- [CNBC, 23 oct: cierre](https://www.cnbc.com/2026/10/22/stock-market-today-live-update.html)
- [AP vía WTOP, 23 oct](https://wtop.com/national/2026/10/how-major-us-stock-indexes-fared-friday-10-23-2026)
- [Tesoro de EE. UU.: rendimientos diarios](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202610)
- [CNBC, 22 oct: bonos](https://www.cnbc.com/2026/10/22/treasurys-bonds-ai-yields.html)
- [CNBC, 23 oct: Brent](https://www.cnbc.com/2026/10/23/oil-price-brent-wti-iran-war-saudi-arabia.html)
- [CNBC, 26 oct: Irán](https://www.cnbc.com/2026/10/26/us-iran-war-hormuz.html)
- [CBS News: Irán en vivo](https://www.cbsnews.com/live-updates/iran-war-trump-us-diplomacy-oil-prices-strait-of-hormuz/)
- [ICE: futuro del Brent](https://www.ice.com/products/219/Brent-Crude-Futures)
- [Yahoo Finance: Brent dic 2026](https://finance.yahoo.com/quote/BZZ26.NYM/history/) y [ene 2027](https://finance.yahoo.com/quote/BZF27.NYM/history/)
- [Cointelegraph, 23 oct: ETF de bitcoin](https://cointelegraph.com/markets/bitcoin-etfs-erase-october-gains-outflow)
- [Decrypt vía Yahoo Finance, 23 oct](https://finance.yahoo.com/markets/crypto/articles/bitcoin-etfs-bleed-636-million-155041101.html)
- [Yahoo Finance: bitcoin](https://finance.yahoo.com/quote/BTC-USD/history/), [USD/JPY](https://finance.yahoo.com/quote/JPY%3DX/history/) y [EUR/USD](https://finance.yahoo.com/quote/EURUSD%3DX/history/)
- [MUFG Research: JPY Weekly, 26 oct](https://www.mufgresearch.com/fx/jpy-weekly-26-october-2026/)
- [FXStreet, 23 oct: EUR/USD semanal](https://www.fxstreet.com/analysis/eur-usd-weekly-forecast-next-bounce-could-be-a-trap-202610231834)
- [Reserva Federal: calendario](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) y [comunicado del 16 sep](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)
- [Trading Economics](https://tradingeconomics.com/calendar?article=29376&g=top&importance=2&startdate=2026-10-23/news/594727)
- [BCE: calendario](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html)
- [Banco de Japón: calendario](https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm)
- [StockTitan: resultados](https://www.stocktitan.net/articles/earnings-calendar-week-of-october-26-2026)
