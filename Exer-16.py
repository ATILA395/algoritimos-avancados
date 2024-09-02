# Função para calcular o custo total das maçãs
def calcular_custo_total(num_macas):
    # Define os preços
    preco_unitario_barato = 1.00
    preco_unitario_caro = 1.30

    # Verifica o preço unitário com base no número de maçãs
    if num_macas >= 12:
        preco_unitario = preco_unitario_barato
    else:
        preco_unitario = preco_unitario_caro

    # Calcula o custo total
    custo_total = num_macas * preco_unitario
    return custo_total

# Função principal
def main():
    # Lê o número de maçãs compradas
    try:
        num_macas = int(input("Digite o número de maçãs compradas: "))
        
        if num_macas < 0:
            print("O número de maçãs não pode ser negativo.")
            return
        
        # Calcula o custo total
        custo_total = calcular_custo_total(num_macas)
        
        # Exibe o custo total
        print(f"O custo total da compra é: R$ {custo_total:.2f}")

    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Executa a função principal
if __name__ == "__main__":
    main()
