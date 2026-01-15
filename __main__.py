"""The Game Loop"""

from map import Map
from player import Player
from save_data import SaveData


def main():
    """Run The Game Loop"""

    load_command: str = start_screen()
    # Get player data

    # Initializes the player and map when starting

    # Create Player()
    # Create Map(position, lever_tiles, tiles, victory_tiles)

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
        print("Try Again")

    return choice


if __name__ == "__main__":
    main()
