

x = int(input("Entrez la coordonnée x du jeton:"))

y = int(input("Entrez la coordonnée y du jeton:"))



if (x > 15 and x < 45 or x > 60) and (x < 85 and y > 60):
    print("Dans la zone rouge.")

else:
    if (x > 25 and x < 50) and (y > 20 and y < 45):
        print("Dans une zone jaune.")
    else:

        if (x > 10 and x < 85) and (y > 10 and y < 55):
            print("Dans une zone bleu.")
        else:
            print("Dans une zone jaune.")
