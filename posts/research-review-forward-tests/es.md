Cuatro actualizaciones publicadas entre el 23 y el 28 de octubre (versiones 1.1.359 a 1.1.362) cambian lo que puedes ver entre "mi bot de investigación encontró algo" y "esta estrategia opera en vivo". Ahora puedes leer cada comprobación de aprobación detrás de un backtest, guardar a los candidatos prometedores en una lista de seguimiento, probarlos con velas nuevas sin colocar órdenes y darle a cada bot de investigación sus propias reglas de despliegue.

Esto es lo que cambió, cómo funciona cada parte y lo que ninguna de ellas hace.

## Por qué un backtest no está aprobado, comprobación por comprobación

Un bot de investigación solo nombra un campeón cuando un backtest pasa cada comprobación, y en un mercado difícil eso puede tomar decenas de miles de backtests. Mientras tanto, la tarjeta del bot muestra su mejor backtest hasta ahora con su curva de equity, marcado como **Mejor hasta ahora · aún no aprobado**, y una línea **Por qué todavía no:** con la primera comprobación que no pasó.

La versión 1.1.360 añade el panorama completo. En la lista **TODOS LOS BACKTESTS** de un bot de investigación, cada fila tiene ahora un botón **COMPROBAR / SEGUIR** junto a **DETALLES**, y la curva del mejor backtest tiene **TODAS LAS COMPROBACIONES / SEGUIR**. Cualquiera de los dos abre una Revisión de investigación con una sola tabla: cada comprobación, el valor real del backtest, el requisito y un estado de **Pasa**, **No pasa** o **Sin evaluar**.

Las comprobaciones se agrupan en tres bloques:

- **Calidad de la investigación:** la calificación de calidad, la elegibilidad de investigación y la validación walk-forward.
- **Datos separados (holdout):** el veredicto guardado sobre datos que se mantuvieron fuera de la búsqueda, una puntuación estadística frente al umbral guardado con esa evaluación, al menos 15 operaciones en holdout y 40 en total, un resultado neto positivo en holdout, un profit factor en holdout de al menos 1.10, costos de trading conocidos y una ganancia media de al menos tres veces el costo medio de ida y vuelta.
- **Tus reglas de despliegue:** mínimo de operaciones, retorno positivo después de costos, drawdown máximo, profit factor mínimo, pérdida máxima por operación y, si lo exiges, un estilo de trading.

Cada fila indica de dónde sale su número: registrado con el backtest, una evaluación guardada, las reglas actuales de tu bot o un valor fijo que un backtest antiguo quizá no registró. Tres elementos aparecen como **Sin evaluar** a propósito, porque solo se comprueban al desplegar: el precio de los costos en vivo, la seguridad de la cuenta y de la ejecución, y la comprobación de Decision AI. Abrir la revisión no gasta créditos de IA.

Tres reglas del propio diálogo merecen repetirse:

> La puntuación de holdout no es un porcentaje de ganancia ni una probabilidad. La evidencia ausente no cuenta como aprobada. Una etiqueta de "campeón registrado" es histórica, no un permiso para operar ahora.

Debajo de la tabla puedes desplegar cada motivo de rechazo registrado, los parámetros y costos exactos que usó el backtest, y sus métricas y validación registradas.

## Una lista de seguimiento para candidatos prometedores

**Seguir este candidato** guarda el backtest y congela una copia, así que sigue siendo legible aunque se limpien resultados antiguos. **GUARDADOS / RETENIDOS / SEGUIMIENTO**, junto a **TODOS LOS BACKTESTS**, reúne tres tipos de resultados: los que guardaste, los que estás siguiendo y los que la aplicación conserva automáticamente.

Desde la 1.1.360, cada bot de investigación conserva los resultados originales completos de sus 100 mejores backtests, además de los resultados protegidos. Los resultados antiguos cuyas operaciones nunca se guardaron pueden seguir apareciendo como no disponibles; no se reconstruyen para hacerlos pasar por el original.

Nada de esto aprueba un backtest. Como dice la propia lista: guardar no es aprobar.

## Pruebas futuras que nunca colocan una orden

Un backtest, incluso con un holdout separado, sigue usando el pasado. La versión 1.1.360 te deja ver cómo se comporta un candidato con velas que no existían cuando lo elegiste.

Cuando un backtest está en tu lista de seguimiento, **Iniciar prueba futura sin órdenes** congela su configuración exacta y el motor de backtest de la aplicación, y luego ejecuta la estrategia en cada vela cerrada nueva:

- **Solo cuentan las velas que abren después de que inicias.** El historial anterior solo sirve para preparar los indicadores.
- **Lee velas cerradas de la caché verificada de la aplicación.** Si no ha llegado una vela nueva, la prueba espera; no se rellena nada.
- **Los costos son los registrados con el backtest.** Un backtest con costos registrados ausentes o en cero se rechaza, así que nunca obtienes una simulación sin costos.
- **El equity simulado cuenta solo operaciones cerradas,** después de esos costos. Una operación que sigue abierta en la última vela no se cuenta como cerrada.
- **Funciona mientras Period Trader está abierto,** revisando las pruebas activas en segundo plano, y puedes pulsar **Actualizar evidencia** cuando quieras. **Detener evaluación** termina una prueba y **Exportar evidencia** guarda su registro completo como archivo JSON.

Algunos límites son deliberados. Pueden correr hasta 20 pruebas futuras a la vez. Funcionan con las estrategias integradas; las estrategias personalizadas y las configuraciones por capas se rechazan con un mensaje en vez de cambiarse por algo parecido. Si cambias de cuenta de trading, o cambia el motor de la aplicación (por ejemplo, después de una actualización), la prueba conserva su evidencia pero no puede continuar, y tienes que iniciar una nueva. Las observaciones anteriores nunca se reescriben.

Lo más importante: una prueba futura no envía órdenes y no aprueba, no despliega ni cambia el veredicto de holdout guardado. Es evidencia adicional, no un filtro.

## Pregúntale a PeriodTrader AI sobre un bot de investigación

**Preguntar a PeriodTrader AI**, dentro de la revisión, adjunta el backtest al chat con una pregunta sugerida, por ejemplo que explique cada comprobación que pasó, falló o no se evaluó. No se envía nada hasta que pulses **Enviar**. El asistente puede leer los parámetros registrados de un bot, su evidencia de validación, su historial de operaciones guardado y sus pruebas futuras. Estas herramientas de investigación son de solo lectura: leerlas no cambia nada, no inicia pruebas y no despliega nada. PeriodTrader AI es parte de Pro y usa tus créditos de IA.

## Reglas de despliegue por bot de investigación

La versión 1.1.359 permite que cada bot de investigación siga las reglas de despliegue globales (Ajustes → Despliegue) o las suyas propias. Abre el menú del bot → **Reglas de despliegue…** y elige **Usar las reglas globales** o **Usar reglas propias de este bot**: mínimo de operaciones, profit factor mínimo, drawdown máximo, pérdida individual máxima y un estilo de trading que prefieres o exiges. **Usar recomendadas** rellena valores sugeridos, y el formulario de **Nueva investigación** ofrece la misma opción cuando creas un bot.

Una elección arriesgada muestra advertencias y pide un segundo clic (**Guardar de todos modos**); la decisión sigue siendo tuya. Una regla más estricta vuelve a calificar al instante los backtests guardados del bot, y si el campeón ya no pasa, ocupa su lugar el mejor backtest guardado que sí pase. Una regla más flexible se aplica desde los próximos backtests. El asistente de IA solo puede endurecer las reglas de un bot; cualquier cambio más flexible necesita tu aprobación. Los cambios quedan en el historial de cambios del bot.

## Desplegar un backtest que no es campeón

El despliegue automático sigue tomando solo un campeón aprobado. Ahora puedes desplegar otro backtest tú mismo con **DESPLEGAR ESTE BACKTEST…**. La aplicación primero enumera cada comprobación que no pasa y te advierte que puede colocar órdenes reales cuando su estrategia dé señal; solo pasa a vivo si confirmas. El despliegue automático y la IA nunca dan esa confirmación.

Las comprobaciones de seguridad estrictas siguen aplicando: precios, claves del exchange, límites de apalancamiento, tu plan, posiciones abiertas y límites de bots. Un backtest cuyo registro de operaciones falta o está incompleto tiene que ejecutarse de nuevo primero; la aplicación te ofrece hacerlo (alrededor de un minuto) y desplegar el resultado nuevo.

## Cuando una búsqueda está tardando

Cuando un bot de investigación ha ejecutado más de 15,000 backtests sin un campeón aprobado, su tarjeta muestra **Está tardando**, el conteo y una temporalidad mayor que podría encontrar más (por ejemplo 1H o 4H para un bot de 15 minutos). **Preguntar a la IA** abre el chat con una explicación sencilla. Nada cambia por sí solo: probar otra temporalidad significa crear un nuevo bot de investigación.

## Operaciones en vivo y gráficos

Las versiones 1.1.361 y 1.1.362 se centran en la precisión en vivo. Los despliegues conservan la vela de entrada correcta, el stop loss y el take profit dibujados en el gráfico se mantienen alineados con la protección que confirmó tu bróker o exchange, y las operaciones actuales tienen marcadores y etiquetas de lote más claros en el gráfico. También mejoraron los gráficos de equity y drawdown de los backtests, los mensajes cuando faltan datos o se está reconstruyendo una curva, y el diario. La configuración de riesgo de tus estrategias y tu historial de trading original se conservan.

## Cambios más pequeños

- **Volver a research:** al abrir un backtest guardado en el gráfico, aparece como **Vista previa del backtest · solo lectura**, con sus operaciones en el gráfico y sus parámetros originales y métricas guardadas en el **Plan del bot**. Los campos de órdenes quedan desactivados, y **Volver a research** te regresa a donde estabas.
- **Indicadores:** 30 estudios analíticos más en la biblioteca de indicadores.
- **Conexiones:** la configuración ofrece MetaTrader 5, Binance, Bybit, MEXC y OKX. Las conexiones guardadas se mantienen.
- **Inicio de sesión:** después de actualizar a la 1.1.359 o posterior, inicia sesión con Whop una vez. Tu plan, tus conexiones con brókers y exchanges y tu configuración quedan como estaban.

## Lo que no cambió

Revisar, seguir, guardar y hacer pruebas futuras son acciones de solo lectura: ninguna coloca una orden, aprueba un backtest ni despliega un bot. El despliegue automático mantiene sus comprobaciones normales, y los bots en vivo siguen operando con sus propias protecciones de riesgo. Cuando hay una actualización disponible, el panel muestra un botón **UPDATE NOW**.
