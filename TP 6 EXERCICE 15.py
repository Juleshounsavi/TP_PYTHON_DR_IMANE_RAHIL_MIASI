
fichier_binaire = str(input("Entrer le nom du fichier binaire:"))
with open(fichier_binaire, "rb") as fichier:  
    contenu = fichier.read(16)  
    hexadecimaux = contenu.hex()  
    hex_formatte = " ".join(hexadecimaux[i:i+2] for i in range(0, len(hexadecimaux), 2))
    print("Les 16 premiers octets en hexadécimal sont:")
    print(hex_formatte)
