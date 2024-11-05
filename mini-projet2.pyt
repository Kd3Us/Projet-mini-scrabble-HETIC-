import random

def lire_dico(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        mots = f.read().splitlines()
    return mots

liste_mots = lire_dico('dictionnaire.txt')

def generer_lettres(liste_mots, nombre_mots):
    mots_choisis = random.sample(liste_mots, nombre_mots)
    lettres = ''.join(mots_choisis)
    lettres_uniques = ''.join(set(lettres))
    return mots_choisis, lettres_uniques

def jouer_manche(liste_mots, nombre_mots):
    mots_choisis, lettres = generer_lettres(liste_mots, nombre_mots)
    print(f"Lettres : {lettres}")
    
    points = 0
    mots_trouves = []
    
    while len(mots_trouves) < nombre_mots:
        mot = input("Entrez un mot ('Quit' pour passer la manche) : ")
        if mot == 'Quit':
            mots_non_trouves = [mot for mot in mots_choisis if mot not in mots_trouves]
            if mots_non_trouves:
                print(f"Les mots à trouver étaient : {', '.join(mots_non_trouves)}")
            break
        if mot in mots_choisis and mot not in mots_trouves:
            mots_trouves.append(mot)
            points += 1
            print(f"Mot trouvé : {mot} (+1)")
        else:
            print("Raté ! Réessaye encore !")

    return points

def jouer_jeu():
    score_total = 0
    manches_gagnes = 0
    nombre_mots = 3

    for manche in range(1, 4):
        print(f"\n| Manche {manche} |")
        points = jouer_manche(liste_mots, nombre_mots)
        score_total += points
        print(f"Points de la manche : {points}")

        if points == nombre_mots:
            manches_gagnes += 1
            nombre_mots += 1
            print("Tu as gagné cette manche !")
        else:
            print("Tu as raté cette manche.")

    print(f"\nScore total : {score_total} points")
    print(f"Nombres total de manches gagnées : {manches_gagnes}")

if __name__ == "__main__":
    jouer_jeu()