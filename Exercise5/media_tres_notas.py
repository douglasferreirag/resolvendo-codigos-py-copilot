"""
Cálculo da Média de Três Notas 🎓

Descrição:
Recebe três notas (números) do usuário e calcula a média aritmética.
Trata entradas inválidas e aceita números com casas decimais.

Uso:
$ python media_tres_notas.py
Digite a primeira nota: 8.5
Digite a segunda nota: 7
Digite a terceira nota: 9
Média: 8.17

Também é possível passar as três notas como argumentos:
$ python media_tres_notas.py 8.5 7 9
Média: 8.17
"""
from typing import Tuple
import sys


def parse_number(value: str) -> float:
    """Converte uma string em float, levantando ValueError se inválida."""
    return float(value.strip())


def calculate_average(a: float, b: float, c: float) -> float:
    """Retorna a média aritmética de três números."""
    return (a + b + c) / 3.0


def read_three_notes_from_input() -> Tuple[float, float, float]:
    a = parse_number(input("Digite a primeira nota: "))
    b = parse_number(input("Digite a segunda nota: "))
    c = parse_number(input("Digite a terceira nota: "))
    return a, b, c


def main() -> None:
    try:
        if len(sys.argv) == 4:
            a = parse_number(sys.argv[1])
            b = parse_number(sys.argv[2])
            c = parse_number(sys.argv[3])
        else:
            a, b, c = read_three_notes_from_input()

        avg = calculate_average(a, b, c)
    except ValueError:
        print("Entrada inválida: por favor informe números (ex.: 7, 8.5).")
        return

    # Exibe a média com duas casas decimais
    print(f"Média: {avg:.2f}")


if __name__ == "__main__":
    main()