from function_os import *
import sys

BASE_DIR = "demo/"

def audit_complet(repertoire_base):
    tableaux = []
    for nom_region in os.listdir(repertoire_base):
        chemin_region = os.path.join(repertoire_base, nom_region)
        if os.path.isdir(chemin_region):
            for nom_client in os.listdir(chemin_region):
                chemin_client = os.path.join(chemin_region, nom_client)
                if os.path.isdir(chemin_client):
                    table_to_csv(
                    tableau= audit_tree(chemin_client), 
                    fichier_destination_csv=nom_region+'_'+nom_client+'.csv'
                    )

    

audit_complet(BASE_DIR)