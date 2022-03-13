import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

o=1
while(o==1):
    print(play())
    o=int(input("\nDo you want to continue playing?\nEnter 1 to continue, 0 to abort.\n"))

print("\n\nWe are friends now, come and play with me again sometime :)\n")