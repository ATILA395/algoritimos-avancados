# Ler os valores de x e y
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

# Calcular z
z = (x + y) + 5

# Verificar as condições e definir a resposta
if z <= 0:
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"

# Exibir a resposta
print(resposta)
