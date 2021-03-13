n = int(input())
sum = 0
line = int(input())

for i in range(n):
    i = line%10
    line = line//10
    sum += i

print(sum)