Desde nuestro último artículo de producto salieron dos actualizaciones. La versión 1.1.379 convierte la pestaña Navegador en la **Terminal web**, con un panel en vivo y un ticket de órdenes para las plataformas que PeriodTrader tiene en un script, empezando por TopstepX. La versión 1.1.380 evita que tu PC se suspenda mientras haya bots, operaciones abiertas o investigación en marcha, y corrige un congelamiento poco frecuente. Esto es lo que cambió y por qué importa.

## La Terminal web (1.1.379, Pro)

La pestaña Navegador te dejaba abrir la web de una plataforma de trading dentro de la aplicación y trabajar en ella con la IA. Ahora se llama **TERMINAL WEB**, y en una plataforma con script ya no te muestra primero la web tal cual. La plataforma corre oculta y, en su lugar, ves un panel de PeriodTrader.

### Un panel en vivo para TopstepX

TopstepX es la primera plataforma con un script incluido en la aplicación. Su panel muestra, actualizado cada segundo:

- el balance, el límite de pérdida máxima y el margen que queda hasta él;
- el P&L realizado y no realizado, y la pérdida diaria frente a su límite;
- pestañas con tus posiciones, órdenes, operaciones y cuentas.

En una cuenta de fondeo, tocar el límite de pérdida máxima normalmente termina la cuenta, así que el margen que queda hasta ese límite está arriba y no perdido en algún rincón de la página de la firma.

La web real no desaparece. Sigue visible como una pequeña ventana en vivo en la esquina, y un clic la abre a tamaño completo si quieres usar el propio sitio. Un selector **PANEL / SITIO WEB** cambia entre los dos. Si tu sesión está cerrada, el sitio se abre a tamaño completo para que inicies sesión en la página de la propia plataforma; PeriodTrader nunca ve tu contraseña, y el panel vuelve solo cuando entras.

### Operar desde nuestro ticket

El panel tiene su propio ticket de órdenes: **COMPRAR A MERCADO**, **VENDER A MERCADO**, **CERRAR POSICIÓN**, **REVERTIR**, **CANCELAR ÓRDENES** y un botón que cierra todas las posiciones y cancela las órdenes de una vez. Vienen con dos protecciones:

- Cada orden te pide confirmación antes de enviar nada.
- **Solo prueba** recorre cada paso de una orden y se detiene antes del botón de orden, así puedes ver exactamente lo que haría el script sin operar.

Detrás del ticket, la aplicación escribe y hace clic dentro de la página oculta de la plataforma igual que lo haría una persona. Por eso importa tener un script que funcione: describe qué campos leer y qué botones pulsar, y pulsar el botón de orden siempre es un paso aparte, marcado, que necesita tu confirmación en el panel.

## Scripts por plataforma, creados una vez por la IA

¿Y una plataforma que PeriodTrader aún no conoce? La primera vez que la usas, la IA hace una **primera ejecución**: lee tu cuenta, tus posiciones y el ticket de órdenes, llena una orden de prueba hasta el botón de orden sin pulsarlo nunca y guarda lo que hizo como un script.

El script se comprueba en la página real antes de guardarse, y las pruebas nunca envían una orden. A partir de ahí el panel funciona con el script, que es mucho más rápido que la IA y no necesita un turno de la IA en cada acción. Si una plataforma cambia su página, **Arreglar con IA** o **Reconstruir con IA** reparan el script de la misma forma.

Algunos detalles que conviene saber:

- **Los scripts son datos, no código.** Un script enumera campos, tablas y pasos como "clic", "llenar" o "esperar"; no puede ejecutar programas en tu PC.
- **Se comparten para revisión.** Los scripts nuevos se comparten con PeriodTrader para que otros usuarios puedan tenerlos. Cada script compartido queda retenido para revisión porque puede enviar órdenes, y un script que contenga algo privado, como números de cuenta, correos electrónicos o montos de dinero, no se comparte.
- **Listos para todos.** Cuando un script se aprueba, cualquier usuario que abra esa plataforma sin script lo recibe instalado automáticamente, y los scripts aprobados también llegan con la siguiente actualización. Tu propio script siempre tiene prioridad sobre uno compartido.

La Terminal web es una función Pro, y la primera ejecución usa la IA, que consume tus créditos de IA compartidos. Después, el uso diario de un script no necesita la IA.

## Mantener este PC despierto (1.1.380)

Si dejas un PC con bots corriendo durante la noche, Windows puede suspenderlo tras un rato de inactividad. Un PC suspendido pausa la aplicación: los bots dejan de vigilar el mercado, la investigación se detiene y las conexiones con el bróker se caen. Los stops y objetivos que ya están en tu bróker o exchange siguen en su sitio, pero nada en la aplicación gestiona la operación hasta que el PC despierta.

PeriodTrader ahora le pide a Windows que se mantenga despierto mientras tenga trabajo:

- hay un bot en vivo o un despliegue automático en marcha;
- hay una posición abierta en MT5 o en cripto;
- hay un bot de investigación corriendo y sin pausar.

Cuando no se cumple ninguna de esas condiciones, la petición se libera y Windows suspende el equipo como siempre. La pantalla puede apagarse igual; solo el sistema se mantiene despierto. El ajuste es **Mantener este PC despierto mientras haya bots o investigación en marcha**, en **AJUSTES → GENERAL**, viene activado y tiene una línea de estado que te dice si ahora mismo está en espera o activo.

Ten en cuenta dos límites. En batería, Windows aún puede suspender el PC. Y esto solo bloquea la suspensión automática cuando el PC está inactivo: la documentación de Microsoft indica que este mecanismo [no puede impedir que el usuario suspenda el equipo](https://learn.microsoft.com/es-es/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate), así que elegir Suspender, apagar o una laptop configurada para suspenderse al cerrar la tapa siguen funcionando como antes. Si tus bots tienen que correr mientras no estás, revisa también la configuración de energía de Windows.

## Un arreglo de congelamiento (1.1.380)

En la 1.1.379 la aplicación podía, rara vez, congelarse y dejar de actualizar los bots, los trailing stops y la protección de riesgo. Pasaba cuando la revisión de depósitos y retiros de la cuenta coincidía con el momento en que la aplicación sincronizaba un stop-loss: cada una esperaba a la otra. Esa revisión ahora corre en segundo plano y ya no puede bloquear la aplicación. Las órdenes que ya estaban en el bróker mantuvieron su stop-loss y take-profit en ese tiempo.

> Si sigues en la 1.1.379, actualiza a la 1.1.380. La actualización automática la instala en un momento seguro, cuando cada operación abierta tiene su stop en el bróker.

## Investigación y el resto de la 1.1.379

### Empezar de cero

El menú del bot de investigación tiene una nueva opción, **Empezar de cero…**. Reconstruye el bot con toda la configuración con la que se creó, como si lo acabaras de crear: el contador de pruebas vuelve a 0 y la búsqueda empieza de nuevo, mientras sus pruebas anteriores se quedan en el historial. Si el bot tiene un despliegue en vivo, ese bot sigue operando igual y se queda en la misma tarjeta; tus reglas de despliegue deciden cuándo un nuevo campeón lo reemplaza.

### La investigación omite ajustes que no cambian nada

Algunas estrategias fijan su propio stop y objetivo e ignoran parte de la cuadrícula compartida, así que la investigación podía gastar cientos de backtests en ajustes que daban resultados idénticos. Cada bot de investigación de una sola estrategia ahora lo comprueba una vez, poco después de arrancar: cambia un ajuste a la vez y fija en un solo valor cualquier ajuste que no cambie nada. Las búsquedas terminan antes y los backtests se dedican a los ajustes que importan.

### Cambios más pequeños

- **Bots de investigación con Recovery:** ya no muestran un mejor resultado de backtests antiguos que se detenían en su primer tope de pérdida; la tarjeta muestra el mejor real en el periodo de prueba completo.
- **Más ligera al investigar:** la aplicación usa menos procesador y memoria mientras corre la investigación.
- **Panel de operaciones del gráfico:** cuando una operación del panel se ejecuta, su stop-loss y take-profit se desactivan para que dejen de mostrarse en el gráfico. Una orden rechazada los mantiene.
- **Análisis de Earn estructurado:** total ganado, rendimiento, promedio por posición, ritmo diario, mejor resultado, un gráfico de crecimiento, una tabla por par y una lista ordenable de cada posición, arriba en la pestaña.
- **Sonidos de alerta:** elige entre 10 sonidos, ajusta el volumen o apaga el sonido en **AJUSTES → NOTIFICACIÓN / INFORMES**, con un botón **Probar sonido**.
- **Comunidad:** compartir e instalar desde la Comunidad vuelve a funcionar para los usuarios con sesión iniciada.

Nada de esto cambia cómo operan tus estrategias. Se trata de ver tu cuenta con claridad, mantener la aplicación funcionando cuando te alejas y gastar el tiempo de investigación donde cuenta.
