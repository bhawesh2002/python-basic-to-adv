# python program to print number pattern

num = int(input("Enter a number: "))
print("0\n")
for i in range(0, num):
    a = i
    for j in range(0, i+1):
        print(a + 1, end="")
        a = a + 1
    print("\n")
