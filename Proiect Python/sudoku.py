import random
import pygame
import time

class Sudoku:
    def __init__(self, mat_sudoku, mat_ocupat):
        self.mat_sudoku = mat_sudoku #matricea sudoku
        self.mat_ocupat = mat_ocupat # matrice pentru a vedea care spatii sunt ocupate     
def is_valid(board, i,j, value): 
    # xij != xik pt k != j -> pentru linie
    for k in range(len(board)):
        if k != i:
            if board[k][j] == value:
                return False 
    # xij ! = xkj pt k ! = i -> pentru coloana
    for k in range(len(board[i])):
        if k != j:
            if board[i][k] == value:
                return False
    # xi1j1 ! = xi2j2 pt (i1,j1) != (i2,j2) && (i1,j1), (i2,j2) pt patrat
    p_i = i // 3
    p_j = j // 3
    for k in range(p_i * 3, (p_i + 1) * 3):
        for l in range(p_j * 3, (p_j + 1) * 3):
            if board[k][l] == value and (i, j) != (k, l):
                return False
    return True
def print_sudoku(board):
    for row in board:
        print(*row)
def solve(board): #
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0          
                return False
    return True
def generate_solved_sudoku():
    board = []
    for i in range(9):
        board.append([0] * 9)
    for _ in range(2):  
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        board[row][col] = num
    if solve(board):
        return board
    else:
        print("didn't generate a valid sudoku board, try again")
def scoate_elemente(self, difficulty):
    for k in range(1,difficulty):
        x = random.randint(0,8)
        y = random.randint(0,8)
        if self.mat_ocupat[x][y] == 0:
            self.mat_ocupat[x][y] = 1
            self.mat_sudoku[x][y] = None
    return self.mat_ocupat
def delete_element(self, row, col):
    print(f"se sterge elem de la ({row}, {col})")
    if self.mat_ocupat[row][col] == 2:
        self.mat_sudoku[row][col] = None
        return True
    else:
        print("element pus initial - nu se ppate sterge")
        return False
mat_ocupat = []
for i in range(9):
    mat_ocupat.append([0] * 9)
global game_over 

def draw_sudoku(stare):
    selected_cell = None
    screen.fill(pygame.Color("white"))  #umple ecranul cu alb
    print("draw")
    #actualizare countdown
    current_time = time.time()
    elapsed_time = current_time - sountdown_start
    remaining_time = max(0, countdown_duration - elapsed_time)
    font_countdown = pygame.font.Font(None, 40)
    text_countdown = font_countdown.render(f"Countdown: {int(remaining_time)} sec", True, pygame.Color("black"))
    text_rect_countdown = text_countdown.get_rect(center=(250, 50))
    countdown_surface.fill(pygame.Color(128,0,0)) 
    countdown_surface.blit(text_countdown, text_rect_countdown)
    screen.blit(countdown_surface, (0, 0))  # deseneaza a doua suprafata in partea de sus
    pygame.display.flip()  #actualizează ecranul
    
    #deseneaza liniile pt joc
    for i in range(10):
        line_width = 2 if i % 3 == 0 else 1  # liniile groase pentru grupele de 3
        pygame.draw.line(screen, pygame.Color("black"), (i * 500/9, 100), (i * 500/9, 600), line_width)
        pygame.draw.line(screen, pygame.Color("black"), (0, (i * 500/9)+100), (500, (i * 500/9)+100), line_width)
    print("aici su")
    print_sudoku(stare.mat_sudoku)
    # se pun nr in celulele corespunzatoare 
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if stare.mat_sudoku[i][j] is not None:
                if stare.mat_ocupat[i][j] == 2:
                    text_color = pygame.Color("grey")  #culoare pentru elem puse de jucator
                else:
                    text_color = pygame.Color("black")
                text = font.render(str(stare.mat_sudoku[i][j]), True, text_color)
            else:
                text = font.render("", True, pygame.Color("black"))
            text_rect = text.get_rect(center=(j * 500/9 + 500/9 // 2, (i * 500/9) + 100 + 500/9 // 2))
            screen.blit(text, text_rect)



def start_game():
        game_over = False
        while not game_over :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # click intr-un anumit patrat
                    if 100 <= event.pos[1] <= 600:
                        row = (event.pos[1] - 100) // (500 // 9)
                        col = event.pos[0] // (500 // 9)
                        selected_cell = (row, col)
                elif event.type == pygame.KEYDOWN:
                    if selected_cell is not None:
                        if pygame.K_1 <= event.key <= pygame.K_9:
                            # pune cifra in celula selectata
                            number = event.key - pygame.K_0
                            if is_valid(sudoku_board, selected_cell[0], selected_cell[1], number):
                                sudoku_board[selected_cell[0]][selected_cell[1]] = number
                                selected_cell = None  #deselecteaza celula dupa ce a fost pus nr
                                stare.mat_ocupat[row][col] = 2
                                draw_sudoku(stare )
                            else:
                                display_conflict_message(screen)
                        elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                            # sterge elem dintr-o anumita celula
                            if selected_cell is not None:
                                if delete_element(stare,selected_cell[0], selected_cell[1]):
                                    draw_sudoku( stare)

            # actualizare countdown
            current_time = time.time()
            elapsed_time = current_time - sountdown_start
            remaining_time = max(0, countdown_duration - elapsed_time)
            min = int(remaining_time) // 60
            sec = int(remaining_time) % 60
            font_countdown = pygame.font.Font(None, 40)
            if min > 0: 
                text_countdown = font_countdown.render(f"Countdown: {min} min {sec} sec", True, pygame.Color("black"))
            else:
                text_countdown = font_countdown.render(f"Countdown: {sec} sec", True, pygame.Color("black"))

            text_rect_countdown = text_countdown.get_rect(center=(250, 50))
            countdown_surface.fill(pygame.Color(128, 0, 0))
            countdown_surface.blit(text_countdown, text_rect_countdown)
            screen.blit(countdown_surface, (0, 0))
            if remaining_time == 0:
                print("Game over! Time's up!")
                show_game_over_screen( "Game over! Time's up! Do you want to play again?")
                game_over = True
            elif all(all(cell is not None for cell in row) for row in sudoku_board):
                print("Congratulations! You won!")
                show_game_over_screen("Congratulations! You won! Do you want to play again?")
                game_over = True
            
            pygame.display.flip()
        pygame.quit()



def display_conflict_message(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Conflict! Choose a different number.", True, pygame.Color(245,230,234))
    text_rect = text.get_rect(center=(250, 80))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  #mesajul e vizibil doar 1 sec
    draw_sudoku(stare )  #redeseneaza tabla fara conflict

def show_game_over_screen( message): #afisare ecran la sf joc
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #joc nou
                    sudoku_board = generate_solved_sudoku()
                    print_sudoku(sudoku_board)
                    mat_ocupat = []
                    for i in range(9):
                        mat_ocupat.append([0] * 9)
                    stare = Sudoku(sudoku_board, mat_ocupat)
                    sudoku_ocupat = scoate_elemente(stare, difficulty=2)
                    selected_cell = None
                    print("aici")
                    print_sudoku(sudoku_board)
                    draw_sudoku(stare)
                elif event.key == pygame.K_q:
                    #inchide jocul
                    pygame.quit()
        screen.fill(pygame.Color("white"))
        font_game_over = pygame.font.Font(None, 26)
        text_game_over = font_game_over.render(message, True, pygame.Color("black"))
        text_rect_game_over = text_game_over.get_rect(center=(250, 200))
        screen.blit(text_game_over, text_rect_game_over)
        font_prompt = pygame.font.Font(None, 30)
        text_prompt = font_prompt.render("Press enter to play again or Q to quit.", True, pygame.Color("black"))
        text_rect_prompt = text_prompt.get_rect(center=(250, 300))
        screen.blit(text_prompt, text_rect_prompt)
        pygame.display.flip()
if __name__ == "__main__":
    sudoku_board = generate_solved_sudoku()
    print("\nSudoku amestecat:")
    print_sudoku(sudoku_board)
    stare = Sudoku(sudoku_board, mat_ocupat)
    sudoku_ocupat = scoate_elemente(stare, difficulty=2)
    
    """ print("Sudoku rezolvat:")
    print_sudoku(sudoku_board)

    print("\nSudoku ocupat:")
    print_sudoku(sudoku_ocupat)

    print("\nSudoku sudoku nou:")
    print_sudoku(sudoku_board) """

    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Sudoku")
    # creare suprafata pt countdown
    countdown_surface = pygame.Surface((500, 100))
    countdown_surface.fill(pygame.Color("blue"))
    sountdown_start = time.time()
    countdown_duration = 10 

    draw_sudoku(stare)
    start_game()

    pygame.quit()


# restartt game!! + cod pt generare sudoku???
