

import random
TPL_Choix = ( "Pierre" , "Feuille" , "Ciseaux" )
DCT_Scores = { "Humain" : 0 , "Machine" : 0 , "Nul" : 0 }
def FNC_Choix ( ) :
    print ( )
    print ( "_____________________________________" )
    print ( )
    print ( "Nouvelle manche. A vous de jouer ... " )
    print ( "Choisisez entre  (Pierre, Feuille, Ciseaux ou Quitter le jeu ): " )
    print ( " - [P]ierre ; " )
    print ( " - [F]euille ;" )
    print ( " - [C]iseaux ;" )
    print ( " - [Q]uitter le jeu." )
    kchoix = input ( "Quel est votre choix ? " )
    if kchoix.lower ( ) == "p" : return "Pierre"
    if kchoix.lower ( ) == "f" : return "Feuille"
    if kchoix.lower ( ) == "c" : return "Ciseaux"
    if kchoix.lower ( ) == "q" : return "Quitter"
def FNC_Manche ( ) :

    Joueur = None
    while Joueur == None : Joueur = FNC_Choix ( )
    if Joueur == "Quitter" :
        DCT_Scores [ "Humain" ] = "Abandon" 
        DCT_Scores [ "Machine" ] = 5
        FNC_Terminer ( "Machine" )
        return
    machine = random.choice ( TPL_Choix )
    if Joueur == "Pierre" and machine == "Pierre" : kgagnant = "Nul"
    if Joueur == "Pierre" and machine == "Feuille" : kgagnant = "Machine"
    if Joueur == "Pierre" and machine == "Ciseaux" : kgagnant = "Humain"

    if Joueur == "Feuille" and machine == "Pierre" : kgagnant = "Humain"
    if Joueur == "Feuille" and machine == "Feuille" : kgagnant = "Nul"
    if Joueur == "Feuille" and machine == "Ciseaux" : kgagnant = "Machine"

    if Joueur == "Ciseaux" and machine == "Pierre" : kgagnant = "Machine"
    if Joueur == "Ciseaux" and machine == "Feuille" : kgagnant = "Humain"
    if Joueur == "Ciseaux" and machine == "Ciseaux" : kgagnant = "Nul"
    DCT_Scores [ kgagnant ] += 1
    FNC_Scores ( Joueur , machine , kgagnant )
def FNC_Scores ( Qhumain , Qmachine , Qgagnant ) :
    kmanches = DCT_Scores [ "Humain" ] + DCT_Scores [ "Machine" ] + DCT_Scores [ "Nul" ] 
    print ( )
    print ( f"Humain  : { Qhumain.upper ( ) } " )
    print ( f"Machine : { Qmachine.upper ( ) } " )
    print ( f"Vainqueur de la manche { kmanches } : { Qgagnant.upper ( ) }" )
    winner = ""
    if DCT_Scores [ "Humain" ] == 5 : winner = " BRAVO VOUS AVEZ GAGNÉ!"
    if DCT_Scores [ "Machine" ] == 5 : winner = "DOMMAGE, VOUS AVEZ PERDU!"
    if winner == "" :
        print ( DCT_Scores )
        print ( )
        input ( "appuyez sur ENTREE pour poursuivre ... " )
        FNC_Manche ( )
    else :
        FNC_Terminer ( winner )
def FNC_Terminer ( Q ) :
    print ( )
    print ( "____________________________________" )
    print ( )
    print ( "FIN DE PARTIE ! " )
    print ( )
    print ( "--------------" )
    print ( f"# { Q } #" )
    print ( "--------------" )
    print ( )
    print ( DCT_Scores )
    print ( )
    print ( "Au revoir et à bientot." )
print ( "Rappel des règles du jeu Pierre - Feuille - Ciseaux (ou Chifoumi)." )
print ( "La pierre casse les ciseaux : la pierre gagne." )
print ( "Les ciseaux coupent la feuille : les ciseaux gagnent." )
print ( "La feuille enveloppe la pierre : la feuille gagne." )
print ( )
print ( "Le premier qui marque 5 points gagne la partie" )
print ( "Bon jeu ..." )     
FNC_Manche ( )

