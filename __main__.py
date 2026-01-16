"""The Game Loop"""

from map import Map
from player import Player
from save_data import SaveData


def main():
    """Run The Game Loop"""

    load_command: str = start_screen()

    # Create New Game
    if load_command == "N":
        main_map: Map = Map((3, 3))
        main_player: Player = Player(0, 0, main_map)
    # Continue GAme
    else:
        # TODO: Load Game
        main_map = ...
        main_player = ...
        SaveData.load_game()

    # Get player data

    # Initializes the player and map when starting

    # Run the game loop for player

    while True:
        # Movement options and current position
        moves: str = main_player.display_available_moves()
        current_pos: tuple[int, int] = main_player.current_position

        # Save game here?
        print("-" * 30)
        print("Type c to See amount of coins")
        print(moves)

        move_direction: str = input("> ").lower()

        # See Amount of Coins
        if move_direction == "c" or move_direction == "coins":
            print(f"You have {main_player.coins} Coins")
            continue

        if move_direction in main_map.availableMoves(current_pos):
            main_player.move_player(move_direction)

            print(f"Your position is: {current_pos}")

            # Check for lever
            if main_player.lever_check():
                print("This Tile Has A Lever")
                print("Do You Want To Pull It: Y/N")

                pull: str = input("> ").lower()
                if pull == "y":
                    death_or_coins: int | str = main_player.lever_pull()
                    if death_or_coins == "GAME_OVER":
                        print("You Were Unlucky And Lost The Game")
                        break

                    print(f"You Got {death_or_coins} Coins")

                else:
                    print("You Decided Not To Pull The Lever")

            # Check if won
            victory_message: str | None = main_map.victory(current_pos)
            if victory_message == "Victory":
                print(victory_message)
                break

        else:
            print("That Is Not A Valid Direction\nTry Again")

        # TODO: SaveData.save_game()


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
