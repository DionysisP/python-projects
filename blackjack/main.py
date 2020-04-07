import random
import os

you1 = random.randrange(1, 11)
you2 = random.randrange(1, 11)
your_hand = you1 + you2

ai1 = random.randrange(1, 11)
ai2 = random.randrange(1, 11)
ai_hand = ai1 + ai2

draw = True

your_input = ""

while draw:

    def main_loop():
        global your_input
        print("AI: hand:", ai_hand)
        print("Your hand: ", your_hand)
        your_input = input("Draw another card? y/n\n")
        #probably needs replace
        #os.system('clear')

    # checks if someone ovapasses 21
    def check_if_overpass(you, ai):
        global draw
        if you > 21 or ai > 21:
            if you > 21:
                print("Your hand: ", your_hand)
                print("AI: hand:", ai_hand)
                print("you overpassed. you lose")
            else:
                print("Your hand: ", your_hand)
                print("AI: hand:", ai_hand)
                print("ai overpass. you win")
            draw = False
        else:
            main_loop()


    def result():
        global draw
        if your_hand > ai_hand:
            print("You win!!")
            draw = False
        else:
            print("You Lose!!")
            draw = False
        print("Your sum is : ", your_hand)
        print("AI sum is : ", ai_hand)


    your_random_draw = random.randrange(1, 11)
    ai_random_draw2 = random.randrange(1, 11)

    check_if_overpass(your_hand, ai_hand)

    if your_input == "y":
        your_hand += your_random_draw
        ai_hand += ai_random_draw2
    else:
        result()
