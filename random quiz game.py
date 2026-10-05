import random

# ============================================================
#                 WELCOME SCREEN
# ============================================================

print("=" * 60)
print("              WELCOME TO MY QUIZ GAME")
print("              An Interesting Game to Play!")
print("=" * 60)

player = input("Do you want to play the game? (yes/no): ").strip().lower()

if player != "yes":
    print("Goodbye! 👋")
    quit()

name_player = input("Enter your name: ").strip()

print(f"\nWelcome {name_player}! 🎮")
print("Let's start the quiz!")
print("Questions and options will appear randomly.\n")


# ============================================================
#                 QUESTION DATABASE
# ============================================================

questions = [

    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Processing Unit",
            "Central Program Unit",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },

    {
        "question": "What does GPU stand for?",
        "options": [
            "Graphical Processing Unit",
            "General Processing Unit",
            "Graphic Program Utility",
            "General Program Unit"
        ],
        "answer": "Graphical Processing Unit"
    },

    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Memory",
            "Rapid Access Module",
            "Random Allocation Memory"
        ],
        "answer": "Random Access Memory"
    },

    {
        "question": "What does ROM stand for?",
        "options": [
            "Read Only Memory",
            "Random Only Memory",
            "Read Open Memory",
            "Run Only Module"
        ],
        "answer": "Read Only Memory"
    },

    {
        "question": "A mouse is which type of device?",
        "options": [
            "Input device",
            "Output device",
            "Storage device",
            "Processing device"
        ],
        "answer": "Input device"
    },

    {
        "question": "Which language is commonly used for web page structure?",
        "options": [
            "HTML",
            "Python",
            "SQL",
            "C++"
        ],
        "answer": "HTML"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "#",
            "//",
            "/* */",
            "<!-- -->"
        ],
        "answer": "#"
    },

    {
        "question": "Which data type stores True or False?",
        "options": [
            "Boolean",
            "String",
            "Integer",
            "Float"
        ],
        "answer": "Boolean"
    },

    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "def",
            "function",
            "define",
            "func"
        ],
        "answer": "def"
    },

    {
        "question": "Which symbol is used to create a list in Python?",
        "options": [
            "[]",
            "{}",
            "()",
            "<>"
        ],
        "answer": "[]"
    },

    {
        "question": "Which keyword is used for a loop in Python?",
        "options": [
            "for",
            "loop",
            "repeat",
            "iterate"
        ],
        "answer": "for"
    },

    {
        "question": "Which function is used to display output in Python?",
        "options": [
            "print()",
            "display()",
            "show()",
            "output()"
        ],
        "answer": "print()"
    },

    {
        "question": "Which function is used to get input from a user?",
        "options": [
            "input()",
            "get()",
            "read()",
            "user_input()"
        ],
        "answer": "input()"
    },

    {
        "question": "Which data type is used for decimal numbers?",
        "options": [
            "float",
            "integer",
            "string",
            "boolean"
        ],
        "answer": "float"
    },

    {
        "question": "Which data type is used for whole numbers?",
        "options": [
            "integer",
            "float",
            "string",
            "boolean"
        ],
        "answer": "integer"
    },

    {
        "question": "Which company developed Windows?",
        "options": [
            "Microsoft",
            "Apple",
            "Google",
            "IBM"
        ],
        "answer": "Microsoft"
    },

    {
        "question": "Which company developed Android?",
        "options": [
            "Google",
            "Microsoft",
            "Apple",
            "IBM"
        ],
        "answer": "Google"
    },

    {
        "question": "Which operating system is developed by Apple?",
        "options": [
            "macOS",
            "Windows",
            "Ubuntu",
            "Android"
        ],
        "answer": "macOS"
    },

    {
        "question": "What does HTML stand for?",
        "options": [
            "HyperText Markup Language",
            "HighText Machine Language",
            "Hyper Transfer Markup Language",
            "Home Tool Markup Language"
        ],
        "answer": "HyperText Markup Language"
    },

    {
        "question": "What does CSS stand for?",
        "options": [
            "Cascading Style Sheets",
            "Computer Style Sheets",
            "Creative Style System",
            "Colorful Style Sheets"
        ],
        "answer": "Cascading Style Sheets"
    },

    {
        "question": "What does SQL stand for?",
        "options": [
            "Structured Query Language",
            "Simple Query Language",
            "System Query Language",
            "Standard Question Language"
        ],
        "answer": "Structured Query Language"
    },

    {
        "question": "Which symbol is used for multiplication in Python?",
        "options": [
            "*",
            "x",
            "%",
            "#"
        ],
        "answer": "*"
    },

    {
        "question": "Which symbol is used for division in Python?",
        "options": [
            "/",
            "\\",
            ":",
            "%"
        ],
        "answer": "/"
    },

    {
        "question": "Which operator is used to find the remainder?",
        "options": [
            "%",
            "/",
            "//",
            "**"
        ],
        "answer": "%"
    },

    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": [
            "**",
            "^",
            "^^",
            "//"
        ],
        "answer": "**"
    },

    {
        "question": "What is the correct extension for a Python file?",
        "options": [
            ".py",
            ".python",
            ".pt",
            ".pyt"
        ],
        "answer": ".py"
    },

    {
        "question": "Which keyword is used to create a class in Python?",
        "options": [
            "class",
            "object",
            "define",
            "struct"
        ],
        "answer": "class"
    },

    {
        "question": "Which keyword is used to import a module?",
        "options": [
            "import",
            "include",
            "using",
            "require"
        ],
        "answer": "import"
    },

    {
        "question": "Which collection stores key-value pairs in Python?",
        "options": [
            "Dictionary",
            "List",
            "Tuple",
            "Set"
        ],
        "answer": "Dictionary"
    },

    {
        "question": "Which collection uses square brackets []?",
        "options": [
            "List",
            "Tuple",
            "Dictionary",
            "Set"
        ],
        "answer": "List"
    },

    {
        "question": "Which collection uses parentheses ()?",
        "options": [
            "Tuple",
            "List",
            "Set",
            "Dictionary"
        ],
        "answer": "Tuple"
    },

    {
        "question": "Which keyword stops a loop immediately?",
        "options": [
            "break",
            "stop",
            "exit",
            "end"
        ],
        "answer": "break"
    },

    {
        "question": "Which keyword skips the current loop iteration?",
        "options": [
            "continue",
            "skip",
            "pass",
            "next"
        ],
        "answer": "continue"
    },

    {
        "question": "Which keyword does nothing and acts as a placeholder?",
        "options": [
            "pass",
            "skip",
            "empty",
            "none"
        ],
        "answer": "pass"
    },

    {
        "question": "What is the output of 2 + 3 * 4?",
        "options": [
            "14",
            "20",
            "24",
            "10"
        ],
        "answer": "14"
    },

    {
        "question": "Which function returns the length of a list?",
        "options": [
            "len()",
            "length()",
            "size()",
            "count()"
        ],
        "answer": "len()"
    },

    {
        "question": "Which function returns the largest value?",
        "options": [
            "max()",
            "largest()",
            "high()",
            "top()"
        ],
        "answer": "max()"
    },

    {
        "question": "Which function returns the smallest value?",
        "options": [
            "min()",
            "smallest()",
            "low()",
            "bottom()"
        ],
        "answer": "min()"
    },

    {
        "question": "Which function rounds a number?",
        "options": [
            "round()",
            "round_number()",
            "decimal()",
            "approx()"
        ],
        "answer": "round()"
    },

    {
        "question": "Which keyword is used for conditional statements?",
        "options": [
            "if",
            "condition",
            "check",
            "when"
        ],
        "answer": "if"
    },

    {
        "question": "Which keyword is used when the if condition is false?",
        "options": [
            "else",
            "otherwise",
            "false",
            "no"
        ],
        "answer": "else"
    },

    {
        "question": "Which keyword checks another condition after if?",
        "options": [
            "elif",
            "elseif",
            "else_if",
            "ifelse"
        ],
        "answer": "elif"
    },

    {
        "question": "Which language is known for machine learning and data science?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "XML"
        ],
        "answer": "Python"
    },

    {
        "question": "What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automatic Information",
            "Advanced Internet",
            "Artificial Internet"
        ],
        "answer": "Artificial Intelligence"
    },

    {
        "question": "What does URL stand for?",
        "options": [
            "Uniform Resource Locator",
            "Universal Resource Link",
            "Uniform Reference Link",
            "Universal Routing Locator"
        ],
        "answer": "Uniform Resource Locator"
    },

    {
        "question": "What does IP stand for in networking?",
        "options": [
            "Internet Protocol",
            "Internet Program",
            "Internal Protocol",
            "Internet Process"
        ],
        "answer": "Internet Protocol"
    },

    {
        "question": "Which device connects multiple computers in a network?",
        "options": [
            "Switch",
            "Monitor",
            "Keyboard",
            "Printer"
        ],
        "answer": "Switch"
    },

    {
        "question": "Which device is commonly used to connect a home network to the internet?",
        "options": [
            "Router",
            "Keyboard",
            "Monitor",
            "Scanner"
        ],
        "answer": "Router"
    },

    {
        "question": "Which storage device generally uses flash memory?",
        "options": [
            "SSD",
            "DVD",
            "Floppy Disk",
            "Tape"
        ],
        "answer": "SSD"
    },

    {
        "question": "Which device is primarily used to display visual output?",
        "options": [
            "Monitor",
            "Keyboard",
            "Mouse",
            "Microphone"
        ],
        "answer": "Monitor"
    },

    {
        "question": "Which device is used to enter text into a computer?",
        "options": [
            "Keyboard",
            "Monitor",
            "Speaker",
            "Projector"
        ],
        "answer": "Keyboard"
    }

]


# ============================================================
#          SELECT RANDOM QUESTIONS
# ============================================================

# How many questions should the player answer?
NUMBER_OF_QUESTIONS = 10

# Make a copy so the original question database isn't changed
quiz_questions = questions.copy()

# Randomize all questions
random.shuffle(quiz_questions)

# Select only the required number
quiz_questions = quiz_questions[:NUMBER_OF_QUESTIONS]


# ============================================================
#                  QUIZ GAME
# ============================================================

score = 0
wrong_answers = []

for number, quiz in enumerate(quiz_questions, start=1):

    print("\n" + "-" * 60)
    print(f"Question {number}/{NUMBER_OF_QUESTIONS}")
    print("-" * 60)

    print(quiz["question"])
    print()

    # Make a copy of options
    options = quiz["options"].copy()

    # Randomize options
    random.shuffle(options)

    # Display options with A, B, C, D
    letters = ["A", "B", "C", "D"]

    for letter, option in zip(letters, options):
        print(f"{letter}. {option}")

    # Ask for answer
    while True:

        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in letters:
            break

        print("❌ Invalid answer!")
        print("Please enter A, B, C, or D.")

    # Convert A/B/C/D into index
    answer_index = letters.index(answer)

    # Get the selected option
    selected_answer = options[answer_index]

    # Check answer
    if selected_answer == quiz["answer"]:

        print("✅ Correct!")
        score += 1

    else:

        print("❌ Wrong!")
        print(f"Correct answer: {quiz['answer']}")

        wrong_answers.append({
            "question": quiz["question"],
            "your_answer": selected_answer,
            "correct_answer": quiz["answer"]
        })


# ============================================================
#                    FINAL RESULT
# ============================================================

total_questions = len(quiz_questions)

percentage = (score / total_questions) * 100

print("\n" + "=" * 60)
print("                    QUIZ RESULT")
print("=" * 60)

print(f"Player       : {name_player}")
print(f"Score        : {score}/{total_questions}")
print(f"Percentage   : {percentage:.2f}%")

# ============================================================
#                     GRADING
# ============================================================

if percentage == 100:

    print("Grade        : A+ 🏆")
    print("Excellent! Perfect score!")

elif percentage >= 80:

    print("Grade        : A 🥇")
    print("Excellent work!")

elif percentage >= 60:

    print("Grade        : B 🥈")
    print("Good job!")

elif percentage >= 40:

    print("Grade        : C 🥉")
    print("Keep practicing!")

else:

    print("Grade        : F 📚")
    print("You need more practice.")


# ============================================================
#                  WRONG ANSWERS
# ============================================================

if wrong_answers:

    print("\n" + "=" * 60)
    print("                  WRONG ANSWERS")
    print("=" * 60)

    for item in wrong_answers:

        print(f"\nQuestion: {item['question']}")
        print(f"Your answer: {item['your_answer']}")
        print(f"Correct answer: {item['correct_answer']}")

else:

    print("\n🎉 AMAZING!")
    print("You got every question correct!")


print("\n" + "=" * 60)
print("             THANKS FOR PLAYING! 🎮")
print("=" * 60)
