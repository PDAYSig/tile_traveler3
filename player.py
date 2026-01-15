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

    def display_available_moves(self) -> str:
        """
        Displays the available moves from a player. Uses the current_position of the player
        and the map layout
        """
        move_str: str = "You can travel: "
        available_moves: list[str] = self.map.availableMoves(self.current_position)
        for cardinal_direction in available_moves:
            if cardinal_direction == "n":
                move_str += "N)orth "
            elif cardinal_direction == "s":
                move_str += "(S)outh "
            elif cardinal_direction == "e":
                move_str += "E)ast "
            elif cardinal_direction == "w":
                move_str += "(W)est "
        return move_str
    
    def move_player(self,move_direction:str):
        x, y = self.current_position
        if move_direction == "n":
            y += 1
        elif move_direction == "e":
            x += 1
        elif move_direction == "s":
            y -= 1
        elif move_direction == "w":
            x -= 1
        
        self.current_position = (x, y)
        return self.current_position

def main():
    kort = Map((1,1),{(1,2), (2,2), (2,3), (3,3)},(1,1),(3,3))
    jon = Player(0,0,kort,(1,1))
    print(jon.display_available_moves())
    print(jon.current_position)
    jon.move_player("n")
    print(jon.current_position)
    print(jon.display_available_moves())

main()