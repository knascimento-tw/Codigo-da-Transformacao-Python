

def operacoes_aritmeticas():
    print("\n=== Operações Aritméticas ===")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    diferenca = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Indefinida (divisão por zero)"
    resto = num1 % num2 if num2 != 0 else "Indefinido"

    print("\n Resultados:")
    print(f"Soma: {soma}")
    print(f"Subtração: {diferenca}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
    print(f"Resto: {resto}")
    print("="*40)


def maior_numero():
    print("\n=== Comparação de Números ===")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a > b:
        print(f"O número {a} é maior que {b}.")
    elif b > a:
        print(f"O número {b} é maior que {a}.")
    else:
        print("Os dois números são iguais.")
    print("="*40)


def classificacao_idade():
    print("\n=== Classificação por Idade ===")
    idade = int(input("Digite a idade: "))

    if idade < 12:
        categoria = "Criança"
    elif idade < 18:
        categoria = "Adolescente"
    elif idade < 60:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    print(f"A pessoa é classificada como: {categoria}")
    print("="*40)


def menu_operacoes():
    while True:
        print("\n=== MENU DE OPERAÇÕES ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            break

        if opcao in ["1", "2", "3", "4"]:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                print(f"Resultado: {n1 + n2}")
            elif opcao == "2":
                print(f"Resultado: {n1 - n2}")
            elif opcao == "3":
                print(f"Resultado: {n1 * n2}")
            elif opcao == "4":
                if n2 != 0:
                    print(f"Resultado: {n1 / n2}")
                else:
                    print("Erro: divisão por zero!")
        else:
            print("Opção inválida! Tente novamente.")


while True:
    print("\n===== CALCULADORA =====")
    print("1 - Operações aritméticas")
    print("2 - Comparar dois números")
    print("3 - Classificar idade")
    print("4 - Desafio Extra (Menu interativo de operações)")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        operacoes_aritmeticas()
    elif escolha == "2":
        maior_numero()
    elif escolha == "3":
        classificacao_idade()
    elif escolha == "4":
        menu_operacoes()
    elif escolha == "5":
        print("Encerrando o programa... Até logo! 👋")
        break
    else:
        print("Opção inválida! Tente novamente.")
