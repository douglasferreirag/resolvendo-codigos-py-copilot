"""
Verificando Palíndromos 🔁

Descrição:
Recebe uma palavra ou frase do usuário e verifica se é um palíndromo.
Por padrão ignora maiúsculas/minúsculas e caracteres não alfanuméricos
(ex.: "A man, a plan, a canal: Panama" => palíndromo).

Uso:
$ python palindromo.py
Digite a palavra/frase: A man, a plan, a canal: Panama
Resultado: É um palíndromo!

Também é possível passar a string como argumento:
$ python palindromo.py "arara"
Resultado: É um palíndromo!
"""
from typing import Tuple
import sys
import re


def normalize(text: str) -> str:
    """Remove caracteres não alfanuméricos e converte para minúsculas."""
    return re.sub(r'[^a-z0-9]', '', text.lower())


def is_palindrome(text: str, *, ignore_non_alnum: bool = True, ignore_case: bool = True) -> bool:
    """
    Retorna True se `text` for palíndromo.
    Por padrão ignora caracteres não alfanuméricos e diferenciação de maiúsculas.
    """
    if ignore_non_alnum or ignore_case:
        normalized = normalize(text)
    else:
        normalized = text
    return normalized == normalized[::-1]


def check_and_format(text: str) -> Tuple[bool, str]:
    """Verifica palíndromo e retorna (resultado, string_normalizada_para_exibir)."""
    normalized = normalize(text)
    return is_palindrome(text), normalized


def main() -> None:
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = input("Digite a palavra ou frase: ").strip()

    if raw == "":
        print("Entrada vazia — por favor informe uma palavra ou frase.")
        return

    result, normalized = check_and_format(raw)
    if result:
        print("Resultado: É um palíndromo!")
    else:
        print("Resultado: Não é um palíndromo.")
    # Mostra a versão normalizada usada na verificação (opcional)
    print(f"(Versão normalizada usada na verificação: '{normalized}')")


if __name__ == "__main__":
    main()