
import logging
from datetime import datetime

log_file = "programme.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def programme_principal():
    nom_fichier = "exemple.txt"
    try:
        logging.info("Démarrage du programme")
        logging.info(f"Création du fichier '{nom_fichier}'")
        with open(nom_fichier, "w") as fichier:
            fichier.write("Ceci est un fichier texte de démonstration.\n")
            fichier.write("Chaque action sera enregistrée dans un fichier de log.\n")

        logging.info(f"Lecture du fichier '{nom_fichier}'")
        with open(nom_fichier, "r") as fichier:
            contenu = fichier.readlines()
            for ligne in contenu:
                print(ligne.strip())

        logging.info("Simulation d'une opération critique")
        if datetime.now().second % 2 == 0:
            raise ValueError("Une erreur simulée s'est produite.")
    except FileNotFoundError as e:
        logging.error(f"Fichier introuvable : {e}")
        print(f"Erreur : le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {e}")
        print(f"Erreur : {e}")
    finally:
        logging.info("Fin du programme")
        print("\nProgramme terminé. Vérifiez le fichier de log pour plus de détails.")

programme_principal()
