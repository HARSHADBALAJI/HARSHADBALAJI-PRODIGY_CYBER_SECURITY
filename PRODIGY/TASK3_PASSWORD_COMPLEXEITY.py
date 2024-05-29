Hdef check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper and has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)

    if strength == 0:
        print("Very weak password")
    elif strength == 1:
        print("Weak password")
    elif strength == 2:
        print("Moderate password")
    elif strength == 3:
        print("Strong password")
    else:
        print("Very strong password")

if __name__ == "__main__":
    main()