board = ["*", "*", "*",
         "*", "*", "*",
         "*", "*", "*"]

# definirea tablei cu identificarea pozitiei 1-9 (legenda idenxurilor)


def display_board():

    print(board[0] + "|" + board[1] + "|" + board[2] + "     1 | 2 | 3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "     4 | 5 | 6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "     7 | 8 | 9")


display_board()


# def jucatorul_curent():
#     print('primul jucator este' + "x")


starting_player = input('Alege cine incepe x sau o ')
while starting_player != 'x' and starting_player != 'o':
    print("nu ai facut o optiune corecta, alege x sau o pentru a putea juca")
    starting_player = input('Alege cine incepe x sau o ')
print("ai ales bine")


position = input('alege o pozitie de la 1 la 9  ')
while position != ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print('trebuie sa alegi din pozitiile libere de la 1 la 9')
    position = input('alege o pozitie de la 1 la 9  ')
current_player = starting_player
print(current_player + "'s turn")
position = input('alege o pozitie de la 1 la 9  ')
# verifica daca user-ul introduce o valoare corecta si ca locul vizat este liber
valid = False
while not valid:
    # Verifica
