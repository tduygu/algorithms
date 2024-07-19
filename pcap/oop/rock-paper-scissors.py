import random


class RockPaperScissorsGame:
    rps = ['r', 'p', 's']
    yourScore = 0
    computerScore = 0
    def __init__(self, round_count):
        for i in range(round_count):
            self.start()
            self.computer_turn()
        self.show_score()

    def start(self):
        self.yourValue = input("Rock, paper or scissors [r/p/s]?")
        if not self.yourValue in RockPaperScissorsGame.rps:
            print("Invalid value")

    def computer_turn(self):
        c = random.choice(RockPaperScissorsGame.rps)
        this_turn_computer = -1
        print(f"computer: {c}")
        if self.yourValue == 'r' and c == 's':
            RockPaperScissorsGame.yourScore += 1
        elif self.yourValue == 's' and c == 'p':
            RockPaperScissorsGame.yourScore += 1
        elif self.yourValue == 'p' and c == 'r':
            RockPaperScissorsGame.yourScore += 1
        elif self.yourValue == c:
            print("equal")
            this_turn_computer = 0
        else:
            RockPaperScissorsGame.computerScore += 1
            this_turn_computer = 1

        print(f"You: {self.yourValue} | Computer: {c}")
        if this_turn_computer == -1:
            print("You won this round.")
        elif this_turn_computer == 0:
            print("You are equal")
        else:
            print("You lost this round")

    def show_score(self):
        print(f"\n\nGame Summary\n Your point {RockPaperScissorsGame.yourScore}\n Computer's point {RockPaperScissorsGame.computerScore}")
        if RockPaperScissorsGame.computerScore > RockPaperScissorsGame.yourScore:
            print("Computer won.")
        elif RockPaperScissorsGame.computerScore < RockPaperScissorsGame.yourScore:
            print("You won.")
        else:
            print("You are equal.")









n = input("How many rounds would you like to play?")
while n.isdigit() is False:
    print("Please provide a number")
    n = input("How many rounds would you like to play?")


oyun = RockPaperScissorsGame(int(n))

