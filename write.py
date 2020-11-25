with open("C:\\Users\Me\Downloads\sample.txt", "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open("C:\\Users\Me\Downloads\sample.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)



