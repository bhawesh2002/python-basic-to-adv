# python program to print fibonacci series upto n terms

terms = int(input("Enter number of terms:"))

first = 0  # first number of the series
second = 1  # second number of the series
sum = 0  # sum of the series

print("Fibonacci series:")
for i in range(1, terms+1):  # for loop to print the series
    print(sum, "+")
    sum = first + second
    first = second
    second = sum

print("=", sum)