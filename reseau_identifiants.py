"""
Module tp2_reseau_identifiants: : Recherche dans un réseau d'amis
    à partir d'identifiants (nombre unique)
IFT-1004 Hiver 2023
"""


def initialiser_matrice_carre(n):
    """
       Crée une matrice de taille nxn, initialisée avec des zéros et retourne la matrice.

       Args:
           n (int): dimension de la matrice nxn

       Returns:
           matrice (list<list<int>>): matrice initialisée
       """

    matrice = []
    for ligne in range(n):  # pour chacune des lignes dans n
        matrice.append([])  # créer une ligne (liste) et l'initialiser à 0
        for colonne in range(n):
            matrice[ligne].append(0)  # ajouter un 0 pour chaque n colonne
    return matrice


def trouver_nombre_elements_communs_entre_listes(liste1, liste2):
    """
       Donne le nombre d'éléments communs entre deux listes

       Args:
           liste1 (list<int>): Une des deux listes
           liste2 (list<int>): Une des deux listes

       Returns:
           int: Le nombre d'éléments communs entre les deux listes

       """
    # Conversion en set pour l'intersection et pour enlever la répetition
    liste_elements_en_commun = set(liste1) & set(liste2)
    return len(liste_elements_en_commun)


def calculer_scores_similarite(reseau):
    """
       Remplit la matrice de similarité. Dans cette matrice, l'élément en position i,j
       donne le nombre d'amis communs entre les utilisateurs i et j.
       Cette matrice devrait être symétrique, c'est-à-dire que i a autant d'amis
       communs avec j que j a d'amis communs avec i. Autrement dit, l'élément en position
       i,j est égal à l'élément en position j,i.

       Args:
           reseau (list<list<int>>): liste contenant la liste des amis pour chaque usager

       Returns:
           list<list<int>>: la matrice de similarité

       """
    utilisateurs = len(reseau)  # Pour dire que la longeur de la liste reseau est le nombre d'usager de ce reseau
    matrice_similarite = initialiser_matrice_carre(utilisateurs)  # initier la matrice
    for ligne in range(utilisateurs):
        for colone in range(ligne, utilisateurs):  # pour remplir la matrice
            amis_commun = trouver_nombre_elements_communs_entre_listes(reseau[ligne], reseau[colone])
            matrice_similarite[ligne][colone] = amis_commun
            matrice_similarite[colone][ligne] = amis_commun
            # pour que la matrice soit carree , ligne = colone
    return matrice_similarite


def recommander(id_usager, reseau, matrice_similarite):
    """
        Pour un usager, détermine l'autre usager ayant le plus d'amis en commun sans être déjà son ami

        Args:
            id_usager (int): l'usager auquel on doit recommander un ami
            reseau (list<list<int>>): liste contenant la liste des amis pour chaque usager
            matrice_similarite (list<list<int>>): matrice indiquant le nombre d'amis communs entre deux usagers

        Returns:
            int: l'id de l'usager recommandé

        """
    #initialisation de l utilisateur ainsi que ses amis
    utilisateurs = len(reseau)
    amis_usager = set(reseau[id_usager])

    #initialiser le maximum des amis et l id de l usager qu on cherche a trouver avec 0 pour s assurer de les changer au moins une fois ( minimum d amis commun est 0)
    max_amis_communs = -1
    id_usager_recommande = -1
    for identifiant in range(utilisateurs):
        if identifiant != id_usager and identifiant in amis_usager:
            amis_communs = matrice_similarite[id_usager][identifiant]

            if amis_communs >= max_amis_communs:
                max_amis_communs = amis_communs
                id_usager_recommande = identifiant




    return id_usager_recommande




if __name__ == "__main__":
    assert initialiser_matrice_carre(1) == [[0]]
    assert initialiser_matrice_carre(2) == [[0, 0], [0, 0]]
    assert initialiser_matrice_carre(10)[9] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert len(initialiser_matrice_carre(100)) == 100
    assert len(initialiser_matrice_carre(42)[20]) == 42

    assert trouver_nombre_elements_communs_entre_listes(['a', 'b', 'c'], ['b', 'a']) == 2
    assert trouver_nombre_elements_communs_entre_listes(['a', 'b', 'c'], ['d', 'e']) == 0
    assert trouver_nombre_elements_communs_entre_listes(['a', 'b', 'c'], []) == 0
    assert trouver_nombre_elements_communs_entre_listes(['a', 'b', 'c'], ['A', 'B', 'c', 'd']) == 1
    assert trouver_nombre_elements_communs_entre_listes(['a', 'b', 'c'], ['a', 'a', 'a']) == 1

    assert calculer_scores_similarite([[1, 2], [0], [0]]) == [[2, 0, 0], [0, 1, 1], [0, 1, 1]]
    assert calculer_scores_similarite([[1, 2], [0, 2], [0, 1]]) == [[2, 1, 1], [1, 2, 1], [1, 1, 2]]
    assert calculer_scores_similarite([[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]) == \
           [[3, 1, 1, 2], [1, 2, 2, 1], [1, 2, 2, 1], [2, 1, 1, 3]]
    assert calculer_scores_similarite([[], []]) == [[0, 0], [0, 0]]
    assert calculer_scores_similarite([[1], [0]]) == [[1, 0], [0, 1]]

    print('Test unitaires passés avec succès!')
