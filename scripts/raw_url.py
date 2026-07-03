#!/usr/bin/env python3
"""Gera a URL raw pública de um arquivo versionado neste repositório.

Uso:
  python3 scripts/raw_url.py imports/arquivo.html
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

OWNER_REPO = "sqz-group/repo-canva-sqz"
BRANCH = "main"


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python3 scripts/raw_url.py <arquivo-relativo>", file=sys.stderr)
        return 2

    rel = Path(sys.argv[1])
    if rel.is_absolute() or ".." in rel.parts:
        print("Erro: informe um caminho relativo dentro do repositório.", file=sys.stderr)
        return 2

    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    target = root / rel
    if not target.exists():
        print(f"Erro: arquivo não existe: {rel}", file=sys.stderr)
        return 1

    print(f"https://raw.githubusercontent.com/{OWNER_REPO}/{BRANCH}/{rel.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
