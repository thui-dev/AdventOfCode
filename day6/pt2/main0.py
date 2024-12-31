from copy import deepcopy
import os

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
    #if out of bounds, finished the maze. stop everything.
    except: return None

    #else, new_pos is fine. return it
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

def run_maze(board, pos):

    dir = 0
    explored = set()

    while actions(board, pos, dir) is not None:

        action, dir = actions(board, pos, dir)
        board = result(board, pos, action)
        pos = action

        if (action, dir%4) in explored:
            return True
        else:
            explored.add((action, dir%4))
    return False


def main():
    board = [list(line) for line in open("../input.txt").read().split('\n')]
    pos = init_pos(board)
    path = deepcopy(board)

    dir = 0
    while actions(board, pos, dir) is not None:
        action, dir = actions(board, pos, dir)
        pos = action
        path[pos[0]][pos[1]] = 'X'
    #print(*path, sep='\n')
    pos = init_pos(board)
    
    loops = 0
    for i, line in enumerate(path):
        for j, item in enumerate(line):

            if item != 'X':
                continue

            new_board = deepcopy(board)
            new_board[i][j] = '#'
            if run_maze(new_board, pos):
                loops += 1

        os.system('cls')
        print(f"analisando {i} de {len(board)} linhas em board")

    #os.system('cls')
    print(loops)

main()