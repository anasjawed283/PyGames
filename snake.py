import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (GRID_SIZE, 0)

    def move(self, food):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)

        # Check if the snake ate the food
        if head == food:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        head = self.body[0]
        return (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in self.body[1:]
        )

    def change_direction(self, new_direction):
        if (
            (new_direction == (GRID_SIZE, 0) and not self.direction == (-GRID_SIZE, 0)) or
            (new_direction == (-GRID_SIZE, 0) and not self.direction == (GRID_SIZE, 0)) or
            (new_direction == (0, GRID_SIZE) and not self.direction == (0, -GRID_SIZE)) or
            (new_direction == (0, -GRID_SIZE) and not self.direction == (0, GRID_SIZE))
        ):
            self.direction = new_direction

# Food class
class Food:
    def __init__(self):
        self.position = self.generate_food_position()

    def generate_food_position(self):
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)
        return x, y

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize the snake and food
snake = Snake()
food = Food()

# Game loop
clock = pygame.time.Clock()

live_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -GRID_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, GRID_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-GRID_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((GRID_SIZE, 0))

    # Move the snake
    if snake.move(food.position):
        live_score += 1
        food.position = food.generate_food_position()

    # Check for collisions
    if snake.check_collision():
        print("Game Over!")
        print(f"Final Score: {live_score}")
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw the food
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Print live score to the terminal
    print(f"Live Score: {live_score}", end='\r')
