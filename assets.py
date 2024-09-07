import pygame, os
os.chdir('C:/game_projects/jogo_da_velha')

def load_assets():
    board = pygame.image.load("assets/Board.png")
    x_img = pygame.image.load("assets/X.png")
    o_img = pygame.image.load("assets/O.png")
    winning_images = {
        'X': pygame.image.load("assets/Winning X.png"),
        'O': pygame.image.load("assets/Winning O.png")
    }
    trophy_image = pygame.image.load("assets/winner.png")
    return board, x_img, o_img, winning_images, trophy_image