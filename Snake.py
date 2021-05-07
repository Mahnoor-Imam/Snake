import pygame
import random

pygame.init()

WIDTH,HEIGHT = 600,400
SQUARE_SIZE = 10

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)


def display_score(score):
    text = SCORE_FONT.render("Your Score: " + str(score), True, YELLOW)
    window.blit(text, [0, 0])

def display_message(message):
    msg = FONT_STYLE.render(message, True, RED)
    window.blit(msg, [WIDTH / 8, HEIGHT / 4])

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(window, BLACK, [block[0], block[1], SQUARE_SIZE, SQUARE_SIZE])


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

def Game():
    game_over = False
    game_close = False

    x = WIDTH / 2
    y = HEIGHT / 2

    x_change = 0
    y_change = 0

    snack_x = round(random.randrange(0, WIDTH - SQUARE_SIZE) / 10.0) * 10.0
    snack_y = round(random.randrange(0, HEIGHT - SQUARE_SIZE) / 10.0) * 10.0

    snake = []
    snake_length = 1

    SPEED = 10
    SCORE_TARGET = 5
    SPEED_LEVEL = 1

    while not game_over:

        if SPEED_LEVEL < 10 and (snake_length - 1) >= SCORE_TARGET:
            SPEED += 2
            SCORE_TARGET += 5*SPEED_LEVEL
            SPEED_LEVEL += 1
        
        clock.tick(SPEED)

        while game_close:

            window.fill(BLUE)
            display_message("Game Over! Press Spacebar to play again")
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     game_over = True
                     game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SQUARE_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SQUARE_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SQUARE_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SQUARE_SIZE
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change
        window.fill(BLUE)
        pygame.draw.rect(window, GREEN, [snack_x, snack_y, SQUARE_SIZE, SQUARE_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)
        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake)
        #display_score(snake_length - 1)
        pygame.display.set_caption('Snake Game     Speed:  ' + str(SPEED_LEVEL) + '     Your Score:  ' + str(snake_length - 1))

        pygame.display.update()

        if x == snack_x and y == snack_y:
            snake_length += 1
            snack_x = round(random.randrange(0, WIDTH - SQUARE_SIZE) / 10.0) * 10.0
            snack_y = round(random.randrange(0, HEIGHT - SQUARE_SIZE) / 10.0) * 10.0

    pygame.quit()
    quit()

Game()