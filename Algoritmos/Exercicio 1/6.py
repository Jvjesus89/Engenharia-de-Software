print("6. Leia um número N e calcule a soma dos números de 1 até N.")
print("-" * 50)

N = int(input("Digite um número: "))

def soma_ate_N(N):
    soma = 0
    for i in range(1, N + 1):
        soma += i
    return soma

soma = soma_ate_N(N)

print(f"A soma dos números de 1 até {N} é {soma}")