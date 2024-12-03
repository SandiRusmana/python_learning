def data():
    print("="*25)
    print("keliling layang-layang")
    print("="*25)

    a = int(input("masukan nilai a\t\t\t:"))
    b = int(input("masukan nilai b\t\t\t:"))
    c = int(input("masukan nilai c\t\t\t:"))
    d = int(input("masukan nilai d\t\t\t:"))

    keliling = lambda : a + b + c + d
    print("hasil keliling layang layang\t:",keliling())
data()