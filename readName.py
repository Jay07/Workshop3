ReadFile = open("name.txt", "r")
name = ReadFile.read().strip()
print("Your name is", name)
ReadFile.close()