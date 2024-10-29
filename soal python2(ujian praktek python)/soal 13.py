x = int(input('masukan nilai x\t:'))
y = int(input('masukan nilai y\t:'))
z = int(input('masukan nilai z\t:'))

if x >= y and x >= z :
    print('nilai terbesar adalah ',x)
elif y >= z and y >= x:
    print('nilai terbesar adalah',y)
else:
    print('nilai terbesar adalah',z)

if x<=y and x<=z:
    print('nilai terkecil adalah',x)
elif y<=x and y<=z:
    print('nilai terkecil adalah',y)
else :
    print('nilai terkecil adalah',z)