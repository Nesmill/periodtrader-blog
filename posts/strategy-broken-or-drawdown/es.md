Toda estrategia termina pasando por una racha perdedora, y la pregunta más difícil del trading sistemático es qué significa. Si te detienes demasiado pronto, abandonas un sistema que funciona en el fondo de un drawdown normal; si te detienes demasiado tarde, sigues pagando por una ventaja que ya desapareció. En nuestra simulación hipotética, una estrategia con una ventaja genuina tuvo una racha de 10 o más pérdidas seguidas en el 70% de sus historiales de 500 operaciones.

Este artículo explica por qué las ventajas dejan de funcionar, cómo luce un drawdown normal en números y qué tan bien funcionan cuatro reglas de parada comunes cuando conocemos la respuesta correcta.

## Por qué una estrategia que funciona puede dejar de funcionar

Hay tres razones distintas por las que una estrategia empieza a perder, y cada una pide una respuesta diferente.

### 1. El mercado cambió de régimen

Los mercados pasan de un estado a otro: con tendencia y en rango, tranquilos y volátiles. Los economistas lo modelan de forma explícita. El artículo de James Hamilton de 1989 en *Econometrica* propuso una forma muy utilizada de modelar los "cambios de régimen", en la que una misma serie alterna entre estados con comportamientos distintos.

Una estrategia que sigue tendencias y una de reversión a la media ganan dinero en regímenes diferentes, así que cualquiera de las dos puede perder durante meses simplemente porque el mercado está en el otro estado. El momentum ofrece un ejemplo bien documentado. Kent Daniel y Tobias Moskowitz encontraron que los colapsos del momentum ocurren "en estados de pánico, después de caídas del mercado y cuando la volatilidad es alta", mientras el mercado rebota. De marzo a mayo de 2009, las acciones con los peores rendimientos pasados subieron un 163%, mientras que las ganadoras pasadas apenas ganaron un 8%: un período durísimo para cualquier estrategia que comprara ganadoras y vendiera perdedoras.

### 2. La ventaja se desgastó

Algunas ventajas se reducen para siempre porque otros traders las descubren. David McLean y Jeffrey Pontiff estudiaron 97 predictores de rendimiento de acciones publicados y encontraron que los rendimientos de las carteras eran un 26% menores fuera de la muestra y un 58% menores después de la publicación. El patrón seguía ahí, pero mucho más débil.

La Hipótesis de los Mercados Adaptativos de Andrew Lo ofrece una visión intermedia: las estrategias "crecen y menguan", funcionan bien en algunos entornos y mal en otros, y pueden decaer durante un tiempo y luego volver a ser rentables.

### 3. Nunca hubo una ventaja

La tercera posibilidad es la incómoda: el backtest estaba [sobreajustado](/blog/why-perfect-backtests-overfit) o era [demasiado corto para demostrar algo](/blog/how-many-trades-backtest), y el trading en vivo simplemente lo está revelando.

> Una racha perdedora no te dice cuál de las tres está pasando. Por eso la decisión de parar tiene que tomarse con números, idealmente antes de que empiece el drawdown.

## Cómo luce un drawdown normal

Toma una estrategia hipotética que gana el 40% de sus operaciones, gana 2R en las ganadoras (el doble de lo arriesgado) y pierde 1R en las perdedoras. Su expectativa es de **+0.20R por operación**: una ventaja real y sana. Simulamos 20,000 historiales independientes de 500 operaciones cada uno:

| Lo que medimos (estrategia sana) | Resultado |
|---|---|
| Probabilidad de que un tramo dado de 20 operaciones pierda dinero | 25.0% |
| Probabilidad de que un tramo dado de 50 operaciones pierda dinero | 15.6% |
| Probabilidad de que un tramo dado de 100 operaciones pierda dinero | 9.1% |
| Historiales con al menos un tramo perdedor de 50 operaciones | 98.9% |
| Racha perdedora más larga (mediana / peor 5%) | 11 / 16 operaciones |
| Mayor tiempo sin un nuevo máximo de capital (mediana / peor 5%) | 93 / 219 operaciones |
| Drawdown máximo (mediana / peor 5%) | 16R / 28R |

Las tres primeras filas son probabilidades binomiales exactas; el resto sale de la simulación. Lee la tabla como una advertencia sobre la intuición. Una estrategia rentable en promedio tendrá, en casi cualquier historial de 500 operaciones, al menos un tramo de 50 operaciones que pierde dinero, y el historial típico pasa 93 operaciones sin marcar un nuevo máximo. Con un riesgo del 1% por operación, un drawdown de 16R equivale aproximadamente a una caída del 15% en la cuenta.

> Las rachas perdedoras y los meses planos son parte de una estrategia que funciona, no una prueba de que esté rota.

## Cuatro reglas de parada, probadas donde conocemos la respuesta

Para comparar las reglas de forma justa, construimos un segundo escenario: la misma estrategia hace 200 operaciones sanas y luego su ventaja se rompe. Su win rate cae al 30%, así que la expectativa pasa a ser de **−0.10R por operación**. Una buena regla debería activarse rara vez con la estrategia sana y detectar rápido la rota. Aplicamos cada regla a 5,000 historiales sanos de 500 operaciones y a 5,000 escenarios con ruptura:

| Regla de parada | Estrategia sana detenida en 500 operaciones | Mediana de operaciones tras la ruptura hasta activarse |
|---|---|---|
| 10 pérdidas seguidas | 70.2% | 78 |
| Últimas 50 operaciones con resultado neto negativo | 98.6% | 30 |
| Drawdown mayor de 28R | 4.8% | 150 |
| CUSUM sobre los resultados en R | 6.0% | 140 |

Las dos reglas intuitivas parecen rápidas, pero son rápidas porque se activan con casi cualquier cosa. Detuvieron la estrategia sana en la mayoría de los historiales y, en el escenario con ruptura, muchas veces ya se habían activado durante las 200 operaciones sanas (en el 38% de las simulaciones con la regla de la racha y en el 80% con la regla de las 50 operaciones).

Las dos reglas calibradas casi nunca detienen una estrategia sana (alrededor del 5% de las veces, por diseño), pero necesitan una mediana de 140 a 150 operaciones después de la ruptura para activarse. A −0.10R por operación, un retraso de 140 operaciones cuesta unos 14R en promedio, aproximadamente un 13% de la cuenta con un riesgo del 1% por operación.

Ese equilibrio no es un defecto de ninguna regla en particular. Cuando los resultados de una estrategia oscilan más de 1R por operación y la ventaja que vigilas es una fracción de 1R, distinguir "mala suerte" de "estrategia rota" exige muchas operaciones. Ninguna regla es rápida y confiable a la vez.

### Cómo funciona CUSUM

CUSUM (suma acumulada) viene del control de calidad industrial y lo presentó E. S. Page en 1954. En términos de trading:

1. Elige un nivel de referencia a mitad de camino entre lo que esperas (+0.20R) y lo que considerarías una estrategia rota (−0.10R): aquí, +0.05R.
2. Después de cada operación, suma lo que el resultado quedó por debajo de esa referencia, y vuelve el total a cero cada vez que quedaría negativo.
3. Detente cuando el total cruce un umbral elegido para que una estrategia sana rara vez lo alcance. En nuestra simulación, un umbral de 33R produjo un 6% de falsas alarmas en 500 operaciones.

Se parece mucho a un drawdown medido contra la ganancia que la estrategia debería haber obtenido, y por eso aquí reaccionó un poco más rápido que la regla de drawdown simple.

## Cómo decidir antes del drawdown

- **Escribe la regla de parada antes de operar en vivo.** Básala en la distribución de drawdowns y rachas perdedoras del propio backtest, como en la tabla de arriba, y no en cómo se sienten las pérdidas en el momento.
- **Mide en R, no en dinero.** Así la regla sigue siendo válida cuando cambian el tamaño de la posición o el balance de la cuenta.
- **Conoce el régimen de tu estrategia.** Divide el backtest en períodos con tendencia y en rango, o tranquilos y volátiles, y mira de dónde salió la ganancia. Un drawdown que llega en un régimen que el backtest señala como malo es información útil; un drawdown en el mejor régimen de la estrategia merece más sospecha.
- **Revisa la ejecución antes de culpar a la ventaja.** Spreads más amplios o más slippage pueden borrar una ventaja en silencio; mira [cómo los costos de trading se comen la ventaja de una estrategia](/blog/trading-costs-spread-commission-slippage).
- **No reajustes la estrategia a las últimas pérdidas.** Ajustar parámetros hasta que desaparezca el drawdown reciente es sobreajuste con una muestra más pequeña. Mejor vuelve a probarla con datos nuevos que no haya visto.
- **Considera reducir el tamaño en lugar de elegir entre ambos extremos.** Bajar el riesgo mientras se acumula evidencia limita el costo de una ventaja rota sin renunciar a una sana.

En Period Trader, cuando configuras un bot de investigación con una sola estrategia, una línea de **Encaje con el mercado** lee las velas del último año del mercado elegido e indica si sus movimientos tienden a continuar o a revertirse, con una etiqueta de buen encaje, encaje regular o mal encaje para el estilo de esa estrategia. Describe el último año, así que tómala como punto de partida: los regímenes pueden cambiar, que es justamente el tema de este artículo.

## Lecturas recomendadas

- Hamilton, J. D. (1989), [A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle](https://doi.org/10.2307/1912559), *Econometrica* 57(2).
- Page, E. S. (1954), [Continuous Inspection Schemes](https://doi.org/10.1093/biomet/41.1-2.100), *Biometrika* 41(1-2).
- Lo, A. W. (2004), [The Adaptive Markets Hypothesis](https://doi.org/10.3905/jpm.2004.442611), *Journal of Portfolio Management* 30(5). Hay una [copia gratuita](https://web.mit.edu/Alo/www/Papers/JPM2004_Pub.pdf) en el sitio del MIT.
- McLean, R. D. y Pontiff, J. (2016), [Does Academic Research Destroy Stock Return Predictability?](https://doi.org/10.1111/jofi.12365), *Journal of Finance* 71(1).
- Daniel, K. y Moskowitz, T. J. (2016), [Momentum Crashes](https://doi.org/10.1016/j.jfineco.2015.12.002), *Journal of Financial Economics* 122(2), de acceso abierto.
