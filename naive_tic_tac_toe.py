size = 3
row, column = (size,size)
my_game = [[' ' for i in range(column)] for j in range(row)]
def print_ui(my_game):
    for item in my_game:
        print(item)
print_ui(my_game)
playing = True

def is_win(board, x, y, choice):
    r, c, d, ad = 0, 0, 0, 0
    for i in range(size):
        if (board[x][i] == choice):  r=r+1
        if (board[i][y] == choice):  c=c+1
        if (board[i][i] == choice):  d=d+1
        if (board[i][size - 1 - i] == choice):  ad=ad+1
    return r == size or c == size or d == size or ad == size

def user_input(board, username):
    reinput = True
    while reinput:
        value = input(f"User {username} choice: ")
        if (not value.isdigit or len(value) != 2):
            print("Input 2 number pls")
            continue
        (row, column) = (int(value[0]), int(value[0]))
        if (not (0 <= row < 3) and not (0 <= column < 3)):
            print(f"Input range 0 - {size}")
            continue
        if (board[row][column] != ' '):
            print(f"Row {row} {column} already selected")
            continue
        return (row, column)
    
def user_play(board, username, maker):
    value = user_input(board, username)
    board[int(value[0])][int(value[1])] = maker
    print_ui(board)
    if (is_win(board, int(value[0]), int(value[1]), maker)):
        print(f"{maker} win")
        return False
    return True

while playing:
    playing = user_play(my_game, "Phuc", "x")
    if (not playing):
        break
    playing = user_play(my_game, "Le Anh", "o")

