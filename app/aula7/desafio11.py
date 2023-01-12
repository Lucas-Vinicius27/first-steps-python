# aluguel de carro 60 reais por dia e 0,15 reais por km
km = float(input('Digite a quantidade de km rodados '))
dia = int(input('Digite a quantidade de dias alugados '))
total = 60 * dia + km * 0.15
print('O total a pagar é de R$ {:.2f}'.format(total))
