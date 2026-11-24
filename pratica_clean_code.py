
# TECHFLOW CORE
# Sistema de cálculo de prioridade e prazo

PRAZO_CRITICO = 2
PRAZO_ALTO = 5
PRAZO_MEDIO = 10
PRAZO_BAIXO = 15


def calcular_prioridade(nivel_urgencia):
    """Calcula a prioridade e o prazo de atendimento."""

    if nivel_urgencia == 1:
        return "Crítica", PRAZO_CRITICO

    elif nivel_urgencia == 2:
        return "Alta", PRAZO_ALTO

    elif nivel_urgencia == 3:
        return "Média", PRAZO_MEDIO

    else:
        return "Baixa", PRAZO_BAIXO


def main():
    print("===== TECHFLOW CORE =====")

    while True:
        try:
            nivel = int(input("Digite a urgência (1 a 4): "))

            if 1 <= nivel <= 4:
                break

            print("Digite um número entre 1 e 4.")

        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    prioridade, prazo = calcular_prioridade(nivel)

    print("\n===== RESULTADO =====")
    print(f"Prioridade: {prioridade}")
    print(f"Prazo: {prazo} dias")


if __name__ == "__main__":
    main()
