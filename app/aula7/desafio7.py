# receber largura e altura em metros
# calcular a area e quantidade de tinta necessário para pintar a area
# 1 litro de tinta pinta uma area de 2m²
largura: float = float(input('Digite a largura em metros da parede '))
altura: float = float(input('Digite a altura em metros da parede '))
area = largura * altura
litroTinta = area / 2
print('Você precisa de {} litros de tinta para pintar a parede'.format(litroTinta))
