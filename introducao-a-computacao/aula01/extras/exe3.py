#   imprime digito da dezena

enter = int(input("Digite um número inteiro: "))

digit = (enter // 10) % 10

print(f"O dígito das dezenas é {digit}")
