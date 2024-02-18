import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Bat settings
BAT_WIDTH = 80
BAT_HEIGHT = 10
BAT_SPEED = 10

# Ball settings
BALL_RADIUS = 10
BALL_SPEED = 5

# Brick settings
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
NUM_BRICKS_ROW = 10
NUM_BRICKS_COL = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Shooter Game")

# Initialize the bat
bat_rect = pygame.Rect(WIDTH // 2 - BAT_WIDTH // 2, HEIGHT - BAT_HEIGHT - 10, BAT_WIDTH, BAT_HEIGHT)

# Initialize the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.choice([-1, 1]) * BALL_SPEED, -BALL_SPEED]

# Initialize bricks
bricks = []
for row in range(NUM_BRICKS_COL):
    for col in range(NUM_BRICKS_ROW):
        brick_rect = pygame.Rect(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5), BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick_rect)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the bat
    if keys[pygame.K_LEFT] and bat_rect.left > 0:
        bat_rect.x -= BAT_SPEED
    if keys[pygame.K_RIGHT] and bat_rect.right < WIDTH:
        bat_rect.x += BAT_SPEED

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Check collisions with walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        ball_speed[0] *= -1
    if ball_pos[1] <= 0:
        ball_speed[1] *= -1

    # Check collision with bat
    if ball_pos[1] + BALL_RADIUS >= bat_rect.top and ball_pos[0] >= bat_rect.left and ball_pos[0] <= bat_rect.right:
        ball_speed[1] *= -1

    # Check collision with bricks
    for brick in bricks:
        if ball_pos[1] - BALL_RADIUS <= brick.bottom and ball_pos[0] >= brick.left and ball_pos[0] <= brick.right:
            bricks.remove(brick)
            ball_speed[1] *= -1

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, bat_rect)
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
