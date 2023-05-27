# esgi-Gestion_SGF

Ces outils peuvent être utilisé soit par le biais de script, soit par le biais d'un programme qui effectuera un ensemble de traitement pour répondre au cahier des charges

## Exemple d'usage des scripts
Afficher le repertoire (substitut de `ls -lah`) :
- `python afficher.py demo/`

Audit un repertoire complet (substitut de `tree` + `ls -lah`) :
- `python audit.py demo/ example_audit_tree_demo.csv`

Audit de tout les repertoire clients (substitut de `tree` + `ls -lah` pour chaque repertoire clients) :
- `python audit_complet.py`

## Usage du programme
- Renseigner les informations de connexion FTP dans config.py
- Run `python main.py` 