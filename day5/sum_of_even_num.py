

sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        sum += i
print(sum)


sum2 = 0
for i in range(0, 101, 2):
    sum2 += i
print(sum2)

b = 0
a = 0
while b < 100:
    b += 2
    a += b
print(a)
