# Carpeta · deja de usar chats, usa una carpeta que lo recuerda todo

Cada chat nuevo empieza de cero y vuelves a explicar quién eres, quiénes son tus clientes y cómo escribes. Una carpeta de
proyecto no: Claude Code lee el archivo de memoria (`CLAUDE.md`) de la carpeta al empezar cada sesión, y el de cada
subcarpeta en cuanto trabaja en ella. Codex hace lo mismo con `AGENTS.md`.

Este recurso te da el prompt que llena esa memoria con lo que ha pasado de verdad en tu negocio: lee los últimos 30 días
de tu correo, tu calendario y tu CRM y escribe un `CLAUDE.md` en la raíz y otro en cada carpeta de cliente o proyecto.

Hecha por Denis Corral · Sell Your AI (https://sellyourai.io)

---

## El prompt

Copia y pega esto dentro de la carpeta de tu negocio (con el correo, el calendario y el CRM ya conectados):

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

La versión para Codex (`AGENTS.md`) y el prompt para actualizarla cada semana están en [PROMPT.md](PROMPT.md).

---

## Monta la carpeta en 30 segundos

**Claude, app de escritorio**
1. Abre la app de Claude y entra en la pestaña **Code**.
2. Elige la carpeta de tu negocio (o crea una nueva, por ejemplo `MiNegocio`, con una subcarpeta por cliente).
3. Pega el prompt.

**Claude Code en la terminal**
```bash
mkdir -p ~/MiNegocio && cd ~/MiNegocio && claude
```
Y pega el prompt.

**Codex (ChatGPT)**
1. Abre Codex (la app de escritorio o `codex` en la terminal) en la carpeta de tu negocio.
2. Pega la versión para Codex de [PROMPT.md](PROMPT.md), que escribe `AGENTS.md`.

A partir de ahí, abre siempre la sesión en esa carpeta. La memoria ya está cargada.

## Conectar Gmail, el calendario y el CRM

- **Conectores oficiales de Claude.** En claude.ai o en la app: Ajustes → Conectores. Gmail, Google Calendar y Google
  Drive están entre los conectores de Anthropic; otros (HubSpot, Notion y más) están en el directorio de conectores.
  Si inicias sesión en Claude Code con tu cuenta de Claude, los conectores que hayas activado aparecen también allí
  (compruébalo con `/mcp`).
- **Otro servidor MCP.** `claude mcp add` en la terminal, siguiendo las instrucciones de la herramienta.
- **Por API, sin MCP.** Con el recurso `/api` (comenta API): Claude Code construye la conexión con la clave de la
  herramienta guardada en un `.env`.
- **Sin conectar nada.** Exporta (correo en `.mbox`, calendario en `.ics`, CRM en `.csv`), mete los archivos en la
  carpeta y el prompt los usa.

## Instalación como skill (opcional)

El prompt funciona solo. Si además quieres el comando `/carpeta`, que comprueba la memoria al terminar:

```bash
git clone https://github.com/deniscorral3am/carpeta-skill ~/.claude/skills/carpeta
```

Abre Claude Code en la carpeta de tu negocio y escribe `/carpeta` (o `/carpeta 60` para 60 días, `/carpeta --agents`
para escribir `AGENTS.md`).

## Qué necesitas

- Claude Code (con tu suscripción de Claude basta) o Codex.
- Python 3 para el revisor (`scripts/revisar.py`, solo librería estándar).
- Al menos una fuente: un conector, una conexión por API o archivos exportados.

## Qué hay dentro

| Archivo | Para qué |
|---|---|
| `PROMPT.md` | el prompt, la versión `AGENTS.md` y el de actualización semanal |
| `SKILL.md` | la skill `/carpeta` |
| `plantillas/` | cómo queda un `CLAUDE.md` de raíz y uno de proyecto |
| `scripts/revisar.py` | revisa tamaño, fechas relativas y datos sensibles (IBAN, DNI, teléfonos, claves, tarjetas) |
| `ejemplo/reformas-albor/` | negocio inventado con correos, calendario y CRM falsos, y la memoria que generó el prompt |

## Ejemplo

En `ejemplo/reformas-albor/` hay una empresa de reformas inventada (todo es ficticio): 14 correos, 9 eventos y un CRM
de 5 oportunidades. El prompt generó el `CLAUDE.md` de la raíz y uno por cada obra. Ábrelos para ver el resultado; en
[PROBADO.md](PROBADO.md) tienes cómo se probó.

## Buenas prácticas

- Repite cada semana con «actualiza la memoria».
- Revisa lo que escribe: es tu memoria, corrígela cuando algo no cuadre.
- No subas la carpeta del negocio a un repositorio público: la memoria tiene nombres de clientes y acuerdos.

## Licencia

MIT. Hecha por Denis Corral · Sell Your AI (https://sellyourai.io)
