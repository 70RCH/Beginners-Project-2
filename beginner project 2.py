import os, time, random
os.system('cls')
numbertostart = random.randint(0,1)
start =[
    r" _       _       _                                 _           _   _                                         ",
    r"( )  _  ( )     (_ )                              ( )_        ( )_( )                                        ",
    r"| | ( ) | |  __  | |   ___   _    ___ ___    __   |  _)  _    |  _) |__    __      __    _ _  ___ ___    __  ",
    "| | | | | |/ __ \\| | / ___)/ _ \\/  _   _  \\/ __ \\ | |  / _ \\  | | |  _  \\/ __ \\  / _  \\/ _  )  _   _  \\/ __ \\",
    r"| (_/ \_) |  ___/| |( (___( (_) ) ( ) ( ) |  ___/ | |_( (_) ) | |_| | | |  ___/ ( (_) | (_| | ( ) ( ) |  ___/",
    r" \__/\___/ \____)___)\____)\___/(_) (_) (_)\____)  \__)\___/   \__)_) (_)\____)  \__  |\__ _)_) (_) (_)\____)",
    r"                                                                                ( )_) |                      ",
    r"                                                                                 \___/                       "
]

for l in start:
    print(  "\033[41m" +"\033[37m" + l + "\033[0m")  
    time.sleep(0.5)

a114514 = input("1: Play! 2:\033[37mQuit…?" + "\033[0m")
if a114514 == "2":
    print("Come back when you are ready to … （no signal）")
    exit()
elif a114514 == "1":
    print("Okay…")
    print("\033[31m" + "I WANT TO PLAY A GAME…" + "\033[0m")
    time.sleep(2)
else:
    print("I can't understand you…")
    exit()


if numbertostart == 0:
    
    c = 0
    print("You need to enter a forest and have to play a series of games to survive!!!")
    print("Ah Oh! A wild monkey appears and the player cannot pass until five fruits have been guessed!")
    mfruits = ["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Strawberry", "Watermelon", "Peach", "Cherry", "Blueberry", "Pear", "Kiwi", "Pomegranate", "Papaya", "Lemon", "Lime", "Coconut", "Plum", "Apricot"]
    selected = random.sample(mfruits, 5)
    while True:
        guesses = input("Enter five fruits, separated by commas: ").split(",")
        guesses = [fruit.strip().capitalize() for fruit in guesses]

        correct_guesses = set(guesses) & set(selected)
        if len(correct_guesses) == 5:
            print("Congratulations! You've guessed all the fruits correctly. You may pass.")
            break
        else:
            c += 1
            print(f"You guessed {len(correct_guesses)} correct fruits: {', '.join(correct_guesses)}")
            print("Try again!")
            print(f"You have {15-c} chances left.")
            if c == 15:
                print("You have failed to guess all the fruits correctly. You have been eaten by the monkey."+"\033[31m" +"YOU DIED!"+"\033[0m")
                break
    
    print ("Here is a hungry tiger! and the only way out is the nearest that needs you to cross a river…")
    print ("WHat is your height? (in cm)")
    height = int(input())
    if height <= 160:
        print("You are too short to cross the river. You have drawn in the water."+"\033[31m" +"YOU DIED!"+"\033[0m")
        exit()
    elif height > 160 and height < 180:
        print("You are just right to cross the river. You have crossed the river safely.")
    else:
        print("You are too tall to cross the river. You have been noticed by the tiger and have been eaten."+"\033[31m" +"YOU DIED!"+"\033[0m")
        exit()

    print ("Finally!!! here is a door that requires a password to unlock- it is a series of four numbers.")
    password = []
    for _ in range(4):
        password.append(random.randint(0, 9))
    attempts = 10
    while attempts > 0:
        guess = input("Enter 4 numbers: ")
        guess_numbers = []
        for x in guess[:4]:
            guess_numbers.append(int(x))
        correct_numbers = 0
        for i in range(4):
            if guess_numbers[i] == password[i]:
                correct_numbers += 1
        if correct_numbers == 4:
            print("Door unlocked successfully!")
            break
        else:
            print(f"{correct_numbers} numbers are correct.")
            attempts -= 1
    if attempts == 0:
        print(f"Failed to unlock the door. The correct password was {password}.")


if numbertostart == 1:
    questions = [
        {"question": "What is the correct file extension for Python files?", 
         "options": ["a) .py", "b) .python", "c) .pt", "d) .p"],
         "answer": "a"},
        {"question": "What is used to define a function in Python?", 
         "options": ["a) func", "b) define", "c) def", "d) function"],
         "answer": "c"},
        {"question": "Which of these is not a Python data type?", 
         "options": ["a) list", "b) tuple", "c) array", "d) dictionary"],
         "answer": "c"},
        {"question": "How do you start a comment in Python?", 
         "options": ["a) //", "b) #", "c) <!--", "d) /*"],
         "answer": "b"},
        {"question": "What is the output of print(2 ** 3)?", 
         "options": ["a) 6", "b) 9", "c) 8", "d) 5"],
         "answer": "c"},
        {"question": "Which of these is a Python framework for web development?", 
         "options": ["a) Flask", "b) React", "c) Angular", "d) Laravel"],
         "answer": "a"},
        {"question": "Which Python keyword is used to handle exceptions?", 
         "options": ["a) except", "b) handle", "c) try", "d) error"],
         "answer": "c"},
        {"question": "What is the purpose of 'self' in a Python class?", 
         "options": ["a) To refer to the current instance", "b) To call a method", "c) To define a static method", "d) To create a global variable"],
         "answer": "a"},
        {"question": "What is the output of print(type([]))?", 
         "options": ["a) <class 'list'>", "b) <class 'dict'>", "c) <class 'tuple'>", "d) <class 'set'>"],
         "answer": "a"},
        {"question": "Which of the following is not a valid loop in Python?", 
         "options": ["a) for", "b) while", "c) repeat", "d) none"],
         "answer": "c"}
    ]
    selected_questions = random.sample(questions, 6)
    
    correct = 0
    user_answers = []
    correct_answers = []

    for i, q in enumerate(selected_questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q["options"]:
            print(option)
        guess = input("Your answer (a, b, c, d): ").lower()
        user_answers.append(guess)
        correct_answers.append(q["answer"])
        
        if guess == q["answer"]:
            correct += 1

    incorrect = 6 - correct
    percentage = (correct / 6) * 100

    print(f"\nYou answered {correct} questions correctly.")
    print(f"You answered {incorrect} questions incorrectly.")
    print(f"Your score is {percentage:.2f}%.")

    if correct == 6:
        print("Congrats, you got a perfect score!")
    elif correct >= 4:
        print("Well done, you know your Python!")
    elif correct >= 2:
        print("Not bad, but you can improve.")
    elif correct == 1:
        print("You need to study more.")
    else:
        print("You're bad at this. Try again!")

    print("\nCorrect Answers:")
    for i, q in enumerate(selected_questions):
        print(f"Question {i+1}: {q['question']}")
        print(f"Your answer: {user_answers[i]}")
        print(f"Correct answer: {correct_answers[i]}\n")























    











