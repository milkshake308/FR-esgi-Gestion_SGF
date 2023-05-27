import os
from datetime import datetime
from prettytable import PrettyTable

def lister_contenu_dossier(chemin):
    tableau = PrettyTable()
    tableau.field_names = ["Type", "Permission", "Owner", "GROUPE", "TAILLE", "Datetime modif", "Nom", "RÃ©pertoire Parents"]

    for dossier_racine, sous_dossiers, fichiers in os.walk(chemin):
        for nom in fichiers:
            chemin_absolu = os.path.join(dossier_racine, nom)
            infos_fichier = os.stat(chemin_absolu)
            permissions = oct(infos_fichier.st_mode)[-3:]
            owner = infos_fichier.st_uid
            groupe = infos_fichier.st_gid
            taille = infos_fichier.st_size
            date_modif = datetime.fromtimestamp(infos_fichier.st_mtime)
            nom_parent = os.path.basename(dossier_racine)

            tableau.add_row(["Fichier", permissions, owner, groupe, taille, date_modif, nom, nom_parent])

        for nom in sous_dossiers:
            chemin_absolu = os.path.join(dossier_racine, nom)
            infos_dossier = os.stat(chemin_absolu)
            permissions = oct(infos_dossier.st_mode)[-3:]
            owner = infos_dossier.st_uid
            groupe = infos_dossier.st_gid
            taille = infos_dossier.st_size
            date_modif = datetime.fromtimestamp(infos_dossier.st_mtime)
            nom_parent = os.path.basename(dossier_racine)

            tableau.add_row(["Dossier", permissions, owner, groupe, taille, date_modif, nom, nom_parent])

    return tableau