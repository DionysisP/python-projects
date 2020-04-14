
import random

kino_numbers = []
winning_numbers = []
numbers = []

#fill kino numbers list with numbers
for i1 in range(20):
    i1 += 1
    kino_numbers.append(i1)

#declare lucky numbers
for i2 in range(5):
    choice = random.choice(kino_numbers)
    kino_numbers.remove(choice)
    winning_numbers.append(choice)

#input numbers
for i3 in range(5):
    x = input("Give me 5 numbers, 1 - 20\n")            
    numbers.append(x)

print("Your numbers:", *numbers)
print("The wining numbers are:", *winning_numbers)


if numbers[1:5] == winning_numbers[1:5]:
    print("YOU WIN")
else:
    print("You lost")


