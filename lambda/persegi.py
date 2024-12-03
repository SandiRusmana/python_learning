def data():
    print("="*20)
    print("luas persegi")
    print("="*20)

    sisi = int(input("masukan nilai sisi\t:"))
    luas = lambda: sisi * sisi
    print("hasil\t:",luas())
data()