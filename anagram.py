import random
from itertools import permutations

palavra = input('Escreve uma palavra até 10 letras: ').casefold()

if palavra.isalpha() and len(palavra) <= 10 :
    lista=sorted(set(["".join(perm) for perm in permutations(palavra)]))
    print(random.choice(lista))

elif len(palavra) > 10:
    print('Não inventes. MENOS de 10 letras sff.')

else:
    print('Não inventes. Usa LETRAS sff.')

while palavra.isalpha() and len(palavra) <= 10:
    decisao = input("Queres outro anagrama com esta palavra? (sim/nao)").casefold()

    if decisao == "sim" or decisao == "s" or decisao == "y":
        print(random.choice(lista))
        continue

    else:
        print("Adeus")
        break
