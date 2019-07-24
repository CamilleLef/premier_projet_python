
from random import randint
entier = randint(1,1000)

print("Bienvenue dans Le Juste Prix !")

for nb_essais in range (1,11):
    print("Il vous reste, ",11-nb_essais, " essai(s).")
    entree=int(input("Votre essai: "))
    if nb_essais!=10:
        if entree<entier:
            print("C'est plus!")
        elif entree>entier:
            print("C'est moins!")
        else:
            break

if entree!=entier:
    print("C'est perdu ! Le Juste Prix était:",entier)
else:
    print("C'est gagné!")

print("Merci d'avoir participé ! A bientôt dans Le Juste Prix!")
