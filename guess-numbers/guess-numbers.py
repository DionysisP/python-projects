import random


numbers = []

attemps = 1
isRunning = True

while isRunning:

    kino_numbers = []
    kino_numbers2 = []
    winning_numbers = []
    ainums = []

    
    #fill kino numbers list with numbers
    for i1 in range(20):
        i1 += 1
        kino_numbers.append(i1)
        kino_numbers2.append(i1)


    #declare lucky numbers
    for i2 in range(5):
        choice = random.choice(kino_numbers)
        winning_numbers.append(choice)
        kino_numbers.remove(choice)
        winning_numbers.sort()



#AI number choices
    for i4 in range(5):
        x2 = random.choice(kino_numbers2)
        ainums.append(x2)
        kino_numbers2.remove(x2)
        ainums.sort()

    print("AI numbers:", *ainums)
    print("The wining numbers are:", *winning_numbers)



    if ainums[0:5] == winning_numbers[0:5]:
        print("Ai finally found the numbers")
        print("Number of attempts:")
        print(attemps)
        isRunning = False
    else:
        print("AI didnt win\n")
        attemps += 1


