import math


# ============================================================
#                  RIGHT TRIANGLE CALCULATOR
# ============================================================

def number_input(message):
    """Get a positive number from the user."""

    while True:
        value = input(message).strip()

        if value == "":
            return None

        try:
            number = float(value)

            if number <= 0:
                print("❌ Please enter a number greater than 0.")
            else:
                return number

        except ValueError:
            print("❌ Invalid input. Please enter a number.")


# ============================================================
#                    FORMAT NUMBER
# ============================================================

def format_number(number):
    """Remove .0 from whole numbers."""

    if number.is_integer():
        return str(int(number))

    return f"{number:.4f}".rstrip("0").rstrip(".")


# ============================================================
#                CALCULATE TRIANGLE
# ============================================================

def calculate_triangle():

    print("\n" + "=" * 60)
    print("              ENTER TRIANGLE SIDES")
    print("=" * 60)

    print("\n💡 Leave ONE value empty to calculate it.\n")

    base = number_input("📏 Enter Base          : ")
    perpendicular = number_input("📏 Enter Perpendicular : ")
    hypotenuse = number_input("📏 Enter Hypotenuse    : ")

    # Count entered values
    entered = sum(
        value is not None
        for value in [base, perpendicular, hypotenuse]
    )

    # Need exactly two values
    if entered < 2:
        print("\n❌ Please enter at least TWO values.")
        return

    if entered == 2:

        # ----------------------------------------------------
        # Calculate Hypotenuse
        # ----------------------------------------------------

        if base is not None and perpendicular is not None:

            hypotenuse = math.hypot(base, perpendicular)

            print("\n✅ Hypotenuse calculated successfully.")

        # ----------------------------------------------------
        # Calculate Perpendicular
        # ----------------------------------------------------

        elif base is not None and hypotenuse is not None:

            if hypotenuse <= base:
                print(
                    "\n❌ Hypotenuse must be greater than Base."
                )
                return

            perpendicular = math.sqrt(
                hypotenuse ** 2 - base ** 2
            )

            print("\n✅ Perpendicular calculated successfully.")

        # ----------------------------------------------------
        # Calculate Base
        # ----------------------------------------------------

        elif perpendicular is not None and hypotenuse is not None:

            if hypotenuse <= perpendicular:
                print(
                    "\n❌ Hypotenuse must be greater "
                    "than Perpendicular."
                )
                return

            base = math.sqrt(
                hypotenuse ** 2 - perpendicular ** 2
            )

            print("\n✅ Base calculated successfully.")

    # ========================================================
    #              CHECK RIGHT TRIANGLE
    # ========================================================

    if not math.isclose(
        base ** 2 + perpendicular ** 2,
        hypotenuse ** 2,
        rel_tol=1e-9
    ):

        print("\n❌ These sides do NOT form a right triangle.")
        return

    # ========================================================
    #                    CALCULATIONS
    # ========================================================

    area = (base * perpendicular) / 2

    perimeter = base + perpendicular + hypotenuse

    # Angles
    angle_base = math.degrees(
        math.atan(base / perpendicular)
    )

    angle_perpendicular = 90 - angle_base

    angle_hypotenuse = 90

    # ========================================================
    #                    RESULTS
    # ========================================================

    print("\n" + "=" * 60)
    print("                 📊 RESULTS")
    print("=" * 60)

    print("\n📐 TRIANGLE SIDES")
    print("-" * 60)

    print(f"Base          : {format_number(base)}")
    print(f"Perpendicular : {format_number(perpendicular)}")
    print(f"Hypotenuse    : {format_number(hypotenuse)}")

    print("\n📊 MEASUREMENTS")
    print("-" * 60)

    print(f"Area          : {format_number(area)}")
    print(f"Perimeter     : {format_number(perimeter)}")

    print("\n📐 ANGLES")
    print("-" * 60)

    print(f"Angle 1       : {angle_base:.2f}°")
    print(f"Angle 2       : {angle_perpendicular:.2f}°")
    print(f"Angle 3       : {angle_hypotenuse:.2f}°")

    print("\n" + "=" * 60)
    print("          ✅ RIGHT-ANGLE TRIANGLE")
    print("=" * 60)


# ============================================================
#                         MAIN MENU
# ============================================================

while True:

    print("\n")
    print("=" * 60)
    print("          📐 RIGHT TRIANGLE CALCULATOR")
    print("=" * 60)

    print("1. Calculate Triangle")
    print("2. Exit")

    choice = input("\nSelect an option: ").strip()

    if choice == "1":

        calculate_triangle()

        input("\nPress ENTER to continue...")

    elif choice == "2":

        print("\n" + "=" * 60)
        print("👋 Thank you for using the calculator!")
        print("=" * 60)

        break

    else:

        print("\n❌ Invalid option. Please choose 1 or 2.")
