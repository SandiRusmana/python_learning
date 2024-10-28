# bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

# bulan.append('Muharram')

# print(bulan[2],bulan[9])

# bulan [7] = 'August'
# bulan [0] = 'January'

# for i,data in enumerate (bulan):
#     print('bulan ke-',i+1,'yaitu',data,)


nilai = []
jml = int(input('jumlah data yang di input'))

for i in range(jml):
    nilai.append(float(input(f'nilai ke-{i+1} : ')))

total = max =0
min = nilai[0]
for data in nilai:
    total += data
    if data > max:
        max = data
    
    if data < min:
        min = data

print(f'tampilkan total{total}')
print(f'tampilkan nilai {max}')
print(f'tampilkan nilai {min}')
