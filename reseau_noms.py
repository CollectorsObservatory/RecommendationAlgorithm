"""
Module tp2_reseau_noms: Recherche dans un réseau d'amis à partir de noms
IFT-1004 Hiver 2023
"""

import reseau_identifiants


def nom_existe(nom_usager, liste_noms):
    """
    Détermine si un nom fait partie de la liste de noms

    Args:
        nom_usager (string): le nom à vérifier
        liste_noms (list<string>): la liste de noms

    Returns:
        bool: True si le nom est dans la liste, False sinon

    """
    #verifier si l element existe dans la liste
    if nom_usager in liste_noms:
        return nom_usager


def obtenir_id(nom_usager, liste_noms):
    """
    Donne l'id associé au nom de l'usager, qui est donné par l'index du nom
    dans la liste de noms. Si le nom n'est pas dans liste, on retourne None.

    Args:
        nom_usager (string): Nom à trouver dans la liste
        liste_noms (list<string>: Liste de noms dans laquelle chercher

    Returns:
        int: L'id associé au nom, ou None
    """
    #verifier si l element existe dans la liste
    if nom_usager in liste_noms:
        #retourner l indice de l element dand la liste
        return liste_noms.index(nom_usager)
    else:
        return None


def recommander(nom_usager, reseau, matrice_similarite, liste_noms):
    """
    Pour un usager, détermine l'autre usager ayant le plus d'amis en commun sans être déjà son ami,
    en procédant avec leurs noms.

    IMPORTANT: vous devez obligatoirement faire appel à tp2_reseau_identifiants.recommander

    Args:
        nom_usager (string): le nom de l'usager auquel on doit recommander un ami
        reseau (list<list<int>>): liste contenant la liste des amis pour chaque usager
        matrice_similarite (list<list<int>>): matrice indiquant le nombre d'amis communs entre deux usagers
        liste_noms (list<string>): la liste de noms

    Returns:
        string: le nom de l'usager recommandé

    """
    # VOTRE CODE ICI

    # recuperer l id de l usager ayant le plus d amis commun
    id = obtenir_id(nom_usager, liste_noms)
    id_usager_recommande = reseau_identifiants.recommander(id,reseau,matrice_similarite)
    #recuperer son nom a partir de l id
    nom_usager_recommande = liste_noms[id_usager_recommande]

    return nom_usager_recommande


if __name__ == "__main__":
    assert nom_existe("Louis", ["Louis", "Pascal"])
    assert nom_existe("Pascal", ["Louis", "Pascal"])
    assert not nom_existe("Lucien", ["Louis", "Pascal"])
    assert not nom_existe("Louis", [])

    assert obtenir_id("Louis", ["Louis", "Pascal"]) == 0
    assert obtenir_id("Pascal", ["Louis", "Pascal"]) == 1

    print('Test unitaires passés avec succès!')
