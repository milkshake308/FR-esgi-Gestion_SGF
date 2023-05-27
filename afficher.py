from utils.function_os import *
import sys

if len(sys.argv) < 2:
    print("Veuillez spécifier un chemin de dossier.")
    sys.exit(1)

chemin_dossier = sys.argv[1]
resultat = lister_contenu_dossier(chemin_dossier)
print(resultat)