def actions(board, pos, dir):

    directions = [
        [-1,0], [0, 1],
        [1, 0], [0,-1],
    ]

    new_pos_x = pos[0] + directions[dir%4][0]
    new_pos_y = pos[1] + directions[dir%4][1]
    try:
    #if obstruction, change dir to right
        if board[new_pos_x][new_pos_y] == '#':
            return actions(board, pos, dir+1)
    except: return None

    #else, next pos is fine. return it
    return ((new_pos_x, new_pos_y), dir)


def result(board, pos, action):
    board[pos[0]][pos[1]] = 'X'
    return board


def init_pos(board):
    for line_index, line in enumerate(board):
        for col_index, item in enumerate(line):
            if item == '^':
                return (line_index, col_index)
    raise Exception("No player found in board. Expected '^' somewhere.")

def main():

    f = open("../input.txt").read().split('\n')

    board = [list(line) for line in f]
    pos = init_pos(board)
    dir = 0

    while actions(board, pos, dir) is not None:
        action, dir = actions(board, pos, dir)
        board = result(board, pos, action)
        pos = action

    print(sum([i.count('X') for i in board])+1)

main()