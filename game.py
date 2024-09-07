import pygame
from board import render_board

def add_XO(board, graphical_board, to_move, x_img, o_img, screen):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2

    if board[round(converted_y)][round(converted_x)] not in ['O', 'X']:
        board[round(converted_y)][round(converted_x)] = to_move
        to_move = 'O' if to_move == 'X' else 'X'
    
    render_board(board, x_img, o_img, graphical_board, screen)

    return board, to_move

def reset_game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    graphical_board = [[[None, None], [None, None], [None, None]], 
                        [[None, None], [None, None], [None, None]], 
                        [[None, None], [None, None], [None, None]]]
    to_move = 'X'
    game_finished = False
    
    return board, graphical_board, to_move, game_finished