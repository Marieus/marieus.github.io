from turtle import clear


message=input("Entrez un message en MAJUSCULE : ")
cle = input("Entrez une cle de chiffrement par substitution, cela doit être un mot en MAJUSCULE : ")

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

print("Voici le message chiffré : ",vigenere(message, cle))
message_chiffre=input("Tapez votre message chiffré en MAJUSCULE : ")
print("Message d'origine est : " ,decode_vigenere(message_chiffre, cle) , "la clé de chiffrement est : ", cle)

input('Appuyez sur ENTREE pour quitter')