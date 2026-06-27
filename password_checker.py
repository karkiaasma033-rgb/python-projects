def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short - use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add at least one UPPERCASE letter")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        feedback.append("Add a special character like !@#$%")

    if score == 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    print(f"\nStrength: {strength} ({score}/5)")
    for tip in feedback:
        print(f"  - {tip}")

while True:
    pwd = input("\nEnter password (or quit): ")
    if pwd == "quit":
        break
    check_password(pwd)
