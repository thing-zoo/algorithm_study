n = int(input())

for i in range(n):
    print(" "*(n-1-i)+" ".join("*"*(i+1)))