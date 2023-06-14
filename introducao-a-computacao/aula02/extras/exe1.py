# Distância entre dois pontos -  plano cartesiano

import math

x1 = int(input("Digite o valor da coordenada x1: "))
y1 = int(input("Digite o valor da coordenada y1: "))
x2 = int(input("Digite o valor da coordenada x2: "))
y2 = int(input("Digite o valor da coordenada y2: "))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
    print("longe")
else:
    print("perto")

