"""
  Pour un usager, détermine l'autre usager ayant le plus d'amis en commun sans être déjà son ami

  Args:
      id_usager (int): l'usager auquel on doit recommander un ami
      reseau (list<list<int>>): liste contenant la liste des amis pour chaque usager
      matrice_similarite (list<list<int>>): matrice indiquant le nombre d'amis communs entre deux usagers

  Returns:
      int: l'id de l'usager recommandé

  """
# VOTRE CODE ICI