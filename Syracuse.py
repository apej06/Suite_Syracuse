debug=False
n=int(input ("enter n= "))
compteur=1
while (n!=1):
  if n%2==0:
      n=n/2
      compteur=compteur+1
      if debug:
          print ("if - compteur=" , compteur)
  else:
      n=3*n+1
      compteur=compteur+1
      if debug:
          print ("else - compteur=" , compteur)
      
if debug:
    print ("n=" , n)
print ("compteur=" , compteur)