# Conway's Game of Life
#
# Instructions:
# - Left click with a mouse to add or remove a life
# - Press → to go to the next generation
# - Press space to go to the next generation automatically
# - Press R to rest the game

from math import floor
from copy import deepcopy
import pygame

pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
ROWS = 50
COLUMNS = 50
COLOR = (255, 255, 255)

done = False
next_gen = False
game = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting up the game
for row in range(ROWS):
    game.append([])
    for column in range(COLUMNS):
        game[row].append(False)

def next_generation():
    next_gen = deepcopy(game)
    for row in range(len(game)):
        for column in range(len(game[row])):
            neighbors = 0
            for r in range(row - 1, row + 2):
                for c in range(column - 1, column + 2):
                    if not (r == row and c == column):
                        if game[r if r < ROWS else 0][c if c < COLUMNS else 0]:
                            neighbors += 1
            if (neighbors == 3 and not game[row][column]) or (2 <= neighbors <= 3 and game[row][column]):
                next_gen[row][column] = True
            else:
                next_gen[row][column] = False
    return next_gen

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            game[floor(pygame.mouse.get_pos()[1] / (WIDTH / ROWS))][floor(pygame.mouse.get_pos()[0] / (HEIGHT / COLUMNS))] = not game[floor(pygame.mouse.get_pos()[1] / (WIDTH / ROWS))][floor(pygame.mouse.get_pos()[0] / (HEIGHT / COLUMNS))]
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                game = next_generation()
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                next_gen = not next_gen
            if pygame.key.get_pressed()[pygame.K_r]:
                game = []
                for row in range(ROWS):
                    game.append([])
                    for column in range(COLUMNS):
                        game[row].append(False)
    if next_gen:
        game = next_generation()
        pygame.draw.polygon(screen, (0, 125, 0), [(12, 10), (35, 25), (12, 40)])
    else:
        pygame.draw.rect(screen, (0, 125, 0), pygame.Rect(10, 10, 10, 30))
        pygame.draw.rect(screen, (0, 125, 0), pygame.Rect(30, 10, 10, 30))

    for row in range(len(game)):
        for column in range(len(game[row])):
            if game[row][column]:
                pygame.draw.rect(screen, COLOR, pygame.Rect((HEIGHT / COLUMNS) * column, (WIDTH / ROWS) * row, WIDTH / ROWS, HEIGHT / COLUMNS))
    
    pygame.display.flip()
pygame.quit()