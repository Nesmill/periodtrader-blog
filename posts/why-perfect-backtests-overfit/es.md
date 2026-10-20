Quien desarrolla estrategias tarde o temprano se topa con el backtest que se ve demasiado bueno: una curva de capital suave, un drawdown mínimo y un ratio de Sharpe que impresionaría a un fondo de cobertura. La mayoría de las veces esa curva no es un descubrimiento. Es el resultado más afortunado entre muchos intentos, y el mercado no tiene ninguna obligación de repetirlo.

En este artículo te explicamos por qué pasa, qué tan grande es el efecto y cuáles son las dos pruebas que lo detectan antes de que una estrategia llegue a una cuenta real: la prueba fuera de muestra (out-of-sample) y el análisis walk-forward.

## Qué es realmente el sobreajuste

Un backtest vuelve a ejecutar un conjunto de reglas sobre datos históricos. Toda regla tiene parámetros (periodos de cálculo, umbrales de entrada, distancias del stop, filtros de sesión), y cada vez que ajustas uno y vuelves a correr el backtest, haces otra prueba. El sobreajuste (overfitting o curve fitting) ocurre cuando los parámetros terminan describiendo el ruido de esa muestra en particular en vez de un patrón que se repite.

La trampa es que el ruido imita muy bien a una señal. En un artículo muy citado de las *Notices of the American Mathematical Society*, Bailey, Borwein, López de Prado y Zhu probaron 8,800 combinaciones de parámetros de una regla mensual sencilla (día de entrada, días de permanencia, stop loss y dirección) sobre una serie de precios de paseo aleatorio, que por construcción no contiene ningún patrón. Aun así, la mejor combinación mostró un ratio de Sharpe anualizado de 1.27. No había nada que encontrar, y la búsqueda lo encontró de todos modos.

## Cómo el número de pruebas infla los resultados

Mientras más variantes pruebas, más alto saldrá la mejor solo por suerte. Corrimos una simulación sencilla para mostrar el tamaño del efecto.

> **Simulación hipotética.** Ninguna variante de la estrategia tiene ventaja real: sus retornos diarios se generan al azar con media cero y una desviación estándar de 1%. Cada variante tiene un backtest de 3 años dentro de muestra (in-sample), seguido de un año más que nunca vio. Nos quedamos con la variante de mejor ratio de Sharpe dentro de muestra y repetimos el experimento completo entre cientos y miles de veces.

| Variantes probadas | Mejor Sharpe dentro de muestra (promedio) | Sharpe fuera de muestra de esa elegida (promedio) | Elegidas con Sharpe dentro de muestra mayor que 1 |
|---|---|---|---|
| 1 | 0.01 | -0.03 | 5% |
| 10 | 0.89 | 0.01 | 34% |
| 100 | 1.46 | -0.01 | 99% |
| 1,000 | 1.89 | -0.02 | ~100% |

Con 100 variantes, la ganadora mostró un ratio de Sharpe dentro de muestra mayor que 1 en el 99% de las corridas. En el año que no había visto, promedió prácticamente cero (-0.01), que es su ventaja real. La ganadora no tenía nada especial, salvo su suerte. Estas cifras coinciden con la aproximación del artículo de Bailey y sus coautores, que predice 1.46 para 100 pruebas y 1.88 para 1,000 en este escenario.

El artículo plantea el mismo problema en función de la cantidad de datos. Con cinco años de datos diarios, unas 45 configuraciones independientes ya bastan para esperar que la mejor muestre un ratio de Sharpe de 1 dentro de muestra, aunque el Sharpe real de cada estrategia sea cero. Con dos años de datos, bastan unas siete configuraciones. La investigación real suele probar muchísimas más: una cuadrícula de 20 valores para un periodo y 20 para otro ya son 400 backtests. Los puntos vecinos de la cuadrícula están correlacionados, así que el número efectivo de pruebas independientes es menor, pero casi nunca lo bastante pequeño como para ignorarlo.

Hay dos detalles más que importan:

- **Cero no es el piso.** Nuestros retornos simulados no tenían memoria, así que la variante sobreajustada simplemente volvió a cero. El mismo artículo muestra que, cuando el rendimiento tiene memoria (por ejemplo, reversión a la media), quedarte con la mejor variante dentro de muestra puede llevar a resultados fuera de muestra *negativos*.
- **La exigencia debe subir con la búsqueda.** Harvey, Liu y Zhu argumentaron en la *Review of Financial Studies* que, como ya se han probado tantísimos factores de rendimiento, un factor nuevo necesita un estadístico t mayor que 3.0 en lugar del 2.0 habitual. La misma lógica aplica a tus propios barridos de parámetros.

## La prueba fuera de muestra: la primera línea de defensa

La idea es sencilla. Divide tu historial en dos partes. Desarrolla y ajusta la estrategia con la primera (dentro de muestra) y luego corre las reglas finales una sola vez sobre datos que nunca tocaste (fuera de muestra). Si la ventaja es real, el resultado fuera de muestra debería parecerse a una versión algo más débil del resultado dentro de muestra. Si la estrategia está sobreajustada, el resultado fuera de muestra tiende a desplomarse hacia cero o por debajo.

Algunas reglas hacen que la prueba tenga sentido:

- **Decide la división antes de empezar**, y deja el periodo fuera de muestra en el extremo más reciente de los datos.
- **Úsalo una sola vez por candidata.** Si miras el resultado fuera de muestra, vuelves atrás, ajustas un parámetro y pruebas otra vez en el mismo periodo, ese periodo se convirtió sin que lo notaras en datos dentro de muestra.
- **Haz que sea lo bastante largo.** Un periodo fuera de muestra con 20 operaciones puede verse excelente o terrible por pura casualidad; necesitas suficientes operaciones para distinguir una ventaja del ruido.
- **Incluye costos realistas** (spread, comisión y slippage) en ambos periodos. Las ventajas pequeñas suelen desaparecer cuando se cuentan los costos.

Una sola reserva de datos tiene límites. Es una única muestra y no sabe cuántas variantes probaste antes de llegar a ella. Bailey y sus coautores señalan que el método de reserva (hold-out) no toma en cuenta el número de pruebas, y su artículo posterior en el *Journal of Computational Finance* afirma que técnicas como la reserva de datos tienden a ser poco fiables e imprecisas en backtests de inversión. Por eso conviene una segunda capa.

## Análisis walk-forward: fuera de muestra, repetido

El análisis walk-forward, que Robert Pardo trata a fondo en *The Evaluation and Optimization of Trading Strategies*, convierte una sola reserva en muchas. Este es un calendario hipotético con cuatro años de datos:

1. Optimiza con los meses 1-12 y luego prueba los parámetros elegidos en los meses 13-15.
2. Desplaza ambas ventanas tres meses hacia adelante: optimiza con los meses 4-15 y prueba en los meses 16-18.
3. Sigue avanzando hasta que se acaben los datos. En este ejemplo salen 12 ventanas de prueba.
4. Une las 12 ventanas de prueba. La curva de capital resultante, de 36 meses, es completamente fuera de muestra, porque cada tramo se operó con parámetros elegidos solo con datos anteriores.

Qué revisar en el resultado:

- **Consistencia entre ventanas.** Una ventana espectacular que carga con otras once planas es una alerta, no una ventaja.
- **La diferencia entre dentro y fuera de muestra.** Cierto deterioro es normal. Un desplome es la firma del sobreajuste.
- **Estabilidad de los parámetros.** Si el "mejor" periodo salta de 9 a 47 y luego a 15 entre ventanas, lo más probable es que el optimizador esté persiguiendo ruido.
- **Drawdown.** Un drawdown fuera de muestra mucho más profundo que el de dentro de muestra merece una explicación antes que cualquier otra cosa.

El walk-forward tampoco es infalible. Sigue recorriendo un solo camino de la historia, y correrlo con muchas longitudes de ventana distintas hasta que una se vea bien es simplemente otra búsqueda. Fija las longitudes de las ventanas antes de mirar los resultados.

## Una lista de verificación práctica

- **Cuenta tus pruebas.** Anota cuántas variantes probaste. La mejor de 500 necesita una exigencia mucho más alta que la mejor de 5.
- **Toma la suavidad como una pregunta.** Una curva de capital casi perfecta es una razón para probar con más rigor, no para ponerla a operar.
- **Prefiere mesetas antes que picos.** Si los valores vecinos de un parámetro rinden parecido, es más probable que el resultado sea robusto que un pico aislado rodeado de pérdidas.
- **Deja los datos más recientes para el final**, y míralos una sola vez.
- **Haz el walk-forward con costos incluidos** antes de poner capital en juego.
- **Trata las primeras semanas en cuenta real como otra prueba fuera de muestra**, con un tamaño de posición acorde.

El bot de investigación de Period Trader sigue el mismo principio: clasifica las configuraciones en una ventana de desarrollo que termina 30 días antes de los datos más recientes, y una configuración solo puede convertirse en la campeona de un trabajo si también se sostiene en esos 30 días que nunca vio, frente a una exigencia estadística que sube con el número de configuraciones que el trabajo ha probado.

> **Idea clave:** un backtest te dice qué tan bien un conjunto de reglas se ajusta al pasado. Solo los datos que esas reglas nunca han visto pueden decirte si aprendieron algo.

## Lecturas recomendadas

- Bailey, Borwein, López de Prado y Zhu (2014), [Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance](https://doi.org/10.1090/noti1105), *Notices of the AMS* 61(5).
- Bailey, Borwein, López de Prado y Zhu (2017), [The Probability of Backtest Overfitting](https://doi.org/10.21314/JCF.2016.322), *Journal of Computational Finance* 20(4).
- Harvey, Liu y Zhu (2016), [… and the Cross-Section of Expected Returns](https://doi.org/10.1093/rfs/hhv059), *Review of Financial Studies* 29(1).
- Robert Pardo (2008), [The Evaluation and Optimization of Trading Strategies, 2.ª edición](https://www.wiley.com/en-us/the-evaluation-and-optimization-of-trading-strategies-2nd-edition-p-9780470128015), Wiley.
