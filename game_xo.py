# Game X/O
def display_table(board: list):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def pl1_game_process(player_1: str, curr_tab: list):
    try:
        pl1_step = int(input(f"{player_1} your turn: "))
        if not str(pl1_step).isdigit:
            raise ValueError(f"{pl1_step} is not a digit.")
        if pl1_step not in range(0, 9):
            raise Exception("The number could not be < 0 or > 8")
    except ValueError as error:
        print(error)
        pl1_step = int(input("Give me a digit: "))
    except Exception as e:
        print(e)
        pl1_step = int(input("Give me a number in range(0, 9): "))

    if curr_tab[pl1_step] == "*":
        curr_tab[pl1_step] = "X"
        display_table(curr_tab)
    else:
        print("You cant input in this box, please try again! ")
        pl1_game_process(player_1, curr_tab)


def pl2_game_process(player_2: str, curr_tab: list):
    try:
        pl2_step = int(input(f"{player_2} your turn: "))
        if not str(pl2_step).isdigit:
            raise ValueError(f"{pl2_step} is not a digit.")
        if pl2_step not in range(0, 9):
            raise Exception("The number could not be < 0 or > 8")
    except ValueError as error:
        print(error)
        pl2_step = int(input("Give me a digit: "))
    except Exception as e:
        print(e)
        pl2_step = int(input("Give me a number in range(0, 9): "))

    if curr_tab[pl2_step] == "*":
        curr_tab[pl2_step] = "O"
        display_table(curr_tab)
    else:
        print("You cant input in this box, please try again! ")
        pl2_game_process(player_2, curr_tab)


def no_free_box(table: list) -> bool:
    b = True
    for item in table:
        if item == "*":
            b = False
    return b


def checking(tab: list):
    bul1 = True
    bul2 = True
    for i in range(0, 9, 3):
        if tab[i] == tab[i + 1] == tab[i + 2] == "X":
            bul1 = False
        elif tab[i] == tab[i + 1] == tab[i + 2] == "O":
            bul2 = False
    for i in range(3):
        if tab[i] == tab[i + 3] == tab[i + 6] == "X":
            bul1 = False
        elif tab[i] == tab[i + 3] == tab[i + 6] == "O":
            bul2 = False
    if tab[0] == tab[4] == tab[8] == "X":
        bul1 = False
    elif tab[0] == tab[4] == tab[8] == "O":
        bul2 = False
    elif tab[2] == tab[4] == tab[6] == "X":
        bul1 = False
    elif tab[2] == tab[4] == tab[6] == "O":
        bul2 = False

    return bul1, bul2


def winner_of_the_game(plr1, plr2, table: list):
    b = True
    if checking(table) == (False, True):
        print(f"Congratulations! {plr1} you won")
        b = False
    elif checking(table) == (True, False):
        print(f"Congratulations! {plr2} you won")
        b = False
    return b


def play_xo_game(pl1: str, pl2: str):
    tab = ["*", "*", "*",
           "*", "*", "*",
           "*", "*", "*"]
    p = 0
    while p < 5:
        pl1_game_process(pl1, tab)
        if not winner_of_the_game(pl1, pl2, tab):
            break
        if not no_free_box(tab):
            pl2_game_process(pl2, tab)
        if not winner_of_the_game(pl1, pl2, tab):
            break
        p += 1
    if checking(tab) == (True, True):
        print("No one won!")
    wish = input("Do you want to play again, please enter Yes or No? ")
    if wish == "Yes":
        play_xo_game(pl1, pl2)
    else:
        print("Thank you for game!")


player1 = input("Name of player1: ")
player2 = input("Name of player2: ")
print("Players please input numbers in (0, 8) ")
play_xo_game(player1, player2)
