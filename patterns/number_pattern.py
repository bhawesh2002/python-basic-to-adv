# python program to print number pattern

num = int(input("Enter a number: "))
print("0\n")
for i in range(0, num):
    for j in range(0, i+1):
        print(i + 1, end="")
        i = i + 1
    print("\n")
