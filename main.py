import random

def main():
    randomDeck = []

    options = {
        "0": "R",
        "1": "P",
        "2": "S"
    }
    print("Randomizing both players card...")
    player1_card = []
    player2_card = []
    for j in range(100):
        randomDeck.append(random.randint(0, 99))
    for i in range(100):
        randomDeck[i] = randomDeck[i] % 3

    for k in range(3):
        player1_card.append(randomDeck[random.randint(0, len(randomDeck)-1)])
        player2_card.append(randomDeck[random.randint(0, len(randomDeck)-1)])

    print("You cards are:")
    for card in player1_card:
        print(options.get(str(card)))
    player1_card_selected = input('''Chose your card:
    R for r,
    P for paper,
    S for scissor
    ''')

    for z in range(0,3):
        player1_card[z] = options.get(str(player1_card[z]))

    if player1_card_selected.upper() not in player1_card:
        print("You don't have this card")
    else:
        player2_card_selected = player2_card[random.randint(0, 2)]

        print("computer drew: "+options.get(str(player2_card_selected)))

        game_result(player1_card_selected, options.get(str(player2_card_selected)))



def game_result(player_input, computer_input):
    if player_input.upper() == computer_input.upper():
        print("Game is draw")
    elif player_input.upper() == "R":
        if computer_input.upper() == "P":
            print("You lost")
        elif computer_input.upper() == "S":
            print("You won")
    elif player_input.upper() == "S":
        if computer_input.upper() == "P":
            print("You won")
        elif computer_input.upper() == "R":
            print("You lost")
    elif player_input.upper() == "P":
        if computer_input.upper() == "S":
            print("You lost")
        elif computer_input.upper() == "R":
            print("You won")
    else:
        print("This is not valid card")

if __name__ == "__main__":
    main()
