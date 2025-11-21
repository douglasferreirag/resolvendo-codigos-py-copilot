#!/usr/bin/env python3
"""
concat.py — Concatenador flexível de valores (2 ou N), com suporte a arquivo de entrada e opções úteis.

Uso (exemplos):
  - Interativo:
      python3 concat.py
    (será solicitado uma lista separada por vírgula ou, se vazio, dois prompts)

  - Via CLI, passando vários valores:
      python3 concat.py --value "Olá" --value "Mundo"
      python3 concat.py -v "a" -v "b" -v "c"

  - Via CLI, passando grupos:
      python3 concat.py -v a b c

  - A partir de arquivo (um valor por linha):
      python3 concat.py --file valores.txt

Opções:
  --value, -v    Valor(s) a concatenar (pode ser usado várias vezes; cada uso pode aceitar múltiplos valores)
  --file, -f     Caminho para arquivo com valores, um por linha
  --sep          Separador entre valores (padrão: "")
  --strip        Remove espaços das extremidades de cada valor antes de concatenar
  --lower        Converte resultado para minúsculas
  --upper        Converte resultado para maiúsculas
  --quiet        Modo silencioso (quando em batch, não solicitar entradas interativas)
"""
from typing import List
import argparse
import sys


def concat_values(values: List[str], sep: str = "", strip: bool = False, lower: bool = False, upper: bool = False) -> str:
    """Concatena uma lista de valores como strings aplicando opções."""
    if not values:
        return ""

    # Converter e aplicar strip opcional em cada elemento
    processed = []
    for v in values:
        s = "" if v is None else str(v)
        if strip:
            s = s.strip()
        processed.append(s)

    result = (sep or "").join(processed)

    if lower:
        result = result.lower()
    if upper:
        result = result.upper()

    return result


def read_values_from_file(path: str) -> List[str]:
    """Lê valores de um arquivo, um por linha (remove apenas o caractere de quebra de linha)."""
    vals = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            vals.append(line.rstrip("\n"))
    return vals


def parse_args():
    p = argparse.ArgumentParser(description="Concatenar valores em uma string (2 ou N).")
    # permitir "-v a b" e também múltiplos "-v" (cada um com múltiplos)
    p.add_argument("--value", "-v", action="append", nargs="+", help="Valor(s) a concatenar (pode ser usado múltiplas vezes)")
    p.add_argument("--file", "-f", help="Arquivo com valores (um por linha)")
    p.add_argument("--sep", default="", help="Separador entre os valores (padrão: sem separador)")
    p.add_argument("--strip", action="store_true", help="Remover espaços das extremidades de cada valor")
    p.add_argument("--lower", action="store_true", help="Converter resultado para minúsculas")
    p.add_argument("--upper", action="store_true", help="Converter resultado para maiúsculas")
    p.add_argument("--quiet", action="store_true", help="Modo silencioso (não entra em prompts)")
    return p.parse_args()


def _flatten_arg_values(arg_value):
    """Flatten da lista de listas retornada por argparse (ou None)."""
    if not arg_value:
        return []
    flat = []
    for group in arg_value:
        # group é uma lista: ex ['a','b'] ou ['a,b'] dependendo do uso; expand se contiver vírgula
        for item in group:
            if isinstance(item, str) and "," in item:
                # permitir --value "a,b,c"
                parts = [p for p in (x.strip() for x in item.split(",")) if p != ""]
                flat.extend(parts)
            else:
                flat.append(item)
    return flat


def main():
    args = parse_args()

    values = _flatten_arg_values(args.value)

    # ler de arquivo se passado
    if args.file:
        try:
            file_vals = read_values_from_file(args.file)
            values.extend(file_vals)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {args.file}", file=sys.stderr)
            sys.exit(2)

    # se nenhum valor foi passado, interativo (salvo se --quiet)
    if not values and not args.quiet:
        # primeiro tentar uma entrada fazível: lista separada por vírgula
        try:
            raw = input("Digite valores separados por vírgula (ou apenas ENTER para inserir dois valores): ")
        except EOFError:
            raw = ""
        if raw:
            # dividir por vírgula e manter espaços (strip será aplicado depois se selecionado)
            values = [v for v in (x for x in (s.strip() for s in raw.split(","))) if v != ""]
        else:
            # fallback: pedir dois prompts separados (para compatibilidade com o enunciado original)
            try:
                a = input("Digite o primeiro valor: ")
            except EOFError:
                a = ""
            try:
                b = input("Digite o segundo valor: ")
            except EOFError:
                b = ""
            values = [a, b]

    # Em modo quiet e sem entradas, usar lista vazia (concat_values retorna "")
    result = concat_values(values, sep=args.sep, strip=args.strip, lower=args.lower, upper=args.upper)
    print(result)


if __name__ == "__main__":
    main()