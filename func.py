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

def current_location():
    # 
    pass