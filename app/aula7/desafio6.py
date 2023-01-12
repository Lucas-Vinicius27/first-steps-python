# conversão real pra dólar => 1 dólar = 5,11 reais
real: float = float(input('Digite a quantidade de reais que você tem '))
print('Você tem R$ {:.2f} que corresponde a US$ {:.2f}'.format(real, real / 5.11))
