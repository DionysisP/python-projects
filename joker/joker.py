import random


money = 0.50

isRunning = True
draws = 1

while isRunning:

    if draws >= 50000:
        print("\nDraws: ", draws)
        isRunning = False
        r = 100 / draws
        print("Winning ratio: ",r)
        print("Money spent:",money)
    list1 = []
    joker = []


    list1_lucky_numbers = []
    joker_lucky_number = []

    ai = []
    ai_joker = []

    #Fill main list
    for i in range(45):
        i += 1
        list1.append(i)

    #Fill Joker list
    for i2 in range(20):
        i2 += 1
        joker.append(i2)


    #AI chooses numbers
    for i3 in range(5):
        #choose random number from list1 and adds it to ai list
        choice = random.choice(list1)
        ai.append(choice)
        #removes choices from list
        list1.remove(choice)

    #retrieves list and sorts it
    list1 = list1 + ai
    list1.sort()

    #AI chooses joker number
    for i4 in range(1):
        #choose random number from joker list and adds it to ai joker list
        choice2 = random.choice(joker)
        ai_joker.append(choice2)

        #removes choices from joker list
        joker.remove(choice2)

    #retrieves list and sorts it
    joker = joker + ai_joker
    joker.sort()

    #Draw lucky numbers
    for i5 in range(5):
        x3 = random.choice(list1)
        list1_lucky_numbers.append(x3)
        list1.remove(x3)

    #Draw lucky joker number
    for i6 in range(1):
        x4 = random.choice(joker)
        joker_lucky_number.append(x4)



    #print("All numbers", *list1)
    #print("All jokers",*joker)

    #sort lists
    ai.sort()
    list1_lucky_numbers.sort()

    print("AI numbers:", *ai)
    print("AI joker:", *ai_joker)

    if ai[0:5] == list1_lucky_numbers [0:5]:
        if ai_joker == joker_lucky_number:
            print("OMG YOU WIN")
            print("Draws: ", draws)
            isRunning = False
            r = 100 / draws
            print("Winning ratio: ",r)
            print("Money spent:", money)
    else:
        money += 0.50
        draws += 1
        print("Too Bad")

    print("\nWINNING NUMBERS ARE:", *list1_lucky_numbers)
    print("JOKER :", *joker_lucky_number)