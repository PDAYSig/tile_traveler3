from random import randint

def get_coin():
    amount_of_coins = randint(1,10)
    ### Randomize later on
    return amount_of_coins

def game_over():
    while True:
        print("GAME OVER!!!")

def lever_pull():
    ### Randomize later on
    chance = randint(1,100)
    death = 67

    if death == chance:
        return game_over()

    return get_coin()

def move():
    pass

def available_moves():
    pass

def update_location(location: tuple, move_direction: str):
    x, y = location
    if move_direction == "n":
        y += 1
    elif move_direction == "e":
        x += 1
    elif move_direction == "s":
        y -= 1
    elif move_direction == "w":
        x -= 1
    
    location == (x, y)
    return location


