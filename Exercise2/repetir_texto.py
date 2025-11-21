"""
Repetindo Textos ✏️

Descrição:
Recebe uma string e um número inteiro como entrada e retorna a string
repetida o número de vezes informado.

Uso:
$ python repetir_texto.py
Digite a string: ola
Digite o número de repetições: 3
Resultado:
olaolaola
"""
from typing import Any


def repeat_text(text: str, times: int) -> str:
    """
    Retorna `text` repetido `times` vezes.
    Levanta ValueError se times for negativo.
    """
    if times < 0:
        raise ValueError("O número de repetições deve ser >= 0")
    return text * times


def _input(prompt: str) -> str:
    # wrapper para facilitar testes / substituição, se necessário
    return input(prompt)


def main() -> None:
    try:
        text = _input("Digite a string: ")
        times_raw = _input("Digite o número de repetições: ")
        times = int(times_raw)
        result = repeat_text(text, times)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return

    print("Resultado:")
    print(result)


if __name__ == "__main__":
    main()