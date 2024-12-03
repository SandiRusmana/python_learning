def data():
    print("="*25)
    print("keliling belah ketupat")
    print("="*25)

    a = int(input("masukan nilai a\t:"))
    b = int(input("masukan nilai b\t:"))
    c = int(input("masukan nilai c\t:"))
    d = int(input("masukan nilai d\t:"))
    
    keliling = lambda: a + b + c + d
    print("hasil\t\t:",keliling())
data()