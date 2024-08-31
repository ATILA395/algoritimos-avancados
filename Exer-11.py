# Função para calcular o salário final do vendedor
def calcular_salario_final(numero_carros, valor_vendas, salario_fixo, valor_por_carro):
    # Comissão fixa total
    comissao_fixa_total = numero_carros * valor_por_carro
    
    # Comissão percentual (5% do valor das vendas)
    comissao_percentual = valor_vendas * 0.05
    
    # Cálculo do salário final
    salario_final = salario_fixo + comissao_fixa_total + comissao_percentual
    
    return salario_final

# Leitura dos dados
numero_carros = int(input("Digite o número de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: R$ "))
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
valor_por_carro = float(input("Digite o valor recebido por carro vendido: R$ "))

# Cálculo do salário final
salario_final = calcular_salario_final(numero_carros, valor_vendas, salario_fixo, valor_por_carro)

# Exibição do salário final
print(f"O salário final do vendedor é: R${salario_final:.2f}")
