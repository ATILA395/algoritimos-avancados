# Função para calcular o salário total
def calcular_salario_total(salario_fixo, vendas):
    if vendas <= 1500:
        comissao = vendas * 0.03
    else:
        comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05)
    
    salario_total = salario_fixo + comissao
    return salario_total

# Leitura de dados
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
vendas = float(input("Digite o valor total das vendas: R$ "))

# Cálculo do salário total
salario_total = calcular_salario_total(salario_fixo, vendas)

# Exibindo o resultado
print(f"O salário total do vendedor é: R$ {salario_total:.2f}")
