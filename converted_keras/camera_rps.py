import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    """
    Randomly pick an option between "rock", "paper", and "scissors".
    Returns:
        str: The computer's choice.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_prediction():
    # Make a list of options
    list_of_options = ["rock", "paper", "scissors", "nothing"]
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data, verbose=0)
        cv2.imshow('frame', frame)
        max_index = np.argmax(prediction[0])
        selection = list_of_options[max_index]
        elapsed_time = time.time() - start_time
        if elapsed_time >= 4:
            break

        cv2.waitKey(1)  # Add this line to refresh the GUI window and handle keyboard events

    cv2.destroyAllWindows()
    return selection

def get_user_choice():
    """
    Get the user's choice using computer vision with a 4-second timer.
    Returns:
        str: The user's choice.
    """
    return get_prediction()

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
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")):
        print("You won!")
        return "user"
    else:
        print("You lost!")
        return "computer"

def play():
    # Initialize scores
    computer_wins = 0
    user_wins = 0

    while True:
        # Get choices from the user and computer
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Determine the winner and print the result
        result = get_winner(computer_choice, user_choice)

        # Update scores
        if result == "computer":
            computer_wins += 1
        elif result == "user":
            user_wins += 1

        print(f"Computer Wins: {computer_wins}, User Wins: {user_wins}")

        # Check if either the computer or the user has won three rounds
        if computer_wins == 3 or user_wins == 3:
            print(f"\nGame Over! {'Computer' if computer_wins == 3 else 'User'} wins!")
            break
        print("Press Enter for the next round...")
        cv2.waitKey(0)  # Wait for any key press, including Enter
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Load the model and initialize the camera
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Call the play function to start the game
    play()
