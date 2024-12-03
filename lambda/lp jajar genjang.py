def data():
    print("="*25)
    print("luas jajar genjang")
    print("="*25)

    alas = int(input("masukan nilai alas\t:"))
    tinggi = int(input("masukan nilai tinggi\t:"))

    luas = lambda: alas * tinggi
    print("hasil\t\t\t:",luas())
data()