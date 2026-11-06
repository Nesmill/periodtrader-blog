Cinco actualizaciones publicadas entre el 31 de octubre y el 5 de noviembre (versiones 1.1.363 a 1.1.367) cambian los primeros diez minutos en Period Trader y buena parte de lo que pasa después. Hay una bienvenida y un inicio de sesión nuevos, recorridos guiados, una página de brókers y exchanges que conecta varias cuentas cripto a la vez, un diario de operaciones rediseñado y un asistente de IA que puede crear bots de investigación por ti.

Esto es lo que cambió, dónde encontrarlo y algunas cosas que a propósito no cambiaron.

## Un primer arranque que se explica solo

La pantalla de inicio de sesión ahora dice qué es la app y cómo funciona antes de pedirte nada. Iniciar sesión con Whop es el botón principal; una clave de licencia es el segundo camino. Cuando inicias sesión con Whop en tu navegador, vuelves a la app y tu plan se actualiza al momento.

Si todavía no tienes bots de investigación, la pestaña Bots muestra una bienvenida corta en lugar de una lista vacía: tres pasos (**Investigación**, **Comprobar**, **Operar**) y una lista para empezar que se marca sola a medida que avanzas:

1. **Conecta un broker o exchange**
2. **Crear un bot de investigación**
3. **Haz el recorrido**

La antigua tarjeta START HERE ya no está. En su lugar hay recorridos guiados: ventanas paso a paso que señalan cada parte de la página principal, de la página Broker y de la pestaña del gráfico (el recorrido del gráfico empieza la primera vez que lo abres). Nada cambia y no se opera nada mientras lees. Cada recorrido se muestra una vez, y puedes repetirlo desde el botón **Guía** en la cabecera o desde la configuración.

**Nueva investigación** ahora abre una ventana con cuatro preguntas:

- **¿Qué mercado?** Cripto, forex, oro o índices (forex y oro necesitan MetaTrader 5).
- **Tamaño de vela**, con un recordatorio de que las velas más pequeñas significan más operaciones y posiciones más cortas.
- **Cuando encuentre una estrategia que pase**, para que decidas desde el principio qué hace el bot de investigación con un resultado.
- **Riesgo por operación**, con un ejemplo en dinero para que el porcentaje signifique algo.

Lo demás queda en **Opciones avanzadas**.

En el plan Free, la ventana de mejora ya no se abre sola cada vez que inicias la app. Si intentas usar una función Pro, aparece una nota pequeña, y la ventana solo se abre cuando tú la pides, por ejemplo desde **FREE · Mejora** en la parte de arriba.

## Brókers y exchanges: varias cuentas, una boleta

La página de configuración ahora se llama **Brokers y exchanges**. Empieza con una sola pregunta, dónde quieres operar: Bybit, MetaTrader 5 u otro exchange. Después solo ves esa parte.

Ahora puedes conectar varios exchanges cripto al mismo tiempo, una cuenta guardada por exchange. La que seleccionas es la predeterminada para gráficos, operaciones manuales, datos de investigación y bots nuevos, y cada bot cripto registra en qué exchange opera. En la práctica:

- La boleta de orden tiene un selector de **Cuenta**. Una orden a mercado o pendiente va a la cuenta que elegiste, y la app rechaza una cuenta desconocida o no conectada.
- **Nueva investigación** y la tarjeta del bot en vivo también tienen un selector de **Cuenta**.
- Las posiciones abiertas, el cierre total y el interruptor de emergencia cripto cubren todas las cuentas conectadas.
- Sin una terminal MT5 conectada, el gráfico abre en Bitcoin desde tu exchange en lugar de un gráfico MT5 vacío.

### Mercados TradFi en Bybit y Binance

Los dos exchanges ofrecen contratos perpetuos sobre acciones, ETF, materias primas y forex. Ahora aparecen en el selector de mercados del gráfico, agrupados por tipo y con su nombre completo. En Binance, la app lee las especificaciones reales de cada contrato, así que los precios de stop-loss y take-profit se redondean al tick correcto, y rechaza una orden antes de enviarla cuando la sesión de ese contrato está cerrada.

En Bybit también puedes graficar y operar **xStocks** (tokens de acciones en el mercado spot de Bybit) y ver cadenas de opciones en la pestaña **Opciones** del selector de mercados. Estas órdenes usan una boleta aparte que te muestra una vista previa para confirmar; la app vuelve a leer el precio y rechaza una orden a mercado si el precio se movió más de un 5%. Los bots de investigación y la boleta normal del gráfico siguen con contratos perpetuos. Si un exchange rechaza una orden porque no aceptaste una vez sus condiciones TradFi, la app te lo dice.

## Un diario de operaciones nuevo

El diario de operaciones (versión 1.1.365) tiene un diseño más simple:

- Una sola línea de cabecera con un selector de cuenta (una cuenta, y por lo tanto una moneda, a la vez; recuerda tu elección) y un selector de fechas.
- Tres tarjetas principales, **Neto**, **Tasa de acierto** y **Factor de beneficio**, más un gráfico de equity.
- Un registro compacto: hora de cierre, símbolo y dirección, estrategia, resultado neto y un icono de revisión. El ticket, el bruto y las comisiones están en el panel de la operación que se abre al lado.
- Un calendario con **Hoy** y un cambio **Mes | Semana**, y 50 filas por página.

Las operaciones también aparecen antes. Los resultados en caché se actualizan en el momento en que cambia tu conjunto de operaciones abiertas, el diario se refresca solo (como mucho cada 4 segundos, nunca mientras editas una nota) y los bots cripto se concilian con el exchange cada 10 segundos en lugar de cada 30.

Algunas cifras del panel estaban mal y ya están corregidas: el P&L del día en Bybit siempre aparecía en 0 y ahora suma las operaciones cerradas de hoy netas de comisiones, el crédito del bróker en una cuenta MT5 ya no se cuenta como ganancia abierta, y el banner de resultados realizados muestra cada cuenta por separado cuando usan monedas distintas.

## Bots de investigación: vistas más claras y el asistente de IA

Los bots de investigación ahora tienen cuatro vistas: **Lista**, **Grandes**, **Medianas** y **Pequeñas**. Desde la 1.1.363, una tarjeta muestra cada operación de un despliegue en vivo (operaciones, ganadoras y perdedoras, win rate, P&L realizado) más una cifra aparte desde el último reinicio, y el historial de operaciones detrás de esas cifras se conserva entre guardados para que los contadores ya no se desvíen.

En **TODOS LOS BACKTESTS**, el backtest que ejecuta un bot en vivo queda fijado arriba con una etiqueta **DESPLEGADO**, su estado y un enlace para abrir el bot, y un filtro **DEPLOYED** muestra solo esas filas. Es solo visual; no cambia nada de la ejecución.

En las estrategias por capas (una entrada base más añadidos), el gráfico ahora dibuja cada añadido como un punto numerado dentro de su ciclo, con la entrada promedio de la cesta, y las pruebas futuras también funcionan con resultados por capas.

El asistente de IA, incluido en Pro, ahora puede crear bots de investigación: de uno en uno o hasta 20 en una sola tarjeta de aprobación, mezclando mercados MT5 y cripto. También puede pausar, reanudar o archivar muchos bots a la vez. Las reglas de siempre se mantienen:

> No se envía nada hasta que apruebas la tarjeta, y solo si las acciones reales están activadas; si no, la aprobación es una simulación que muestra la solicitud que se habría enviado.

Crear un bot de investigación inicia una investigación. No despliega nada en trading en vivo; eso sigue dependiendo de tus reglas de despliegue y del ajuste aparte de despliegue automático. En Free, la tarjeta te avisa de que el plan incluye un bot de investigación.

## Ejecución en vivo más segura

Algunos de los cambios más importantes no se ven hasta que hacen falta:

- **La protección de MT5 sobrevive a los reinicios.** Después de reiniciar la app, un paso de reparación podía ejecutarse antes de que MetaTrader 5 informara qué cuenta tenía la sesión abierta. Entonces las actualizaciones del trailing stop y del take-profit de una operación abierta quedaban retenidas hasta que se cerraba. Ahora la app espera hasta conocer la cuenta.
- **Las salidas de los bots MT5 cierran solo las posiciones del propio bot**, cada tramo de una cesta por capas y nada más. En una cuenta con cobertura, una posición manual o la de otro bot en el mismo símbolo no se toca.
- **Los planes de los bots MT5 conservan el stop-loss y el take-profit exactos** que se enviaron al bróker.
- **Los cierres de Bybit se registran bien** aunque el historial del exchange repita una fila con los decimales escritos de otra forma.
- **Las notificaciones hacen lo que dice la configuración.** Una casilla marcada ya no se desmarca sola, **PROBAR WEBHOOK** guarda la URL antes de probarla, la app envía por sí misma los mensajes de webhook de MT5 y de las protecciones de riesgo, a las instalaciones solo cripto ya no se les avisa cada 15 minutos de que MT5 no está conectado, y los bots EMA ahora envían la notificación de entrada ejecutada. Las notificaciones siguen siendo notificaciones de Windows más tu webhook.
- Ya no se abren ventanas de comandos al iniciar ni durante una actualización, y desde la 1.1.367 la app y el instalador están firmados digitalmente por Period Trader LLC.

## Lo que no cambió

La investigación sigue ejecutándose en tu propio PC, y un backtest que pasa sigue siendo una hipótesis que hay que probar, no una promesa. Los recorridos guiados, el diario nuevo y las etiquetas de despliegue solo te muestran más; ninguno coloca, dimensiona ni aprueba operaciones. Si eres nuevo, la lista de bienvenida de arriba es la forma más rápida de empezar.
