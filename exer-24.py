
def calcular_salario_total(salario_fixo, valor_vendas):
    # Percentuais de comissão
    percentual_comissao_ate_1500 = 0.03
    percentual_comissao_acima_1500 = 0.05
    limite_comissao = 1500
    
 
    if valor_vendas <= limite_comissao:
        comissao = valor_vendas * percentual_comissao_ate_1500
    else:
        comissao = (limite_comissao * percentual_comissao_ate_1500) + ((valor_vendas - limite_comissao) * percentual_comissao_acima_1500)
    
  
    salario_total = salario_fixo + comissao
    return salario_total


salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
valor_vendas = float(input("Digite o valor total das vendas realizadas: R$ "))


salario_total = calcular_salario_total(salario_fixo, valor_vendas)
print(f"O salário total do vendedor é: R$ {salario_total:.2f}")
