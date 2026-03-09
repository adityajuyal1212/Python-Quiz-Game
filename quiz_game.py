# Python Quiz Game

questions = (("Q1. What is the output of type([]) in Python?"),
            ("Q2. Which keyword is used to define a function in Python?"),
            ("Q3. What does the len() function return?"),
            ("Q4. Which of the following is an immutable data type in Python?"),
            ("Q5. What will print(2 ** 3) output?"))

options = (("A. <class 'tuple'>", "B. <class 'list'>", "C. <class 'array'>", "D. <class 'dict'>"),
            ("A. function", "B. define", "C. def", "D. fun"),
            ("A. The largest element in a sequence", "B. The memory size of an object", "C. The number of items in an object", "D. The last index of a sequence"),
            ("A. List", "B) Dictionary", "C) Set", "D) Tuple "),
            ("A. 6", "B. 8 ", "C. 9", "D. 23"))

answers = ("B", "C", "C", "D", "B")
guesses = []
score = 0
question_num = 0

print("Welcome to the Python Quiz Game!")
print("(One correct ans = +2, One wrong ans = -1)")

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter the correct option (A, B, C, D):").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT")
        score += 2

    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
        score -= 1

    question_num += 1

print("--------------------")

print("       RESULTS       ")
print("--------------------")

print()
print("Answers:", end="")
for answer in answers:
    print(answer, end=" ")

print()

print("Your Guesses:", end="")
for guess in guesses:
    print(guess, end=" ")

print()
print(f"Your final score is: {score}")

print()

print("----- THANK YOU -----")
