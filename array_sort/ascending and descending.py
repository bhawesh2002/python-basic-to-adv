terms = int(input("Enter the number of terms: "))
num = []
print("Fill the array")

for i in range(0, terms):
    print("Enter the ", i + 1, " number")
    element = int(input())
    num.append(element)

temp = 0
print("In Descending")
for i in range(0, terms):
    for j in range(0, terms - 1):
        if(num[i] > num[j]):
            temp = num[i]
            num[i] = num[j]
            num[j] = temp

print(num)
print("In Descending")
for i in range(0, terms):
    for j in range(0, terms - 1):
        if(num[i] < num[j]):
            temp = num[j]
            num[j] = num[i]
            num[i] = temp
print(num)
