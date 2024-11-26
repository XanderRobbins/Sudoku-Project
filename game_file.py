import pygame
import sys
from sudoku_generator import generate_sudoku
pygame.init()
#IMPORTS LIBRARIES AND INITIALIZED PYGAME

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
LINE_COLOR = (0, 0, 0)  # Black
BG_COLOR = (255, 255, 255)  # White
HIGHLIGHT_COLOR = (173, 216, 230)  # Light Blue
FONT = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
screen.fill(BG_COLOR)
#creating board


board = generate_sudoku(GRID_SIZE, 30)
selected_cell = None

def draw_grid():
    for row in range(GRID_SIZE + 1):
        line_width = 3 if row % 3 == 0 else 1
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), line_width)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), line_width)
def draw_numbers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = board[row][col]
            if num != 0:
                text = FONT.render(str(num), True, LINE_COLOR)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 5))

def highlight_cell():
    if selected_cell:
        row, col = selected_cell
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


#takes inputs from the mousepad
def handle_mouse_click(pos):
    global selected_cell
    col, row = pos[0] // CELL_SIZE, pos[1] // CELL_SIZE
    if row < GRID_SIZE and col < GRID_SIZE:
        selected_cell = (row, col)
#takes inputs from the keyboard
def handle_key_input(key):
    if selected_cell:
        row, col = selected_cell
        if key == pygame.K_1:
            board[row][col] = 1
        elif key == pygame.K_2:
            board[row][col] = 2
        elif key == pygame.K_3:
            board[row][col] = 3
        elif key == pygame.K_4:
            board[row][col] = 4
        elif key == pygame.K_5:
            board[row][col] = 5
        elif key == pygame.K_6:
            board[row][col] = 6
        elif key == pygame.K_7:
            board[row][col] = 7
        elif key == pygame.K_8:
            board[row][col] = 8
        elif key == pygame.K_9:
            board[row][col] = 9
        elif key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
            board[row][col] = 0




def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                handle_key_input(event.key)

        screen.fill(BG_COLOR)
        draw_grid()
        draw_numbers()
        highlight_cell()
        pygame.display.flip()

    pygame.quit()
    sys.exit()



#runs main funcy-wuncy
if __name__ == "__main__":
    main()
