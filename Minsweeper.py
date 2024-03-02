import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
NUM_MINES = 40
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Initialize the grid
grid = [[0 for _ in range(WIDTH // GRID_SIZE)] for _ in range(HEIGHT // GRID_SIZE)]
revealed = [[False for _ in range(WIDTH // GRID_SIZE)] for _ in range(HEIGHT // GRID_SIZE)]
mines = []

# Generate random mine positions
for _ in range(NUM_MINES):
    mine_x = random.randint(0, len(grid[0]) - 1)
    mine_y = random.randint(0, len(grid) - 1)

    while grid[mine_y][mine_x] == -1:
        mine_x = random.randint(0, len(grid[0]) - 1)
        mine_y = random.randint(0, len(grid) - 1)

    grid[mine_y][mine_x] = -1
    mines.append((mine_x, mine_y))

# Set the numbers around mines
for mine_x, mine_y in mines:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            new_x, new_y = mine_x + dx, mine_y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] != -1:
                grid[new_y][new_x] += 1

# Game loop
clock = pygame.time.Clock()

def reveal_cell(x, y):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and not revealed[y][x]:
        revealed[y][x] = True
        if grid[y][x] == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    reveal_cell(x + dx, y + dy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cell_x, cell_y = mouse_x // GRID_SIZE, mouse_y // GRID_SIZE

            if event.button == 1:  # Left-click
                if (cell_x, cell_y) in mines:
                    # Game over if mine is clicked
                    print("Game Over!")
                    pygame.quit()
                    sys.exit()
                else:
                    reveal_cell(cell_x, cell_y)
            elif event.button == 3:  # Right-click
                revealed[cell_y][cell_x] = not revealed[cell_y][cell_x]

    # Draw everything
    screen.fill(GRAY)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if revealed[y][x]:
                pygame.draw.rect(screen, WHITE, rect)
                if grid[y][x] > 0:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(grid[y][x]), True, BLACK)
                    screen.blit(text, (rect.centerx - text.get_width() // 2, rect.centery - text.get_height() // 2))
                elif grid[y][x] == -1:  # Mine
                    pygame.draw.circle(screen, BLACK, rect.center, GRID_SIZE // 2)
            else:
                pygame.draw.rect(screen, GRAY, rect)
                if revealed[y][x]:
                    pygame.draw.rect(screen, WHITE, rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
