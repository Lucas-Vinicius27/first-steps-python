# conversão de temperatura ºC para ºF
celcius: float = float(input('Informe a temperatura em ºC: '))
fahrenheit = (celcius * 9/5) + 32
print('A temperatura de {:.2f}ºC corresponde a {:.2f}ºF!'.format(celcius, fahrenheit))
