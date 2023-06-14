#   verifica se o numero é primo

num = int(input("Digite um valor inteiro para verificar se é um número primo: "))

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

if is_prime(num):
    print("primo")
else:
    print("não primo")
        
    

    