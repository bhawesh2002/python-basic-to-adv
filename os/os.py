import os

print(os.getcwd())#print current working directory
print(os.listdir())#list the files and folders in current directory
os.mkdir('os_test')#create a new directory
print(os.listdir())#list the files and folders in current directory
os.rename('os_test', 'os_op_test')#rename a existing directory
