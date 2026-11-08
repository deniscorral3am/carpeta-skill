#!/usr/bin/env python3
"""Revisa los archivos de memoria (CLAUDE.md / AGENTS.md) de una carpeta.

Comprueba tamaño, fechas relativas y datos sensibles que no deberían estar.
Solo librería estándar. Uso:

    python3 revisar.py RUTA_CARPETA [--json]

Sale con código 1 si encuentra datos sensibles.
"""
import json
import os
import re
import sys

NOMBRES = ("CLAUDE.md", "AGENTS.md", "CLAUDE.local.md")
MAX_RAIZ = 200
MAX_PROYECTO = 120
IGNORAR = {".git", "node_modules", ".venv", "venv", "__pycache__", ".claude"}

SENSIBLE = [
    ("IBAN", re.compile(r"\b[A-Z]{2}\d{2}(?:[ ]?\d{4}){4,7}\b")),
    ("DNI/NIE", re.compile(r"\b[XYZ]?\d{7,8}[ -]?[A-HJ-NP-TV-Z]\b")),
    ("teléfono", re.compile(r"(?:\+34[ ]?)?\b[6789]\d{2}[ ]?\d{3}[ ]?\d{3}\b")),
    ("clave/token", re.compile(r"\b(?:sk|pk|rk|xox[bp]|ghp|gho|AKIA)[-_A-Za-z0-9]{12,}\b")),
    ("contraseña", re.compile(r"(?i)\b(?:contraseña|password|passwd|pwd)\s*[:=]\s*\S+")),
]
TARJETA = re.compile(r"\b(?:\d[ -]?){13,19}\b")
RELATIVAS = re.compile(
    r"(?i)\b(?:ayer|anteayer|mañana|pasado mañana|la semana que viene|la próxima semana|"
    r"el mes que viene|este lunes|este martes|este miércoles|este jueves|este viernes)\b"
)


def luhn(numero):
    digitos = [int(c) for c in numero if c.isdigit()]
    if not 13 <= len(digitos) <= 19:
        return False
    total = 0
    for i, d in enumerate(reversed(digitos)):
        if i % 2:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def revisar_archivo(ruta, es_raiz):
    with open(ruta, encoding="utf-8") as f:
        lineas = f.read().splitlines()
    limite = MAX_RAIZ if es_raiz else MAX_PROYECTO
    avisos, sensibles = [], []
    if len(lineas) > limite:
        avisos.append(f"{len(lineas)} líneas (máximo recomendado {limite})")
    if lineas and len(lineas) <= 3 and lineas[0].strip().startswith("@"):
        return {"archivo": ruta, "lineas": len(lineas), "avisos": [], "sensibles": [], "importa": lineas[0].strip()}
    for n, linea in enumerate(lineas, 1):
        for etiqueta, patron in SENSIBLE:
            for m in patron.finditer(linea):
                sensibles.append(f"L{n} {etiqueta}: {m.group(0)}")
        for m in TARJETA.finditer(linea):
            if luhn(m.group(0)):
                sensibles.append(f"L{n} tarjeta: {m.group(0)}")
        if RELATIVAS.search(linea) and "nunca" not in linea.lower():
            avisos.append(f"L{n} fecha relativa: {linea.strip()[:80]}")
    if not any(l.lower().startswith("actualizado") or "actualizado:" in l.lower() for l in lineas[-5:]):
        avisos.append("falta la línea final «Actualizado: dd/mm/aaaa»")
    return {"archivo": ruta, "lineas": len(lineas), "avisos": avisos, "sensibles": sensibles}


def buscar(raiz, profundidad=3):
    raiz = os.path.abspath(raiz)
    encontrados = []
    for actual, dirs, archivos in os.walk(raiz):
        nivel = actual[len(raiz):].count(os.sep)
        dirs[:] = [d for d in dirs if d not in IGNORAR and not d.startswith(".")]
        if nivel >= profundidad:
            dirs[:] = []
        for nombre in archivos:
            if nombre in NOMBRES:
                encontrados.append((os.path.join(actual, nombre), actual == raiz))
    return sorted(encontrados)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__)
        sys.exit(2)
    resultados = [revisar_archivo(r, es_raiz) for r, es_raiz in buscar(args[0])]
    if "--json" in sys.argv:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        if not resultados:
            print("No hay ningún CLAUDE.md ni AGENTS.md en esa carpeta.")
        for r in resultados:
            estado = "SENSIBLE" if r["sensibles"] else ("aviso" if r["avisos"] else "ok")
            print(f"[{estado}] {os.path.relpath(r['archivo'], args[0])} ({r['lineas']} líneas)")
            for s in r["sensibles"]:
                print(f"    - dato sensible {s}")
            for a in r["avisos"]:
                print(f"    - {a}")
        total = sum(len(r["sensibles"]) for r in resultados)
        print(f"\n{len(resultados)} archivos revisados · {total} datos sensibles")
    sys.exit(1 if any(r["sensibles"] for r in resultados) else 0)


if __name__ == "__main__":
    main()
