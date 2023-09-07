"""
Programme principal et point d'entrée du TP2.
Pose diverses questions à l'utilisateur et appelle les fonctions appropriées.
IFT-1004 Hiver 2023
"""

import donnees
import reseau_identifiants
import reseau_noms

print("Bienvenue dans le programme de recommandation d'amis. ")


def choix_mode(question):
    """
    Fonction utilitaire pour demander un mode, avec validation de l'entrée

    Args:
        question (string): La question à poser à l'utilisateur

    Returns:
        int: Le mode choisi par l'utilisateurr

    """
    mode = input(question)
    while mode != "1" and mode != "2":
        print("Entrée invalide. Entrez 1 ou 2. ")
        mode = input(question)
    return int(mode)


# On demande le mode d'exécution du programme
id_ou_nom = choix_mode("Souhaitez-vous procéder par ID (1) ou par nom (2) ? ")
petit_ou_grand = choix_mode("Souhaitez-vous utiliser le réseau 'mini' (1) ou le réseau 'Facebook' (2) ? ")

# On charge le réseau et les noms
liste_noms = None
if petit_ou_grand == 1:
    reseau = donnees.obtenir_reseau_mini()
    if id_ou_nom == 2:
        liste_noms = donnees.obtenir_liste_noms_mini()
else:
    reseau = donnees.obtenir_reseau_facebook()
    if id_ou_nom == 2:
        liste_noms = donnees.obtenir_liste_noms_facebook()

# On calcule la matrice de similarité du réseau
nb_usagers = len(reseau)
matrice = reseau_identifiants.calculer_scores_similarite(reseau)

# Début de la boucle d'interaction avec l'utilisateur
fin_du_programme = False
while not fin_du_programme:
    print()

    # Boucle pour obtenir une entrée valide, par ID ou par nom
    usager_valide, usager = False, None
    while not usager_valide:
        if liste_noms is None:
            usager = input(
                "Entrer l'id de l'usager pour lequel vous voulez une recommandation (entre 0 et {}): ".format(
                    nb_usagers - 1))
            if usager.isnumeric():
                usager = int(usager)
                if 0 <= usager <= nb_usagers - 1:
                    usager_valide = True
                else:
                    print("L'id doit être entre 0 et {} inclusivement. ".format(nb_usagers - 1))
            else:
                print("L'id doit être un nombre entier. ")
        else:
            usager = input("Entrez le nom de l'usager pour lequel vous voulez une recommandation: ")
            usager = usager.strip()  # Enlève les espaces superflus au début et à la fin de la chaîne de caractères
            if reseau_noms.nom_existe(usager, liste_noms):
                usager_valide = True
            else:
                print("Ce nom n'existe pas. ")

    # On trouve la recommandation pour la personne
    if liste_noms is None:
        id_recommandation = reseau_identifiants.recommander(usager, reseau, matrice)
        print("Pour la personne {}, nous recommandons l'ami {}.".format(usager, id_recommandation))
    else:
        nom_recommandation = reseau_noms.recommander(usager, reseau, matrice, liste_noms)
        print("Pour {}, nous recommandons l'ami(e) {}.".format(usager, nom_recommandation))

    # On demande si on veut poursuivre
    encore = input("Souhaitez-vous une autre recommandation? ").lower()
    while encore != "oui" and encore != "non":
        print("Entrée invalide. Entrez oui ou non. ")
        encore = input("Souhaitez-vous une autre recommandation? ").lower()
    fin_du_programme = encore == "non"

print("\nAu revoir!")
