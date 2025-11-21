"""
Operações Matemáticas Simples 📐

Descrição:
Solicita ao usuário dois números e uma operação simples, então exibe o resultado.
Suporta as operações: +, -, *, /, //, %, **

Uso:
$ python operacoes_simples.py
Digite o primeiro número: 10
Digite o segundo número: 3
Escolha a operação (+, -, *, /, //, %, **): /
Resultado: 3.3333333333333335
"""
from typing import Callable


def parse_number(value: str) -> float:
    """Converte a entrada em número (int ou float). Levanta ValueError se inválido."""
    value = value.strip()
    try:
        if "." in value or "e" in value.lower():
            return float(value)
        return int(value)
    except ValueError:
        # tenta float por segurança (ex.: "3.0")
        return float(value)  # permitirá propagar ValueError se continuar inválido


def perform_operation(a: float, b: float, op: str) -> float:
    """Executa a operação op entre a e b. Levanta ValueError para operações desconhecidas
    e ZeroDivisionError quando apropriado."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*" or op.lower() == "x":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Divisão por zero")
        return a / b
    if op == "//":
        if b == 0:
            raise ZeroDivisionError("Divisão inteira por zero")
        return a // b
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("Módulo por zero")
        return a % b
    if op == "**" or op.lower() == "pow":
        return a ** b
    raise ValueError(f"Operação desconhecida: {op}")


def main() -> None:
    try:
        raw_a = input("Digite o primeiro número: ")
        a = parse_number(raw_a)

        raw_b = input("Digite o segundo número: ")
        b = parse_number(raw_b)

        op = input("Escolha a operação (+, -, *, /, //, %, **): ").strip()
        result = perform_operation(a, b, op)
    except ValueError as e:
        print(f"Entrada inválida: {e}")
        return
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        return

    print("Resultado:")
    print(result)


if __name__ == "__main__":
    main()