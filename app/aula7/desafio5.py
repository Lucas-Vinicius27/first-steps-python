# tabuada
numero: int = int(input('Digite um número '))
multiplicador = 1
print('Tabuada do número {}'.format(numero))
while multiplicador <= 10:
    print('{} x {:2} = {}'.format(numero, multiplicador, numero * multiplicador))
    multiplicador += 1
