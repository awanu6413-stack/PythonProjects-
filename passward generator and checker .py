import secrets
import string

# -------------------------------
# PASSWORD GENERATOR
# -------------------------------

def generate_password(length, use_numbers=True, use_symbols=True):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = "@#$%&*!?"

    characters = lowercase + uppercase

    if use_numbers:
        characters += numbers

    if use_symbols:
        characters += symbols

    # Make sure password contains required character types
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase)
    ]

    if use_numbers:
        password.append(secrets.choice(numbers))

    if use_symbols:
        password.append(secrets.choice(symbols))

    # Add remaining characters
    while len(password) < length:
        password.append(secrets.choice(characters))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# -------------------------------
# PASSWORD STRENGTH
# -------------------------------

def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "@#$%&*!?" for c in password):
        score += 1

    if score <= 2:
        return "🔴 WEAK"

    elif score <= 4:
        return "🟡 MEDIUM"

    else:
        return "🟢 STRONG"


# -------------------------------
# MAIN PROGRAM
# -------------------------------

while True:

    print("\n" + "=" * 45)
    print("        🔐 PASSWORD GENERATOR")
    print("=" * 45)

    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Generate Multiple Passwords")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------
    # GENERATE PASSWORD
    # --------------------------------

    if choice == "1":

        try:
            length = int(input("\nEnter password length: "))

            if length < 8:
                print("❌ Password must be at least 8 characters.")
                continue

            numbers = input("Include numbers? (y/n): ").lower()
            symbols = input("Include symbols? (y/n): ").lower()

            use_numbers = numbers == "y"
            use_symbols = symbols == "y"

            password = generate_password(
                length,
                use_numbers,
                use_symbols
            )

            print("\n" + "-" * 45)
            print("🔐 YOUR PASSWORD:")
            print(password)
            print("-" * 45)

            print("📊 Strength:", check_strength(password))

        except ValueError:
            print("❌ Please enter a valid number.")

    # --------------------------------
    # CHECK PASSWORD
    # --------------------------------

    elif choice == "2":

        password = input("\nEnter your password: ")

        strength = check_strength(password)

        print("\nPassword Strength:", strength)

    # --------------------------------
    # MULTIPLE PASSWORDS
    # --------------------------------

    elif choice == "3":

        try:
            length = int(input("\nPassword length: "))
            amount = int(input("How many passwords? "))

            if length < 8:
                print("❌ Password must be at least 8 characters.")
                continue

            if amount <= 0:
                print("❌ Number of passwords must be greater than 0.")
                continue

            print("\n🔐 GENERATED PASSWORDS")
            print("-" * 45)

            for i in range(amount):

                password = generate_password(
                    length,
                    True,
                    True
                )

                print(f"{i + 1}. {password}")

        except ValueError:
            print("❌ Please enter valid numbers.")

    # --------------------------------
    # EXIT
    # --------------------------------

    elif choice == "4":

        print("\n👋 Thank you for using Password Generator!")
        break

    else:

        print("❌ Invalid choice. Please select 1-4.")
