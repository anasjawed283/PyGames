import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [['', '', ''], ['', '', ''], ['', '', '']]
current_player = 'X'

# Game loop
clock = pygame.time.Clock()

def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

def draw_symbols():
    font = pygame.font.Font(None, 100)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, WHITE)
                screen.blit(text, (col * WIDTH // 3 + 30, row * HEIGHT // 3 + 30))
            elif board[row][col] == 'O':
                text = font.render('O', True, WHITE)
                screen.blit(text, (col * WIDTH // 3 + 30, row * HEIGHT // 3 + 30))

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return True

    return False

def check_draw():
    for row in board:
        if '' in row:
            return False
    return True

def reset_game():
    global board, current_player
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    current_player = 'X'

def make_computer_move():
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == '']
    if available_moves:
        return random.choice(available_moves)
    return None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and current_player == 'X':
            mouseX, mouseY = event.pos
            col = mouseX // (WIDTH // 3)
            row = mouseY // (HEIGHT // 3)

            if board[row][col] == '':
                board[row][col] = 'X'
                if check_winner():
                    print("Player X wins!")
                    reset_game()
                elif check_draw():
                    print("It's a draw!")
                    reset_game()
                else:
                    current_player = 'O'

    if current_player == 'O':
        computer_move = make_computer_move()
        if computer_move:
            row, col = computer_move
            board[row][col] = 'O'
            if check_winner():
                print("Player O wins!")
                reset_game()
            elif check_draw():
                print("It's a draw!")
                reset_game()
            else:
                current_player = 'X'

    # Draw everything
    screen.fill(BLACK)
    draw_board()
    draw_symbols()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
