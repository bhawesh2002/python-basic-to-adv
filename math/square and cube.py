import math

num = int(input("Enter a number:"))

sqRoot = math.sqrt(num)
sq = num*num
cube = num*num*num
fact = 1
print("The Square root of ", num, " is ", sqRoot)
print("The Cube of ", num, " is ", cube)
for i in range(2, num):
    if(num % i == 0):
        print(num, " is not a prime number")
        break
    if(i == num - 1):
        print(num, "is a prime number")

for i in range(1, num+1):
    fact *= i

print(num, "! = ", fact)
print("Prime factors of ", num, " are")
for i in range(1, num + 1):
    if(num % i == 0):
        print(i, " ", end="")
