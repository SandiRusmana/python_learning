print("="*25)
print("luas permukaan balok")
print("="*25)

panjang = int(input("masukan nilai panjang\t:"))
lebar = int(input("masukan nilai lebar\t:"))
tinggi = int(input("masukan nilai tinggi\t:"))

luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("luas permukaan\t:",luas_permukaan)