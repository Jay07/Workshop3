lower = 10
upper = 100
LowNumber = input("Enter a number ({}-­‐{}): ".format(str(lower), str(upper)))
LowNumber = LowNumber.strip()
HighNumber = input("Enter a number ({}-­‐{}): ".format(str(LowNumber), str(upper)))
HighNumber = HighNumber.strip()
for i in range(int(LowNumber), int(HighNumber)):
    print("{} {}".format(i, chr(i)))
