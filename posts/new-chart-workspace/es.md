Tres actualizaciones publicadas el 21 de octubre (versiones 1.1.356, 1.1.357 y 1.1.358) reconstruyeron el gráfico de Period Trader. Ahora puedes ver hasta cuatro gráficos a la vez, crear alertas de precio directamente desde la escala de precios, cerrar parte de una operación desde su etiqueta en el gráfico, ver tus operaciones del backtest y en vivo justo donde ocurrieron, y pedirle al asistente de IA que lea y marque el gráfico que tienes abierto.

Aquí tienes qué cambió, qué partes están en Free y cuáles en Pro, y qué reglas de seguridad siguen igual.

## Hasta cuatro gráficos, vinculados por color

La barra del gráfico tiene un nuevo botón **Diseño** con cinco opciones: un gráfico, dos lado a lado, dos apilados, tres (uno grande y dos pequeños) y cuatro en una cuadrícula de 2 × 2.

Cada gráfico puede unirse a un grupo de vínculo por color: verde, azul, naranja o morado. Los gráficos del mismo grupo se siguen entre sí. Por defecto comparten el símbolo, la cruz del cursor y el rango de fechas visible, y también puedes sincronizar la temporalidad. Los gráficos sin vincular siguen siendo independientes.

Cualquier gráfico adicional se puede abrir en su propia ventana para un segundo monitor; **Volver a la ventana principal** lo devuelve. El gráfico principal siempre conserva el ticket de órdenes y el plan del bot, así que solo hay un lugar donde se preparan las órdenes.

Un uso común: vincula un gráfico de temporalidad alta con uno de temporalidad de entrada del mismo mercado, y al mover la cruz en uno verás el mismo momento en el otro.

## Una lista de mercados que puedes explorar

Al hacer clic en el nombre del símbolo ahora se abre un tablero de instrumentos: listas de MT5 y Cripto con Favoritos, Todos y pestañas por categoría, un buscador y columnas ordenables de precio, cambio en 24 horas y volumen. Marca una fila con la estrella para añadirla a tus favoritos, o ancla el tablero a la izquierda del gráfico.

La versión 1.1.358 añadió una **Lista de seguimiento** junto a las listas de MT5 y Cripto. Una lista puede mezclar mercados de distintos brókers y exchanges, por ejemplo un par de forex de MT5 junto a un perpetuo cripto, y tiene filtros de Ganadores y Perdedores. Cuando está anclada, muestra los detalles del mercado elegido: el cambio y el rango del día, las cuatro sesiones de forex, una lectura técnica de una hora (RSI 14, EMA 20/50 y MACD) y los eventos del calendario de esta semana para sus divisas. La lectura técnica describe los indicadores; no es una señal. Un dato que falta aparece como un guion con el motivo, nunca como una suposición. Las listas se guardan en tu computadora.

## Alertas de precio que viven en el gráfico

Lleva el cursor a un precio, haz clic en la campana junto a la escala de precios, revisa la alerta y pulsa **Guardar alerta**. Las alertas guardadas aparecen como líneas discontinuas: arrastra una para moverla (Escape cancela el arrastre) o haz clic en ella para editar la condición o cambiar su color. Las condiciones incluyen por encima, por debajo, cruce y dentro o fuera de un rango.

Desde la 1.1.358, cada alerta se dibuja en todas las temporalidades de su símbolo, y una barra de **Alertas** a la derecha del gráfico, de ancho ajustable, reúne tus alertas con opciones para pausar, quitar, ver el registro de disparos anteriores y abrir el gráfico de cada alerta.

Las opciones de entrega son una notificación dentro de la app, una notificación de Windows y un webhook a una dirección HTTPS pública. Hay dos límites que conviene conocer:

- **Tu computadora revisa las alertas.** Period Trader tiene que estar abierto y conectado; la ventana del gráfico sí se puede cerrar. Nada se evalúa en la nube mientras la computadora está apagada.
- **Las alertas nunca operan.** No abren órdenes, no despliegan una estrategia ni gastan créditos de IA.

Las alertas de precio son parte de Period Trader Pro.

## Gestionar una operación desde el gráfico

Las posiciones abiertas y las órdenes pendientes ahora aparecen como etiquetas en el gráfico, por defecto en el borde derecho (puedes moverlas a la izquierda o al centro en la configuración del gráfico). Desde la etiqueta de una posición puedes editar el stop loss y el take profit, o cerrar el 25 %, el 50 %, el 75 % o la posición completa. El cierre parcial sigue algunas reglas:

- Está disponible para posiciones de MT5. En los exchanges cripto, un cierre cierra la posición entera.
- El tamaño se redondea hacia abajo al paso de lote de tu bróker, y el cierre se rechaza si la parte que cierras o la que queda abierta quedaría por debajo del lote mínimo del bróker.
- Se rechaza mientras un bot de investigación opera ese símbolo, porque la salida del propio bot espera el tamaño con el que entró. Cierra la posición completa o detén el bot primero.
- La parte que sigue abierta conserva su stop loss y su take profit sin cambios.

El clic derecho sobre el gráfico abre un menú con órdenes limitadas o stop de compra y venta al precio donde hiciste clic, crear alerta, dibujar una línea horizontal y copiar el precio. Una orden de este menú solo se prepara en el ticket: aun así tienes que revisarla y confirmarla.

El ticket de órdenes también puede guardar **preajustes** de stop loss y take profit. Un preajuste es una cantidad de dinero, no una distancia: coloca el stop donde el tamaño del ticket perdería esa cantidad y el objetivo donde ganaría la otra, alrededor de la entrada que estás preparando.

La 1.1.357 trajo además una corrección de seguridad: con el trading con un clic activado, cambiar de mercado podía dejar armada la intención de un clic, y el siguiente cierre se confirmaba solo. Ahora el modo de un clic aplica únicamente a la acción para la que se hizo, y un ticket preparado siempre abre su vista previa.

## Operaciones del backtest y en vivo, dibujadas donde ocurrieron

La versión 1.1.358 dibuja cada operación en vivo cerrada, y cada operación de un backtest que elijas mostrar desde el panel Plan del bot, como un recuadro desde la entrada hasta la salida: verde si ganó dinero y rojo si perdió. Al pasar el cursor sobre una operación aparece una tarjeta con la dirección, el resultado en porcentaje del precio y en dinero, la hora, el precio y el motivo de entrada y de salida, el tamaño y la duración. Haz clic para fijar la tarjeta.

Nada se recalcula: los recuadros salen del informe guardado del backtest y de tu historial de operaciones, y un stop o un objetivo que el informe no registró no se dibuja. Así es más fácil ver si las pérdidas de una estrategia se concentran en cierta hora del día o si las salidas en vivo se parecen a las del backtest.

## Una IA que lee y dibuja en tu gráfico

El chat de PeriodTrader AI ahora se ancla junto a tus gráficos y se queda ahí también en pantalla completa. Cuando preguntas por el gráfico, el chat envía junto con tu mensaje lo que el gráfico muestra: símbolo, temporalidad, rango visible, último precio, tus indicadores y dibujos, y tus posiciones abiertas en ese símbolo.

Puede dibujar niveles, zonas, líneas de tendencia, order blocks, fair value gaps, marcas de ruptura de estructura y recuadros de riesgo/beneficio. Son dibujos normales, así que puedes moverlos, cambiarles el estilo o borrarlos, y al limpiar los dibujos de la IA nunca se borran los tuyos.

También puede preparar una **tarjeta de orden** con dirección, tipo, entrada, stop loss, take profit, tamaño y riesgo. Las reglas son estrictas:

- Cada tarjeta lleva un stop loss.
- Se rechaza una tarjeta que arriesgue más del 5 % de la cuenta (puedes seguir dimensionando una operación a mano).
- Una tarjeta caduca a los tres minutos.
- **APROBAR** solo prepara la orden en el ticket del gráfico y abre la vista previa del bróker. Solo **CONFIRMAR** la envía.

El interruptor **Educación** del chat activa un modo que mantiene las respuestas cortas y visuales: diagramas pequeños, ejemplos dibujados sobre velas reales y capturas del gráfico dentro del chat. Explica cómo funcionan las cosas y nunca te dice que tomes una operación concreta. **Explicar con IA** en un evento del calendario o un titular le pregunta al asistente de inmediato. **Preguntar a la IA** en un recuadro de operación solo adjunta la operación al chat; no se envía nada hasta que pulses Enviar.

PeriodTrader AI es parte de Pro y usa tus créditos de IA.

## Noticias y calendario económico en el eje del tiempo

Los datos económicos ahora aparecen como banderas en el eje del tiempo del gráfico, con líneas discontinuas para los próximos eventos de alto impacto. Al hacer clic en una bandera se abre una tarjeta del evento con una cuenta regresiva y los valores de previsión y anterior. Un panel lateral de ancho ajustable muestra el calendario y los titulares recientes, filtrados por impacto o por el símbolo actual. Los spreads pueden ampliarse y el precio puede dar saltos alrededor de los datos importantes, así que verlos en el gráfico ayuda a revisar por qué una operación se comportó distinto a su backtest.

## Biblioteca de indicadores y cambios menores

- **Ventana de la biblioteca de indicadores:** explora por familias, con buscador, favoritos y vistas previas calculadas sobre el gráfico actual. Desde la 1.1.358 también guarda tus propios indicadores y estrategias, con descripciones escritas por la IA, **Hacer público** y la sección Comunidad dentro de la misma ventana.
- **Configuración del gráfico:** velas, velas huecas, barras, línea o área, con tus propios colores.
- **Color de acento** en la sección de apariencia de Ajustes. Los colores de ganancia y pérdida siguen siendo verde y rojo, sin importar el acento que elijas.
- Más historial al desplazarte hacia atrás, la zona horaria de tu dispositivo por defecto, un trazado más nítido y una lista de instrumentos que se actualiza cuando cambias de cuenta de MT5.

## Lo que no cambió

Las nuevas herramientas del gráfico nunca envían una orden por su cuenta: una orden del menú del clic derecho o de la IA solo queda preparada hasta que la confirmes, y las alertas son de solo lectura. Los bots de investigación que despliegues siguen operando con sus propias protecciones de riesgo, como antes. Period Trader Free sigue incluyendo el gráfico y el trading manual en todos tus brókers y exchanges; PeriodTrader AI y las alertas son parte de Pro. Cuando hay una actualización disponible, el panel principal muestra un aviso con un botón para instalarla.
