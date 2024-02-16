import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SPEED = 8
BLOCK_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

# Initialize the player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 50, 50, 50)

# Initialize the bullets
bullets = []

# Initialize the blocks
blocks = []

# Create a new block at random intervals
def create_block():
    block_width = random.randint(20, 50)
    block_height = random.randint(20, 50)
    block_x = random.randint(0, WIDTH - block_width)
    block_y = 0
    block = pygame.Rect(block_x, block_y, block_width, block_height)
    blocks.append(block)

# Game loop
clock = pygame.time.Clock()
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-PLAYER_SPEED, 0)
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.move_ip(PLAYER_SPEED, 0)

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        bullet = pygame.Rect(player.centerx - 5, player.top - 10, 10, 10)
        bullets.append(bullet)

    # Move the bullets
    for bullet in bullets:
        bullet.move_ip(0, -10)
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Create blocks at random intervals
    if random.randint(0, 100) < 5:
        create_block()

    # Move the blocks
    for block in blocks:
        block.move_ip(0, BLOCK_SPEED)
        if block.top > HEIGHT:
            blocks.remove(block)
            score += 1

    # Check collisions between bullets and blocks
    for bullet in bullets:
        for block in blocks:
            if bullet.colliderect(block):
                bullets.remove(bullet)
                blocks.remove(block)
                score += 10

    # Check collisions between player and blocks
    for block in blocks:
        if player.colliderect(block):
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for block in blocks:
        pygame.draw.rect(screen, WHITE, block)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
