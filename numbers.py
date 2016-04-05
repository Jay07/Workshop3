ReadFile = open("numbers.txt", "r")
sum = 0
for line in ReadFile:
    number = int(line)
    sum = sum + number

sum = number1 + number2
print(sum)
ReadFile.close()