terms = int(input("Enter the number of terms: "))
num = []
print("Fill the array")

for i in range (0,terms):
    print("Enter the ", i + 1, " number")
    element = int(input())
    num.append(element)

even = []
odd = []

for i in range(0,terms):
    if(num[i] % 2 == 0):
        even.append(num[i])
    else:
        odd.append(num[i])

print("Even numbers: ",even)
print("Odd numbers: ",odd)
