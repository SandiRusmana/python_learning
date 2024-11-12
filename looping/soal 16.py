n = 5
for x in range (1, n+1):
    print(" " * (n-x) + "* " * x)
for x in range (n-1, 0, -1):
    print(" " * (n-x) + "* " * x)