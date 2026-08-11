print("10. Desafio: Faça um programa que leia 5 números e informe o maior e o menor valor.")
print("-" * 50)

def maior_menor_5_numeros():
    maior = float(input("Digite o primeiro número: "))
    menor = maior
    for i in range(4):
        numero = float(input(f"Digite o {i+2}º número: "))
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor

maior, menor = maior_menor_5_numeros()

print(f"Maior: {maior}")
print(f"Menor: {menor}")