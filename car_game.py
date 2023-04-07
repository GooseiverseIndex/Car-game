class CarGame:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.car_row = 0
        self.car_col = 0
        self.obstacle_col = None

    def initialize(self):
        self.car_row = 0
        self.car_col = 0
        self.obstacle_col = None

    def draw_grid(self):
        print("+" + "---+" * self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                if row == self.car_row and col == self.car_col:
                    print("| C ", end="")
                elif row == self.rows - 1 and col == self.obstacle_col:
                    print("| O ", end="")
                else:
                    print("|   ", end="")
            print("|")
            print("+" + "---+" * self.cols)

    def move_car(self, direction):
        if direction == "left":
            if self.car_col > 0:
                self.car_col -= 1
        elif direction == "right":
            if self.car_col < self.cols - 1:
                self.car_col += 1
        elif direction == "up":
            if self.car_row > 0:
                self.car_row -= 1
        elif direction == "down":
            if self.car_row < self.rows - 1:
                self.car_row += 1

    def place_obstacle(self):
        import random
        self.obstacle_col = random.randint(0, self.cols - 1)

    def play(self):
        print("Welcome to Car Game!")
        self.initialize()
        self.place_obstacle()

        while True:
            self.draw_grid()

            if self.car_row == self.rows - 1 and self.car_col == self.obstacle_col:
                print("You lost!")
                break
            elif self.car_row == self.rows - 1 and self.car_col == self.cols - 1:
                print("You won!")
                break

            direction = input("Enter move (left/right/up/down): ")
            self.move_car(direction)

