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
def solve(board): 
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
    count = 0
    while count < difficulty[0]:
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        if self.mat_ocupat[x][y] == 0:
            self.mat_ocupat[x][y] = 1
            self.mat_sudoku[x][y] = None
            count += 1
    return self.mat_ocupat
def delete_element(self, row, col):
    print(f"se sterge elem de la ({row}, {col})")
    if self.mat_ocupat[row][col] == 2:
        self.mat_sudoku[row][col] = None
        return True
    else:
        print("element pus initial - nu se ppate sterge")
        return False
def draw_sudoku(stare):
    global run
    if run is True:
        screen.fill(pygame.Color("white"))  #umple ecranul cu alb
        
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
        print_sudoku(stare.mat_ocupat)   
def screen_difficulty(run):
    global countdown_duration 
    dif = None
    while dif is None and run is not False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 150 <= x <= 350 and 240 <= y <= 290:  # easy
                    dif = 1
                    countdown_duration = 5
                elif 150 <= x <= 350 and 300 <= y <= 350:  # medium
                    dif = 50
                    countdown_duration = 1200  # 20 min pentru joc mediu
                elif 150 <= x <= 350 and 360 <= y <= 410:  # hard
                    dif = 57
                    countdown_duration = 2400  # 40 min pentru joc greu
            if event.type == pygame.QUIT:
                game_over = True
                run = False

        if run is True:
            screen.fill(pygame.Color("white"))
            font = pygame.font.Font(None, 36)
            text = font.render("Select difficulty:", True, pygame.Color("black"))
            text_rect = text.get_rect(center=(250, 200))
            screen.blit(text, text_rect)

            button_easy = pygame.Rect(150, 240, 200, 50)  # Coord stanga, sus + latime si inaltime
            pygame.draw.rect(screen, ("grey"), button_easy)
            text_easy = font.render("Easy", True, pygame.Color("black"))
            text_rect_easy = text_easy.get_rect(center=(250, 265))
            screen.blit(text_easy, text_rect_easy)

            button_medium = pygame.Rect(150, 300, 200, 50)
            pygame.draw.rect(screen, ("grey"), button_medium)
            text_medium = font.render("Medium", True, pygame.Color("black"))
            text_rect_medium = text_medium.get_rect(center=(250, 325))
            screen.blit(text_medium, text_rect_medium)

            button_hard = pygame.Rect(150, 360, 200, 50)
            pygame.draw.rect(screen, ("grey"), button_hard)
            text_hard = font.render("Hard", True, pygame.Color("black"))
            text_rect_hard = text_hard.get_rect(center=(250, 385))
            screen.blit(text_hard, text_rect_hard)
            pygame.display.flip()   
   
    return dif, countdown_duration
def start_game():
    global difficulty, stare, sudoku_board, sountdown_start, selected_cell, game_over, run, sudoku_ocupat
    sountdown_start = time.time()
        
    if nr_games >1:
            difficulty = screen_difficulty(run)
            if difficulty[0] is None:
                pygame.quit() 
                return            
            sudoku_board = generate_solved_sudoku()
            mat_ocupat = []
            for i in range(9):
                mat_ocupat.append([0] * 9)
            stare = Sudoku(sudoku_board, mat_ocupat)
            if difficulty[0] is not None:
                sudoku_ocupat = scoate_elemente(stare, difficulty)
            selected_cell = (-1,-1)
            sountdown_start = time.time()
    draw_sudoku(stare)
    game_over = False
    while not game_over :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # click intr-un anumit patrat
                    if 100 <= event.pos[1] <= 600:
                        row = (event.pos[1] - 100) // (500 // 9)
                        col = event.pos[0] // (500 // 9)
                        selected_cell = (row, col)
                elif event.type == pygame.KEYDOWN:
                    if selected_cell != (-1,-1):
                        print(selected_cell)
                        if pygame.K_1 <= event.key <= pygame.K_9:
                            # pune cifra in celula selectata
                            number = event.key - pygame.K_0
                            if is_valid(sudoku_board, selected_cell[0], selected_cell[1], number):
                                sudoku_board[selected_cell[0]][selected_cell[1]] = number
                                selected_cell = (-1,-1)  #deselecteaza celula dupa ce a fost pus nr
                                stare.mat_ocupat[row][col] = 2
                                draw_sudoku(stare )
                            else:
                                display_conflict_message(screen)
                        elif event.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                            # sterge elem dintr-o anumita celula
                            if selected_cell != (-1,-1):
                                if delete_element(stare,selected_cell[0], selected_cell[1]):
                                    draw_sudoku( stare)
                    else:
                        print(selected_cell)
                        print("square")
                        font = pygame.font.Font(None, 36)
                        text = font.render("Choose a square", True, pygame.Color(245,230,234))
                        text_rect = text.get_rect(center=(250, 80))
                        screen.blit(text, text_rect)
                        pygame.display.flip()
                        pygame.time.wait(1000)  #mesajul e vizibil doar 1 sec
                        draw_sudoku(stare)  #redeseneaza tabla fara conflict 
            if not game_over:
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
                elif all(all(cell is not None for cell in row) for row in sudoku_board):
                    print("Congratulations! You won!")
                    show_game_over_screen("Congratulations! You won! Do you want to play again?")
                if game_over == False:
                    pygame.display.flip()
    pygame.quit()
def display_conflict_message(screen):
    font = pygame.font.Font(None, 36)
    text = font.render("Conflict! Choose a different number.", True, pygame.Color(245,230,234))
    text_rect = text.get_rect(center=(250, 80))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  #mesajul e vizibil doar 1 sec
    draw_sudoku(stare)  #redeseneaza tabla fara conflict
def show_game_over_screen(message):
    global nr_games, game_over, run, sudoku_ocupat
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                game_over = True
                print(game_over)
            
        if game_over is False:
            screen.fill(pygame.Color("white"))
            font_game_over = pygame.font.Font(None, 26)
            text_game_over = font_game_over.render(message, True, pygame.Color("black"))
            text_rect_game_over = text_game_over.get_rect(center=(250, 200))
            screen.blit(text_game_over, text_rect_game_over)
            #buton PlayAgain
            button_play_again = pygame.Rect(150, 300, 200, 50) 
            pygame.draw.rect(screen, ("grey"), button_play_again)
            font_play_again = pygame.font.Font(None, 20)
            text_play_again = font_play_again.render("Play Again", True, pygame.Color("black"))
            text_rect_play_again = text_play_again.get_rect(center=(250, 325))
            screen.blit(text_play_again, text_rect_play_again)
            #buton Quit
            button_quit = pygame.Rect(150, 360, 200, 50)
            pygame.draw.rect(screen, ("grey"), button_quit)
            font_quit = pygame.font.Font(None, 20)
            text_quit = font_quit.render("Quit", True, pygame.Color("black"))
            text_rect_quit = text_quit.get_rect(center=(250, 385))
            screen.blit(text_quit, text_rect_quit)

            pygame.display.flip()

            # asare butoane
            x, y = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 150 <= x <= 350 and 300 <= y <= 350 and click[0] == 1:  # play again
                print("Play Again pressed")
                sudoku_board = generate_solved_sudoku()
                mat_ocupat = []
                for i in range(9):
                    mat_ocupat.append([0] * 9)
                stare = Sudoku(sudoku_board, mat_ocupat)
                sudoku_ocupat = scoate_elemente(stare, difficulty)
                selected_cell = (-1, -1)
                nr_games = nr_games + 1
                print("aici")
                print_sudoku(sudoku_board)
                start_game()

            elif 150 <= x <= 350 and 360 <= y <= 410 and click[0] == 1:  # quit
                print("Quit pressed")
                game_over = True
                run = False
                pygame.quit()
                print(game_over)

if __name__ == "__main__":
    """ sudoku_board = generate_solved_sudoku()
    print("\nSudoku amestecat:")
    print_sudoku(sudoku_board)
    stare = Sudoku(sudoku_board, mat_ocupat)
    sudoku_ocupat = scoate_elemente(stare, difficulty=30) """
    
    """ print("Sudoku rezolvat:")
    print_sudoku(sudoku_board)

    print("\nSudoku ocupat:")
    print_sudoku(sudoku_ocupat)

    print("\nSudoku sudoku nou:")
    print_sudoku(sudoku_board) """
    try:
        pygame.init()
        screen = pygame.display.set_mode((500, 600))
        pygame.display.set_caption("Sudoku")
        # creare suprafata pt countdown
        countdown_surface = pygame.Surface((500, 100))
        countdown_surface.fill(pygame.Color("blue"))
        countdown_duration = 100 
        game_over = False
        run = True
        mat_ocupat = []
        for i in range(9):
            mat_ocupat.append([0] * 9)
        nr_games = 1
        sudoku_board = generate_solved_sudoku()    
        stare = Sudoku(sudoku_board, mat_ocupat)
        selected_cell = (-1,-1)
        difficulty = screen_difficulty(run)
        #print(difficulty)
        if difficulty[0] is not None:
            sudoku_ocupat = scoate_elemente(stare, difficulty)
            start_game()
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        pygame.quit()
