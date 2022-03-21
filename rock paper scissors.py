import random


def rps(name):
    nickname = name

    player_win_count = 0
    ai_win_count = 0

    player_choices = ["Rock", "Paper", "Scissors"]

    print(f"Hi, {nickname}. \n P = Paper \n S = Scissors \n R = Rock")
    while player_win_count < 3 and ai_win_count < 3:
        ai = random.choice(player_choices)

        player = choose_shape()

        if player == "Scissors" and ai == "Paper" or \
                player == "Rock" and ai == "Scissors" or \
                player == "Paper" and ai == "Rock":

            player_win_count += 1
            happy(nickname, player_win_count, ai_win_count)

        elif player == ai:
            print("Boo. The game is draw. Restarting the game.")

        else:
            ai_win_count += 1
            print("'Sad noises' You lost.")
            sadge(nickname, player_win_count, ai_win_count)

    if player_win_count >= 3 or ai_win_count >= 3:
        calculate_result(nickname, ai_win_count, player_win_count)


def choose_shape():
    shape = input("Type your choices, P, R, S: ").upper()

    if shape == "P":
        return "Paper"

    elif shape == "S":
        return "Scissors"

    elif shape == "R":
        return "Rock"

    else:
        choose_shape()


def happy(nickname, player_win_count, ai_win_count):
    print(f"Yay! you won! {nickname}"
          f"\nYou won round\n\tYour score is currently {player_win_count}\n\t"
          f"My score is currently {ai_win_count}")


def sadge(nickname, player_win_count, ai_win_count):
    print(f"Boo. You lost {nickname}"
          f"You lost round\n\tYour score is currently {player_win_count}\n\t"
          f"My score is currently {ai_win_count}")


def calculate_result(nickname, player_win_count, ai_win_count):
    print("========================================================")
    if player_win_count > ai_win_count:
        difference = player_win_count - ai_win_count
        print(f"congratulations! you won game by {difference} point(s) difference.")

    elif player_win_count < ai_win_count:
        difference = ai_win_count - player_win_count
        print(f"Boo. You lost by {difference} point(s) difference")

    end_game = input("DO you want to continue the game? (Y/N): ").upper()

    if end_game == "Y":
        rps(name)

# Main routine
print()
print("====================================================")
print("RPS game \nRPS stands for Rock, Paper, Scissors. Beat the computer by guess what the A.I is going to draw!")
name = input("What is your name?: ")
rps(name)
print("Thank you for playing my game")

# I do not know why this code is not running properly.
