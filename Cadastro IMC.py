# define uma lista para guardar os cadastros
lista = []






# função pra calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)






# função de classificação
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"






# função de dados cadastrais
def cadastrar():
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = round(calcular_imc(peso, altura), 2)
    classificacao = classificar_imc(imc)

    usuario = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": imc,
        "classificacao": classificacao
    }

    lista.append(usuario)
    print(f"{nome} cadastrado com sucesso!\n")






# função pra ver lista de cadastrados (senha: 2035)
def ver_lista():
    senha = input("Digite a senha de quatro dígitos: ")
    if senha != "3264":
        print("Senha incorreta.\n")
        return

    if not lista:
        print("Nenhum cadastro encontrado.\n")
        return

    else:
        lista_ordenada = lista

    for i, u in enumerate(lista_ordenada):
        print(f"{i} - {u['nome']} | {u['idade']} anos | IMC: {u['imc']} ({u['classificacao']})")
    print()






# função pra remover usuário da lista pelo nome
def remover():
    if not lista:
        print("Nenhum cadastro para remover.\n")
        return

    print("Cadastros:")
    for u in lista:
        print(f"- {u['nome']}")

    nome = input("Digite o nome do usuário a remover: ").strip().lower()

    for u in lista:
        if u["nome"].lower() == nome:
            lista.remove(u)
            print(f"{u['nome']} removido com sucesso.\n")
            return

    print("Nome não encontrado.\n")






# Menu principal
def menu():
    while True:
        print("=== MENU ===")
        print("1. Cadastrar Usuário")
        print("2. Ver Lista")
        print("3. Remover Cadastro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            ver_lista()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            confirmacao = input("Tem certeza que deseja sair? (S/N): ").strip().upper()
            if confirmacao == "S":
                print("Saindo do programa.")
                break
        else:
            print("Opção inválida.\n")






# Iniciar
menu()
