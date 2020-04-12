import random
import time

coins = 300
bet = 10

run = True

while run:

    print("Coins : ", coins)
    inpt = input("\nGive 20 coins to play? y/n\n")
    
    if inpt == "y":

        if coins < bet:
            print("Not enough coins!")
            run = False
        else:
            coins -= bet
            slot1 = random.randrange(1,4)
            slot2 = random.randrange(1,4)
            slot3 = random.randrange(1,4)
            time.sleep(1)
            print(slot1)
            time.sleep(1)
            print(slot2)
            time.sleep(1)
            print(slot3)

            if slot1 == slot2 and slot2 == slot3:
                print("You win! You get 100 coins")
                coins += 100
    else:
        run = False

