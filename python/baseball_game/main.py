import random


# Build Question
def build_question():
    question = [str(x) for x in range(0, 9)]
    # Shuffle the digits
    random.shuffle(question)
    return question[:3]


# Submit answer
def submit_answer():
    print("Please enter 3 digits without duplicates.")
    a = input()
    is_digit = not a.isdigit()
    is_three = not (len(a) == 3)
    while is_digit or is_three:
        print("Must write 3 digits, re-input 3 digits")
        a = input()
        is_digit = not a.isdigit()
        is_three = not (len(a) == 3)
    return a


# Check answer
def check_answer(questions, answer):
    strike = 0
    ball = 0

    idx1 = 0
    for idx1, num in enumerate(answer):
        if num == questions[idx1]:
            strike += 1
        else:
            idx2 = 0
            for idx2, q in enumerate(questions):
                if idx1 != idx2:
                    if num == q:
                        ball += 1

    if ball == 0 and strike == 0:
        print("Out")
    elif strike == 3:
        print("That's Great!!")
        return False
    else:
        print("Strike : {}, Ball : {}".format(strike, ball))
    return True


questions = build_question()
is_continue = True
while is_continue:
    answer = submit_answer()
    is_continue = check_answer(questions, answer)
