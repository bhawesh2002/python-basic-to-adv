num = int(input("Enter a number: "))

a = 0

for i in range(1, num + 1):

    for j in range(1, i + 1):

        print(a + 1, end=" ")

        a += 1

    print("\n")
