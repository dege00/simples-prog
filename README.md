# Simples Programa de Média

Este projeto calcula a média de duas notas digitadas pelo usuário em Python.

## Código

```python
while True:
    try:
        primeira_nota = float(input("Digite a primeira nota: "))
        segunda_nota = float(input("Digite a segunda nota: "))

        media = (primeira_nota + segunda_nota) / 2

        print(f"A média final é {media:.2f}")
        break  # sai do loop se deu tudo certo
    except ValueError:
        print("Erro: digite apenas números válidos!")
