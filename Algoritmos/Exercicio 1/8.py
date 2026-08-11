print("8. Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.")
print("-" * 50)

def soma_ate_zero():
    soma = 0
    numero = 1
    while numero != 0:
        numero = float(input("Digite um número (digite 0 para sair): "))
        soma += numero
    return soma

soma = soma_ate_zero()

print(f"A soma dos números digitados é {soma}")