file = open("D:\games\Account_Details.txt", "r")

# print(file.read())

print(file.readline())  # reads content in .txt line wise
print(file.readline())

file.close()

# print all content in .txt line by line

file1 = open("C:\\Users\Me\Downloads\sample.txt", "r")
#print(file1.read())

#line = file1.readline()

#while line!="":
   # print(line)
   # line = file1.readline()
#print(file1.readlines())

for line in file1.readlines():
    print(line)
file.close()
