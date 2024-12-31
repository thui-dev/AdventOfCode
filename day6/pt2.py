from copy import deepcopy
import os

from pt1 import actions, result, init_pos

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
    board = [list(line) for line in open("demo.txt").read().split('\n')]
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