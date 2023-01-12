# Ordem de Precedência
# 1 -> () parenteses
# 2 -> ** pontência
# 3 -> * multiplicação, / divisão, // divisão inteira, % resto de divisão
# 4 -> + soma, - subtração
n1: int = int(input('Digite um número '))
n2: int = int(input('Digite outro número '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
msg = 'Você digitou os números {} e {}\n'.format(n1, n2)
msg += 'A soma é {}\n'.format(s)
msg += 'O produto é {}\n'.format(m)
msg += 'A divisão é {:.3f}\n'.format(d)
print(msg, end='>>>>\n')
print('A divisão inteira é {}\nA potência é {}'.format(di, e))
