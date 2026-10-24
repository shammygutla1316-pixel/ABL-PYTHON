# Topics: strings, string methods, loops, Boolean variables and conditions.
password = input("Enter password: ")
has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_upper and has_lower and has_digit:
    print("Password meets the basic rules.")
else:
    print("Password does not meet the basic rules.")
    if len(password) < 8:
        print("- Use at least 8 characters.")
    if has_upper == False:
        print("- Include an uppercase letter.")
    if has_lower == False:
        print("- Include a lowercase letter.")
    if has_digit == False:
        print("- Include a digit.")
