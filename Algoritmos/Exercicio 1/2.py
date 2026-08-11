print("2. Leia o nome e a idade de uma pessoa e exiba uma mensagem com essas informações")
print("-" * 50)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

def dados_pessoa(nome, idade):
    return nome, idade

dados = dados_pessoa(nome, idade)

print(f"Nome: {dados[0]}, Idade: {dados[1]}")