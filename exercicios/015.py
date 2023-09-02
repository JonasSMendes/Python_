n1 = float(input('quantos dias se ta com o carro? '))
n2 = float(input('quantos km o carro rodou? '))

dia = 60 * n1
km = 0.15 * n2

custo = int(dia + km)

print('você me deve {}R$'.format(custo))
