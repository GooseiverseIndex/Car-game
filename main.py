import random

# Define the car class
class Car:
    def __init__(self):
        self.position = 0
    
    def move(self):
        self.position += random.randint(1, 3)
    
    def crash(self):
        self.position -= random.randint(1, 3)

# Define the game loop
def play_game():
    car = Car()
    track_length = 10
    play_again = 'y'
    
    while play_again.lower() == 'y':
        print("Welcome to the Car Game!")
        print("The track has a length of", track_length, "units.")
        print("You start at position 0. Avoid obstacles and reach the end!")
        
        while car.position < track_length:
            move_or_crash = input("Press 'm' to move or 'c' to crash: ")
            if move_or_crash.lower() == 'm':
                car.move()
            elif move_or_crash.lower() == 'c':
                car.crash()
            else:
                print("Invalid input. Try again.")
        
        if car.position >= track_length:
            print("Congratulations! You reached the end of the track!")
        else:
            print("Oops! You crashed.")
        
        play_again = input("Do you want to play again? (y/n): ")

# Start the game
play_game()
