
n = int(input("Entrez un nombre entier positif:"))


somme = 0
if n < 0:
    print("Error.")
else:
    for i in range(1, n + 1):
        somme += i
        print("La somme de tous les nombres de 1 à", n, "est", somme)
