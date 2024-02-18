import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
FPS = 60
FONT_SIZE = 36

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Speed Check")

# Initialize the font
font = pygame.font.Font(None, FONT_SIZE)

# Game loop
clock = pygame.time.Clock()

start_time = None
clicks = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start_time is None:
                    start_time = time.time()
                clicks += 1

    # Check if 10 seconds have passed
    if start_time is not None and time.time() - start_time >= 10:
        running = False

    # Draw everything
    screen.fill(BLACK)

    # Display the clicks
    clicks_text = font.render(f"Clicks: {clicks}", True, WHITE)
    screen.blit(clicks_text, (WIDTH // 2 - clicks_text.get_width() // 2, HEIGHT // 2 - FONT_SIZE // 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Calculate clicks per second
cps = clicks / 10 if clicks > 0 else 0

# Display the result
result_text = font.render(f"Clicks per Second: {cps:.2f}", True, WHITE)
screen.fill(BLACK)
screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2 - FONT_SIZE // 2))
pygame.display.flip()

# Wait for a moment before exiting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
sys.exit()
