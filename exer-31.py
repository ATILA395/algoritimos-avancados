# Função para verificar se as medidas formam um triângulo
def verifica_triangulo(A, B, C):
    if A < B + C and B < A + C and C < A + B:
        return "Formam um triângulo"
    else:
        return "Não formam um triângulo"

# Ler os valores A, B e C
A = float(input("Digite o valor do lado A: "))
B = float(input("Digite o valor do lado B: "))
C = float(input("Digite o valor do lado C: "))

# Verificar e imprimir o resultado
resultado = verifica_triangulo(A, B, C)
print(resultado)
