import math

num = int(input('valor do angulo: '))

radianos = math.radians(num)

seno = math.sin(radianos)
tang = math.tan(radianos)
cos = math.cos(radianos)

seno_arredondado = round(seno, 2)
tang_arredondado = round(tang, 2)
cos_arredondado = round(cos, 2)

print('o valor de seno {} tengente {} e cosseno {} do angulo de {}graus'.format(
    seno_arredondado, tang_arredondado, cos_arredondado, num))
