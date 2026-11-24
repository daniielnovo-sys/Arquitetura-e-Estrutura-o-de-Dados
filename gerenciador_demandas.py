
# TECHFLOW CORE - GERENCIADOR DE DEMANDAS

demandas = []

STATUS_VALIDOS = [
    "Aberta",
    "Em andamento",
    "Concluída"
]

PRIORIDADES_VALIDAS = [
    "Baixa",
    "Média",
    "Alta",
    "Crítica"
]


def cadastrar_demanda():
    print("\n=== CADASTRAR DEMANDA ===")

    try:
        identificador = int(input("ID: "))
    except ValueError:
        print("Erro: informe um ID numérico.")
        return

    if identificador <= 0:
        print("Erro: o ID deve ser positivo.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("Erro: ID já cadastrado.")
            return

    titulo = input("Título: ").strip()
    solicitante = input("Solicitante: ").strip()
    prioridade = input("Prioridade: ").strip().capitalize()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()

    campos = [
        titulo,
        solicitante,
        prioridade,
        cep,
        cidade
    ]

    if any(not campo for campo in campos):
        print("Erro: todos os campos são obrigatórios.")
        return

    if prioridade not in PRIORIDADES_VALIDAS:
        print("Erro: prioridade inválida.")
        return

    nova_demanda = {
        "id": identificador,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Aberta"
    }

    demandas.append(nova_demanda)

    print("Demanda cadastrada com sucesso!")


def listar_demandas():
    print("\n=== LISTA DE DEMANDAS ===")

    if not demandas:
        print("Nenhuma demanda cadastrada.")
        return

    for demanda in demandas:
        print("-" * 35)

        for campo, valor in demanda.items():
            print(f"{campo.capitalize()}: {valor}")


def buscar_demanda():
    print("\n=== BUSCAR DEMANDA ===")

    try:
        identificador = int(input("ID da demanda: "))
    except ValueError:
        print("ID inválido.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("\nDemanda encontrada:")

            for campo, valor in demanda.items():
                print(f"{campo.capitalize()}: {valor}")

            return

    print("Demanda não encontrada.")


def atualizar_status():
    print("\n=== ATUALIZAR STATUS ===")

    try:
        identificador = int(input("ID da demanda: "))
    except ValueError:
        print("ID inválido.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            print("\nStatus disponíveis:")

            for status in STATUS_VALIDOS:
                print(status)

            novo_status = input(
                "Novo status: "
            ).strip().capitalize()

            if novo_status not in STATUS_VALIDOS:
                print("Status inválido.")
                return

            demanda["status"] = novo_status

            print("Status atualizado com sucesso!")
            return

    print("Demanda não encontrada.")


def excluir_demanda():
    print("\n=== EXCLUIR DEMANDA ===")

    try:
        identificador = int(input("ID da demanda: "))
    except ValueError:
        print("ID inválido.")
        return

    for demanda in demandas:
        if demanda["id"] == identificador:
            demandas.remove(demanda)

            print("Demanda excluída com sucesso!")
            return

    print("Demanda não encontrada.")


def menu():
    while True:
        print("\n===== TECHFLOW CORE =====")
        print("1 - Cadastrar demanda")
        print("2 - Listar demandas")
        print("3 - Buscar demanda")
        print("4 - Atualizar status")
        print("5 - Excluir demanda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_demanda()

        elif opcao == "2":
            listar_demandas()

        elif opcao == "3":
            buscar_demanda()

        elif opcao == "4":
            atualizar_status()

        elif opcao == "5":
            excluir_demanda()

        elif opcao == "0":
            print("Sistema encerrado!")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
