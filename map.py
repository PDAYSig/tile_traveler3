from random import randint


class Map:
    """
    Constants fyrir áttirnar (Döh)
    """
    NORTH = 'n'
    EAST = 'e'
    SOUTH = 's'
    WEST = 'w'


    def __init__(self, positions, lever_tiles, tiles, victory_tile):
        self.postition = positions
        self.lever_tiles = lever_tiles
        self.tiles = tiles
        self.victory_tile = victory_tile
        pass


    """
    Level 1 placeholder tölur
    """
    def availableMoves(self, position):
        valid_moves = {
            (1, 1): [Map.NORTH],
            (1, 2): [Map.NORTH, Map.EAST, Map.SOUTH],
            (1, 3): [Map.EAST, Map.SOUTH],
            (2, 1): [Map.NORTH],
            (2, 2): [Map.SOUTH, Map.WEST],
            (2, 3): [Map.EAST, Map.WEST],  
            (3, 1): [],
            (3, 2): [Map.NORTH, Map.SOUTH],
            (3, 3): [Map.SOUTH, Map.WEST],
        }
        return valid_moves.get(position, [])


    """
    seinna fyrri flóknari level
    """
    def generateMap():
        pass

    """
    Victory tile f. level 1
    """
    def victory(self, victory_tile):
        victory_tile = {(3,1)}
        if victory_tile == True:
            return "227.30.175.27"
        
    
    def levers(self):
        tiles = {(1,2), (2,2), (2,3), (3,3)}
