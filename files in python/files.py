f = open("files in python/foo.txt","r") #Open a file in python
no_of_lines = 0
for i in f:
    print(f.readline(12))
    no_of_lines += 1

print("The no of lines in foo.txt are: ",no_of_lines )
