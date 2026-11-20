Nueve actualizaciones desde nuestro último artículo de producto (versiones 1.1.370 a 1.1.378) llevan mucho más de la vida de una operación al gráfico: puedes poner un trailing stop a cualquier operación abierta, quitar o mover un stop-loss con una sola confirmación, cerrar parte de una posición y ver dónde una operación queda en break-even después de costos. Además, las estrategias que la IA escribe para ti ya pueden operar en vivo, la investigación puede probar contra las reglas de una firma de fondeo y un nuevo mapa de calor muestra todos los mercados a la vez.

## Gestionar una operación abierta desde el gráfico

### Tus operaciones junto a tus bots (1.1.373)

Las órdenes manuales desde el gráfico se bloqueaban mientras un bot tenía una operación abierta. Ahora solo espera un símbolo que ya tiene una posición abierta, así tu operación nunca se mezcla con la de un bot. Tus operaciones manuales siguen siendo tuyas: ningún bot cuenta, cierra ni toma una posición que abriste a mano.

### Un trailing stop en cualquier operación (1.1.374)

Pulsa **TRAILING** en una operación abierta, manual o de un bot, y elige:

- la distancia, en precio, pips, porcentaje o ATR (la 1.1.377 suma puntos y ticks);
- cuándo empieza: de inmediato, tras cierta ganancia, en un múltiplo de R o en un precio;
- un paso mínimo, un movimiento a breakeven y si sigue cada tick o solo velas cerradas.

Mueve el stop-loss real en tu bróker o exchange, y siempre solo más cerca del precio: nunca quita ni aleja un stop. Funciona en MetaTrader 5 y en cada exchange de cripto conectado excepto Binance, que no tiene una forma segura de reemplazar un stop en un solo paso.

En la operación de un bot, tu trailing toma el control del stop de esa operación y el trailing propio del bot se pausa para ella; el bot mantiene su take-profit y sus señales de salida. También puedes dejar que ambos funcionen, y gana el stop más ajustado. Quita el tuyo y el bot vuelve a mover el stop.

### Quitar, mover o dividir las salidas (1.1.375 a 1.1.378)

- **✕ en una línea** quita ese stop-loss o take-profit. Primero ves una vista previa, no se envía nada hasta que pulsas **CONFIRMAR**, y la confirmación avisa de que una operación sin stop no tiene límite de pérdida. El stop-loss de un bot no tiene ✕: los bots siempre mantienen uno en el bróker.
- **✎ en el stop-loss** abre una ventana pequeña para moverlo o cambiar el trailing. Una etiqueta dorada **TL** marca un trailing stop en marcha.
- **Arrastrar** un stop-loss o take-profit ahora mueve la línea al instante y muestra *Aplicando…* hasta que el exchange lo confirma.
- **Varios take-profits** en una operación de Bybit, cada uno cerrando parte de la posición. Puedes arrastrar cada uno o cancelarlo con su x.
- **Cierre parcial** del 25%, 50% o 75% en MetaTrader 5 y Bybit, desde el menú de posiciones o con clic derecho sobre la operación. El tamaño se redondea a la baja al paso del mercado, y se rechaza si alguna de las dos partes quedaría por debajo del mínimo.
- **Añadir a una posición de Bybit** que abriste tú: una orden del mismo lado promedia la entrada y mantiene tu stop-loss y take-profit salvo que los cambies.

El chat de IA (Pro) también puede poner, mover o quitar stops y objetivos, y tú apruebas cada cambio.

### Unidades que significan lo que dicen (1.1.377)

Los stops, objetivos y distancias de trailing ahora se pueden poner en puntos, pips, ticks, precio, porcentaje o ATR, desde las estrategias y los backtests hasta las operaciones abiertas. Un stop de 30 puntos son exactamente 30 puntos en cada vela.

### Break-even después de costos (1.1.376)

Una línea violeta **BE** marca el precio al que cerrar la operación te dejaría en cero después de sus costos. En MetaTrader 5 incluye la comisión de ida y vuelta, el swap acumulado y el spread; en cripto, la comisión del exchange de ida y vuelta, pero no el funding.

## Tus propias estrategias, en vivo (1.1.371)

Las estrategias que el chat de IA escribe para ti antes eran solo de investigación. Ahora se investigan, se prueban en papel y se despliegan en vivo como las incluidas, en MetaTrader 5 y cripto, con despliegue automático y pruebas en vivo incluidos. Algunas reglas lo mantienen honesto:

- La IA prueba el código antes de guardarlo, y la investigación barre la estrategia sobre sus propios ajustes.
- Un bot en vivo ejecuta exactamente el código que se probó. Si editas la estrategia después de desplegarla, el bot no abre operaciones nuevas hasta que lo vuelvas a desplegar.
- Las salidas, el stop-loss y take-profit en el bróker y las protecciones de la cuenta son los mismos que en las estrategias incluidas. Las entradas escalonadas y el modo Recuperación siguen siendo solo para las incluidas.

## Investigación en cuentas de fondeo (1.1.370 a 1.1.377)

Puedes agregar una cuenta de Topstep, responder unas preguntas sobre ella y hacer un backtest de una estrategia como esa cuenta, con un resultado de aprobado o suspendido según las reglas de la firma. Los bots de investigación también pueden correr sobre una cuenta de fondeo, así cada backtest opera con esas reglas.

La versión 1.1.377 suma **inicios escalonados**: cuando una configuración aprueba, los mismos ajustes vuelven a empezar desde distintos días de la ventana, y la tarjeta muestra "aprueba desde X de Y días de inicio", además de qué regla suspendió al resto. Las configuraciones que aprueban desde más días de inicio suben en el ranking, porque un aprobado que depende de una sola fecha de inicio afortunada es una prueba débil.

## Modo Recuperación, con límites estrictos (1.1.370)

El modo Recuperación es una opción avanzada en **Nueva investigación**. Después de una operación perdedora, las siguientes operaciones del mismo ciclo son más grandes, para que una ganancia pueda recuperar la pérdida del ciclo. Justo por eso importa su peor caso: una racha de pérdidas aumenta el tamaño en cada paso.

La app no lo esconde. **Recomendado por IA** elige los ajustes según tu saldo, el tamaño mínimo del instrumento, su spread y su volatilidad, y muestra el peor caso si todos los pasos pierden. Cada ciclo tiene un límite de pérdida estricto que la app hace cumplir (10% del saldo por defecto, 50% como máximo), y puedes añadir un tamaño máximo de operación y un límite de pérdida diaria. Como con cualquier stop, un gap o un mercado rápido aún puede llevar una pérdida más allá del plan. Un bot de Recuperación en vivo solo empieza cuando lo despliegas y confirmas; las pruebas en vivo y el cambio automático nunca lo usan.

> Trata la Recuperación como un ajuste de riesgo que eliges a conciencia, no como una forma de evitar pérdidas. Primero haz un backtest del peor caso.

## La pestaña Navegador y tu propia IA (1.1.370, 1.1.371)

- **Pestaña Navegador (Pro):** abre la web de una plataforma de trading dentro de la app, mantén la sesión iniciada y deja que la IA lea la página y trabaje en ella. Cualquier acción que pueda abrir una orden o mover dinero te pide aprobación primero.
- **Conecta tu propia IA:** usa apps de IA como Claude Desktop, ChatGPT, Cursor o VS Code con Period Trader. Puedes confiar en una conexión una vez para que las solicitudes de rutina no pidan una tarjeta de aprobación, pero las acciones con dinero real siguen necesitando tu OK explícito.
- **Nivel de IA:** elige bajo, medio o alto junto al cuadro del chat. Los niveles más altos usan más de los créditos de IA semanales compartidos por pregunta.

## Ver más, esperar menos

- **Mapa de calor (1.1.378):** todos los mercados de MetaTrader 5 y cripto coloreados por el cambio de hoy y con tamaño según el volumen, con selecciones como Mayores alzas, Metales o Índices CFD. Acércate a una casilla para ver el rango del día y un pequeño gráfico de velas, o haz clic para abrirla en el gráfico.
- **Ventanas separadas (1.1.378):** abre cualquier sección en su propia ventana.
- **Diario de operaciones (1.1.377):** un gráfico de la operación más claro, el mejor y el peor recorrido mientras estuvo abierta (MFE/MAE) y, en MetaTrader 5, el riesgo inicial y la R.
- **Modo Ligero (1.1.371):** usa menos CPU y memoria en PCs pequeños. Los bots en vivo, los stops y el riesgo nunca cambian.

## Actualizaciones y arreglos de seguridad

La **actualización automática (1.1.372)** instala las versiones nuevas en un momento seguro: cada operación abierta tiene su stop en el bróker o exchange, no hay ninguna orden en curso, ningún ciclo de Recuperación está a medias y una vela acaba de cerrar. Una cuenta atrás te deja posponerla, y los instaladores se verifican antes con la firma de Period Trader LLC.

Otros arreglos que vale la pena conocer:

- Los bots en vivo ahora solo evalúan velas cerradas, igual que el backtest (1.1.370).
- Una **red de seguridad para stops no ejecutados**, activada por defecto, cierra la posición de un bot si el precio se queda más allá de su stop mientras el mercado aún la muestra abierta (1.1.370).
- Los bots de MetaTrader 5 desplegados automáticamente vuelven a seguir su trailing, y un bot cuya señal llega justo después de un reinicio espera hasta tres minutos a MetaTrader 5 en lugar de perder la entrada (1.1.377).

La investigación sigue corriendo en tu propio PC, y cada control nuevo de esta lista es una herramienta para gestionar el riesgo, no una promesa de resultados.
