from map import Map

class Player():
    def __init__(self,moves: int,coins:int ,map: Map, current_position: tuple = (1,1)) -> None:
        self.current_position = current_position
        self.moves = moves
        self.coins = coins
        self.map = map

    def move_player(self) -> None:
        move_str: str = "You can travel: "
        available_moves: list[str] = self.map.availableMoves(self.current_position)
        for cardinal_direction in available_moves:
            if cardinal_direction == "n":
                move_str.join("N)orth ")
            elif cardinal_direction == "s":
                move_str.join("(S)outh ")
            elif cardinal_direction == "e":
                move_str.join("E)ast ")
            elif cardinal_direction == "w":
                move_str.join("(W)est ")