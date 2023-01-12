# Ler valor em metros mostrar o valor em centimetros e milimetros
metros: float = float(input('Digite a quantidade de metros '))
centimetros = metros * 100
milimetros = metros * 1000
msg = 'Você digitou {} metros '.format(metros)
msg += 'que corresponde a {} centimetros '.format(centimetros)
msg += 'e {} milimetros'.format(milimetros)
print(msg)
