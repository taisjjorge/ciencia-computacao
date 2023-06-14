#   Escreva um programa que receba um número inteiro na entrada 
# e verifique se o número recebido possui ao menos um dígito
#  com um dígito adjacente igual a ele. Caso exista, imprima "sim"; 
# se não existir, imprima "não".

# exemplo:
# Digite um número inteiro: 12345; saída: não
# Digite um número inteiro: 1011; saída: sim

input = int(input("Digite um número inteiro: "))

def is_near_equal(input):
    format_number = str(input)

    for i in range(len(format_number) - 1):
        if format_number[i] == format_number[i + 1]:
            return True
    
    return False

if is_near_equal(input):
    print("sim")
else:
    print("não")


