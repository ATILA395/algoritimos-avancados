# Função principal para calcular o novo salário
def calcular_novo_salario():
    # Ler o salário atual
    salario_atual = float(input("Digite o salário atual do funcionário: "))
    
    # Ler o percentual de reajuste
    percentual_reajuste = float(input("Digite o percentual de reajuste: "))
    
    # Calcular o valor do reajuste
    reajuste = salario_atual * (percentual_reajuste / 100)
    
    # Calcular o novo salário
    novo_salario = salario_atual + reajuste
    
    # Escrever o valor do novo salário
    print(f"O novo salário é: R${novo_salario:.2f}")

# Chama a função para executar
calcular_novo_salario()
