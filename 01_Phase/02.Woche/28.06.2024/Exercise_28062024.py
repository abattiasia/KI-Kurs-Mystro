# Simple Dice Game
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
        #print(f"My Score : {self.score}")
        return self.score
    
class ComputerPlayer(Player):  # subclass due to Player Inherits
    def __init__(self, name = "computer" ):  #  hat kein Einfluss, muss man den Namen beim Spielen geben
        super().__init__(name) # was macht genau dieses Satz

class Game:
    def __init__(self, player_name) -> None:
        self.player = Player(player_name)
        #self.plyer2 = Player(player_name)  # muss ich medinsten 2 Players definieren
        self.computer = ComputerPlayer()   # cann ich auch der Computer anderes definieren
        

    def play_round(self):
        player_roll = self.player.roll_dice()
        computer_roll = self.computer.roll_dice()
        #print(f"{self.player.name} :  {player_roll}")
        #print(f"{self.computer.name} :  {computer_roll}")


    def display_score(self):
        print(f"{self.player.name}  score  : {self.player.get_score()}")
        print(f"{self.computer.name}  score  : {self.computer.get_score()}")
        return
    
    def determine_winner(self):
        if self.player.get_score() > self.computer.get_score():
            #winner = self.player.get_score()
            return (f"winner is {self.player.name}")
        return (f"winner is {self.computer.name}")

def main():
    p1=Game("abdou")
    for i in range(15):
        p1.play_round()
    print(f"we are schon played  =  {i}  round" )
    print(f"{p1.display_score()}")
    print(f"{p1.determine_winner()}")
    
if __name__ == "__main__":
    main()



    