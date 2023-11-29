import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def display_countdown(frame, countdown):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 12
    font_thickness = 20
    font_color = (255, 255, 255)
    position = (50, 300)

    cv2.putText(frame, str(countdown), position, font, font_scale, font_color, font_thickness)

def get_prediction():
    list_of_options = ["rock", "paper", "scissors", "nothing"]
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        elapsed_time = time.time() - start_time
        if elapsed_time < 4:
            countdown = 4 - int(elapsed_time)
            display_countdown(frame, countdown)
        else:
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(1000)  # Update every 1 second

    cv2.destroyAllWindows()

    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    prediction = model.predict(data, verbose=0)
    max_index = np.argmax(prediction[0])
    selection = list_of_options[max_index]

    return selection

def get_user_choice():
    return get_prediction()

def get_winner(computer_choice, user_choice):
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
    computer_wins = 0
    user_wins = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = get_winner(computer_choice, user_choice)

        if result == "computer":
            computer_wins += 1
        elif result == "user":
            user_wins += 1

        print(f"Computer Wins: {computer_wins}, User Wins: {user_wins}")

        if computer_wins == 3 or user_wins == 3:
            print(f"\nGame Over! {'Computer' if computer_wins == 3 else 'User'} wins!")
            break

        print("Press Enter for the next round...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    play()
