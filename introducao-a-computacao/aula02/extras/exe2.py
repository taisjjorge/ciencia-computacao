#   Equaçao 2o grau
import math

a = float(input("Digite o valor para a: "))
b = float(input("Digite o valor para b: "))
c = float(input("Digite o valor c: "))

def funcao():
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

        if delta == 0:
            print("a raiz dupla desta equação é", raiz1)
        else:
            if raiz2 > raiz1:
                print(f"as raízes da equação são {raiz1} e {raiz2}")
            else:
                print(f"as raízes da equação são {raiz2} e {raiz1}")

funcao()
