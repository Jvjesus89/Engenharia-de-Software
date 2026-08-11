print("5. Leia um número inteiro e mostre sua tabuada de 1 a 10.")
print("-" * 50)

numero = int(input("Digite um número: "))

def tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabuada(numero)
