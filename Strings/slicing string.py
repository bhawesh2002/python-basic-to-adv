str = "Name is Jimmy"
print(str[1:8])
print(str[5:10])
print(str[:6])
print(str[6:])
print(str[1:-1])
print(str[1:-3])
print(str[::-1])
print("Name" not in str)
print("Jimmy" in str)
for i in str:
    print(i,end="")
i = 0
while (i< len(str)):
    print(str[i],end="")
    i+=1