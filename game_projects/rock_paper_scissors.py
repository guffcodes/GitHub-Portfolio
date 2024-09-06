import random
# Create a Program: Rock, Paper, Scissors

# Ask user to start the game with a choice
print ("Lets Play: Rock, Paper, or Scissors")
user_inp = input ("Which one will you choose? ")
user_inp = user_inp.lower()


# Create an CPU Opponent that will play against the user
def CPU(user_inp):
    choice_list = ["rock", "paper", "scissors"]
    cpu_choice = (random.choice(choice_list))
    user_choice = user_inp
    if (cpu_choice == ("rock") and user_choice == ("rock")) or (cpu_choice == ("scissors") and user_choice == ("scissors")) or (cpu_choice == ("paper") and user_choice == ("paper")):
        print ("Your opponent chose: ", cpu_choice)
        return ("It's a tie!")
    elif (cpu_choice == ("paper") and user_choice == ("rock")) or (cpu_choice == ("rock") and user_choice == ("scissors")) or (cpu_choice == ("scissors") and user_choice == ("paper")):
        print ("Your opponent chose: ", cpu_choice)
        return "Sorry but you lost! Better luck next time!"
    elif (cpu_choice == ("scissors") and user_choice == ("rock")) or (cpu_choice == ("paper") and user_choice == ("scissors")) or (cpu_choice == ("rock") and user_choice == ("paper")):
        print ("Your opponent chose: ", cpu_choice)
        return "You win!"
    else:
        print ("Make sure you enter either: Rock, Paper, or Scissors")


print (CPU(user_inp))
