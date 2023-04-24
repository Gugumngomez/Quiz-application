# small python game just to play around with code !!!!!

questions = ("How many dots appear on a pair of dice?: ", 
             "What phone company produced the 3310?: ", 
             "Where did sushi originate?: ", 
             "Pink Ladies and Granny Smiths are types of what fruit?: ", 
             "Which country drinks the most coffee?: ", 
             "What year was Cinderella released?: ", 
             "What is a Beaujolais?: ", 
             "Cacio & Pepe is a staple of what Italian citys cuisine?: ", 
             "Which country features a shipwreck on its national flag?: ", 
             "What is the state capital of New York?: ")

options = (("A. 21", "B. 6", "C. 42", "D. 12"), 
           ("A. Samsung", "B.Nokia", "C.iPhone", "D. Huawei"), 
           ("A. Canada", "B. Japan", "C. Brazil", "D. China"),
           ("A. Apples", "B. Banana", "C. Kiwi", "D. Strawberry"),
           ("A. Ireland", "B. Finland", "C. Iceland", "D. Switzerland"), 
           ("A. 2001", "B. 1850", "C. 1950", "D. 1990"), 
           ("A. Orange Juice", "B. Grape Juice", "C. White wine", "D. A type of red wine"),
           ("A. Naples", "B. Rome", "C. Venice", "D. Milan"),  
           ("A. USA", "B. China", "C. Bermuda", "D. Netherlands"), 
           ("A. Albany", "B.Austin", "C. Honolulu", "D. Columbus"))

answers = ("C", "B", "D", "A", "B", "C", "D", "B", "C", "A")
guesses = []
score = 0
q_num = 0

for i in questions: 
    print(i)
    for j in options[q_num]:
        print(j)

    guess = input("Enter A, B, C or D: ").upper()
    guesses.append(guess)
    if guess == answers[q_num]:
        score+= 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        # print(f"{answers[q_num]} is the correct answer.")
    q_num += 1

print(".............................")
print("          UR RESULTS         ")
print(".............................")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100 )
print(f"Your score is: {score}%")

