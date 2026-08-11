print("7. Leia 10 números e informe a soma e a média.")
print("-" * 50)

def soma_media_10_numeros():
    soma = 0
    for i in range(10):
        numero = float(input(f"Digite o {i+1}º número: "))
        soma += numero
    media = soma / 10
    return soma, media

soma, media = soma_media_10_numeros()

print(f"Soma: {soma}")
print(f"Média: {media}")