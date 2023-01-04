from human import Human
from ai import ai 
import interface as ui
from player import Player
class Game:
    def __init__(self) -> None:
        self.player_one = None
        self.player_two = None
        pass 

    def run(self):
        self.game_type()
        self.winner_check
        pass

    def game_type(self):
        user_selection = ui.validate_to_int("""
        Choose from the options listed:
        Select 1 for  Human vs Human
        Select 2 for Human vs AI 
        """)
        if user_selection == 1:
            self.player_one = Human("Player One")
            self.player_two = Human("Player_Two")
        elif user_selection == 2:
            self.player_one = Human("Player_One")
            self.player_two = ai("Player_Two")
            pass
            

    def player_rolls(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

    def winner_check(self):
        while self.player_one.score < 3 and self.player_two.score < 3:
            self.player_rolls()
        pass



    def victory_message(self):
        pass
