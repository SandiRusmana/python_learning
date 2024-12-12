nomor = int(input("perkalian:"))
while nomor <= 10:
    i = 1
    while i <= nomor:
        product = nomor * i
        print(nomor," * ",i," = ",product,"\n")
        i =i + 1
    print("\n")
    nomor = nomor + 1