# author: Ngoc Bui
# Date: 2021.

def display():
    print(' '.join(str(e) for e in row1))
    print(' '.join(str(e) for e in row2))
    print(' '.join(str(e) for e in row3))


def win(cell, mark):
    if cell[0] == mark and cell[1] == mark and cell[2] == mark:
        return 1


def win_row():
    if win(row1, x) or win(row2, x) or win(row3, x) == 1:
        return 1
    if win(row1, o) or win(row2, o) or win(row3, o) == 1:
        return 2


def win_column():
    if win(column1, x) or win(column2, x) or win(column3, x) == 1:
        return 1
    if win(column1, o) or win(column2, o) or win(column3, o) == 1:
        return 2


def win_diagonal():
    if win(diagonal1, x) or win(diagonal2, x) == 1:
        return 1
    if win(diagonal1, o) or win(diagonal2, o) == 1:
        return 2


def win_final():
    if win_row() or win_column() or win_diagonal() == 1:
        return 1
    if win_row() or win_column() or win_diagonal() == 2:
        return 1


def location_cell(player, row, mark):
    i = 1
    while i <= 3:
        if player[1] == str(i):
            row[i - 1] = mark
        i = i + 1
    return row


def location_column(player, column, mark):
    i = 1
    while i <= 3:
        if player[0] == str(i):
            column[i - 1] = mark
        i = i + 1
    return column


def location_column_final(player, mark):
    if player[1] == '1':
        return location_column(player, column1, mark)
    elif player[1] == '2':
        return location_column(player, column2, mark)
    else:
        return location_column(player, column3, mark)


def location_diagonal(player, mark):
    if player[1] == player[0] and player[0] == '1':
        diagonal1[0] = mark
    elif player[1] == player[0] and player[0] == '3':
        diagonal1[2] = mark
    if player[0] == '1' and player[1] == '3':
        diagonal2[0] = mark
    elif player[0] == '3' and player[1] == '1':
        diagonal2[2] = mark
    if player[1] == player[0] and player[1] == '2':
        diagonal1[1] = mark
        diagonal2[1] = mark
    return diagonal1, diagonal2


print("Hello! Welcome you to my tic_tac_toe game!")


again = 'yes'
right_again = ['Yes', 'yes', 'No', 'no']
o = 'o'
x = 'x'

while True:
    ans = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    row1 = ans[0]
    row2 = ans[1]
    row3 = ans[2]

    column1 = [row1[0], row2[0], row3[0]]
    column2 = [row1[1], row2[1], row3[1]]
    column3 = [row1[2], row2[2], row3[2]]

    diagonal1 = [row1[0], row2[1], row3[2]]
    diagonal2 = [row1[2], row2[1], row3[0]]
    display()

    right_input = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
    right_answer1 = []
    right_answer2 = []

    while win_final() != 1:
        player1 = input("Player 1 put the location of x(ex: Enter 12 for row 1 - column 2): ")
        while player1 not in right_input or player1 in right_answer2 or player1 in right_answer1:
            if player1 not in right_input:
                player1 = input("Your enter is wrong, please enter again: ")
            if player1 in right_answer2:
                player1 = input("Please enter again, you entered a place that the other player already put: ")
            if player1 in right_answer1:
                player1 = input("You already entered this location, please enter again another location: ")
        right_answer1.append(player1)
        if player1[0] == '1':
            location_cell(player1, row1, x)
            location_column_final(player1, x)
            location_diagonal(player1, x)
        elif player1[0] == '2':
            location_cell(player1, row2, x)
            location_column_final(player1, x)
            location_diagonal(player1, x)
        else:
            location_cell(player1, row3, x)
            location_column_final(player1, x)
            location_diagonal(player1, x)
        display()
        if win_row() or win_column() or win_diagonal() == 1:
            print("Player 1 win! Game end.")
            break
        if '-' not in row1 and '-' not in row2 and '-' not in row3:
            print("Draw! Game end.")
            break
        player2 = input("Player 2 enter location of o(ex: enter 1,2 for row 1 - column 2): ")
        while player2 not in right_input or player2 in right_answer1 or player2 in right_answer2:
            if player2 not in right_input:
                player2 = input("Your enter is wrong, please enter again: ")
            if player2 in right_answer1:
                player2 = input("Please enter again, you entered a place that the other player already put: ")
            if player2 in right_answer2:
                player2 = input("You already entered this location, please enter again another location: ")
        right_answer2.append(player2)
        if player2[0] == '1':
            location_cell(player2, row1, o)
            location_column_final(player2, o)
            location_diagonal(player2, o)
        elif player2[0] == '2':
            location_cell(player2, row2, o)
            location_column_final(player2, o)
            location_diagonal(player2, o)
        else:
            location_cell(player2, row3, o)
            location_column_final(player2, o)
            location_diagonal(player2, o)
        display()
        if win_row() or win_column() or win_diagonal() == 2:
            print("Player 2 win! Game end.")
    again = input("You want to play again?(enter Yes or No): ")
    while again not in right_again:
        again = input("Just enter 'yes' or 'no' please: ")
    if again == 'No' or again == 'no':
        print("Okay, see ya next time!")
        break
