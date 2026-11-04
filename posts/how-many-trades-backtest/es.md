Un backtest con 40 operaciones y un win rate del 60% parece una prueba. Estadísticamente, se parece más a una moneda que salió cara 24 veces de 40: interesante, pero no demuestra nada. Cada número que reporta un backtest (win rate, esperanza matemática, profit factor) es una estimación hecha con una muestra, y las muestras pequeñas producen estimaciones amplias y ruidosas.

Este artículo muestra qué tan grande es ese ruido según el número de operaciones, con qué frecuencia la pura suerte pasa por ventaja, y una fórmula sencilla para estimar cuántas operaciones necesita una estrategia antes de que sus resultados signifiquen algo. Todos los números salen de una simulación hipotética, no de operaciones reales.

## Un backtest es una muestra, no una medición

Piensa que una estrategia tiene un win rate "verdadero" y una esperanza matemática "verdadera": los valores que verías si pudiera operar las mismas condiciones de mercado para siempre. Un backtest nunca ve "para siempre". Ve un tramo de la historia, y las operaciones de ese tramo son una extracción al azar de lo que la estrategia pudo haber hecho.

Dos estrategias con la misma ventaja real producirán backtests distintos, igual que dos personas que lanzan la misma moneda justa 40 veces obtendrán conteos distintos. La pregunta no es "¿qué mostró el backtest?", sino "¿qué tan lejos de la verdad podría estar este resultado, con tan pocas operaciones?"

Esa distancia se llama **error de muestreo**, y se reduce con la raíz cuadrada del número de operaciones. Para reducir el error a la mitad necesitas cuatro veces más operaciones, no el doble.

## ¿Qué tan grande es la incertidumbre?

Toma una estrategia hipotética que gana el 40% de las veces, gana 2R en las ganadoras (el doble de lo arriesgado) y pierde 1R en las perdedoras. Su esperanza matemática real es 0.40 × 2 − 0.60 × 1 = **+0.20R por operación**, y llega al punto de equilibrio con un win rate del 33.3%. El resultado de cada operación oscila mucho alrededor de ese promedio: la desviación estándar es de unos 1.47R por operación.

Supón que un backtest muestra exactamente esos números. Este es el rango de confianza del 95% a su alrededor con distintos tamaños de muestra (el rango del win rate usa el intervalo de Wilson que recomienda el [e-Handbook de NIST/SEMATECH](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm); el de la esperanza usa la aproximación normal):

| Operaciones | Rango del win rate (95%) | Rango de la esperanza (95%) |
|---|---|---|
| 20 | 21.9% a 61.3% | −0.44R a +0.84R |
| 50 | 27.6% a 53.8% | −0.21R a +0.61R |
| 100 | 30.9% a 49.8% | −0.09R a +0.49R |
| 300 | 34.6% a 45.6% | +0.03R a +0.37R |
| 1,000 | 37.0% a 43.1% | +0.11R a +0.29R |

Con 20, 50 e incluso 100 operaciones, el rango todavía incluye una esperanza negativa. El rango del win rate con 100 operaciones va desde debajo del 33.3% de equilibrio hasta casi el 50%. Solo alrededor de las 300 operaciones el rango completo queda por encima de cero, y aun así la estrategia podría valer desde apenas positivo hasta casi el doble de lo estimado.

> El win rate y la esperanza de un backtest vienen con un margen de error. Con menos de unas 100 operaciones, ese margen suele ser más ancho que la ventaja que intentas medir.

## Cuando la suerte parece ventaja

Los rangos de confianza son abstractos, así que también simulamos el problema directamente.

> **Simulación hipotética.** La estrategia A es la de arriba: una ventaja real de +0.20R. La estrategia Z no tiene ninguna ventaja: gana el 40% de las veces a +1.5R / −1R, así que su esperanza real es exactamente cero. Para cada número de operaciones corrimos 100,000 backtests independientes de cada estrategia, con operaciones independientes y sin costos.

| Operaciones | A (ventaja real) muestra pérdida | Z (sin ventaja) muestra profit factor ≥ 1.3 | Z (sin ventaja) muestra esperanza ≥ +0.20R |
|---|---|---|---|
| 20 | 24.8% | 24.3% | 24.3% |
| 50 | 15.7% | 15.5% | 15.5% |
| 100 | 9.1% | 9.3% | 6.4% |
| 300 | 0.8% | 1.1% | 0.3% |
| 1,000 | <0.1% | <0.1% | <0.1% |

Lee con calma la fila de 20 operaciones. Una estrategia realmente rentable mostró un backtest perdedor aproximadamente una vez de cada cuatro. Una estrategia sin ninguna ventaja se vio al menos tan bien como la rentable, también una vez de cada cuatro. Con 20 operaciones, el backtest casi no sirve para distinguirlas.

Empeora cuando corres muchos backtests. También probamos 50 variantes sin ventaja con 50 operaciones cada una y nos quedamos con la mejor, 20,000 veces. El profit factor de la ganadora fue de al menos 1.3 en más del 99.9% de las corridas, con una mediana de 1.91, aunque ninguna variante tenía ventaja. Es el problema del sobreajuste de nuestro artículo sobre [por qué un backtest casi perfecto suele estar sobreajustado](/blog/why-perfect-backtests-overfit?lang=es): las muestras pequeñas y las muchas pruebas se multiplican entre sí.

## ¿Cuántas operaciones son suficientes?

Una forma práctica de juzgar un backtest es la relación entre su operación promedio y la incertidumbre de ese promedio, un estadístico t:

**t = esperanza ÷ (desviación estándar por operación ÷ √operaciones)**

Si la despejas, te dice aproximadamente cuántas operaciones necesitas para llegar a cierto t:

**operaciones ≈ (t × desviación estándar ÷ esperanza)²**

Un t de 2 corresponde más o menos al nivel de significancia clásico del 5% (a dos colas). La tabla usa el mismo pago de 2R / 1R de arriba con distintos win rates reales:

| Win rate | Esperanza | Operaciones para t = 2 | Operaciones para t = 3 |
|---|---|---|---|
| 35.0% | +0.05R | 3,277 | 7,372 |
| 36.7% | +0.10R | 835 | 1,878 |
| 40.0% | +0.20R | 216 | 486 |
| 43.3% | +0.30R | 99 | 222 |

Hay dos cosas que llaman la atención. Primero, las ventajas pequeñas necesitan muestras enormes: si reduces la esperanza a la mitad, las operaciones necesarias se multiplican aproximadamente por cuatro. Segundo, la forma del pago también importa. Con la esperanza fija en +0.20R, una estrategia que gana el 60% a 1R / 1R necesita unas 97 operaciones para t = 2, mientras que una que gana el 24% a 4R / 1R necesita unas 457, porque las ganancias grandes y poco frecuentes hacen mucho más ruidoso el resultado de cada operación.

### Por qué t = 2 suele quedarse corto

El umbral del 5% supone que hiciste una sola prueba. En un artículo de 2016 en *The Review of Financial Studies*, Campbell Harvey, Yan Liu y Heqing Zhu contaron cientos de factores de rentabilidad publicados y argumentaron que, teniendo en cuenta cuántos se habían probado, un factor nuevo debería superar un estadístico t de 3.0, y que un t de 2.0 "ya no es apropiado". Su tema era la investigación académica, pero la lógica aplica a cualquiera que pruebe muchas variantes de una estrategia: cuanto más buscas, más alta debe ser la vara. Con t = 3, nuestra estrategia de +0.20R necesita casi 500 operaciones.

## No cada operación cuenta como una

Las fórmulas de arriba suponen que cada operación es una apuesta independiente. Las operaciones reales muchas veces no lo son:

- **Grupos.** Una estrategia que abre cinco posiciones en la misma hora, por la misma noticia, hizo algo más parecido a una apuesta que a cinco.
- **Símbolos correlacionados.** Estar largo en EUR/USD y en GBP/USD al mismo tiempo es, en buena parte, la misma operación sobre el dólar estadounidense.
- **Un solo régimen.** 400 operaciones hechas durante un único año de tendencia te dicen cómo se comporta la estrategia en ese tipo de mercado, no en un rango ni en un desplome.

Repetimos la estrategia A con 300 operaciones agrupadas en 60 grupos de cinco, donde cada operación de un grupo comparte el mismo resultado. Contadas de forma ingenua, 300 operaciones dan un t de 2.36. Contadas como las 60 apuestas independientes que realmente son, el t cae a 1.05. En la simulación, la proporción de backtests con pérdida subió de menos del 1% con 300 operaciones independientes al 11.6% con 60 grupos de cinco.

El mismo problema afecta a los ratios de rentabilidad. En "The Statistics of Sharpe Ratios" (*Financial Analysts Journal*, 2002), Andrew Lo mostró que ignorar la correlación serial de los retornos mensuales podía exagerar hasta en un 65% el Sharpe ratio anual de un hedge fund. La dependencia entre resultados hace que un historial parezca más confiable de lo que es.

## Una lista de verificación práctica

- **Lee cada métrica de un backtest como un rango**, no como un punto. Un win rate del 55% con 60 operaciones es compatible con un win rate real de entre un 42% y un 67%, aproximadamente.
- **Estima cuántas operaciones necesitas antes de probar.** Usa la fórmula con una estimación conservadora de la ventaja. Si la respuesta es muchas más operaciones de las que tus datos pueden producir, prueba con más símbolos, un historial más largo u otra temporalidad, o acepta que el resultado seguirá siendo incierto.
- **Sube la vara según cuántas variantes hayas probado.** Una idea probada una vez puede vivir con t = 2. Un barrido de cientos de combinaciones necesita más.
- **Cuenta apuestas independientes, no ejecuciones.** Agrupa las operaciones que se abren juntas o en instrumentos correlacionados, y asegúrate de que la muestra abarque más de un régimen de mercado.
- **Guarda datos no vistos para la prueba final.** El holdout de investigación de Period Trader, por ejemplo, no aprueba un backtest a menos que tenga al menos 15 operaciones en datos apartados de la búsqueda y al menos 40 operaciones en total. Son mínimos, no una prueba; tu propia regla de operaciones mínimas puede ser más estricta.
- **Trata igual los primeros resultados en vivo.** Diez operaciones en vivo dicen muy poco sobre si una estrategia sigue funcionando, en cualquier dirección.

## Lecturas recomendadas

- Harvey, C. R., Liu, Y. y Zhu, H. (2016). "… and the Cross-Section of Expected Returns." *The Review of Financial Studies*, 29(1), 5–68. [DOI 10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059) · [PDF del autor](https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.PDF)
- Lo, A. W. (2002). "The Statistics of Sharpe Ratios." *Financial Analysts Journal*, 58(4), 36–52. [DOI 10.2469/faj.v58.n4.2453](https://doi.org/10.2469/faj.v58.n4.2453)
- NIST/SEMATECH e-Handbook of Statistical Methods, [7.2.4.1 Intervalos de confianza para una proporción](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) (en inglés)
