import random

num = random.randint(1, 4)

if num == 1:
    num = 'julia'
if num == 2:
    num = 'vitor'
if num == 3:
    num = 'marcia'
if num == 4:
    num = 'pedro'

print('o ecolhido do professor foi {}'.format(num))
