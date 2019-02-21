
def create_board():
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'W', 'B', '.', '.', '.'],
             ['.', '.', '.', 'B', 'W', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
    return board


"""---Create the board---"""


def print_board(board):
    list_alp = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in list_alp:
        print(i, end=' ')
    print('')
    for i in range(len(board)):
        print(str(i+1), *board[i])


"""---Print the board---"""


def inverse(team):
    return Black if team is White else White


"""---Opponent---"""


def char_to_pos(cell):    # ma hoa vi tri ban co    #VD: 'c5' thanh '42'
    cell = str(int(cell[1]) - 1) + str(col.index(cell[0]))
    return cell


def pos_to_char(cell):  # giai ma vi tri ban co (nguoc lai voi ben tren) 42->c5
    cell = str(int(cell[0])+1) + col[int(cell[1])]  # 42 -> 5c
    cell = cell[::-1]
    return cell


"""---Ma~ hoa' vi. tri'---"""


def test_valid_move(board, cell, team):
    y = int(cell[0])
    x = int(cell[1])
    if board[y][x] != '.':
        return False
    for direct in directions:
        y = int(cell[0])
        x = int(cell[1])
        y = y + direct[0]
        x = x + direct[1]
        while 0 <= y <= 7 and 0 <= x <= 7 and board[y][x] == inverse(team):
            y += direct[0]
            x += direct[1]
            if board[y][x] == team:
                return True
    return False


"""---Kiem tra vi tri---"""


def find_valid_move(board, team):
    valid_choices = []
    for y in range(8):
        for x in range(8):
            if test_valid_move(board, str(y) + str(x), team):
                valid_choices.append(str(y) + str(x))
    return valid_choices


"""---Tim valid choices---"""


def place_piece(board, move, team):
    move = char_to_pos(move)
    y = int(move[0])
    x = int(move[1])
    board[y][x] = team
    for direct in directions:
        y = int(move[0])
        x = int(move[1])
        y = y + direct[0]
        x = x + direct[1]
        if not (0 <= y <= 7 and 0 <= x <= 7):
            break
        while 0 <= y <= 7 and 0 <= x <= 7:
            if board[y][x] == '.':
                break
            if board[y][x] == team:
                turned(board, move, team, direct)
                break
            y += direct[0]
            x += direct[1]


"""---Dat quan co---"""


def turned(board, move, team, direct):
    y = int(move[0]) + direct[0]
    x = int(move[1]) + direct[1]
    while board[y][x] == inverse(team):
        board[y][x] = team
        y += direct[0]
        x += direct[1]


"""---Quan ben nay an quan ben kia---"""


def game_loop(board, team):
    while(True):
        try:
            while len(find_valid_move(board, team)) > 0:
                print_board(board)
                choices = find_valid_move(board, team)
                print('Valid choices: ', end=' ')
                for i in range(len(choices)):
                    choices[i] = pos_to_char(choices[i])
                    print(choices[i], end=' ')
                print('')
                print('Player', team + ':', end='')
                move = input(' ')
                while move not in choices:
                    print(move + ':', 'Invalid choice')
                    move = input('Player B: ')
                place_piece(board, move, team)
                team = inverse(team)
            print('Player', team, 'cannot play')
            team = inverse(team)
        except IndexError:
            pass


"""---Cho game chay di chay lai---"""

Black = 'B'
White = 'W'
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0],
              [1, -1], [0, -1], [-1, -1]]
col = 'abcdefgh'
board = create_board()
team = Black
while len(find_valid_move(board, team)) > 0 or \
len(find_valid_move(board, inverse(team))) > 0:
    game_loop(board, team)
point_b, point_w = 0, 0
for i in range(8):
    point_w += board[i].count(Black)
    point_b += board[i].count(White)
print('End of the game. W: %d, B: %d' % (point_w, point_b))
if point_b == point_w:
    print('Draw')
else:
    print('%s wins' % (Black if point_b > point_w else White))
