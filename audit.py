from function_os import *
import sys

if len(sys.argv) < 3:
    print("Veuillez spécifier un chemin de dossier et un fichier de sortie")
    sys.exit(1)


table_to_csv(
        tableau= audit_tree(sys.argv[1]), 
        fichier_destination_csv=sys.argv[2]
        )