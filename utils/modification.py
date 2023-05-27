import os
import shutil



def renommer_repertoire(chemin_repertoire, nouveau_nom):
    nouveau_chemin = os.path.join(os.path.dirname(chemin_repertoire), nouveau_nom)
    os.rename(chemin_repertoire, nouveau_chemin)


def creer_repertoire(chemin):
    os.makedirs(chemin)

def ajouter_repertoire(chemin_parent, nouveau_nom, repertoire=False):
    chemin_nouvel_element = os.path.join(chemin_parent, nouveau_nom)
    if repertoire:
        os.mkdir(chemin_nouvel_element)
    else:
        with open(chemin_nouvel_element, 'w') as fichier:
            
            pass

def copier(source, destination):
    if os.path.isdir(source):
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)


def deplacer(source, destination):
    shutil.move(source, destination)


def supprimer(chemin_repetoire, no_confirm=False):
    confirmation = "a"
    if not no_confirm:
        confirmation = input(f"Voulez-vous vraiment supprimer {chemin_repetoire}? (Y/N): ")
    if confirmation.lower() == "y" or no_confirm:
        if os.path.isdir(chemin_repetoire) :
            shutil.rmtree(chemin_repetoire)
        else:
            os.remove(chemin_repetoire)
        print(f"{chemin_repetoire} a été supprimé.")
    else:
        print("Suppression annulée.")

