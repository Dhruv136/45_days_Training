password = input("Enter password: ")
print("password must be start in caps , include a special symbol and contain digits")
correct_password = "Secret@123"

if password == correct_password:
    print("Access granted")
else:
    print("Access denied. Wrong password.")