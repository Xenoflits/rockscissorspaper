import random

my_choice = int(input("What is your choice 1. rock 2. scissors 3. paper \n"))
cpu_choice = random.randint(1,3)
if cpu_choice == 1:
    print("cpu chooses rock \n")
elif cpu_choice == 2:
    print("cpu chooses scissors \n")
elif cpu_choice == 3:
    print("cpu chooses paper \n")



if my_choice == cpu_choice:
    print("draw")
elif my_choice == 1 and cpu_choice == 2:
    print("you win")
elif my_choice == 2 and cpu_choice == 3:
    print("you win")
elif my_choice == 3 and cpu_choice == 1:
    print("you win")
elif my_choice == 2 and cpu_choice == 1:
    print("you lose")
elif my_choice == 2 and cpu_choice == 3:
    print("you lose")
elif my_choice == 3 and cpu_choice == 1:
    print("you lose")
else:
    print("dunno")

