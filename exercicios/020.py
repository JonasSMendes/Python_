import random

n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('quarto aluno: ')

list = [n1, n2, n3, n4]

valor_unicos = random.sample(list, 4)

valor_unicos = [str(valor) for valor in valor_unicos]

for valor in valor_unicos:
    print('#{}'.format(valor))
