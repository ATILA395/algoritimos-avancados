# Função para calcular o custo final ao consumidor
def calcular_custo_final(custo_fabrica):
    percentual_distribuidor = 28  # percentual do distribuidor
    percentual_impostos = 45      # percentual dos impostos

    # Cálculo do valor do distribuidor
    valor_distribuidor = custo_fabrica * (percentual_distribuidor / 100)
    
    # Cálculo do valor dos impostos
    valor_impostos = custo_fabrica * (percentual_impostos / 100)
    
    # Cálculo do custo final ao consumidor
    custo_final = custo_fabrica + valor_distribuidor + valor_impostos
    
    return custo_final

# Leitura do custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# Cálculo do custo final
custo_final = calcular_custo_final(custo_fabrica)

# Exibição do custo final
print(f"O custo final ao consumidor é: R${custo_final:.2f}")
