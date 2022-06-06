import math  #to use functions defined in math library

num = int(input("Enter a number:"))  #get the input

sqRoot = math.sqrt(num) #use sqrt function defined in math library
sq = num*num #store the square of number
cube = num*num*num #store the cube of number
fact = 1 #initialise factorial to 1
print("The Square root of ", num, " is ", sqRoot) #print the square root
print("The Cube of ", num, " is ", cube) #print the cube root
for i in range(2, num): #for loop
    if(num % i == 0): #check weather number is completely divisible 
        print(num, " is not a prime number")#if divisible by i print is prime
        break #break the loop if number is divisible by i
    if(i == num - 1):  #condition for prime number
        print(num, "is a prime number")

for i in range(1, num+1): #for loop to compute factorial
    fact *= i

print(num, "! = ", fact) #print factorial
print("Prime factors of ", num, " are")#print prime factorial
for i in range(1, num + 1):
    if(num % i == 0):
        print(i, " ", end="")


