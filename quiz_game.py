# Python__Quiz__Game


questions = ("Who is the CEO of spaceX ? :",
             "who is the first richest person in india ?:",
             "Founder of FaceBook ?: ",
             "World's n0.1n Business School ?:",
             "Best programming Languages ? : ",
             )

options = (
            ("A. Elon_musk","B. mark","C. warren","D. JAGAN"),
            ("A. Rakesh","B. Mukesh","C. REDDY","D. aditya"),
            ("A. vijay","B. john","C. mark_zuberberg","D. peter"),
            ("A. stanford","B. karunya","C. gates_UNIV","D. HARDWARD"),
            ("A. python","B. java","C. GO","D. C++")
            )
answers = ("A","B","C","D","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("_ _ _ _ _ _ _ _ _ _ _ _")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("ENter the (A,B,C,D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("!  CORRECT  !")
    else:
        print("!  INCORRECT  !")
        print(f"{answers[question_num]} is the correct answers ")

    question_num += 1 

print("-------------------------")
print("     !!! RESULT  !!!      ")
print("-------------------------")

print("Answers : " , end = "")
for answer in answers:
    print(answer,end = " ")
print()

print("Guess : " , end = "")
for guess in guesses:
    print(guess,end = " ")
print()

score = int(score / len(questions)*100)
print(f"Your Score is :  {score}%")


