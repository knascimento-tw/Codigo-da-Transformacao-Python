# Programa: Dados de um aluno em um dicionário

# Criação do dicionário com as informações do aluno
aluno = {
    "nome": input("Digite o nome do aluno: "),
    "idade": int(input("Digite a idade do aluno: ")),
    "nota": float(input("Digite a nota do aluno: "))
}

# Exibição dos dados armazenados
print("\n--- Dados do Aluno ---")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
