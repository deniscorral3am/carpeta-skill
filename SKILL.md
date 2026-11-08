---
name: carpeta
description: Crea o actualiza la memoria de la carpeta de tu negocio. Lee los últimos 30 días de tu correo, calendario y CRM conectados (o de los archivos de la carpeta) y escribe un CLAUDE.md en la raíz y otro en cada carpeta de cliente o proyecto con quién es quién, clientes, proyectos abiertos, decisiones, acuerdos, tu tono y pendientes, sin datos sensibles. También hace la versión AGENTS.md para Codex. Úsala cuando digan /carpeta, «comenta CARPETA», «crea la memoria», «lee los últimos 30 días», «archivo de memoria para mis carpetas», «actualiza la memoria» o «que recuerde todo de mi negocio».
argument-hint: "[días] [--agents]"
---

# /carpeta · una carpeta de proyecto que lo recuerda todo

Idea: en vez de abrir un chat nuevo y volver a explicar tu negocio, trabajas dentro de una carpeta. Claude Code lee el
`CLAUDE.md` de la carpeta (y de las superiores) al empezar cada sesión, y el de una subcarpeta en cuanto trabaja en ella.
Esta skill escribe esos archivos a partir de lo que ha pasado de verdad en tu negocio.

`${CLAUDE_SKILL_DIR}` es la carpeta de esta skill (Claude Code la sustituye sola).

## 01 · Antes de leer nada
1. Directorio de trabajo = la carpeta del negocio. Si es tu carpeta personal (`~`) o el Escritorio entero, para y
   pregunta en qué carpeta quiere la memoria (o propón crear `~/MiNegocio`).
2. Argumentos: un número cambia los días (por defecto 30). `--agents` escribe `AGENTS.md` en vez de `CLAUDE.md`
   (para Codex o para compartir memoria entre herramientas; mira el paso 05).
3. Detecta fuentes, en este orden:
   - Conectores o servidores MCP disponibles en la sesión (Gmail, Google Calendar, Outlook, HubSpot, Pipedrive, Notion,
     Drive...). Usa solo sus herramientas de lectura.
   - Clientes de API hechos con la skill `/api` (carpeta `conexiones/` o skills de herramientas instaladas).
   - Archivos de la carpeta: exportaciones (`.json`, `.csv`, `.mbox`, `.ics`), notas y documentos.
4. Di en una línea qué fuentes vas a leer y desde qué fecha (hoy menos N días, en dd/mm/aaaa). Si no hay ninguna fuente,
   explica cómo conectar una (README, sección «Conectar») y para.

## 02 · Leer (solo lectura)
Sigue el prompt de `${CLAUDE_SKILL_DIR}/PROMPT.md` al pie de la letra. Lo esencial:
- Nunca envíes, borres, archives, aceptes invitaciones ni marques como leído.
- Correo: busca por fecha (`after:AAAA/MM/DD` en Gmail). Prioriza los enviados (dicen cómo escribe) y los hilos con
  clientes. Ignora boletines, notificaciones y publicidad.
- Calendario: eventos de los últimos N días y de los próximos 30 (para pendientes con fecha).
- CRM: contactos y oportunidades con actividad en el periodo, etapa, valor y siguiente paso.
- Lo anterior al periodo solo entra si sigue abierto.

## 03 · Escribir
- `./CLAUDE.md` con `${CLAUDE_SKILL_DIR}/plantillas/CLAUDE-raiz.md` como guía.
- `<carpeta>/CLAUDE.md` en cada carpeta de primer nivel que sea de un cliente o proyecto, con
  `${CLAUDE_SKILL_DIR}/plantillas/CLAUDE-proyecto.md`. Las carpetas de sistema, exportaciones o facturas no llevan.
- Si el archivo existe: conserva lo escrito por la persona, añade lo nuevo, tacha lo obsoleto con fecha, no dupliques.
- Clientes activos sin carpeta: proponlos al final; créalos solo si lo pide.

Reglas que no se saltan: menos de 200 líneas la raíz y 120 cada proyecto; fechas absolutas; nada inventado (lo dudoso
con «(¿confirmar?)»); fuera contraseñas, claves, tarjetas, IBAN, DNI/NIE, salud, direcciones y teléfonos personales;
cada dato con su fuente; última línea «Actualizado: dd/mm/aaaa · fuentes: ...».

## 04 · Comprobar
```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/revisar.py .
```
Si marca datos sensibles, quítalos y vuelve a pasarlo hasta que salga limpio. Corrige también los avisos de tamaño y de
fechas relativas.

## 05 · Codex y AGENTS.md
Con `--agents`, escribe `AGENTS.md` con el mismo contenido. Si la persona usa Claude Code y Codex a la vez, deja la
memoria en `AGENTS.md` y en cada carpeta un `CLAUDE.md` con una sola línea `@AGENTS.md` (Claude Code lo importa).

## 06 · Cierre
Dile: archivos creados o actualizados, 5 cosas aprendidas para que confirme, pendientes de los próximos 7 días y
carpetas propuestas. Sugiere repetir cada semana con «actualiza la memoria» (solo lee desde la última fecha).
