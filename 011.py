alt = int(input('digite a altura: '))
larg = int(input('digite a largura: '))

area = larg * alt

tinta = area / 2

print('com uma altura de {} e uma largura de {} \n temos {} metros quadrados \n você precisa de {:.0f} litros de tinta'
      .format(alt, larg, area, tinta))
