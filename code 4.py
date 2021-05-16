import random
coin =('heads','tails')
heads, tails = 0, 0
games=0
print('Hit x to exit')
while True:
    flip= random.choice(coin)
    your_choice = input('Type heads or tails')
    if your_choice == 'x' or your_choice =='X':
        print("GAME OVER :(")
        print('Coin flipping stats:')
        print('Games played = {}'.format(games))
        print('heads = {}'.format(heads))
        print('tails = {}'.format(tails))
        break
    if your_choice == flip:
        print('Coin landed on {}. Yeah boi you win!'.
              format(flip))
        games += 1
    else:
        print("Uh oh. Coin landed on {}. Better luck next time"
              .format(flip))
        games += 1
    if flip == 'heads':
        heads += 1
    elif flip == 'tails':
        tails += 1