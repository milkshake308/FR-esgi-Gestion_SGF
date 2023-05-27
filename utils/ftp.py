import ftplib
import config
import re
import os

def test_ftp():
    print('Test de connexion FTP...', end=' ')
    try:
        # Connexion au serveur FTP
        ftp = ftplib.FTP(config.HOST)
        ftp.login(config.USER, config.PASSWD)

        # Vérification de la connexion réussie
        if ftp.getwelcome():
            print("OK")
        else:
            print("ERREUR")
        ftp.quit()

    except ftplib.all_errors as e:
        print("Erreur lors de la connexion FTP :", str(e))
        raise ftplib.Error


def get_last_audit_version():
    
    try:
        ftp = ftplib.FTP(config.HOST)
        ftp.login(config.USER, config.PASSWD)
        fichiers_audit = []
        ftp.retrlines("NLST", lambda nom: fichiers_audit.append(nom) if nom.startswith("audit") else None)
        print("Fichiers d'audit présent dans le FTP :", fichiers_audit)
        # Recherche du fichier "audit" avec la version la plus élevée
        return max([int(re.findall(r'\d+', f)[0]) for f in fichiers_audit if re.findall(r'audit\.\d+', f)], default=None)

    except Exception as e:
        print("Une erreur est survenue lors de la récupération du dernier fichier d'audit !")
        return 0

def uploader_repertoire(chemin_local, chemin_distant):
    ftp = ftplib.FTP(config.HOST)
    ftp.login(config.USER, config.PASSWD)
    if os.path.isfile(chemin_local):
        with open(chemin_local, 'rb') as fichier:
            ftp.storbinary('STOR ' + chemin_distant, fichier)
    elif os.path.isdir(chemin_local):
        ftp.mkd(chemin_distant)  # Créer le répertoire distant s'il n'existe pas déjà
        ftp.cwd(chemin_distant)  # Changer de répertoire distant
        for nom in os.listdir(chemin_local):
            uploader_repertoire(os.path.join(chemin_local, nom), os.path.join(chemin_distant, nom))
        ftp.cwd("..")  # Revenir au répertoire parent distant



