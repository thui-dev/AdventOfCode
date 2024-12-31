LOOPS = 0

def search_loop(board, pos, dir):

    global LOOPS

    new_pos, new_dir = actions(board, pos, dir+1, SEARCH_LOOPS=False)
    while True:
        
        if actions(board, new_pos, new_dir, SEARCH_LOOPS=False) is None:
            return None

        new_pos, new_dir = actions(board, new_pos, new_dir, SEARCH_LOOPS=False)
        if dir % 2 == 0: #if dir we first bumped == vertical
            if new_pos[1] == pos[1]:
                LOOPS += 1
                return None
        else: #if dir we first bumped == horizontal
            if new_pos[0] == pos[0]:
                LOOPS += 1
                return None
        if new_dir == dir+4:
            return None


def actions(board, pos, dir, SEARCH_LOOPS):
    
    directions = [
        [-1,0], [0, 1],
        [1, 0], [0,-1],
    ]

    new_pos_x = pos[0] + directions[dir % 4][0]
    new_pos_y = pos[1] + directions[dir % 4][1]

    try:
    #if obstruction, change dir to right
        if board[new_pos_x][new_pos_y] == '#':
            if SEARCH_LOOPS == True:
                search_loop(board, pos, dir)
            return actions(board, pos, dir+1, SEARCH_LOOPS=False)

    #if out of bounds, finished the maze. stop everything.
    except: return None

    #else, new_pos is fine. return it
    return ((new_pos_x, new_pos_y), dir)


def result(board, pos):
    board[pos[0]][pos[1]] = 'X'
    return board


def init_pos(board):
    for line_index, line in enumerate(board):
        for col_index, item in enumerate(line):
            if item == '^':
                return (line_index, col_index)
    raise Exception("No player found in board. Expected '^' somewhere.")

def main():

    board = [list(line) for line in open("../demo.txt").read().split('\n')]
    pos = init_pos(board)
    dir = 0

    while actions(board, pos, dir, SEARCH_LOOPS=False) is not None:
        action, dir = actions(board, pos, dir, SEARCH_LOOPS=True)
        board = result(board, pos)
        pos = action

    print(LOOPS)

main()