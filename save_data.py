class SaveData:
    SAVE_FILE = "save_file.txt"
    @staticmethod
    def save_game(
            map : dict[tuple, str],
            player_tile : tuple[int, int],
            winning_tile : tuple[int, int],
            coin_tally : int,
            unflipped_levers : list[tuple]
        ) -> None:
        save_state = open(SaveData.SAVE_FILE, "w+", encoding="utf-8")
        for tile in map:
            save_state.write(f"{tile} {map[tile]}\n")
        save_state.write(f"{player_tile}\n")
        save_state.write(f"{winning_tile}\n")
        save_state.write(f"{coin_tally}\n")
        save_state.write(f"{[lever_position for lever_position in unflipped_levers]}")


    @staticmethod
    def load_game():
        pass