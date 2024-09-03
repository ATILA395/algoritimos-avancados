# Função para calcular o peso ideal com base na altura e no sexo
def calcular_peso_ideal(altura, sexo):
    if sexo == "M":
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido! Digite M para masculino ou F para feminino.")
    return peso_ideal

# Entrada de dados
nome = input("Digite o nome da pessoa: ")
altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").upper()

try:
    # Processamento
    peso_ideal = calcular_peso_ideal(altura, sexo)
    
    # Saída de dados
    print(f"O peso ideal para {nome} é {peso_ideal:.2f} kg.")
except ValueError as e:
    print(e)
