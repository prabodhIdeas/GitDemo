Itemsincart = 0

if Itemsincart!=2:
    pass
    #raise Exception("Cart is empty")

#assert(Itemsincart==2)

try:

    with open("C:\\Users\Me\Downloads\sample.txt", "r") as reader:
        reader.read()

except:
        print("it is ok if you did not find the file")

#to print the actual error what python showed

try:

    with open("C:\\Users\Me\Downloads\sample2.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
