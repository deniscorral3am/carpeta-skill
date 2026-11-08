# El prompt (cópialo entero)

Ábrelo en la carpeta de tu negocio (Claude Code o Codex), conecta antes tu correo, tu calendario y tu CRM, y pega esto:

```text
Lee lo que ha pasado en mi negocio en los últimos 30 días y crea la memoria de esta carpeta para que no tenga que volver a explicarte nada.

1. FUENTES. Usa las herramientas que tengo conectadas: correo, calendario, CRM y cualquier otra (Gmail, Google Calendar, Outlook, HubSpot, Pipedrive, Notion, Drive...). Si no hay ninguna conectada, usa los archivos de esta carpeta (exportaciones, notas, documentos). Antes de empezar dime en una línea qué fuentes vas a leer y desde qué fecha. Solo lectura: no envíes, borres, archives, aceptes ni marques nada.

2. QUÉ BUSCAR (desde hoy menos 30 días; ignora lo anterior salvo que siga abierto):
- Quién es quién: clientes, equipo, proveedores y socios (nombre, empresa, rol y cómo prefieren que les hables).
- Clientes y en qué punto está cada uno.
- Proyectos abiertos: siguiente paso y fecha.
- Decisiones tomadas: qué, cuándo y por qué.
- Acuerdos cerrados: precio, alcance y plazos.
- Cómo escribo yo: fíjate en mis correos enviados (saludo, despedida, tú o usted, largo de los mensajes, palabras que repito).
- Pendientes con responsable y fecha, y lo que se repite cada semana.

3. CARPETAS. Mira las carpetas de primer nivel de este directorio. Cada una que sea de un cliente o un proyecto es una carpeta de proyecto; las de sistema o de exportaciones no. Si un cliente o proyecto activo no tiene carpeta, propónmela al final, pero no la crees si no te lo digo.

4. ESCRIBE:
- ./CLAUDE.md (la raíz): mi negocio en 3 líneas, equipo y quién es quién, clientes (una línea cada uno con su carpeta), cómo escribo, reglas de trabajo, pendientes generales e índice de carpetas. Añade esta regla al final: «Cuando termines una tarea y hayas aprendido algo que sirva para la próxima vez, actualiza el CLAUDE.md que corresponda».
- <carpeta>/CLAUDE.md en cada carpeta de proyecto: contexto en 3 líneas, personas (rol y cómo tratarlas), estado y siguiente paso, decisiones con fecha, acuerdos (precio, alcance, plazos), pendientes como casillas [ ] con responsable y fecha, y de dónde sale cada dato (por ejemplo «correo de Laura, 12/10/2026»).
- Si ya existe un CLAUDE.md, actualízalo: conserva lo que escribí yo, añade lo nuevo, tacha lo que ya no vale (~~así~~, con la fecha) y no dupliques.

5. REGLAS:
- Menos de 200 líneas el de la raíz y menos de 120 cada uno de proyecto. Viñetas cortas, nada de párrafos.
- Fechas absolutas (dd/mm/aaaa), nunca «ayer», «el jueves» ni «la semana que viene».
- No inventes nada. Si un dato no está en las fuentes, no lo pongas; si es dudoso, añade (¿confirmar?).
- Fuera datos sensibles: contraseñas, claves, tokens, tarjetas, IBAN, DNI/NIE, datos de salud, direcciones y teléfonos personales. Del correo, solo lo que sirve para trabajar (quién, qué, cuándo y cuánto se ha acordado). Si algo importante es sensible, escribe solo que existe y dónde está («contrato firmado: en Drive»).
- No copies correos enteros: resume.
- Cierra cada archivo con la línea «Actualizado: dd/mm/aaaa · fuentes: ...».

6. AL TERMINAR dime: qué archivos has creado o actualizado, 5 cosas que has aprendido de mi negocio para que te las confirme, los pendientes que vencen en los próximos 7 días y las carpetas que me propones crear.
```

## Versión para Codex (AGENTS.md)

Codex lee `AGENTS.md`, no `CLAUDE.md`. Usa el mismo prompt cambiando el punto 4 por este:

```text
4. ESCRIBE la memoria en archivos AGENTS.md (no CLAUDE.md): ./AGENTS.md en la raíz y <carpeta>/AGENTS.md en cada carpeta de proyecto, con el mismo contenido que te describo a continuación. [pega aquí el resto del punto 4 tal cual]
```

¿Usas los dos? Deja la memoria en `AGENTS.md` y crea un `CLAUDE.md` de una sola línea en cada carpeta con:

```text
@AGENTS.md
```

Claude Code importa el archivo con esa línea, así los dos leen la misma memoria y solo la mantienes una vez.

## Para repetirlo cada semana

```text
Actualiza la memoria: lee solo lo que ha pasado desde la última actualización (mira la fecha al final de cada CLAUDE.md), aplica las mismas reglas de siempre y dime qué ha cambiado.
```
