print("4. Leia a nota de um aluno e informe se ele foi aprovado (nota ≥ 7) ou reprovado.")
print("-" * 50)

nota = float(input("Digite a nota do aluno: "))

def verificar_aprovacao(nota):
    if nota >= 7:
        return "aprovado"
    else:
        return "reprovado"

verificacao = verificar_aprovacao(nota)

print(f"O aluno foi {verificacao}")
