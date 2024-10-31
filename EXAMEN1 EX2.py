
correct = "secure123"
code = str(input("Entrez le mot de passe:"))
if code == correct:
    print("Accès accordé.")
while code!= correct:
    print("Accès refusé.")
    code = str(input("Entrez le mot de passe:"))
if code == correct:
    print("Accès accordé.")    