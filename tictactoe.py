import numpy as np
import pygame
import sys

ROWS = 3
COLUMNS = 3
board = np.zeros((ROWS, COLUMNS))
game_over = False
WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
CIRCLE = pygame.image.load('circle.png')
CROSS  = pygame.image.load('x.png')

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

def is_wining_move(window, player):
    if player == 1:
        winning_color = BLUE
    else:
        winning_color = RED
    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            pygame.draw.line(window, winning_color, (10, (r*200)+100), (WIDTH-10, (r*200)+100),10)
            return True
    for c in range(ROWS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            pygame.draw.line(window, winning_color, ((c*200)+100,10), ((c*200)+100,HEIGHT-10) ,10)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, winning_color, (10,10),(590,590) ,10)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        pygame.draw.line(window, winning_color, (590,10),(100,590) ,10)
        return True

def draw_lines():
    pygame.draw.line(window, BLACK, (200,0),(200,600),10)
    pygame.draw.line(window, BLACK, (400,0),(400,600),10)
    pygame.draw.line(window, BLACK, (0,200),(600,200),10)
    pygame.draw.line(window, BLACK, (0,400),(600,400),10)

def draw_board(window):
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                window.blit(CIRCLE, ((c*200)+50, (r*200)+50))
            elif board[r][c] == 2:
                window.blit(CROSS, ((c*200)+50, (r*200)+50))
    pygame.display.update()


def main(game_over):
    turn = 0
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn % 2 == 0:
                    #p1
                    row = event.pos[1]//200
                    col = event.pos[0]//200
                    if is_valid_mark(row, col):
                        mark(row, col, 1)
                        if is_wining_move(window,1):
                            game_over = True
                    else:
                        turn = turn - 1
                else:
                    #p2
                    row = event.pos[1]//200
                    col = event.pos[0]//200
                    if is_valid_mark(row, col):
                        mark(row, col, 2)
                        if is_wining_move(window,2):
                            game_over = True
                    else:
                        turn =  turn - 1
                turn = turn +  1
                print(board)
                draw_board(window)

        if is_board_full():
            game_over = True

        if game_over:
            print("Game Over")
            pygame.time.wait(2000)
            board.fill(0)
            window.fill(WHITE)
            draw_lines()
            draw_board(window)
            game_over = False
            pygame.display.update()



pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TIC TAC TOE")
window.fill(WHITE)
draw_lines()
pygame.display.update()


if __name__ == '__main__':
    main(game_over)
