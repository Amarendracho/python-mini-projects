
# Rules
# Password is strong if:
# Length ≥ 8
# Contains:
# at least one uppercase
# at least one lowercase
# at least one digit


def password_strength_check():

    password = input("Enter your password : \n").strip()

    if len(password) < 8:
        return "Password is weak (less than 8 characters)"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Strong password"
    else:
        return "Weak password"

print(password_strength_check())