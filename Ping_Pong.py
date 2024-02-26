import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Initialize the paddles and ball
player_paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Set initial ball speed
ball_speed = [5, 5]

# Initialize hit counter and font
hit_count = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_paddle.left > 0:
        player_paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player_paddle.right < WIDTH:
        player_paddle.move_ip(5, 0)

    # Move the ball
    ball.move_ip(ball_speed[0], ball_speed[1])

    # Check collisions with walls
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0:
        ball_speed[1] = -ball_speed[1]

    # Check collision with the paddle
    if ball.colliderect(player_paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]
        hit_count += 1

    # Check if the ball missed the paddle
    if ball.bottom > HEIGHT:
        # Game over
        game_over_text = font.render(f"Game Over - Hits: {hit_count}", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)  # Display game over message for 2 seconds
        # Reset game
        hit_count = 0
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_speed = [5, 5]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display hit count
    hit_text = font.render(f"Hits: {hit_count}", True, WHITE)
    screen.blit(hit_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
