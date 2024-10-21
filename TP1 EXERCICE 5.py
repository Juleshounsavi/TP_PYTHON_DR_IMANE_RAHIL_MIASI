
seq = str(input("Entrez la sequence ADN:"))    
if (seq[0]=="A") and (seq[1]=="T") and (seq[2]=="G"):
    if((seq[-1]=="A") and (seq[-2]=="A") and (seq[-3]=="T")) or \
      ((seq[-1]=="G") and (seq[-2]=="A") and (seq[-3]=="T")) or \
      ((seq[-1]=="A") and (seq[-2]=="G") and (seq[-3]=="T")):
        print("C'est un gène.")
else:
    print("Ce n'est pas un gène.")        
 
    
 
    
 
    
 
