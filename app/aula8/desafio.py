# import math
import random
from math import sqrt

num: int = int(input('Digite um número: '))
# raiz: float = math.sqrt(num)
raiz: float = sqrt(num)
print('A raiz de {} vale {}'.format(num, raiz))

num = random.random()
num1 = random.randint(1, 10)
print('Número aleatório entre 0 e 1 {}\nnúmero aletório entre 1 e 10 {}'.format(num, num1))
