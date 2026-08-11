print("9. Crie uma função que receba dois números e retorne o maior deles.")
print("-" * 50)

def maior_numero():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num1 > num2:
        return num1
    else:
        return num2

print(f"O maior número é {maior_numero()}")