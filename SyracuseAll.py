debug=False
#n=int(input ("enter n= "))
MaxCompteur=-1
MaxN=-1
for n in range (1,100000,1):
    compteur=1
    nInit=n
    while (n!=1):
      if n%2==0:
          n=int(n/2)
          compteur=compteur+1
          if debug:
              print ("if - compteur=" , compteur)
      else:
          n=3*n+1
          compteur=compteur+1
          if debug:
              print ("else - compteur=" , compteur)
              
    if(compteur > MaxCompteur):
        MaxCompteur=compteur
        MaxN=nInit
        print (">MaxN:",nInit,">Compteur:", compteur)
    elif (compteur == MaxCompteur):
        print ("EQMaxN:",nInit,"EQCompteur:", compteur)
    if debug:
        print ("n=" , n, "compteur=" , compteur)
    
print ("MaxN:",MaxN,"MaxCompteur:", MaxCompteur)