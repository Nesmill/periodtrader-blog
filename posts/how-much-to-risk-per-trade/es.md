Dos traders pueden operar exactamente la misma estrategia, con las mismas entradas, salidas y ventaja, y terminar en lugares completamente distintos. Uno hace crecer la cuenta de forma estable. El otro pasa casi el año entero en un drawdown profundo o quema la cuenta. La única diferencia es cuánto arriesga cada uno por operación.

Este artículo muestra por qué el tamaño de posición importa tanto como la estrategia misma, con una simulación hipotética: cómo funciona el dimensionamiento de fracción fija, cómo las rachas perdedoras normales se convierten en drawdowns, qué dice el criterio de Kelly sobre la apuesta "óptima" y por qué la respuesta prudente suele ser mucho más pequeña que la óptima.

## El dimensionamiento de fracción fija en una fórmula

Dimensionar con fracción fija significa que cada operación arriesga el mismo porcentaje de tu capital **actual**. Aquí "riesgo" es lo que pierdes si salta el stop, no el tamaño de la posición:

> Tamaño de posición = (capital × % de riesgo) ÷ (distancia del stop × valor por unidad de movimiento del precio)

Un ejemplo hipotético: una cuenta de $10,000 que arriesga el 1% pone $100 en juego. Si el stop en EURUSD está a 25 pips y un lote estándar vale unos $10 por pip, la posición es $100 ÷ (25 × $10) = 0.40 lotes. Si alejas el stop a 50 pips, la posición se reduce a la mitad, 0.20 lotes, y el riesgo en dólares sigue siendo $100.

De ahí salen dos consecuencias:

- **El stop decide el tamaño, no al revés.** Eliges el stop donde la idea de la operación deja de ser válida y luego dejas que la fórmula te diga qué tan grande puede ser la posición.
- **El tamaño baja después de las pérdidas y sube después de las ganancias.** Cada pérdida es un porcentaje de un saldo más pequeño, así que en teoría una serie de stops nunca lleva la cuenta a cero. En la práctica, los gaps y el slippage pueden hacer que una sola pérdida sea mayor de lo previsto.

## Las rachas perdedoras no son eventos raros

Para que los números sean concretos, toma una estrategia hipotética que gana el 40% de sus operaciones, gana 2R en las ganadoras (el doble de lo arriesgado) y pierde 1R en las perdedoras. Su esperanza matemática es 0.40 × 2 − 0.60 × 1 = **+0.2R por operación**, y su win rate de equilibrio con una relación beneficio-riesgo de 2:1 es 100 ÷ (1 + 2) = 33.3%. Sobre el papel es una estrategia realmente rentable.

Aun así, pierde la mayoría de sus operaciones. En 500 operaciones, nuestro cálculo da un 97% de probabilidad de al menos una racha de 8 o más pérdidas seguidas, un 71% de una racha de 10 o más y un 35% de una de 12 o más. En las corridas simuladas, la mediana de la racha perdedora más larga fue de 11 operaciones.

Esto es lo que hacen diez pérdidas seguidas con distintos niveles de riesgo:

| Riesgo por operación | Tras 5 pérdidas | Tras 10 pérdidas | Ganancia necesaria para recuperar 10 pérdidas |
|---|---|---|---|
| 0.5% | -2.5% | -4.9% | +5.1% |
| 1% | -4.9% | -9.6% | +10.6% |
| 2% | -9.6% | -18.3% | +22.4% |
| 5% | -22.6% | -40.1% | +67.0% |
| 10% | -41.0% | -65.1% | +186.8% |

La última columna muestra la asimetría que hace tan caro arriesgar mucho: un drawdown del 10% necesita una ganancia del 11.1% para recuperarse, uno del 50% necesita un 100% y uno del 75% necesita un 300%.

## La misma ventaja, distinto riesgo: un Monte Carlo

> **Simulación hipotética.** 20,000 secuencias aleatorias de 500 operaciones de la estrategia anterior (win rate del 40%, +2R / −1R, operaciones independientes). Cada nivel de riesgo opera las **mismas** 20,000 secuencias, así que lo único que cambia es el tamaño de cada apuesta.

El riesgo de ruina suele referirse a la probabilidad de perder tanto que ya no puedes continuar. Como aproximación a ese punto, la tercera columna cuenta las corridas que en algún momento cayeron un 50% o más desde un máximo, un hueco que necesita una ganancia del 100% para salir.

| Riesgo por operación | Mediana del drawdown máximo | Corridas con drawdown de 50% o más | Corridas que terminan por debajo del inicio | Mediana del capital final |
|---|---|---|---|---|
| 0.5% | 7.9% | 0% | 0.1% | 1.63× |
| 1% | 15.4% | menos de 0.1% | 0.2% | 2.57× |
| 2% | 29.2% | 2.0% | 0.2% | 5.95× |
| 5% | 60.8% | 84.5% | 0.9% | 39.4× |
| 10% | 88.7% | 100% | 6.5% | 128.5× |
| 20% | 99.9% | 100% | 48.0% | 1.42× |

Hay tres cosas que resaltan:

- **Al principio, el drawdown crece casi en la misma proporción que el riesgo.** Pasar del 1% al 2% casi duplicó el peor drawdown típico, de alrededor del 15% a alrededor del 29%.
- **Más riesgo deja de pagar.** El crecimiento mediano sube con el riesgo hasta el 10% por operación y luego se desploma: con el 20%, la corrida mediana termina en apenas 1.42× su inicio, menos que la fila del 1%, y casi la mitad de las corridas pierde dinero, con la misma ventaja de +0.2R en cada operación.
- **Los números grandes de crecimiento no se pueden operar.** La fila del 10% solo funciona si aguantas un drawdown mediano de casi el 89%. Poca gente seguiría operando con eso, y una cuenta apalancada puede recibir un stop-out por margen mucho antes.

Estas cifras salen de una ventaja fija y conocida de antemano. El trading real nunca te da eso, y eso importa más que cualquier número de la tabla.

## El criterio de Kelly, y por qué los traders apuestan menos

En un artículo de 1956 en el *Bell System Technical Journal*, John L. Kelly Jr. calculó el tamaño de apuesta que maximiza la tasa de crecimiento del capital a largo plazo. Para una operación que gana con probabilidad *p* y paga *b* veces lo arriesgado, la fracción de Kelly es *p* − (1 − *p*) ÷ *b*. MacLean, Thorp y Ziemba la resumen como la ventaja dividida entre las probabilidades de pago (las "odds"). Para nuestra estrategia eso da 0.40 − 0.60 ÷ 2 = **10%**, justo la fila con el mayor crecimiento y el drawdown mediano del 89%.

Los mismos autores son directos sobre la desventaja: el criterio de Kelly "puede ser muy arriesgado a corto plazo" y, en su análisis en tiempo continuo, apostar el doble de Kelly lleva la tasa de crecimiento a largo plazo a casi cero. Nuestra fila del 20% (el doble de Kelly) muestra lo mismo. Su conclusión es que quien invierte buscando crecimiento a largo plazo "debería apostar Kelly o menos".

Apostar menos cuesta sorprendentemente poco crecimiento. En un ejemplo de blackjack que citan (con una ventaja del 2%), apostar la mitad de la fracción de Kelly conservó cerca del 75% de la tasa de crecimiento y subió la probabilidad de duplicar el capital antes de perder la mitad del 67% al 89%.

### El verdadero problema: no conoces tu ventaja

Kelly asume que conoces *p* y *b*. Un trader solo tiene estimaciones, normalmente de un backtest, y [los backtests tienden a exagerar la ventaja](/blog/why-perfect-backtests-overfit?lang=es). Repetimos la simulación con un win rate real del 35% en lugar del 40%. La estrategia sigue siendo rentable sobre el papel (+0.05R por operación), pero dimensionada al 10% como si el win rate fuera del 40%:

- la corrida mediana terminó en **0.10×** su capital inicial, y el 78.5% de las corridas perdió dinero;
- el mismo error con un riesgo del 1% terminó en una mediana de **1.22×**, con el 27% de las corridas por debajo del inicio y una mediana del drawdown máximo del 24.7%.

Arriesgar poco no es solo más cómodo. También deja margen para equivocarte sobre la ventaja. MacLean, Thorp y Ziemba plantean lo mismo: como el crecimiento es tan sensible a los errores en la media estimada, "para ir a lo seguro, el tamaño de las apuestas debería reducirse".

## Lo que la fórmula deja fuera

- **Costos.** El spread, la comisión y el slippage se suman al stop. Un mercado que abre con gap después del fin de semana puede ejecutar un stop muy lejos de su nivel.
- **Tamaño mínimo de operación.** En una cuenta hipotética de $500, el 1% son $5. Si el tamaño más pequeño que acepta el bróker pierde $10 en tu stop, en realidad estás arriesgando el 2%, el doble de lo que elegiste.
- **Posiciones correlacionadas.** Tres operaciones largas en dólar al 1% cada una se comportan más como una sola apuesta del 3% cuando el dólar se mueve.
- **Varias estrategias a la vez.** El riesgo abierto total se acumula entre bots y cuentas.

Period Trader se encarga de la parte del dimensionamiento y del tamaño mínimo en los bots de MT5: calcula cada orden a partir del stop que realmente queda puesto en el bróker, de modo que un stop-out cuesta aproximadamente el porcentaje del capital que elegiste (1% por defecto). Cuando el tamaño mínimo que acepta el bróker obliga a arriesgar más que eso, la orden se envía igual, y la tarjeta del bot lo marca con una insignia OVER que muestra el porcentaje real.

## Una lista de verificación práctica

- **Dimensiona a partir del stop.** Decide dónde la idea deja de ser válida y luego calcula la posición.
- **Fija el porcentaje de riesgo antes de la operación**, y no lo subas para recuperar una pérdida.
- **Planifica la racha.** En nuestro ejemplo hipotético, la probabilidad de una racha de 10 o más pérdidas en 500 operaciones fue de alrededor del 71%. Ten claro qué le hace eso a tu cuenta con el riesgo que elegiste.
- **Si usas Kelly, usa una fracción de una estimación conservadora**, nunca la cifra completa de un backtest.
- **Cuenta el riesgo abierto total**, incluyendo posiciones correlacionadas y cada estrategia en marcha.
- **Revisa el riesgo real en cuentas pequeñas** frente al tamaño mínimo del bróker.

> **Idea clave:** la ventaja decide si una estrategia puede ganar dinero. El tamaño de cada apuesta decide si todavía sigues operando cuando lo hace.

## Lecturas recomendadas

- J. L. Kelly Jr. (1956), [A New Interpretation of Information Rate](https://doi.org/10.1002/j.1538-7305.1956.tb03809.x), *Bell System Technical Journal* 35(4).
- MacLean, Thorp y Ziemba (2010), [Long-term capital growth: the good and bad properties of the Kelly and fractional Kelly capital growth criteria](https://doi.org/10.1080/14697688.2010.506108), *Quantitative Finance* 10(7). Una versión anterior gratuita, [Good and bad properties of the Kelly criterion](https://www.stat.berkeley.edu/~aldous/157/Papers/Good%5FBad%5FKelly.pdf), está disponible en el sitio de UC Berkeley.
