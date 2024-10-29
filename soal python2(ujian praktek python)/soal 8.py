print ("="*35)
print ("PROGRAM TABUNG")
print ("="*35)

jari_jari = int(input("masukan nilai jari jari\t:"))
tinggi = int(input("masukan nilai keliling\t:"))
pilihPhi = int(input("Pilih antara 1/2: "))

if pilihPhi == 1:
    phi = 3.14
    print("Kamu memilih", phi, "\n")
else:
    phi = 22/7
    print("Kamu memilih", phi, "\n")

volume = 2 * phi * jari_jari * tinggi
luas_permukaan = 2 * phi * jari_jari * jari_jari + 2 * phi * jari_jari *tinggi

print("Hasil volume:", volume)
print("Hasil luas permukaan:", luas_permukaan)