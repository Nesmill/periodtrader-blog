Una estrategia puede tener una ventaja real antes de costos y aun así perder dinero después de ellos. El spread, la comisión y el slippage se cobran en cada operación, gane o pierda, y es fácil subestimarlos en un backtest porque parecen diminutos al lado del precio.

Este artículo muestra cómo medir los costos en la unidad que importa, lo que arriesgas en cada operación, con un ejemplo hipotético y una simulación. La versión corta: los mismos costos que apenas tocan una estrategia lenta pueden borrar una rápida.

## Tres costos, una sola factura

Cada operación completa, de la entrada a la salida, paga alguna combinación de:

- **Spread.** La diferencia entre el bid y el ask. Una compra a mercado se ejecuta al ask y una venta a mercado al bid, así que una operación que entra y sale a mercado paga aproximadamente un spread completo por ida y vuelta.
- **Comisión.** En muchas cuentas de forex y CFD, un monto fijo por lote. En los exchanges de cripto, normalmente un porcentaje del valor nocional de la posición (la comisión taker, para las órdenes que se ejecutan al instante).
- **Slippage.** La diferencia entre el precio que esperabas y el que obtuviste. Las órdenes stop-loss están especialmente expuestas: como explica Investor.gov, de la SEC, el precio stop "no es el precio de ejecución garantizado". Es un disparador que convierte el stop en una orden a mercado, y la ejecución "puede desviarse significativamente del precio stop".

El financiamiento nocturno (swap) es un cuarto costo, que aquí dejamos de lado.

En el resto del artículo usamos un solo supuesto hipotético de costos en un par parecido a EURUSD, donde un pip vale $10 por lote estándar: un spread promedio de 0.6 pips, una comisión de $7 por lote ida y vuelta (0.7 pips) y 0.2 pips de slippage promedio, para un total de **1.5 pips por ida y vuelta**.

## Mide los costos en R, no en pips

Lo que importa no son los 1.5 pips, sino el costo en relación con lo que arriesga la operación. Si R es lo que pierdes cuando salta el stop, el costo de una ida y vuelta en R es:

> Costo en R = costo de ida y vuelta ÷ distancia del stop

Con el dimensionamiento de fracción fija, esto tiene un significado concreto en dólares. Una cuenta hipotética de $10,000 que arriesga el 1% pone $100 en juego en cada operación. Un stop más ajustado significa una posición más grande, y una posición más grande paga más spread y más comisión:

| Stop | Posición para $100 de riesgo | Costo por ida y vuelta | Costo en R |
|---|---|---|---|
| 5 pips | 2.00 lotes | $30.00 | 0.30R |
| 10 pips | 1.00 lote | $15.00 | 0.15R |
| 20 pips | 0.50 lotes | $7.50 | 0.075R |
| 50 pips | 0.20 lotes | $3.00 | 0.03R |
| 100 pips | 0.10 lotes | $1.50 | 0.015R |

El riesgo es de $100 en cada fila, pero el stop de 5 pips paga veinte veces el costo del de 100 pips, porque su posición es veinte veces más grande.

## Lo que los costos le hacen a la esperanza matemática

Ahora toma una estrategia hipotética que gana el 45% de sus operaciones, apunta a 1.5 veces su stop y pierde 1R cuando salta el stop. Antes de costos, su esperanza matemática es 0.45 × 1.5 − 0.55 × 1 = **+0.125R por operación**, su profit factor es 1.23 y queda en equilibrio con un win rate del 40%.

Los costos golpean a ganadoras y perdedoras por igual: cada ganancia deja 1.5R menos el costo y cada pérdida cuesta 1R más el costo, así que la esperanza neta es la esperanza bruta menos el costo en R. Suponemos las mismas estadísticas en R con cualquier stop, para aislar el efecto de los costos:

| Stop | Esperanza neta | Win rate de equilibrio | Profit factor neto | Ventaja bruta que se va en costos |
|---|---|---|---|---|
| Sin costos | +0.125R | 40.0% | 1.23 | 0% |
| 5 pips | −0.175R | 52.0% | 0.76 | 240% |
| 10 pips | −0.025R | 46.0% | 0.96 | 120% |
| 20 pips | +0.050R | 43.0% | 1.08 | 60% |
| 50 pips | +0.095R | 41.2% | 1.17 | 24% |
| 100 pips | +0.110R | 40.6% | 1.20 | 12% |

Con los costos incluidos, el win rate de equilibrio pasa a ser (1 + costo en R) ÷ (1 + relación beneficio-riesgo). Con un stop de 5 pips necesita un win rate del 52% solo para quedar en equilibrio, y gana el 45%: las mismas señales, una estrategia perdedora.

### Las mismas señales, 500 operaciones

> **Simulación hipotética.** 20,000 secuencias aleatorias de 500 operaciones de la estrategia anterior, con un tamaño del 1% del capital actual por operación. Cada tamaño de stop opera las **mismas** 20,000 secuencias, así que solo cambian los costos.

| Stop | Corridas que terminan por debajo del inicio | Capital final mediano | Drawdown máximo mediano |
|---|---|---|---|
| Sin costos | 1.7% | 1.80× | 15.6% |
| 5 pips | 99.9% | 0.40× | 62.8% |
| 10 pips | 72.4% | 0.85× | 32.3% |
| 20 pips | 22.4% | 1.24× | 21.4% |
| 50 pips | 6.0% | 1.55× | 17.5% |
| 100 pips | 3.3% | 1.67× | 16.6% |

Sin costos, menos del 2% de las corridas terminó por debajo de donde empezó. Con un costo de 1.5 pips y un stop de 5 pips, casi todas lo hicieron, y la corrida mediana perdió el 60% de su capital.

## Mientras más operas, más grande tiene que ser la ventaja

Los costos se pagan por operación, así que crecen con la frecuencia. En el ejemplo anterior, la versión de 5 pips paga 30R en costos cada 100 operaciones frente a una ventaja bruta de 12.5R. La versión de 100 pips paga 1.5R.

La investigación con carteras reales apunta en la misma dirección. Barber y Odean estudiaron 66,465 hogares estadounidenses de un gran bróker de descuento entre 1991 y 1996. Los hogares que más operaban obtuvieron un 11.4% neto al año, frente al 17.9% del mercado y el 18.5% de los que menos operaban, con rendimientos brutos muy parecidos. En sus palabras, son "el costo de operar y la frecuencia de las operaciones, no la selección de la cartera", lo que explica los malos resultados. Los costos eran mucho más altos entonces: en sus datos, la ida y vuelta promedio de más de $1,000 costaba cerca de un 3% en comisiones y un 1% en spread. El mecanismo no ha cambiado.

Novy-Marx y Velikov pusieron a prueba un gran conjunto de anomalías publicadas del mercado de acciones después de los costos de trading. La mayoría de las estrategias con una rotación mensual (de un solo lado) inferior al 50% mantuvo rendimientos netos estadísticamente significativos, al menos cuando estaban diseñadas para operar menos, pero "pocas de las estrategias con mayor rotación lo logran". Los costos también redujeron la significancia estadística en todos los casos, "lo que aumenta las preocupaciones relacionadas con el data snooping", el mismo problema que hay detrás de los [backtests sobreajustados](/blog/why-perfect-backtests-overfit).

## Los costos no son una constante

Un backtest sencillo cobra un costo fijo por operación. Los costos reales se mueven:

- **Los spreads se amplían cuando baja la liquidez.** Un informe de 2017 del Banco de Pagos Internacionales (BIS) sobre la liquidez del mercado de divisas señala que los creadores de mercado algorítmicos suelen responder al estrés "ampliando los precios antes de dejar de cotizarlos por completo". En el evento relámpago del 7 de octubre de 2016, la libra cayó un 9% frente al dólar en las primeras horas asiáticas, y las órdenes stop-loss ejecutadas ayudaron a agotar la poca liquidez de la principal plataforma al contado.
- **Los stops se deslizan en mercados rápidos y con gaps.** Un stop que se convierte en orden a mercado se ejecuta al siguiente precio disponible, que después de un gap de fin de semana o de un dato económico importante puede quedar muy lejos del stop.
- **Un spread cotizado no es un spread promedio.** Uno consultado en un momento tranquilo puede subestimar lo que una estrategia paga en las horas en que opera.

Un stop ajustado amplifica cada fracción de pip adicional, así que estas variaciones castigan más a las estrategias de corto plazo.

## Cómo incluir los costos en un backtest

- **Usa los números de tu propio bróker**: el spread promedio de varios días, la comisión por lote de ida y vuelta o la comisión taker del exchange, no el mejor caso de una página de marketing.
- **Convierte los costos a R** según tu stop habitual. Si los costos se comen una parte grande de la ventaja esperada por operación, la estrategia tiene poco margen de error.
- **Cobra los costos en cada operación**, ganadoras y perdedoras, y añade un margen de slippage en las salidas por stop.
- **Haz una prueba de estrés con el doble de costo.** En nuestro ejemplo, la versión de 20 pips sigue en positivo con 1.5 pips (+0.05R) pero pasa a negativo con 3 pips (−0.025R), mientras que la de 50 pips conserva +0.065R.
- **Compara las ejecuciones en vivo con el backtest.** Si el spread y el slippage reales salen más altos de lo supuesto, vuelve a correr la investigación con las cifras reales.

Period Trader incluye estos costos en su investigación. En MT5, cada backtest cobra el spread medido en las cotizaciones recientes de tu cuenta conectada más la comisión por lote de ida y vuelta de tu bróker (la cifra que introduces en SETUP, o una medida en tus propias operaciones liquidadas), y los backtests de cripto cobran la comisión taker del exchange. Un bot de investigación cuyos backtests corrieron sin esos costos aparece marcado con el aviso COSTS NOT PRICED.

> **Idea clave:** juzga una estrategia por su ventaja después de costos, medida en R. Mientras más ajustado sea el stop y más a menudo opere, más grande tiene que ser esa ventaja.

## Lecturas recomendadas

- B. M. Barber y T. Odean (2000), [Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors](https://doi.org/10.1111/0022-1082.00226), *Journal of Finance* 55(2). Hay una [copia gratuita](https://faculty.haas.berkeley.edu/odean/papers/returns/individual_investor_performance_final.pdf) en el sitio de UC Berkeley.
- R. Novy-Marx y M. Velikov (2016), [A Taxonomy of Anomalies and Their Trading Costs](https://doi.org/10.1093/rfs/hhv063), *Review of Financial Studies* 29(1). Las citas de arriba vienen del [documento de trabajo del NBER](https://www.nber.org/papers/w20721) de 2014, de acceso gratuito.
- Comisión de Bolsa y Valores de EE. UU. (SEC), Investor.gov: [Stop, Stop-Limit, and Trailing Stop Orders](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-15) (en inglés).
- Banco de Pagos Internacionales (2017), [Foreign exchange liquidity in the Americas](https://www.bis.org/publications/paper-90-foreign-exchange-liquidity-americas.pdf), BIS Papers No 90 (en inglés).
