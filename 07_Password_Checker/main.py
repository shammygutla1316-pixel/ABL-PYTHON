password = input("Enter password: ")
has_upper = has_lower = has_digit = False
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
    if not has_upper:
        print("- Include an uppercase letter.")
    if not has_lower:
        print("- Include a lowercase letter.")
    if not has_digit:
        print("- Include a digit.")
