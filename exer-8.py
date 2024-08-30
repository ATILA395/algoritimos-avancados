# Função principal
def calcular_percentuais():
    # Entrada de dados
    total_eleitores = int(input("Qual a quantidade total de eleitores? "))
    votos_brancos = int(input("Quantos votos brancos? "))
    votos_nulos = int(input("Quantos votos nulos? "))
    votos_validos = int(input("Quantos votos válidos? "))

    # Verificação de validade dos dados
    if total_eleitores <= 0:
        print("O número total de eleitores deve ser maior que zero.")
        return
    if votos_brancos < 0 or votos_nulos < 0 or votos_validos < 0:
        print("O número de votos não pode ser negativo.")
        return

    # Cálculo dos percentuais
    percentual_validos = (votos_validos / total_eleitores) * 100
    percentual_brancos = (votos_brancos / total_eleitores) * 100
    percentual_nulos = (votos_nulos / total_eleitores) * 100

    # Saída dos resultados
    print(f"Total de votos válidos: {percentual_validos:.2f}%")
    print(f"Total de votos em branco: {percentual_brancos:.2f}%")
    print(f"Total de votos nulos: {percentual_nulos:.2f}%")

# Chamada da função
calcular_percentuais()
