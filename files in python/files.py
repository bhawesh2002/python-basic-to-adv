f = open("files in python/foo.txt","r") #Open a file in python
no_of_lines = 0
for line in f:
    print(line)
    no_of_lines += 1

print("The no of lines in foo.txt are: ",no_of_lines )
f.close()
file1 = open("info.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.write("Hello \n")
with open("steal.txt","w+") as steal:
    for line in file1:
        steal.write(line)
        
print("The information is stolen")
