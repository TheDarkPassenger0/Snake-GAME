import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up the display
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set up the snake
snake_block = 10
snake_speed = 15

# Set up fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Functions for displaying score and message
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Snake function to draw
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Snake initial position
    x1 = width / 2
    y1 = height / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Clock to control the snake's speed
    clock = pygame.time.Clock()

    # Game loop
    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Boundary check: if the snake hits the boundary
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])

        # Snake body mechanics
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake collides with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Set the snake speed (frames per second)
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
