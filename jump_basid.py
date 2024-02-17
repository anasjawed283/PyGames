import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Player settings
player_size = 50
player_color = (0, 128, 255)
player_speed = 5
jump_velocity = -12
gravity = 0.5

# Obstacle settings
obstacle_width = 30
obstacle_height = 30
obstacle_speed = 5
obstacle_color = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Game")

# Initialize the player
player_rect = pygame.Rect(WIDTH // 4, HEIGHT - player_size, player_size, player_size)
player_velocity_y = 0
on_ground = True

# Initialize the jumping block
jumping_block_rect = pygame.Rect(WIDTH - player_size * 2, HEIGHT - player_size * 2, player_size, player_size)

# Initialize obstacles
obstacles = []

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move player horizontally
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed

    # Jump when on the ground
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = jump_velocity
        on_ground = False

    # Apply gravity
    player_velocity_y += gravity
    player_rect.y += player_velocity_y

    # Check if the player is on the ground
    if player_rect.y >= HEIGHT - player_size:
        player_rect.y = HEIGHT - player_size
        on_ground = True

    # Move the jumping block
    jumping_block_rect.y -= player_velocity_y  # Move with the player's jump

    # Spawn new obstacles
    if random.randint(0, 100) < 5:
        obstacle = pygame.Rect(0, random.randint(0, HEIGHT - obstacle_height), obstacle_width, obstacle_height)
        obstacles.append(obstacle)

    # Move obstacles
    for obstacle in obstacles:
        obstacle.x += obstacle_speed
        if obstacle.right > WIDTH:
            obstacles.remove(obstacle)

        # Check collision with player
        if player_rect.colliderect(obstacle):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, WHITE, jumping_block_rect)
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
                 
