import math

num = int(input('quadrado oposto: '))
num2 = int(input('cateto adjacente: '))

oposto = num**2
adjacente = num2 ** 2

hipotenusa = oposto + adjacente

print(math.sqrt(hipotenusa))
