MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"

ValidPassword = False

while not ValidPassword:
    LOW_CHAR = 0
    UPP_CHAR = 0
    DIGIT = 0
    SPE_CHAR = 0
    Password = input("""
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
1 or more uppercase characters
1 or more lowercase characters
1 or more numbers
and 1 or more special characters:	!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|
""")
    for character in Password:
        if character.islower():
            LOW_CHAR = LOW_CHAR + 1
        elif character.isupper():
            UPP_CHAR = UPP_CHAR + 1
        elif character.isdigit():
            DIGIT = DIGIT + 1
        elif character in SPECIAL_CHARS:
            SPE_CHAR = SPE_CHAR + 1

    PasswordLength = UPP_CHAR + LOW_CHAR + DIGIT + SPE_CHAR
    if PasswordLength < 5 or PasswordLength > 15:
        print("Invalid Password. Password length must be between 5 to 15.")
    elif LOW_CHAR < 1:
        print("Invalid Password. Must have at least 1 lowercase character.")
    elif UPP_CHAR < 1:
        print("Invalid Password. Must have at least 1 uppercase character.")
    elif DIGIT < 1:
        print("Invalid Password. Must have at least 1 number.")
    elif SPE_CHAR < 1:
        print("Invalid Password. Must have at least 1 special character.")
    else:
        ValidPassword = True
        print("Your {} character password is valid: {}".format(str(PasswordLength), Password))