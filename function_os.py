import os
from datetime import datetime
from prettytable import PrettyTable

def convertir_taille(taille):
    unite = ["B", "KB", "MB", "GB", "TB"]
    index = 0
    while taille >= 1024 and index < len(unite) - 1:
        taille /= 1024
        index += 1
    return f"{taille:,.2f} {unite[index]}"


def lister_contenu_dossier(chemin):
    tableau = PrettyTable()
    tableau.field_names = ["TYPE", "MASK", "UID", "GID", "SIZE", "LAST EDIT", "FILENAME", "PARENT DIRECTORY"]

    for nom in os.listdir(chemin):
        chemin_absolu = os.path.join(chemin, nom)
        infos_fichier = os.stat(chemin_absolu)
        permissions = oct(infos_fichier.st_mode)[-3:]
        owner = infos_fichier.st_uid
        groupe = infos_fichier.st_gid
        taille = convertir_taille(infos_fichier.st_size)
        date_modif = datetime.fromtimestamp(infos_fichier.st_mtime)
        nom_parent = os.path.basename(chemin)
        if os.path.isfile(chemin_absolu):
            tableau.add_row(["FILE", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        elif os.path.isdir(chemin_absolu):
            tableau.add_row(["DIR", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        else:
            tableau.add_row(["SPECIAL", permissions, owner, groupe, taille, date_modif, nom, nom_parent])

    return tableau