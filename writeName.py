WriteFile = open("name.txt", "w")
Name = input("What is your name? ")
print(Name, file=WriteFile)
WriteFile.close()
