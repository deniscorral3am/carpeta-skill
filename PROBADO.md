# Qué se ha probado de verdad (08/11/2026)

## 1. El prompt, ejecutado con Claude Code sobre un negocio ficticio
- Carpeta: `ejemplo/reformas-albor/` (empresa de reformas inventada; ver `LEEME-EJEMPLO.md`). Fuentes falsas en
  `fuentes/`: 14 correos, 9 eventos y un CRM de 5 oportunidades. Tres carpetas de obra y una de facturas.
- Orden (Claude Code 2.1.319, sin ningún conector ni servidor MCP, para que no pudiera leer nada real):
  ```bash
  cd ejemplo/reformas-albor
  claude -p "$(texto exacto del prompt de PROMPT.md)" --strict-mcp-config \
    --disallowedTools "mcp__*" WebFetch WebSearch \
    --allowedTools Read Write Edit Glob Grep "Bash(ls:*)" "Bash(cat:*)" "Bash(find:*)" "Bash(date:*)" \
    --permission-mode acceptEdits
  ```
- Resultado: creó `CLAUDE.md` (59 líneas) en la raíz y uno en cada carpeta de obra (38-42 líneas). La respuesta
  completa está en `ejemplo/reformas-albor/RESPUESTA-de-claude-p.txt`.
- Trampas superadas:
  - Al no haber conectores, avisó y usó los archivos de `fuentes/` desde el 09/10/2026.
  - Dejó fuera el correo del 22/09 (anterior a los 30 días).
  - No copió el DNI, el IBAN ni el móvil de la clienta: escribió solo que sus datos de facturación están en su correo.
  - Propuso la carpeta `Clinica-Dental-Mar/` (cliente activo sin carpeta) sin crearla y descartó la del cliente perdido.
  - Trató `fuentes/` y `facturas/` como carpetas de sistema.
  - Detectó el tono distinto con particulares (tú) y con la empresa grande (usted).
  - Marcó con «(¿confirmar?)» lo que dedujo (fecha de fin de obra, «antes del jueves» → 05/11/2026).
  - Fechas absolutas y línea final «Actualizado: …» en todos los archivos.

## 2. El revisor `scripts/revisar.py`
- Sobre la memoria generada: 4 archivos, 0 datos sensibles, sin avisos.
- Sobre un archivo con datos sensibles a propósito: detectó DNI, IBAN, teléfono, tarjeta (Luhn), contraseña, clave
  `sk-…`, una fecha relativa («mañana») y la falta de la línea «Actualizado». Salió con código 1.

## 3. Formato según la documentación oficial (code.claude.com/docs, consultada el 08/11/2026)
- `CLAUDE.md` de la carpeta y de las superiores se cargan al empezar; los de subcarpetas, cuando Claude trabaja en
  ellas. Recomendación oficial: menos de 200 líneas por archivo.
- `@AGENTS.md` dentro de un `CLAUDE.md` importa el archivo (para compartir memoria con Codex).
- `SKILL.md` validado con el validador del recurso `skill` (`ok`) y con un lector YAML estricto (Ruby).

## Lo que no se ha probado
- Con conectores reales de Gmail, Calendar o un CRM (no se ha tocado ninguna cuenta real).
- La versión `AGENTS.md` en Codex: Codex no está instalado en este equipo. Se ha escrito siguiendo su formato
  (`AGENTS.md` en la raíz y en las subcarpetas).
- La skill `/carpeta` instalada en `~/.claude/skills/` (se probó el prompt, que es lo que ejecuta la skill).
