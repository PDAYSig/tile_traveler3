"""The Game Loop"""

from map import Map
from player import Player
from save_data import SaveData


def main():
    """Run The Game Loop"""

    load_command: str = start_screen()

    # Create New Game
    if load_command == "N":
        create_map: Map = Map((3, 3))
        create_player: Player = Player(0, 0, create_map)
    # Continue GAme
    else:
        create_map = "SHIT"
        create_player = "Shit"
        SaveData.load_game()

    # Get player data

    # Initializes the player and map when starting

    # Run the game loop for player
    while True:
        moves: str = create_player.display_available_moves()
        print(moves)

        print("-----------")

        move_direction: str = input().lower()
        if move_direction in create_map.availableMoves(
            create_player.current_position
        ):
            create_player.move_player(move_direction)
            curr_pos = create_player.current_position
            print(f"Your position is: {curr_pos}")
            ip = create_map.victory(curr_pos)

            if ip == "Victory":
                print(ip)
                break

            # create_player.
        # SaveData.save_game()


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
