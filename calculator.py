print("=" * 50)
print("          ADVANCED CALCULATOR")
print("=" * 50)

try:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Exponent")
    print("7. Floor Division")
    print("8. Average")
    print("9. Maximum")
    print("10. Minimum")

    choice = input("\nEnter choice: ")

    if choice == "1":
        answer = a + b

    elif choice == "2":
        answer = a - b

    elif choice == "3":
        answer = a * b

    elif choice == "4":
        if b == 0:
            print("❌ Cannot divide by zero.")
            exit()
        answer = a / b

    elif choice == "5":
        if b == 0:
            print("❌ Cannot divide by zero.")
            exit()
        answer = a % b

    elif choice == "6":
        answer = a ** b

    elif choice == "7":
        if b == 0:
            print("❌ Cannot divide by zero.")
            exit()
        answer = a // b

    elif choice == "8":
        answer = (a + b) / 2

    elif choice == "9":
        answer = max(a, b)

    elif choice == "10":
        answer = min(a, b)

    else:
        print("❌ Invalid choice.")
        exit()

    # Remove .0 if the answer is a whole number
    if answer.is_integer():
        answer = int(answer)

    print("\n✅ Answer:", answer)

except ValueError:
    print("❌ Please enter valid numbers.")
