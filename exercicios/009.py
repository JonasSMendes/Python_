n1 = int(input('numero da tabuada: '))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for list in list:

    tabuada = n1 * list

print('{} x {} : {:-^5} '.format(n1, list, tabuada))
