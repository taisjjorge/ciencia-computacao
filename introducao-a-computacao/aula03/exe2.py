#   Receba um número inteiro positivo na entrada e imprima os 
#   n primeiros números ímpares naturais. Para a saída

n = int(input("Digite o valor de n: "))

contador = 0
numero_impar = 1

while contador < n:
    print(numero_impar)
    numero_impar += 2
    contador += 1
    #   print(f'contador: {contador}; impar: {numero_impar}')
