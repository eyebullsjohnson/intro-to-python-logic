password = input("please set a new password")

Special_character_check= "!" in password

if len(password) < 16 and len(password) > 5:
    print("password is corect lenth")
elif len(password) < 5:
    print("Password is too short")
else:
    print("password must be between 5 and 16 characters")

if Special_character_check:
    print("special character found")
else:
    print("this password needs an ! somewhere")