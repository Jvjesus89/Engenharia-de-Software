print("3. Leia um número e informe se ele é positivo, negativo ou zero.")
print("-" * 50)

numero = float(input("Digite um número: "))

def verificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

verificacao = verificar_numero(numero)

print(f"O número é {verificacao}")