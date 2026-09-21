# Features of Quiz Masters:

# 1. Welcome Screen with App name and instructions.
# 2. Predefined set of multiple choice questions.
# 3. User answers with A, B, C, D
# 4. Correct and wrong answer checking.
# 5. Score calculations.
# 6. Display total score and percentage.
# 7. Performance feedback (Excellent / Good/ Practise score).
# 8. Option to play again (replay feature).

def quiz():

    questions = [
        {
            "question": "Which language is known as mother of all languages?",
            "options": ["A. C", "B. Python", "C. Java", "D. Assembly"],
            "answer": "A"
        },
        {
            "question": "What is Capital of India?",
            "options": ["A. Delhi", "B. Kolkata", "C. Bengaluru", "D. Chennai"],
            "answer": "A"
        },
        {
            "question": "Which data structure uses LIFO?",
            "options": ["A. Queue", "B. Linked List", "C. Stack", "D. Array"],
            "answer": "C"
        },
        {
            "question": "Which Company developed Python?",
            "options": ["A. Microsoft", "B. Google", "C. Bell labs", "D.CWI"],
            "answer": "D"
        }
    ]
    score = 0 # Variable

    print("\nWelcome to the Quiz Master!")
    print("Answer the questions by just typing the options.")

    for i, q in enumerate(questions, start=1):
        print(f'{i}: {q["question"]}')

        for option in q["options"]:
            print(option)

        answer = input("Your answer: ").strip().upper()

        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, that's wrong, Answer: {q[answer]}\n")

    # 6.Displaying total score & percentage.
    total =len(questions)
    print(f"Quiz Completed!:{score}/{total}\n")

    percentage = (score/total) * 100
    print(f"Your Percentage: {percentage}%")

    if percentage >= 100:
        print("Excellent!")
    elif percentage >= 60:
        print("Good!")
    else:
        print("Need Practise.")

    retry = input("Do you want to try again? (Y/N): ").strip().lower()
    if retry == "y":
        quiz()
quiz()














