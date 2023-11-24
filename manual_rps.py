import random

def get_computer_choice():
    """
    Randomly pick an option between "rock", "paper", and "scissors".
    Returns:
        str: The computer's choice.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """
    Ask the user for an input and return it.
    Returns:
        str: The user's choice.
    """
    while True:
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_winner(computer_choice, user_choice):
    """
    Determine the winner based on the classic rules of Rock-Paper-Scissors.
    Print the result.
    Arguments:
        computer_choice (str): The computer's choice.
        user_choice (str): The user's choice.
    """
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")):
        print("You won!")
    else:
        print("You lost!")

def play():
    # Get choices from the user and computer
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    # Determine the winner and print the result
    get_winner(computer_choice, user_choice)

if __name__ == "__main__":
    # Call the play function to start the game
    play()
