# Dice game for 2 Player
import random
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def roll_dice(self):
        roll = random.randint(1,6)
        self.score += roll
        return roll
    
    def get_score(self):
        return self.score
    
class Game:
    def __init__(self, pl1, pl2) -> None:
        self.pl1 = Player(pl1)
        self.pl2 = Player(pl2)
        self.round_number = 1

    def play_round(self):
        roll_pl1 = self.pl1.roll_dice()
        roll_pl2 = self.pl2.roll_dice()
        self.round_number += 1

    def display_scores(self):
        print(f"d_s {self.pl1.name}  score : {self.pl1.get_score()}")
        print(f"d_s {self.pl2.name}  score : {self.pl2.get_score()}")

    def determine_winner(self):
        if self.pl1.get_score() == self.pl2.get_score(): return print(f" no winner")
        if self.pl1.get_score() > self.pl2.get_score():
            winner = self.pl1.get_score()
            return (f"winner is {self.pl1.name}")
        return (f"winner is {self.pl2.name}")

def main():
    game = Game("abdou", "Ali")
    
    for i in range(15):
      game.play_round()
    print(f"we are played  =  {i}  round" )
    print(f"{game.pl1.name}  has  score  {game.pl1.get_score()}")
    print(f"{game.pl2.name}   has score  {game.pl2.get_score()}")
    #print(f"{game.display_scores()}")
    print(f"{game.determine_winner()}")  
if __name__ == "__main__":
    main()  