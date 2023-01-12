# Mostrar o dobro, triplo e raiz quadrada de um número
numero: int = int(input('Digite um número '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)
msg = 'Você digitou o número {}\n'.format(numero)
msg += 'O dobro dele é {}\n'.format(dobro)
msg += 'O triplo dele é {}\n'.format(triplo)
msg += 'A raiz quadrada dele é {:.3f}'.format(raiz)
print(msg)
