import re

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add an uppercase letter (A-Z)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add a lowercase letter (a-z)")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add a number (0-9)")

    if re.search(r'[!@#$%^&*(),.?]', password):
        score += 1
    else:
        feedback.append("Add a symbol like ! @ # $ %")

    return score, feedback


print("Password Strength Checker")
print("Type 'quit' to exit")
print("")

while True:
    password = input("Enter a password: ")

    if password.lower() == "quit":
        print("Goodbye!")
        break

    if password == "":
        print("Please enter a password.\n")
        continue

    score, feedback = check_password(password)

    if score <= 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print(f"Strength: {strength} ({score}/5)")

    if feedback:
        print("Tips to improve:")
        for tip in feedback:
            print("  -", tip)
    else:
        print("Great password! All 5 rules passed.")

    with open("results.txt", "a") as f:
        f.write(f"Password: {password} | {strength} ({score}/5)\n")

    print("")