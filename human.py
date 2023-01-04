from player import Player
import interface as ui

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
    pass
    def choose_gesture(self):
        
        user_selection = ui.validate_to_int(f"""
        Choose from one of the options below: 
        1 for {self.gesture_list[0]}
        2 for {self.gesture_list[1]}
        3 for {self.gesture_list[2]}
        4 for {self.gesture_list[3]}
        5 for {self.gesture_list[4]}
        """)
        self.current_gesture = self.gesture_list[user_selection-1]
        print(f"{self.name} chose {self.current_gesture}!")
        pass