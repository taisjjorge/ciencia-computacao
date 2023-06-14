#   Escreva um programa que receba um número inteiro na entrada,
#  calcule e imprima a soma dos dígitos deste número na saída

#  (Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão 
# inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor; 
# O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado,
#  ou seja, tudo que é maior ou igual ao divisor.

entrada = int(input("Digite o valor de entrada: "))

total = 0

while entrada > 0:
    digito = entrada % 10
    total += digito
    entrada //= 10

print(total)