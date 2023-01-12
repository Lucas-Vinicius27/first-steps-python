# ler salario e fazer um aumento de 15%
salario: float = float(input('Digite o valor do salario '))
aumento = salario * 0.15
novoSalario = salario + aumento
msg = 'O salario era no valor de R$ {} '.format(salario)
msg += 'com um aumento de 15% ficou R$ {}'.format(novoSalario)
print(msg)
