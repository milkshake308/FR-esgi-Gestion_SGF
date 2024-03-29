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
        nom_parent = os.path.realpath(chemin)
        if os.path.isfile(chemin_absolu):
            tableau.add_row(["FILE", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        elif os.path.isdir(chemin_absolu):
            tableau.add_row(["DIR", permissions, owner, groupe, taille, date_modif, nom, nom_parent])
        else:
            tableau.add_row(["SPECIAL", permissions, owner, groupe, taille, date_modif, nom, nom_parent])

    return tableau


def audit_tree(root_dir):

    tableau = PrettyTable()
    tableau.field_names = ["TYPE", "MASK", "UID", "GID", "SIZE", "LAST EDIT", "FILENAME", "PARENT DIRECTORY"]
    def recursion(tableau, root_dir):
        for nom in os.listdir(root_dir):
            chemin = os.path.join(root_dir, nom)
            if os.path.isdir(chemin):
                tableau.add_rows(lister_contenu_dossier(chemin).rows)
                recursion(tableau, chemin)
        return tableau

    recursion(tableau, root_dir)
    return tableau



# Fonction qui prend un tableau et le transforme en CSV à l'endroit indiqué
def table_to_csv(tableau, fichier_destination_csv):
    with open(fichier_destination_csv, 'w', newline='') as fichier_csv:
        fichier_csv.write(tableau.get_csv_string())



def audit_complet(repertoire_base, repertoire_dest):
    tableaux = []
    for nom_region in os.listdir(repertoire_base):
        chemin_region = os.path.join(repertoire_base, nom_region)
        if os.path.isdir(chemin_region):
            for nom_client in os.listdir(chemin_region):
                chemin_client = os.path.join(chemin_region, nom_client)
                if os.path.isdir(chemin_client):
                    table_to_csv(
                    tableau= audit_tree(chemin_client), 
                    fichier_destination_csv=repertoire_dest+nom_region+'_'+nom_client+'.csv'
                    )