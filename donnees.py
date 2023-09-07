"""
Module tp2_donnees: : Permet l'obtention des données, pour le réseau "mini"
ou le réseau "facebook".
IFT-1004 Hiver 2023
"""


def obtenir_couples_amis_mini():
    """
    Donne tous les couples d'amis pour les données "mini".

    Returns:
        list<tuple<int>>: les couples d'amis

    """
    return [
        (0, 1), (0, 2), (0, 3), (1, 4), (1, 6), (1, 7), (1, 9), (2, 3), (2, 6), (2, 8),
        (2, 9), (3, 8), (3, 9), (4, 6), (4, 7), (4, 8), (5, 9), (6, 8), (7, 8)
    ]


def obtenir_reseau(couples_amis):
    """
    Étant donnée la liste de couples d'amis, crée un réseau,
    c'est-à-dire une liste dont la valeur à l'index i
    est une liste énumérant les amis de l'usager i.

    Args:
        couples_amis (list<tuple<int>>): les couples d'amis

    Returns:
        list<list<int>>: le réseau

    """
    reseau = []
    for id_usager_1, id_usager_2 in couples_amis:
        id_superieur = max(id_usager_1, id_usager_2)
        while id_superieur >= len(reseau):
            reseau.append([])
        reseau[id_usager_1].append(id_usager_2)
        reseau[id_usager_2].append(id_usager_1)
    print(reseau)
    return reseau


def obtenir_reseau_mini():
    """
    Donne le réseau provenant des données "mini"

    Returns:
        list<list<int>>: le réseau "mini"

    """
    return obtenir_reseau(obtenir_couples_amis_mini())


def obtenir_liste_noms_mini():
    """
    Donne les noms des usagers des données "mini"

    Returns:
        list<string>: les noms des usagers

    """
    return ["Tremblay", "Gagnon", "Roy", "Cote", "Bouchard",
            "Gauthier", "Morin", "Lavoie", "Fortin", "Gagne"]


def obtenir_couples_amis_facebook():
    """
    Donne tous les couples d'amis pour les données "facebook".

    Important: une ligne du fichier au format "123 456" doit
    être convertie en un tuple d'entiers (123, 456). Vous pouvez utiliser
    "123 456".split(" ") et la fonction int.

    Returns:
        list<tuple<int>>: les couples d'amis

    """

    list_final = []
    fichier = open('facebook_reseau.txt', 'r')
    for line in fichier.readlines():
        list = line.split(' ')
        tuple = (int(list[0]), int(list[1]))
        list_final.append(tuple)

    return list_final





def obtenir_liste_noms_facebook():
    """
    Donne les noms des usagers des données "facebook"

    Important: une fois dans la liste, les noms ne doivent pas terminer par un
    retour de ligne. Lire une ligne d'un fichier pourrait retourner quelque chose
    comme "Fortier\n". Vous devez éliminer le \n, par exemple avec la méthode
    chaine.rstrip().

    Returns:
        list<string>: les noms des usagers

    """
    list_final = []
    fichier = open('facebook_noms.txt', 'r')
    for line in fichier.readlines():
        nom = line.rstrip()
        list_final.append(nom)



    return list_final



def obtenir_reseau_facebook():
    """
    Donne le réseau provenant des données "facebook"

    Returns:
        list<list<int>>: le réseau "facebook"

    """
    return obtenir_reseau(obtenir_couples_amis_facebook())


if __name__ == '__main__':
    couples_amis_facebook = obtenir_couples_amis_facebook()
    assert len(couples_amis_facebook) == 9890
    assert couples_amis_facebook[0] == (0, 1)
    assert couples_amis_facebook[-1] == (995, 997)

    liste_noms_facebook = obtenir_liste_noms_facebook()
    assert len(liste_noms_facebook) == 1000
    assert liste_noms_facebook[0] == "Tremblay"
    assert liste_noms_facebook[-1] == "McDuff"

    print('Test unitaires passés avec succès!')
