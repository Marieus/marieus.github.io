
from copy import deepcopy
from random import shuffle

alphabet = []

for nombre in range(97,123):
    alphabet.append(chr(nombre))

for nombre in range(65,90):
    alphabet.append(chr(nombre))

clef = deepcopy(alphabet)
shuffle(clef)

message = input("Saisir votre message : ")
chiffrage = str ()

for lettre in message:
    chiffrage += clef[ord(lettre)-97]

question = int(input('Voir la clé ? 1=oui 0=non'))
if question == 1:
    print(clef)
    
print(chiffrage)


input('Appuyez sur ENTREE pour fermer cette fenêtre')