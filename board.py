import pygame

def render_board(board, ximg, oimg, graphical_board, screen):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))

            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                screen.blit(graphical_board[i][j][0], graphical_board[i][j][1])

def check_win(board, graphical_board, screen, winning_images, trophy_image):
    winner = None

    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]

            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                screen.blit(graphical_board[row][i][0], graphical_board[row][i][1])

            pygame.display.update()

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]

            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                screen.blit(graphical_board[i][col][0], graphical_board[i][col][1])

            pygame.display.update()

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]

        for i in range(3):
            graphical_board[i][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
            screen.blit(graphical_board[i][i][0], graphical_board[i][i][1])

        pygame.display.update()

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][2]

        for i in range(3):
            graphical_board[i][2 - i][0] = pygame.image.load(f"assets/Winning {winner}.png")
            screen.blit(graphical_board[i][2 - i][0], graphical_board[i][2 - i][1])

        pygame.display.update()

    if winner is not None:
        # Exibir o troféu
        trophy_image = pygame.image.load("assets/winner.png")
        trophy_image = pygame.transform.scale(trophy_image, (trophy_image.get_width() // 2, trophy_image.get_height() // 2))  # Redimensiona o troféu
        screen.blit(trophy_image, (screen.get_width() // 2 - trophy_image.get_width() // 2, screen.get_height() // 2 - trophy_image.get_height() // 2))

        # Exibir o texto do vencedor
        font = pygame.font.Font(None, 74)
        if winner == 'X':
            text = "player 1 ganhou!"
        else:
            text = "player 2 ganhou!"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + trophy_image.get_height() // 2 + 20))
        screen.blit(text_surface, text_rect)

        pygame.display.update()
        return winner

    # Verifica se o jogo terminou em empate
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"