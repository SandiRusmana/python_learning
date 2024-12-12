kota = ["Cianjur","Bogor","Bandung","Surabaya","Garut"]
kota_yang_dicari = input("masukan kota yang ingin di tuju:")

i = 0
while i < len(kota):
    if kota[i].lower()==kota_yang_dicari.lower():
        print('ketemu di index',i)
        break
    print('bukan',kota[i])
    i += 1