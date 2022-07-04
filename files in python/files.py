f = open("files in python/foo.txt","r") #Open a file in python
no_of_lines = 0
for line in f:
    print(line)
    no_of_lines += 1

print("The no of lines in foo.txt are: ",no_of_lines )
