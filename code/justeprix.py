import random #import du Module random, base de notre script

number=random.randint (0,1000) # On utilise le module pour nous générer un ENTIER aléatoire


number1 = int(input("Devinez un nombre : ")) #Le premier essai
e = 1 #On prépare le compteur des essais 
while number != number1: #Le jeu en lui même, qui s'éxécute tant que number est différent de number 1
    
    if number < number1:
        print("C'est plus petit !")
        number1 = int(input("Essai : "))
    
    elif number > number1:
        print("C'est plus grand !")
        number1 = int(input("Essai : "))
    e=e+1
    
else:
    print("Gagné ! Vous avez trouvé en", e, "essais" )