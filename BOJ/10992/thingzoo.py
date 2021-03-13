n = int(input())

for i in range(n):
    if n == 1 or i == 0:
        print(" "*(n-1)+"*")
    elif n > 1 and i == n-1:
        print("*"*(2*n-1))
    elif n > 2:
        print(" "*(n-i-1)+"*"+" "*(2*i-1)+"*")