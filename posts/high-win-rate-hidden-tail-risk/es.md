Una estrategia que gana nueve de cada diez operaciones suena segura. No lo es, o al menos no por esa razón. El win rate dice con qué frecuencia acierta una estrategia; no dice nada de cuánto pierde cuando se equivoca, y unas pocas pérdidas grandes pueden borrar cientos de ganancias pequeñas.

Este artículo muestra cómo un win rate alto puede esconder lo que los traders llaman riesgo de cola: pérdidas raras y grandes que un backtest corto muchas veces nunca llega a ver. Todos los números salen de ejemplos y simulaciones hipotéticos, no de trading real, salvo donde se cita una fuente.

## El win rate es solo la mitad de la ecuación

La expectativa de una estrategia, su resultado promedio por operación, necesita las dos mitades:

> Expectativa = win rate × ganancia promedio − tasa de pérdidas × pérdida promedio

Cuanto más alto el win rate, más grande puede ser la pérdida promedio antes de que la estrategia deje de ganar dinero. Este es el punto de equilibrio para distintos win rates:

| Win rate | Pérdida promedio máxima para quedar en equilibrio |
|---|---|
| 40% | 0.67 × la ganancia promedio |
| 50% | 1.00 × la ganancia promedio |
| 70% | 2.33 × la ganancia promedio |
| 90% | 9 × la ganancia promedio |
| 95% | 19 × la ganancia promedio |
| 99% | 99 × la ganancia promedio |

Un win rate del 90% no es un margen de seguridad. Es un presupuesto: la estrategia puede perder como mucho nueve ganancias promedio por cada operación perdedora. Si sus pérdidas son mayores, cada operación adicional achica la cuenta, por muchas veces que gane.

## Un historial perfecto que pierde dinero

> **Estrategia hipotética T.** Gana el 97% de sus operaciones con +1 unidad y pierde el 3% con −40 unidades. Su expectativa es 0.97 × 1 − 0.03 × 40 = **−0.23 unidades por operación**, y su profit factor real es 0.81. Para quedar en equilibrio necesitaría ganar el 97.6% de las veces.

La estrategia T pierde dinero a largo plazo. Un backtest no siempre lo va a decir. Simulamos 200,000 backtests de la estrategia T para cada duración:

| Duración del backtest | No muestra ninguna operación perdedora | Muestra una ganancia neta |
|---|---|---|
| 20 operaciones | 54.4% | 54.4% |
| 50 operaciones | 21.8% | 55.5% |
| 100 operaciones | 4.8% | 42.0% |
| 200 operaciones | 0.2% | 28.1% |
| 500 operaciones | 0.0% | 26.4% |
| 1,000 operaciones | 0.0% | 15.3% |

Más de la mitad de los backtests de 20 operaciones muestran un historial perfecto: ninguna operación perdedora, un profit factor que ni siquiera se puede calcular y una curva de capital que solo sube. Incluso con 500 operaciones, más o menos uno de cada cuatro backtests todavía termina en ganancia.

La razón es pura aritmética. Para ver al menos una vez un evento que ocurre 1 de cada N veces, con un 95% de probabilidad, necesitas unas 3 × N operaciones. La gran pérdida de la estrategia T llega más o menos una vez cada 33 operaciones, así que un backtest necesita cerca de 100 operaciones para que sea probable que contenga una, y muchas más para contener suficientes y medir su frecuencia real. Nuestro artículo sobre [cuántas operaciones necesita un backtest](/blog/how-many-trades-backtest?lang=es) trata el problema general del tamaño de la muestra; el riesgo de cola lo empeora, porque las operaciones que más importan son las más raras.

## Martingala: un win rate del 99% por diseño

Algunos sistemas producen un win rate alto a propósito. El clásico es el tamaño martingala: después de cada pérdida, duplicas la siguiente operación para que una sola ganancia recupere toda la secuencia.

> **Martingala hipotética.** Cada operación gana o pierde lo mismo que arriesga, con un 49% de probabilidad de ganar (una moneda justa, menos un poco por costos). Un ciclo empieza con una apuesta del 0.5% del saldo inicial y se duplica después de cada pérdida, por un máximo de 7 operaciones: 0.5%, 1%, 2%, 4%, 8%, 16% y 32%. Una ganancia en cualquier paso cierra el ciclo con +0.5%.

El win rate por ciclo es del **99.1%**. El ciclo fallido, siete pérdidas seguidas, ocurre más o menos una vez cada 111 ciclos y pierde 127 apuestas base: **el 63.5% del saldo inicial**. El resultado esperado por ciclo es negativo (−0.15 apuestas base), porque las operaciones en sí no tienen ventaja y duplicar no puede crearla.

| Ciclos jugados | Probabilidad de al menos un ciclo fallido |
|---|---|
| 50 | 36.3% |
| 100 | 59.4% |
| 250 | 89.5% |
| 500 | 98.9% |
| 1,000 | más del 99.9% |

En 100,000 recorridos simulados, el recorrido mediano llegó a su primer ciclo fallido después de 77 ganancias seguidas. Para entonces iba un 38.5% arriba del saldo inicial, y el ciclo fallido lo dejó un 25% por debajo del inicio. La curva de capital antes del fallo es justo el tipo de curva que convence a la gente de operar un sistema.

La misma lógica aplica a los sistemas de grid, a promediar a la baja sin stop y a cualquier regla que aumente el tamaño después de perder. Se pueden operar con límites estrictos, pero hay que juzgarlos por su peor ciclo, no por su win rate.

## Los mercados reales bajan por el ascensor

El riesgo de cola no es solo un efecto de las simulaciones. Brunnermeier, Nagel y Pedersen estudiaron el carry trade de divisas, que consiste en pedir prestado en una moneda de interés bajo para mantener otra de interés alto. Encontraron que estas operaciones están expuestas a riesgo de desplome: los movimientos del tipo de cambio entre monedas de tasa alta y de tasa baja tienen asimetría negativa. Como dice el estudio, el hallazgo es coherente con el dicho de los traders de que los tipos de cambio "suben por la escalera y bajan por el ascensor".

Un ejemplo más claro es el franco suizo. Según el [informe anual 2015](https://snb.ch/public/asset/en/www-snb-ch/publications/communication/annual-report/annrep_2015_komplett/publications0_en/annrep_2015_komplett.en.pdf) del Banco Nacional Suizo (SNB), rigió un tipo de cambio mínimo de 1.20 francos por euro desde el 6 de septiembre de 2011 hasta el 15 de enero de 2015. El 15 de enero el SNB [lo eliminó](https://snb.ch/public/publication/en/www-snb-ch/publications/communication/press-releases/2015/pre_20150115/publications0_en/pre_20150115.en.pdf), y en los minutos después del anuncio el tipo de cambio cayó a un mínimo histórico de 0.85 francos por euro, antes de estabilizarse cerca de la paridad esa misma tarde.

De 1.20 a 0.85 hay un movimiento del 29.2%, o 3,500 pips, en cuestión de minutos. Una estrategia que comprara EUR/CHF cerca del piso habría tenido más de tres años de historia en los que comprar cerca de 1.20 funcionaba. Un backtest sobre esos años habría contenido cero ejemplos del piso fallando.

Un stop-loss no protege por completo contra este tipo de movimiento. Como explica el [boletín de Investor.gov sobre órdenes stop](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) de la SEC, el precio stop "no es el precio de ejecución garantizado": al activarse, el stop se convierte en una orden a mercado, y la ejecución puede desviarse de forma significativa del precio stop.

## Cómo detectar una cola oculta en un backtest

No puedes ver una pérdida que nunca ocurrió en tus datos, pero sí puedes buscar las condiciones que la producen:

- **Compara la peor pérdida con la ganancia promedio.** Si una operación perdedora cuesta 10 o 20 ganancias promedio, el win rate carga con el trabajo completo, y la próxima pérdida decide el resultado.
- **Revisa si hay un stop fijo.** Una estrategia que mantiene las operaciones perdedoras hasta que se recuperen va a mostrar un win rate alto hasta el día en que el mercado no se recupere.
- **Vigila las reglas de tamaño.** Cualquier cosa que aumente el tamaño después de una pérdida (martingala, ciclos de recuperación, promediar a la baja) convierte una racha perdedora normal en una sola pérdida muy grande.
- **Cuenta los eventos raros.** Si la gran pérdida de la estrategia puede llegar una vez cada 50 operaciones, un backtest de 50 operaciones casi no prueba nada. Apunta a unas tres veces ese número y prefiere datos que incluyan periodos de estrés: sorpresas de bancos centrales, desplomes, gaps de fin de semana.
- **Lee el profit factor con cuidado.** Un profit factor de 3 en 40 operaciones con solo dos pérdidas pequeñas es una evidencia más débil que un profit factor de 1.4 en 300 operaciones con rachas perdedoras reales.
- **Ponle un techo a la pérdida por operación.** En Period Trader, **Ajustes → Despliegue → Umbral de despliegue en vivo** tiene la regla **Pérdida máxima por operación**: la mayor pérdida individual que puede mostrar un backtest, en porcentaje del capital, antes de poder pasar a vivo. No puede ver pérdidas que no están en los datos, así que funciona junto con las revisiones anteriores, no en su lugar.

> Un win rate alto describe cómo gana una estrategia, no prueba que gane. Júzgala por sus peores operaciones y por cuántas oportunidades tuvo su backtest de mostrarlas.

## Lecturas recomendadas

- Brunnermeier, Nagel y Pedersen (2008), [Carry Trades and Currency Crashes](https://doi.org/10.1086/593088), *NBER Macroeconomics Annual* 23. Hay una versión gratuita del documento de trabajo en [NBER](https://www.nber.org/papers/w14473).
- Banco Nacional Suizo (15 de enero de 2015), [Swiss National Bank discontinues minimum exchange rate and lowers interest rate to −0.75%](https://snb.ch/public/publication/en/www-snb-ch/publications/communication/press-releases/2015/pre_20150115/publications0_en/pre_20150115.en.pdf).
- Comisión de Bolsa y Valores de EE. UU. (SEC), Investor.gov, [Stop, Stop-Limit, and Trailing Stop Orders – Investor Bulletin](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15).
