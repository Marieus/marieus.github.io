from turtle import clear
from copy import deepcopy
from random import shuffle
import random
def vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code +=  chr((((ord(c[i]) - ord('A')) + (ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A')) 
            indice_cle =  (indice_cle + 1) % len(cle)
        else:
            msg_code +=  c[i]
    return msg_code
    
def decode_vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code +=  chr((((ord(c[i]) - ord('A')) - (ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A')) 
            indice_cle =  (indice_cle + 1) % len(cle)
        else:
            msg_code +=  c[i]
    return msg_code

choix = int(input('Entrez votre choix : \n   1 pour Chiffrer avec la méthode du code de Vigenere  \n   2 pour Dechiffrer avec la methode du code de Vigenere \n   3 pour Chiffrer avec la méthode de Substitution \n   4 pour jouer au Juste Prix \n   Votre choix :  '))

if choix == 1:
    print('Vous avez choisis de chiffrer grâce au code de Vigenere')
    message=input("Entrez un message en MAJUSCULE :")
    cle = input("Entrez une cle de chiffrement par substitution, cela doit être un mot en MAJUSCULE :")

    print("Voici le message chiffré : ",vigenere(message, cle))

if choix == 3:
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

if choix ==2:
    print('Vous avez choisis de dechiffrer grâce au code de Vigenere ')
    message_chiffre=input("Tapez votre message chiffré en MAJUSCULE :")
    cle = input("Entrez une cle de chiffrement par substitution, cela doit être un mot en MAJUSCULE : ")
    print("Message d'origine est : " ,decode_vigenere(message_chiffre, cle))
    
    
if choix ==4:
    number=random.randint (0,1000)
    number1 = int(input("Devinez un nombre : ")) 
    e = 1
    while number != number1: 
    
        if number < number1:
            print("C'est plus petit !")
            number1 = int(input("Essai : "))
    
        elif number > number1:
            print("C'est plus grand !")
            number1 = int(input("Essai : "))
        e=e+1
    else:
        print("Gagné ! Vous avez trouvé en", e, "essais" )

            
        



input('Appuyez sur ENTREE pour quitter')