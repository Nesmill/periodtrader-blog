Cuatro bots de trading que arriesgan un 1% por operación cada uno parecen cuatro riesgos pequeños y separados. Que lo sean de verdad depende de un número que la mayoría de los traders nunca mide: qué tanto se mueven juntos los resultados de las estrategias. En nuestra simulación hipotética, cuatro estrategias con la misma ventaja y el mismo tamaño del 1% pasaron de un drawdown mediano del 17% al 38% solo porque sus resultados se volvieron más correlacionados.

## Cuatro apuestas del 1% no siempre son cuatro riesgos pequeños

La correlación mide cómo se mueven juntas dos series, en una escala de −1 a +1. En 0, el resultado de una estrategia no te dice nada sobre el de la otra. En +1, ganan y pierden juntas, así que dos estrategias son en realidad una sola estrategia operada al doble de tamaño.

Lo que importa para el riesgo es la correlación de los **resultados** de las estrategias (su ganancia o pérdida operación por operación o día por día), no solo la de los precios que operan. La superposición se esconde en configuraciones muy comunes:

- **El mismo mercado con distintos ajustes.** Una estrategia de tendencia de 15 minutos y otra de 1 hora en oro pueden entrar fácilmente en el mismo movimiento.
- **Una divisa compartida.** EURUSD y GBPUSD cotizan ambos contra el dólar estadounidense, así que un movimiento amplio del dólar empuja a los dos en la misma dirección.
- **Una misma clase de activo.** Muchas criptomonedas tienden a subir y bajar junto con Bitcoin.
- **Entre clases de activos.** Un estudio del FMI encontró que la correlación entre los rendimientos de Bitcoin y del S&P 500 fue de 0.01 en 2017–19 y de 0.36 en 2020–21.

## ¿Cuánta diversificación tienes realmente?

La teoría de carteras usa esta aritmética desde el artículo de Harry Markowitz de 1952: el riesgo de una combinación depende de las correlaciones entre sus partes, no solo de sus tamaños individuales. Toma N estrategias con oscilaciones del mismo tamaño, cada una arriesgando lo mismo, y una correlación ρ entre los resultados de cada par:

> Oscilación combinada = oscilación de una estrategia × √(N + N × (N − 1) × ρ)
>
> Apuestas independientes efectivas = N ÷ (1 + (N − 1) × ρ)

| Estrategias | ρ = 0 | ρ = 0.3 | ρ = 0.6 | ρ = 0.9 |
|---|---|---|---|---|
| 2 | 2.00 | 1.54 | 1.25 | 1.05 |
| 4 | 4.00 | 2.11 | 1.43 | 1.08 |
| 10 | 10.00 | 2.70 | 1.56 | 1.10 |

La tabla muestra las apuestas independientes efectivas. Diez estrategias con una correlación de 0.3 te dan la diversificación de menos de tres independientes. A medida que agregas estrategias, el número efectivo nunca pasa de 1 ÷ ρ, que es 3.3 con ρ = 0.3. Agregar un quinto o un décimo bot parecido añade principalmente tamaño, no diversificación.

## Una simulación hipotética: la misma ventaja, distinta correlación

> **Simulación hipotética.** Cuatro estrategias, cada una con un win rate del 40%, +2R en las ganadoras y −1R en las perdedoras (expectativa de +0.2R por operación). Cada estrategia hace una operación por periodo y arriesga en ella el 1% del capital actual, durante 250 periodos, 20,000 veces. Lo único que cambia entre filas es qué tan correlacionados están los resultados de las cuatro estrategias.

| Correlación de resultados | Las cuatro pierden en el mismo periodo | Drawdown máximo mediano | Drawdown máximo, percentil 95 | Probabilidad de un drawdown mayor al 20% |
|---|---|---|---|---|
| 0.00 | 12.9% | 16.9% | 27.1% | 28.0% |
| 0.19 | 22.6% | 23.5% | 37.2% | 73.6% |
| 0.41 | 32.9% | 29.9% | 46.6% | 94.6% |
| 0.71 | 47.0% | 37.8% | 57.7% | 99.6% |

Todas las filas tienen la misma ventaja y el mismo 1% por operación. Aun así, el periodo en que las cuatro estrategias pierden a la vez (un golpe del 4%) pasa de aproximadamente uno de cada ocho periodos a casi uno de cada dos, y el peor drawdown típico se duplica con creces.

Para comparar, simulamos una sola estrategia con la misma ventaja y el mismo horizonte a distintos niveles de riesgo. Al 2% por operación, su drawdown máximo mediano fue del 24.3%. Al 3%, del 34.9%. Al 4%, del 44.1%. Es decir, cuatro bots al 1% con una correlación de apenas 0.19 tuvieron drawdowns parecidos a los de un bot al 2%, y cuatro bots con una correlación de 0.71 quedaron entre un bot al 3% y uno al 4%.

> **Idea clave:** el riesgo total no es el riesgo por bot multiplicado por el número de bots, y tampoco es el riesgo de un solo bot. La correlación decide en qué punto entre los dos terminas.

## La correlación no es una constante

Una correlación estimada con un backtest es un promedio del periodo que probaste. El problema es que las correlaciones tienden a subir justo cuando más necesitas que sean bajas.

- **Longin y Solnik (2001)** estudiaron la correlación entre los mercados de acciones internacionales y encontraron que la correlación aumenta en los mercados bajistas, pero no en los alcistas.
- **Ang y Chen (2002)** encontraron que las correlaciones entre carteras de acciones de EE. UU. y el mercado estadounidense durante caídas conjuntas eran, en promedio, un 11.6% más altas de lo que implica una distribución normal, mientras que las correlaciones al alza no se distinguían de ella. Su conclusión: si ignoras esto, el valor de la diversificación puede estar sobrestimado.
- Las cifras del **FMI** mencionadas arriba muestran una correlación que casi no existía antes de 2020 y que apareció en un par de años.

Longin y Solnik también hacen una advertencia: si simplemente divides la historia en días tranquilos y días volátiles y comparas las correlaciones, puedes ver una correlación más alta en los periodos volátiles aunque la correlación real nunca haya cambiado. En su ejemplo, una correlación constante de 0.50 aparecía como 0.21 en los días de movimientos pequeños y como 0.62 en los días de movimientos grandes. Medir la correlación exige cuidado en ambas direcciones.

### Lo que un backtest en calma no ve

Repetimos la simulación de cuatro estrategias con un cambio de régimen. La mayor parte del tiempo las estrategias casi no tenían relación entre sí, pero dos veces en cada recorrido de 250 periodos hubo un bloque de estrés de 20 periodos en el que sus resultados se volvieron muy correlacionados (0.71).

| Escenario | Correlación que medirías | Drawdown máximo mediano | Drawdown máximo, percentil 95 | Probabilidad de un drawdown mayor al 20% |
|---|---|---|---|---|
| Lo que sugieren los periodos tranquilos | 0.06 | 19.3% | 30.3% | 44.1% |
| Lo que pasó en realidad, con bloques de estrés | 0.06 en calma / 0.71 en estrés | 24.0% | 38.7% | 74.3% |

Los bloques de estrés fueron solo el 16% de los periodos, pero subieron el drawdown típico casi cinco puntos porcentuales y el drawdown del escenario malo más de ocho. Un backtest cuya ventana no hubiera incluido un episodio de estrés habría medido el 0.06 y se habría preparado para la primera fila.

## Cómo medir la correlación entre tus estrategias

1. **Usa resultados, no precios.** Arma una serie diaria de ganancias y pérdidas para cada estrategia (en R o en % del capital) sobre las mismas fechas, contando como cero los días sin posiciones.
2. **Incluye periodos de estrés.** Asegúrate de que la ventana tenga al menos una caída fuerte o un pico de volatilidad en los mercados que operas. Una muestra de un solo régimen tranquilo subestimará la correlación.
3. **Mira los peores días, no solo el coeficiente.** Cuenta cuántas veces varias estrategias perdieron el mismo día y qué tan grande fue la pérdida combinada. Ese número se traduce directamente en drawdown.
4. **Trata la estimación como ruidosa.** Una correlación calculada con unas pocas docenas de operaciones es tan incierta como cualquier otra estadística de un backtest; mira nuestro artículo sobre [cuántas operaciones necesita un backtest](/blog/how-many-trades-backtest).

## Una lista práctica

- **Suma el riesgo abierto total** de todas las estrategias en marcha, y trata las estrategias muy correlacionadas como una sola posición más grande.
- **Dimensiona el conjunto para el día en que todas pierden a la vez.** Si cuatro bots al 1% pueden tocar su stop en la misma sesión, tu riesgo real de un solo día ronda el 4%, antes de gaps y slippage.
- **Diversifica según lo que mueve el resultado**, no según el número de bots: mercados distintos, lógica de señal distinta, periodos de tenencia distintos.
- **Vuelve a revisar las correlaciones después de eventos grandes del mercado**, porque una relación medida en un año tranquilo puede no sostenerse en el siguiente año de estrés.
- **Usa los límites de la plataforma como techo, no como control de correlación.** En Period Trader, Ajustes tiene un *Riesgo por operación* para los despliegues nuevos y un límite de *Despliegues en vivo máximos* que fija cuántos bots corren a la vez. Ambos acotan el tamaño y la cantidad; ninguno sabe si tus bots están operando la misma idea. Esa decisión es tuya.

Para ver cómo el riesgo por operación se convierte en drawdowns en una sola estrategia, lee [cuánto arriesgar por operación](/blog/how-much-to-risk-per-trade).

## Lecturas recomendadas

- Markowitz, H. (1952). "Portfolio Selection." *The Journal of Finance*, 7(1), 77–91. [DOI 10.1111/j.1540-6261.1952.tb01525.x](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x)
- Longin, F. y Solnik, B. (2001). "Extreme Correlation of International Equity Markets." *The Journal of Finance*, 56(2), 649–676. [DOI 10.1111/0022-1082.00340](https://doi.org/10.1111/0022-1082.00340)
- Ang, A. y Chen, J. (2002). "Asymmetric Correlations of Equity Portfolios." *Journal of Financial Economics*. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0304405X02000685) · [PDF de los autores](https://business.columbia.edu/sites/default/files-efs/pubfiles/1516/corr.pdf)
- Adrian, T., Iyer, T. y Qureshi, M. S. (2022). "Crypto Prices Move More in Sync With Stocks, Posing New Risks." [Blog del FMI](https://www.imf.org/en/blogs/articles/2022/01/11/crypto-prices-move-more-in-sync-with-stocks-posing-new-risks)
