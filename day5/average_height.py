stu_height = input("input a list of student height").split()
sum = 0
for i in range(0, len(stu_height)):
    x = int(stu_height[i])
    sum += x
print(stu_height)
print(sum)
ave = int(sum / len(stu_height))
print(ave)


high_score = input("input a list of student scores").split()
