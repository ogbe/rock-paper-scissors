import random

print("Starting the Rock Paper Scissors game!")

# Prompt the user for his name and for an input
player_name = input("Enter your name: ")

player_hand = input("Please enter a letter (R: Rock, P: Paper, S: Scissors): ")

def start(input):
    # Get an input from the user
    return input

player_name = start(player_name)
# Convert the input to uppercase
player_hand = start(player_hand).upper()

# Validate the input
def validate(hand):
    if hand == "R":
        return True
    if hand == "P":
        return True
    if hand == "S":
        return True
    else: return False

# Display the user's choice
def print_hand(hand, player, computer):
    # Convert the input to a number for both player and computer
    if hand == "R":
        hand = 0
    elif hand == "P":
        hand = 1
    else: hand = 2

    if computer == "R":
        computer = 0
    elif computer == "P":
        computer = 1
    else: computer = 2


    # Create a list of options to choose from 
    hands = ["Rock", "Paper", "Scissors"]
    print(player + " (" + hands[hand] + "): " + "CPU" + " (" + hands[computer] + ")")

# Choose a winner
def judge(computer, player):
    if computer == player:
        return "Draw"
    elif computer == "R" and player == "S":
        return "Lose"
    if computer == "P" and player == "R":
        return "Lose"
    elif computer == "S" and player == "P":
        return "Lose"
    else: return "Win"
    
# Control flow based on the user's input

while player_hand: 
    if validate(player_hand):
        computer_hand = random.choice(("R", "P", "S"))
        print_hand(player_hand, player_name, computer_hand)
        result = judge(computer_hand, player_hand)
        print("Result: You " + result)

        # Repeat the game if the result is a draw
        if result == "Draw":
            player_hand = input("Please enter a letter (R: Rock, P: Paper, S: Scissors): ")
            player_hand = player_hand.upper()
            print_hand(player_hand, player_name, computer_hand)
            result = judge(computer_hand, player_hand)
            print("Result: You " + result)
        break
    # Restart the gaame if the user gives a wrong input
    print("You picked: " + player_hand + ". You should pick R, P or S.")
    player_hand = input("Please enter a letter (R: Rock, P: Paper, S: Scissors): ")
    player_hand = player_hand.upper()
    validate(player_hand)