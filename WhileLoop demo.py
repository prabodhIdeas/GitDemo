var = 2

while var>2:
    if var == 4:
        var = var - 1
        continue
    if var == 2:
        break
    print(var)
    var = var - 1
print("while loop exec is completed")