import random
from itertools import permutations

palavra = input('Escreve uma palavra até 10 letras: ').casefold()


if len(palavra) <= 10:
    lista=sorted(set(["".join(perm) for perm in permutations(palavra)]))
    print(random.choice(lista))

elif len(palavra) > 10:
    print('Não inventes. MENOS de 10 sff.')

while True:
    decisao = input("Queres outro anagrama com esta palavra? (sim/nao)").casefold()

    if decisao == "sim" or decisao == "s" or decisao == "y":
        print(random.choice(lista))
        continue

    else:
        print("Adeus")
        break
