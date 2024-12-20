
import re

def mot_de_passe_est_fort(mdp):
    if len(mdp) < 8:
        return False
    if not any(char.isupper() for char in mdp):
        return False
    if not any(char.islower() for char in mdp):
        return False
    if not any(char.isdigit() for char in mdp):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", mdp):
        return False
    return True
