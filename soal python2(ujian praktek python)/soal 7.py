print('='*25)
print('PROGRAM LINGKARAN')
print('='*25)

jari_jari = int(input("masukan nilai jari jari\t:"))
luas = int(input("masukan nilai luas\t:"))
keliling = int(input("masukan nilai keliling\t:"))
pilihPhi = int(input("Pilih antara 1/2: "))

if pilihPhi == 1:
    phi = 3.14
    print("Kamu memilih", phi, "\n")
else:
    phi = 22/7
    print("Kamu memilih", phi, "\n")

luas = phi * jari_jari * jari_jari
keliling = phi * 2 * jari_jari

print("Hasil luas:", luas)
print("Hasil keliling:", keliling)