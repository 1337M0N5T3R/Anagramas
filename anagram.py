import random
from itertools import permutations

palavra = input('Escreve uma palavra até 10 letras: ')

if len(palavra) <= 10:
    lista=sorted(set(["".join(perm) for perm in permutations(palavra)]))
    print(random.choice(lista))

elif len(palavra) > 10:
    print('MemoryError')