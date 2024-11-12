print ("="*20)
print ("bilangan bulat")
print ("="*20)
a = 1
b = 2
c = 3
if a > b:
   a,b = b,a
if a > c:
   a,c = c,a
if b > c:
   b,c = c,b
a = int(input("masukan nilai a:"))
b = int(input("masukan nilai b:"))
c = int(input("masukan nilai c:"))

print (f"bilangan yang terurut:{a},{b},{c}")