import os
from datetime import datetime
from prettytable import PrettyTable

def lister_contenu_dossier(chemin):
    tableau = PrettyTable()
    tableau.field_names = ["TYPE", "MASK", "OWNER", "GROUP", "SIZE (B)", "LAST EDIT", "FILENAME", "PARENT DIRECTORY"]

    for nom in os.listdir(chemin):
        chemin_absolu = os.path.join(chemin, nom)
        infos_fichier = os.stat(chemin_absolu)
        permissions = oct(infos_fichier.st_mode)[-3:]
        owner = infos_fichier.st_uid
        groupe = infos_fichier.st_gid
        taille = infos_fichier.st_size
        date_modif = datetime.fromtimestamp(infos_fichier.st_mtime)
        nom_parent = os.path.basename(chemin)
        if os.path.isfile(chemin_absolu):
            tableau.add_row(["FILE", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        elif os.path.isdir(chemin_absolu):
            tableau.add_row(["DIR", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        else:
            tableau.add_row(["SPECIAL", permissions, owner, groupe, taille, date_modif, nom, nom_parent])

    return tableau