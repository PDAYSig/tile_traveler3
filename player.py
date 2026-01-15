from map import Map

class Player():
    """
    Docstring for PLayer Class
    
    :param moves: How many times he has moved
    :type moves: int
    :param coins: Amount of coins
    :type coins: int
    :param map: A Map object that holds the grid map
    :type map: Map
    :param current_position: Current position of player.
    Default = (1,1)
    :type current_position: tuple
    """

    def __init__(self,moves: int,coins:int ,map: Map, current_position: tuple = (1,1)) -> None:
        """
        Docstring for PLayer Init Class
        
        :param moves: How many times he has moved
        :type moves: int
        :param coins: Amount of coins
        :type coins: int
        :param map: A Map object that holds the grid map
        :type map: Map
        :param current_position: Current position of player.
        Default = (1,1)
        :type current_position: tuple
        """

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