from random import randint


def lance_de():
    """ Ne pas modifier. Fonction retournant la face d'un dé équilibré.
    """
    de = randint(1, 6)
    print(de, end=" ")
    return de


def score_des(cmpt1, cmpt5):
    """ Fonction retournant le score lié au nombre de 1 et au nombre de 5. cmpt1
    correspondant au nombre de 1 et cmpt5 au nombre de 5.
    Parameters:
        cmpt1 (int): nombre de 1
        cmpt5 (int): nombre de 5
    Returns:
        (int): score correspondant
    """
    return cmpt1*100+cmpt5*50  # à modifier


def lance_des(nbde):
    """ Fonction simulant le lancer de nbde dés et retournant le nombre de 1 et
    le nombre de 5. Utilise la fonction lance_de().
    Parameters:
        nbde (int): nombre de dés lancés
    Returns:
        (int, int): couple de nombre de 1 et nombre de 5 réalisés.
    """
    while(nbde <= 0):
        nbde += 5
    cmpt1, cmpt5 = 0, 0
    for i in range(nbde):
        de = lance_de()
        if(de == 1):
            cmpt1 += 1
        if(de == 5):
            cmpt5 += 1
    return cmpt1, cmpt5


def affichage_choix_continuer(score_tour, nbde):
    """ Fonction affichant le score du tour score_tour ainsi que le nombre
    de dés encore jouable et retournant le choix du joueur concernant sa
    volonté de continuer à lancer les dés.
    Parameters:
        score_tour (int): score du tour
        nbde (int): nombre de dés encore jouable
    Returns:
        (bool): False si le joueur décide d'arrêter, True sinon
    """
    while(nbde <= 0):
        nbde += 5
    if(nbde == 5):
        print("Score du tour",score_tour,"pts - Les dés sont relancés")
        return True
    else:
        print("Score du tour",score_tour,"pts - Relancer",nbde,"dés ? (o,n)")
        reponse = "a"
        while(reponse != "o" and reponse != "n"):
            reponse = input()
            if(reponse == "n"):
                return False
            elif(reponse == "o"):
                return True


def affichage_tout_perdu():
    """ Affiche que le score du tour est nul car il n'y a aucun 1 et 5.
    """
    print('Aucun 1 ou 5. Score de ce tour: 0')


def affichage_lancer(nbde):
    """ Affiche le nombre de dés lancer.
    """
    while(nbde <= 0):
        nbde += 5
    print("-- Lancer de", nbde, "dés --")


def tour():
    """ Ne pas modifier. Fonction principale d'un tour. Tant que la variable
    continuer est vraie, on lance les dés, on compte les 1 et les 5.
    Si il y en a, alors on demande si on veut continuer, on ajoute le score et
    on enlève les dés 1 et 5.
    Sinon, on sort (en mettant continuer à Faux et le score du tour à 0)
    """
    continuer = True  # Idem pour le booléen continuer
    nbde = 5  # Nb de dé au début de tour
    score_tour = 0  # Score en début de tour
    while continuer:
        affichage_lancer(nbde)
        cmpt1, cmpt5 = lance_des(nbde)
        score_lancer = score_des(cmpt1, cmpt5)
        if score_lancer != 0:
            score_tour += score_lancer
            nbde -= cmpt1 + cmpt5
            continuer = affichage_choix_continuer(score_tour, nbde)
        else:
            affichage_tout_perdu()
            continuer = False
            score_tour = 0
    return score_tour


""" Boucle principale du jeu. Tant que l'on est pas arrivé à 1000, on continue
 de jouer en incrémentant le numéro du tour et en ajoutant le score """
score1 = 0
winPoints1 = False
score2 = 0
winPoints2 = False
cmpt_tour = 0
print('Nom du joueur 1 :')
j1 = input()
print('Nom du joueur 2 :')
j2 = input()
print('Score à atteindre :')
scoreMax = int(input())

print("Début de la partie !", end="\n\n")
while score1 < scoreMax:
    cmpt_tour += 1
    print("TOUR", cmpt_tour, ": DEBUT DU TOUR. Score :", j1, score1,",",j2,score2)
    print('A ton tour,',j1)
    if(winPoints1 == True):
        score1 += tour()
    else:
        ptsTour = tour()
        if(ptsTour >= 500):
            winPoints1 = True
            score1 = ptsTour
        else:
            print('Nombre de points insuffisants. Merci de réessayer au prochain tour.')
    print('A ton tour,',j2)
    if(winPoints2 == True):
        score2 += tour()
    else:
        ptsTour = tour()
        if(ptsTour >= 500):
            winPoints2 = True
            score2 = ptsTour
    print("TOUR", cmpt_tour, ": FIN DU TOUR. Score :", j1, score1,",",j2,score2,"\n")
