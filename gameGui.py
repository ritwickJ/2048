import pygame
from pygame.locals import *
import numpy as np
from util import colors, W, H, SPACING
import game

def draw_game(screen, grid, myfont, N):
    screen.fill(colors['back'])

    for i in range(N):
        for j in range(N):
            n = grid[i][j]

            rect_x = j * W // N + SPACING
            rect_y = i * H // N + SPACING
            rect_w = W // N - 2 * SPACING
            rect_h = H // N - 2 * SPACING

            pygame.draw.rect(screen,
                             colors[n],
                             pygame.Rect(rect_x, rect_y, rect_w, rect_h),
                             border_radius=8)
            if n==0:
                n = ""
            text_surface = myfont.render(f'{n}', True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(rect_x + rect_w/2,
                                                      rect_y + rect_h/2))
            screen.blit(text_surface, text_rect)


def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 'q'
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    return 'u'
                elif event.key == K_RIGHT:
                    return 'r'
                elif event.key == K_LEFT:
                    return 'l'
                elif event.key == K_DOWN:
                    return 'd'
                elif event.key == K_q or event.key == K_ESCAPE:
                    return 'q'


def main():
    N = int(input('enter N for NxN grid : '))
    b = game.Board(N)
    
    pygame.init()
    pygame.display.set_caption("2048")

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)

    screen = pygame.display.set_mode((W, H))

    game_over = False
    while not game_over:
        draw_game(screen, b.board, myfont, N)
        pygame.display.flip()
        key = wait_for_key()
        if key == 'q':
            game_over = True
            pygame.quit()
        elif key == 'u':
            game_over = b.up()
        elif key == 'd':
            game_over = b.down()
        elif key == 'l':
            game_over = b.left()
        elif key == 'r':
            game_over = b.right()
        else:
            continue
        
        if game_over:
            pygame.quit()
    
    print(f'game over! score = {b.score}')

    print('history')
    b.print_history()
            

if __name__ == "__main__":
    main()