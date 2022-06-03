import random

computer = ['R', 'P', 'S']
p = 'Paper'
r = 'Rock'
s = 'Scissors'


def game():
    computer_pick = random.choice(computer)
    pick_status = False

    while pick_status == False:
        player_pick = input(
            'choose between [Rock] R, [Paper] P, [Scissors] S \n').upper()

        if check_computer(player_pick) == check_player(computer_pick):
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print('No winner this is a draw')
            print('----------------------------------------------')
            game()

        elif check_computer(player_pick) == p and check_player(computer_pick) == r:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("player won this round")
        elif check_computer(player_pick) == p and check_player(computer_pick) == s:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("Computer won this round")
        elif check_computer(player_pick) == r and check_player(computer_pick) == p:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("Computer won this round")
        elif check_computer(player_pick) == r and check_player(computer_pick) == s:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("Player won this round")
        elif check_computer(player_pick) == s and check_player(computer_pick) == r:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("Computer won this round")
        elif check_computer(player_pick) == s and check_player(computer_pick) == p:
            pick_status = True
            print("Player (%s) : CPU (%s)" %
                  (check_computer(player_pick), check_player(computer_pick)))
            print("Player won this round")

        else:
            print("you've Picked an invalid option please try again")


def check_player(player):
    if player == 'R':
        return r
    if player == 'P':
        return p
    if player == 'S':
        return s


def check_computer(computer):
    if computer == 'R':
        return r
    if computer == 'P':
        return p
    if computer == 'S':
        return s


game()