print("1. Leia dois números e exiba a soma, subtração, multiplicação e divisão.")
print("-" * 50)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def calcular_operacoes(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    return soma, subtracao, multiplicacao, divisao

operacoes = calcular_operacoes(num1, num2)

print("Soma: ", operacoes[0])
print("Subtração: ", operacoes[1])
print("Multiplicação: ", operacoes[2])
print("Divisão: ", operacoes[3])