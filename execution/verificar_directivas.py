#!/usr/bin/env python3
"""Falla si CLAUDE.md, AGENTS.md y GEMINI.md no son byte a byte iguales.

Uso:  python3 execution/verificar_directivas.py [--arreglar]
  --arreglar  copia CLAUDE.md sobre los otros dos en lugar de fallar.
Pensado para correr antes de cada PR y como hook de pre-commit.
"""
import hashlib, pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTE = RAIZ / "CLAUDE.md"
COPIAS = [RAIZ / "AGENTS.md", RAIZ / "GEMINI.md"]

def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    arreglar = "--arreglar" in sys.argv
    if not FUENTE.exists():
        print("Falta CLAUDE.md"); return 2
    ref = h(FUENTE); distintos = []
    for c in COPIAS:
        if not c.exists() or h(c) != ref:
            distintos.append(c.name)
    if not distintos:
        print("OK: CLAUDE.md, AGENTS.md y GEMINI.md son idénticos"); return 0
    if arreglar:
        for c in COPIAS: c.write_bytes(FUENTE.read_bytes())
        print(f"Arreglado: {', '.join(distintos)} copiados desde CLAUDE.md"); return 0
    print(f"DIFIEREN de CLAUDE.md: {', '.join(distintos)}. Corre con --arreglar o replica el cambio a mano.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
