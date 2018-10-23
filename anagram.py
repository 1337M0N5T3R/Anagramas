import random
from itertools import permutations

palavra = input('Escreve uma palavra até 10 letras: ')

if len(palavra) <= 10:
    lista=sorted(set(["".join(perm) for perm in permutations(palavra)]))
    print(random.choice(lista))

elif len(palavra) > 10:
    print('Nope. MENOS de 10 sff.')

while True:
    decisao = input("Queres outro anagrama com esta palavra? (sim/nao)")
    decisao = decisao.casefold()

    if decisao == "sim" or decisao == "s" or decisao == "y":
        print(random.choice(lista))
        continue

    elif decisao != "sim" or decisao == "s" or decisao == "y":
        print("Adeus")
        break
