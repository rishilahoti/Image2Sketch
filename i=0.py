n=5
for i in range(n):
    for j in range(n-i-1):
        print(chr(j+97), end="")
    print()