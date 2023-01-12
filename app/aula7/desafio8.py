# Ler preço e mostrar novo preço com desconto de 5%
valor: float = float(input('Digite o preço de um produto R$ '))
desconto = valor * 0.05
novoValor = valor - desconto
print('O preço que você digitou foi R$ {:.2f} aplicando o desconto de 5% ficou R$ {:.2f}'.format(valor, novoValor))
