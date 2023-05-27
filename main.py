import utils.function_os as function_os
from datetime import datetime
import utils.modification as modification
import utils.ftp as ftp
import shutil

ftp.test_ftp()

LOGS = []
VERBOSE = True
REPERTOIRE_CLIENTS = "demo/"


def log(task_name, text, timestamp=True):
    if timestamp:
        timestamp = datetime.now().strftime("%Y%m%d-%H:%S.%f")
    new_line = f"{timestamp}-\t{task_name}:\t\t{text}"
    LOGS.append(new_line)
    if VERBOSE:
        print(new_line)

def archive_list(list, destination_file):
    try:
        with open(destination_file, "w") as fichier:
            for element in list:
                fichier.write(str(element) + "\n")
    except IOError:
        if VERBOSE:
            print("Erreur : Impossible d'écrire dans le fichier", destination_file)

def main_process():
    # Création du repertoire de travail
    work_dir = "audit."+str(ftp.get_last_audit_version()+1)
    if VERBOSE:
        print("Repertoire de session de travail :", work_dir)
    modification.creer_repertoire(work_dir)

    #  Création d'un rapport d'audit du SFG
    log("AUDIT", "Création des rapports d'audit du SGF")
    function_os.audit_complet(REPERTOIRE_CLIENTS, work_dir+"/")
    log("AUDIT", "Rapports d'audit crées avec succès !")

    #  Archivage du repertoire client
    log("SAUV", "Archivage du répertoire client...")
    modification.copier(REPERTOIRE_CLIENTS, work_dir+"/"+REPERTOIRE_CLIENTS)
    log("SAUV", "Repertoire clients archivés avec succès !")

    #  Archivage des logs
    log("MAIN", "Archivage du journal d'activité...")
    archive_list(LOGS, work_dir+"/"+work_dir+".log")

    log("FTP", "Envoi de l'archive d'audit "+work_dir+" sur le FTP...")
    #  Sauvegarde dans FTP
    try:
       ftp.uploader_repertoire(work_dir, work_dir)
       log("FTP", "Archive "+work_dir+" envoyé avec succès !")
    except Exception as e:
       log("FTP", f"Erreur lors de la connexion ou de l'upload FTP : {str(e)}")

    log("MAIN", "Suppression du repertoire temporaire")
    modification.supprimer(work_dir, no_confirm=True)

main_process()