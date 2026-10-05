print("=" * 50)
print("        STUDENT MARKSHEET SYSTEM")
print("=" * 50)

userName = input("Enter Your Name: ")

# Number of subjects
while True:
    try:
        num_subjects = int(input("Enter Number of Subjects: "))

        if num_subjects > 0:
            break
        else:
            print("Please enter at least 1 subject.")

    except ValueError:
        print("Please enter a valid number.")


subjects = []

# Taking subject information
for i in range(num_subjects):

    print(f"\n--- Subject {i + 1} ---")

    subject_name = input("Enter Subject Name: ")

    # Maximum marks
    while True:
        try:
            max_marks = float(input("Enter Maximum Marks: "))

            if max_marks > 0:
                break
            else:
                print("Maximum marks must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Obtained marks
    while True:
        try:
            obtained = float(input("Enter Obtained Marks: "))

            if 0 <= obtained <= max_marks:
                break
            else:
                print(
                    f"Obtained marks must be between 0 and {max_marks}."
                )

        except ValueError:
            print("Please enter a valid number.")

    subjects.append({
        "name": subject_name,
        "max": max_marks,
        "obtained": obtained
    })


# Calculate totals
total_marks = sum(subject["max"] for subject in subjects)
obtain_marks = sum(subject["obtained"] for subject in subjects)

percentage = (obtain_marks / total_marks) * 100


# Grade
if percentage >= 95:
    grade = "A+"
elif percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "Pass"
else:
    grade = "Fail"


# Find highest and lowest subject
highest_subject = max(subjects, key=lambda x: x["obtained"] / x["max"])
lowest_subject = min(subjects, key=lambda x: x["obtained"] / x["max"])


# Remarks
if percentage >= 90:
    remarks = "Excellent Performance!"
elif percentage >= 80:
    remarks = "Very Good Performance!"
elif percentage >= 70:
    remarks = "Good Performance!"
elif percentage >= 60:
    remarks = "Satisfactory Performance."
else:
    remarks = "Need Improvement."


# Display Marksheet
print("\n")
print("=" * 60)
print("                    MARKSHEET")
print("=" * 60)

print(f"Name: {userName}")
print(f"Number of Subjects: {num_subjects}")

print("-" * 60)
print(f"{'Subject':<20}{'Max Marks':<15}{'Obtained':<15}{'Percentage'}")
print("-" * 60)

for subject in subjects:

    subject_percentage = (
        subject["obtained"] / subject["max"]
    ) * 100

    print(
        f"{subject['name']:<20}"
        f"{subject['max']:<15.0f}"
        f"{subject['obtained']:<15.0f}"
        f"{subject_percentage:.2f}%"
    )

print("-" * 60)

print(f"Total Marks:      {total_marks:.0f}")
print(f"Obtained Marks:   {obtain_marks:.0f}")
print(f"Overall Percentage: {percentage:.2f}%")
print(f"Grade:            {grade}")

print("-" * 60)

print(f"Highest Subject: {highest_subject['name']}")
print(f"Lowest Subject:  {lowest_subject['name']}")
print(f"Remarks: {remarks}")

print("=" * 60)
