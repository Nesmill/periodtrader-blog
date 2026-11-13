Dos actualizaciones publicadas el 9 y el 11 de noviembre (versiones 1.1.368 y 1.1.369) cambian cómo los bots de investigación pasan de un buen backtest a una configuración demostrada, y lo que puede pasar entre medio. La novedad más grande es la prueba en vivo: una forma pequeña y limitada de que una configuración bien revisada opere con dinero real antes de estar demostrada por completo. Alrededor de ella, la investigación se volvió más estricta con los costos y la suerte, sumó 68 estrategias y aprende de otras instalaciones.

Esto es lo que cambió, cómo funciona cada parte y dónde están los límites.

## Pruebas en vivo: dinero real, tamaño pequeño, límites claros

Hasta ahora una configuración de investigación tenía que convertirse en **Campeón** antes de operar en vivo. Con velas rápidas eso puede tardar semanas, porque la prueba llega de una en una, con cada operación simulada cerrada. La prueba en vivo es el paso intermedio. Una configuración está **lista** para una solo cuando se cumple lo siguiente:

- Es **Prometedora**: ganó dinero después de comisiones en días no vistos, la parte de los datos con la que nunca se ajustó, con una puntuación estadística de al menos 1,0.
- Es **Estable** (lo explicamos abajo) y no resultó ser una casualidad en mercados similares.
- Su prueba simulada no la ha descartado, y el bot no tiene un campeón ni un despliegue en vivo propio.
- Hay menos de tres pruebas en marcha entre todos tus bots, y esta configuración nunca tuvo una prueba antes.
- El mercado es cripto. Los mercados de MetaTrader 5 quedan fuera de las pruebas a menos que los actives.

Una prueba usa el camino normal de despliegue con un **riesgo del 0,1% por operación**. Se detiene y cierra su posición cuando su pérdida realizada más la abierta desde el inicio llega al **1% de la cuenta** con la que empezó, cuando su prueba simulada descarta la configuración o cuando otra configuración se convierte en el campeón del bot. Si la propia configuración se convierte en campeón, sigue operando con el tamaño de la prueba hasta que tú lo cambies. Después de una prueba detenida, ese bot espera seis horas antes de que otra configuración pueda empezar una.

> Una prueba solo arranca sola si el despliegue automático está activado. Si no, la tarjeta muestra **Prueba en vivo lista** y un botón **Iniciar prueba en vivo**, y una confirmación te dice el riesgo por operación y el límite de pérdida antes de que empiece nada.

Los cinco valores (riesgo por operación, límite de pérdida, número máximo de pruebas, puntuación mínima y el interruptor de MT5) están en **Ajustes > Despliegue**. El riesgo por operación puede ir del 0,1% al 1%.

Ten en cuenta dos cosas. Una prueba en vivo no es un campeón; la app lo dice, y la configuración sigue a prueba. Y el límite del 1% es una regla que la app aplica cerrando la posición, no una garantía: en un mercado rápido o con huecos de precio, la pérdida puede terminar siendo mayor.

## Pruebas más rápidas, sin bajar el listón

### Configuraciones prometedoras y pruebas simuladas (1.1.368)

Una ejecución que ganó dinero con datos no vistos, pero que todavía tiene muy pocas operaciones para descartar la suerte, ahora se marca como **Prometedora** y se muestra pronto, en lugar de desaparecer. Después empieza sola una prueba simulada: opera velas nuevas sin dinero real. Se convierte en campeón cuando su resultado en datos no vistos y sus operaciones simuladas, juntos, superan la barra de suerte.

### Cinco pruebas simuladas por bot y mercados similares (1.1.369)

Cada bot de investigación ahora prueba en simulado hasta **cinco configuraciones a la vez**, como mucho dos de la misma estrategia. Una prueba simulada solo se evalúa en puntos de control, cada cinco operaciones simuladas cerradas, frente a una barra de al menos 2,2. Es a propósito: revisar una prueba cada pocos minutos deja que una configuración sin ventaja real pase con solo esperar lo suficiente. Las pruebas que claramente no funcionan se descartan pronto, y eso libera el hueco para la siguiente configuración.

Las configuraciones prometedoras también se comprueban en **mercados similares**: los mismos ajustes se ejecutan en hasta ocho mercados parecidos durante los mismos días de calendario no vistos, dejando fuera el mercado propio de la configuración y contando una sola vez las operaciones del mismo día. Aguantar ahí puede confirmar un campeón en minutos, porque no hacen falta velas nuevas. Perder ahí no descarta la prueba simulada, ya que una ventaja puede ser propia de un solo mercado, pero la configuración pasa al final de la cola.

Cada tarjeta muestra una estimación de los **días que faltan para la prueba**, así que es fácil ver una configuración que opera tan poco que no podrá demostrar nada a tiempo.

### Una investigación que respeta los costos

- **Búsqueda consciente de las comisiones.** Los ajustes cuyo take-profit está a menos de cuatro costos de ida y vuelta, o cuyo stop está a menos de 1,5 costos de ida y vuelta, ya no se prueban con backtest: las comisiones se llevarían la mayor parte de cada operación. La regla se adapta sola a cada mercado y tamaño de vela, así que en velas de 1 hora o de 4 horas casi no se salta nada.
- **Estable o Inestable.** Cada configuración prometedora se vuelve a ejecutar con cada ajuste un paso más abajo y un paso más arriba. Si el 40% o menos de esas variantes vecinas son rentables, se marca como **Inestable** y espera detrás de las demás.
- **Rachas de pérdidas.** Una racha de más de seis operaciones perdedoras seguidas, o un win rate por debajo del 35%, ahora resta puntos en la clasificación.

Lo que cuenta como campeón no cambió con estos filtros.

### Una ventana más larga (1.1.368)

La investigación puede usar ventanas de 180 y 365 días; elige 365 días para velas de 1 hora y 4 horas, y 180 para 30 minutos o menos, hasta que tú decidas otra cosa. La prueba con datos no vistos es una cuarta parte de la ventana, entre 30 y 90 días, y la barra de suerte deja de subir en 2,0.

## 68 estrategias nuevas con nombres sencillos

La versión 1.1.368 añade 68 estrategias de tendencia, momentum, Smart Money, volumen y tasa de financiación (funding rate), así que la investigación ya puede probar más de 100, y todas pueden usar entradas escalonadas. **Todas las estrategias** es la opción predeterminada; las estrategias medidas como muertas en un mercado se saltan, y la opción **Shortlist** es el arranque más rápido. Las estrategias antiguas recibieron nombres sencillos (por ejemplo Band Snapback, Quiet Pullback, Daily Range Breakout, Trend Turn y Dip Ladder), y los bots e informes que ya tenías siguen funcionando con los nombres nuevos.

El chat de IA (Pro) puede listar y explicar cada estrategia y crear bots de investigación con cualquiera de ellas, también las escalonadas, con la tarjeta de aprobación de siempre.

## Aprendizaje colectivo: qué se comparte y qué no

La investigación ahora aprende, de cada backtest que ejecuta, qué valores de ajuste suelen funcionar para cada estrategia, mercado y tamaño de vela. Las instalaciones también comparten un mapa anónimo de esa evidencia, para que cada una busque de forma más eficiente. Según el aviso de la app, comparte resultados agregados de estrategias y los ajustes de las configuraciones que funcionaron bien, y nunca claves, accesos, saldos, operaciones ni tu código.

Hay tres protecciones importantes:

- Una parte del mapa solo orienta la investigación cuando al menos tres instalaciones aportan datos a ella.
- Al menos una cuarta parte de cada tanda de ajustes nuevos sigue siendo totalmente aleatoria.
- Una configuración sugerida por otra instalación se vuelve a probar con tus propios datos, pero nunca puede llegar a campeón solo con eso, únicamente con operaciones simuladas nuevas. Sus "días no vistos" podrían no serlo desde el punto de vista de otra instalación.

El aprendizaje colectivo viene activado. El aviso del primer arranque tiene un botón **Desactivar**, y el interruptor está en Ajustes. Mientras está activado, la app también envía cada cierto tiempo un aviso de actividad que solo lleva su número de versión, para poder contar las instalaciones activas.

## Pantallas más limpias y una ventana de novedades

Las tarjetas de investigación, la ventana de **Detalles** y los Ajustes ahora usan textos más cortos; al dejar el puntero sobre un término se abre una breve explicación. La ventana de Revisión de investigación se rediseñó con un veredicto en palabras sencillas, un **Camino a campeón**, un **Medidor de suerte** y un embudo de backtests. El mejor backtest tiene su propio botón **Desplegar**, y **Todos los backtests** se ve como tarjetas. El protector de riesgo y la franja de la cuenta (saldo, capital, P&L del día) se explican con palabras sencillas.

Después de cada actualización, una ventana te cuenta qué cambió. Puedes volver a abrirla desde **Ajustes > Actualizaciones**, o preguntarle al chat de IA "¿qué hay de nuevo?".

## Exchanges: entra Bitunix, salen tres

**Bitunix** ya es un exchange compatible para perpetuos en USDT. Conéctalo en **Brokers y exchanges**; tu cuenta de Bitunix debe usar el modo de posición One-way. **MEXC, Coinbase International y Kraken Futures** ya no son compatibles.

El historial de órdenes de Bybit ya no muestra las órdenes canceladas, rechazadas y desactivadas a menos que se pidan por estado (mira la [documentación de la API de Bybit](https://bybit-exchange.github.io/docs/v5/order/order-list)). La app ahora las pide de forma explícita, así que el historial de operaciones de Bybit sigue funcionando.

## Correcciones y lo que no cambió

- Las pruebas simuladas que dejaban de contar velas nuevas se reinician y conservan sus operaciones, y la investigación ya no las deja sin recursos.
- Las estrategias de la biblioteca ahora funcionan en las pruebas simuladas.
- La Revisión de investigación muestra los cambios sin pulsar Ctrl+F5.

La investigación sigue ejecutándose en tu propio PC. Un campeón, una configuración prometedora o una prueba en vivo siguen siendo una hipótesis a prueba, no una promesa de ganancias, y el despliegue automático sigue siendo un interruptor aparte que controlas tú.
