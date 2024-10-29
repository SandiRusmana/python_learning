print ("="*35)
jumlah = int(input("masukan total harga : "))
print ("="*35)

diskon = 0
if jumlah >= 100000:
    diskon = 0.05 *jumlah
    total_harga = jumlah - diskon
    print("diskon yang di dapat\t:",diskon)
    print("total harga yang harus dibayar\t:",total_harga)
elif jumlah <= 100000:
    print("total harga :",jumlah)    