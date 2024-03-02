import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
MOLE_SIZE = 50
FPS = 60
GAME_DURATION = 20  # in seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hit the Mole")

# Game variables
score = 0
moles = []
start_time = pygame.time.get_ticks()

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for mole in moles:
                if mole.collidepoint(mouse_x, mouse_y):
                    moles.remove(mole)
                    score += 1

    # Generate a new mole at random positions
    if random.randint(0, 100) < 5:  # 5% chance of a mole appearing
        mole_x = random.randint(0, WIDTH - MOLE_SIZE)
        mole_y = random.randint(0, HEIGHT - MOLE_SIZE)
        moles.append(pygame.Rect(mole_x, mole_y, MOLE_SIZE, MOLE_SIZE))

    # Draw everything
    screen.fill(BLACK)

    for mole in moles:
        pygame.draw.rect(screen, RED, mole)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Display timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, GAME_DURATION - elapsed_time)
    timer_text = font.render(f"Time: {remaining_time}s", True, WHITE)
    screen.blit(timer_text, (10, 50))

    # Check game over condition
    if remaining_time == 0:
        print(f"Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
