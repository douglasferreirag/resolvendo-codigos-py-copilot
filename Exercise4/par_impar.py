"""
Verificando Números Pares e Ímpares 🧮

Descrição:
Recebe um número inteiro como entrada e verifica se ele é par ou ímpar.
Trata entradas inválidas e pode receber o número via argumento de linha de comando
ou via prompt interativo.

Uso:
$ python par_impar.py
Digite um número inteiro: 7
7 é ímpar.

Ou:
$ python par_impar.py 10
10 é par.
"""
from typing import Tuple
import sys


def is_even(n: int) -> bool:
    """Retorna True se n for par, False caso contrário."""
    return n % 2 == 0


def parse_int(value: str) -> int:
    """Tenta converter value para int, levantando ValueError em caso de falha."""
    return int(value.strip())


def check_number_from_string(value: str) -> Tuple[int, str]:
    """
    Converte a string em inteiro e retorna uma tupla (n, mensagem_resposta).
    Levanta ValueError se a conversão falhar.
    """
    n = parse_int(value)
    message = f"{n} é {'par' if is_even(n) else 'ímpar'}."
    return n, message


def main() -> None:
    try:
        if len(sys.argv) > 1:
            raw = sys.argv[1]
        else:
            raw = input("Digite um número inteiro: ")

        _, msg = check_number_from_string(raw)
    except ValueError:
        print("Entrada inválida: por favor informe um número inteiro (ex.: 4, -3).")
        return

    print(msg)


if __name__ == "__main__":
    main()