"""The Game Loop"""

from map import Map
from player import Player
from save_data import SaveData


def main():
    """Run The Game Loop"""

    load_command: str = start_screen()

    # Create New Game
    if load_command == "N":
        SaveData.new_game()
    # Continue GAme
    elif load_command == "C":
        SaveData.load_game()

    # Get player data

    # Initializes the player and map when starting

    create_map: Map =  Map(position, lever_tiles, tiles, victory_tiles)
    create_player: Player = Player(amount_of_moves, coins, create_map, current_position)

    # Run the game loop for player
    while True:
        # available_moves = Player.display_moves()

        print("SHIT")

        # SaveData.save_game()
        break


def start_screen() -> str:
    print(
        "Welcome To The Game Do You Want To Start New(N) or Continue(C) From Last Game"
    )

    choice: str = "LOOP_STARTER"
    while choice != "C" and choice != "N":
        choice: str = input("(C)ontinue or (N)ew Game: ").upper()
        if choice != "C" and choice != "N":
            print("Try Again")

    return choice


if __name__ == "__main__":
    main()
