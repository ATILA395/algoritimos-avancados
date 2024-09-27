# Função para calcular o saldo atual
def calcular_saldo_atual(saldo, debito, credito):
    return saldo - debito + credito

# Leitura de dados
numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo: R$ "))
debito = float(input("Digite o débito: R$ "))
credito = float(input("Digite o crédito: R$ "))

# Cálculo do saldo atual
saldo_atual = calcular_saldo_atual(saldo, debito, credito)

# Exibindo o saldo atual
print(f"Saldo atual: R$ {saldo_atual:.2f}")

# Verificando se o saldo é positivo ou negativo
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
