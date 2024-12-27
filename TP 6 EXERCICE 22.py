
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info('Application démarrée')
logging.debug('Variable x initialisée')
logging.error('Erreur dans le calcul de y')
logging.info('Traitement des données terminé')
logging.error('Échec de la connexion à la base de données')

def afficher_erreurs():
    with open('app.log', 'r') as file:
        for line in file:
            if 'ERROR' in line:
                print(line.strip())

afficher_erreurs()
