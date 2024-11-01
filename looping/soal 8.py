jumlah = 0
for x in range(2,11,2):
    if x <10:
        print(x ,end=' + ')
    else:
        print(x ,end=' = ')
    jumlah = jumlah + x
print(jumlah)