#   !n fatorial

valor = int(input("Digite o valor inteiro e descubra o fatorial: "))

def calcula_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcula_fatorial(n - 1)

resultado = calcula_fatorial(valor)

print(resultado)

