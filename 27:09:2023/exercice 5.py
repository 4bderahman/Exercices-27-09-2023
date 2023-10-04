
n = int(input("Entrez un nombre entier positif:"))

factorielle = 1


if n < 0:
    print("error.")
else:
    
    for i in range(1, n + 1):
        factorielle *= i
   
    print(f"La factorielle de {n} est {factorielle}.")