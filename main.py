import pygame, sys
from assets import load_assets
from board import check_win
from game import add_XO, reset_game

pygame.init()

WIDTH, HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

BG_COLOR = (214, 201, 227)
BOARD, X_IMG, O_IMG, WINNING_IMAGES, TROPHY_IMAGE = load_assets()

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]

to_move = 'X'
game_finished = False

SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move, X_IMG, O_IMG, SCREEN)

            if game_finished:
                board, graphical_board, to_move, game_finished = reset_game()
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))
                pygame.display.update()
            
            if check_win(board, graphical_board, SCREEN, WINNING_IMAGES, TROPHY_IMAGE) is not None:
                game_finished = True
            
            pygame.display.update()