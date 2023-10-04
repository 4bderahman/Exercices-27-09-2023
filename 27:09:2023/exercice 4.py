 
n = int(input("saisir le nbr de copies:")) 

if n <= 10:
    total = n * 0.30
else:
    if n > 10 and n <= 30:
        total = 10 * 0.30 + (n - 10) * 0.25
    else:
        total = 10 * 0.30 + 20 * 0.25 + (n - 30) * 0.20
print("le prix est:", total) 