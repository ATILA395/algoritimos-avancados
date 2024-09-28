# Preços dos combustíveis
preco_alcool = 2.90
preco_gasolina = 3.30

# Ler o número de litros vendidos
litros = float(input("Digite o número de litros vendidos: "))

# Ler o tipo de combustível
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").strip().upper()

# Calcular o valor a ser pago
if tipo_combustivel == 'A':
    valor_pago = litros * preco_alcool
elif tipo_combustivel == 'G':
    valor_pago = litros * preco_gasolina
else:
    valor_pago = 0
    print("Tipo de combustível inválido.")

# Imprimir o valor a ser pago, se válido
if valor_pago > 0:
    print(f"O valor a ser pago é: R$ {valor_pago:.2f}")
