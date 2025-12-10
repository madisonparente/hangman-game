# I pledge my honor that I have abided by the Stevens Honor System - Madison Parente

import pygame
import sys
import random

# Initialize Pygame
clock = pygame.time.Clock()
pygame.init()

# Window Setup and Colors
WIDTH, HEIGHT = 1000, 650
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (77, 43, 5)
SHIRT = (242, 2, 238)
SKIN = (240, 194, 149)
JEANS = (21, 42, 77)
GREEN = (72, 122, 56)
RED = (184, 40, 24)
LIGHT_GRAY = (183, 188, 196)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

background = pygame.image.load("hman_2.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
TITLE_FONT = pygame.font.SysFont('calabri', 60 )
END_FONT = pygame.font.SysFont('georgia', 75)
END_FONT2 = pygame.font.SysFont('georgia', 30)
SMALL_FONT = pygame.font.SysFont('comicsans', 25)
DESC_FONT = pygame.font.SysFont('comicsans', 23)
SMALLER_FONT = pygame.font.SysFont('comicsans', 15)

#screens
curr_screen = "menu"
gState = "hide"

check_img = pygame.image.load("checkmark.png").convert_alpha()
check_img = pygame.transform.scale(check_img, (40, 40))

face_img = pygame.image.load("face.png").convert_alpha()
face_img = pygame.transform.scale(face_img, (53, 53))

def load_words(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

easy_words = load_words("easy.txt")
medium_words = load_words("medium.txt")
hard_words = load_words("hard.txt")

def menu_screen():
    background = pygame.image.load("hman_1.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
    screen.blit(background, (0, 0))

    playgame_button = pygame.Rect(440, 210, 150, 80)
    htp_buttoncirc = {"htppos": (35,35), "htprad": (20)} #howtoplay

    pygame.draw.rect(screen, BLACK, playgame_button, border_radius=10)
    htp_button = pygame.draw.circle(screen, (20, 28, 181), htp_buttoncirc["htppos"], htp_buttoncirc["htprad"])
    
    playgame_text = LETTER_FONT.render("Play", True, WHITE)
    title_text = TITLE_FONT.render("Welcome to Hangman!", True, WHITE)
    htp_text = LETTER_FONT.render("i", True, WHITE)

    screen.blit(playgame_text, (playgame_button.x + 45, playgame_button.y + 20))
    screen.blit(title_text, (285, 100))
    screen.blit(htp_text, (30,10))

    # Draw Hangman Figure on Menu Screen
    draw_head(517, 387)
    draw_body(506, 411)
    draw_arm1(490, 425, 470, 425)
    draw_arm2(520, 425, 532, 425)
    draw_leg1(508, 473, 494, 508)
    draw_leg2(515, 473, 515, 508)
    screen.blit(face_img, (490, 360))

    return playgame_button, htp_button

def htpscreen():
    overlay = pygame.Surface((700, 500), pygame.SRCALPHA)
    overlay.fill((181, 180, 176, 250)) # fourth number is alpha for transparency, increase for less transparent
    screen.blit(overlay, (150, 65))

    htp_text = TITLE_FONT.render("How To Play Hangman", True, BLACK)
    screen.blit(htp_text, (275, 100))
    htp_desc = SMALL_FONT.render("Hangman is a word-guessing game. The objective ", True, BLACK)
    htp_desc_2 = SMALL_FONT.render("is to guess the hidden word by suggesting letters", True, BLACK)
    htp_desc_3 = SMALL_FONT.render("within a certain number of guesses. Each incorrect", True, BLACK)
    htp_desc_4 = SMALL_FONT.render("guess results in a part of the hangman being drawn.", True, BLACK)
    screen.blit(htp_desc, (215, 225))
    screen.blit(htp_desc_2, (215, 275))
    screen.blit(htp_desc_3, (205, 325))
    screen.blit(htp_desc_4, (205, 375))

def diffdesc(diffState):
        diffdesc_box = pygame.Rect(500, 200, 350, 275)
        pygame.draw.rect(screen, LIGHT_GRAY, diffdesc_box, border_radius=10)
        if (diffState == 'easy'):
            pygame.draw.rect(screen, WHITE, easy_button, border_radius=10)
            easy_text = LETTER_FONT.render("Easy", True, BLACK)
            screen.blit(easy_text, (easy_button.x + 65, easy_button.y + 20))
            easydesc = DESC_FONT.render("Easy Difficulty Info", True, WHITE)
            easydesc_1 = DESC_FONT.render("Word Length: 3-4 Characters", True, WHITE)
            easydesc_2 = DESC_FONT.render("# of Guesses: 10", True, WHITE)
            easydesc_3 = DESC_FONT.render("Beginner Level", True, WHITE)
            screen.blit(easydesc, (diffdesc_box.x + 70, diffdesc_box.y + 10))
            screen.blit(easydesc_1, (diffdesc_box.x + 12, diffdesc_box.y + 75))
            screen.blit(easydesc_2, (diffdesc_box.x + 80, diffdesc_box.y + 125))
            screen.blit(easydesc_3, (diffdesc_box.x + 95, diffdesc_box.y + 175))
        if (diffState == 'medium'):
            pygame.draw.rect(screen, WHITE, medium_button, border_radius=10)
            medium_text = LETTER_FONT.render("Medium", True, BLACK)
            screen.blit(medium_text, (medium_button.x + 45, medium_button.y + 20))
            mediumdesc = DESC_FONT.render("Medium Difficulty Info", True, WHITE)
            mediumdesc_1 = DESC_FONT.render("Word Length: 5-6 Characters", True, WHITE)
            mediumdesc_2 = DESC_FONT.render("# of Guesses: 7", True, WHITE)
            mediumdesc_3 = DESC_FONT.render("Intermediate Level", True, WHITE)
            screen.blit(mediumdesc, (diffdesc_box.x + 50, diffdesc_box.y + 10))
            screen.blit(mediumdesc_1, (diffdesc_box.x + 12, diffdesc_box.y + 75))
            screen.blit(mediumdesc_2, (diffdesc_box.x + 80, diffdesc_box.y + 125))
            screen.blit(mediumdesc_3, (diffdesc_box.x + 65, diffdesc_box.y + 175))
        if (diffState == 'hard'):
            pygame.draw.rect(screen, WHITE, hard_button, border_radius=10)
            hard_text = LETTER_FONT.render("Hard", True, BLACK)
            screen.blit(hard_text, (hard_button.x + 60, hard_button.y + 20))
            harddesc = DESC_FONT.render("Hard Difficulty Info", True, WHITE)
            harddesc_1 = DESC_FONT.render("Word Length: 7-10 Characters", True, WHITE)
            harddesc_2 = DESC_FONT.render("# of Guesses: 5", True, WHITE)
            harddesc_3 = DESC_FONT.render("Expert Level", True, WHITE)
            screen.blit(harddesc, (diffdesc_box.x + 65, diffdesc_box.y + 10))
            screen.blit(harddesc_1, (diffdesc_box.x + 10, diffdesc_box.y + 75))
            screen.blit(harddesc_2, (diffdesc_box.x + 85, diffdesc_box.y + 125))
            screen.blit(harddesc_3, (diffdesc_box.x + 105, diffdesc_box.y + 175))


def difficulty_screen():
    background = pygame.image.load("hman_1.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # scale to fit window
    screen.blit(background, (0, 0))

    # Base in back to fill empty space
    draw_base1(565, 500)
    draw_base2(630, 220)
    draw_base3(640, 220)
    draw_base4(765, 240)

    easy_button = pygame.Rect(250, 200, 200, 80)
    medium_button = pygame.Rect(250, 300, 200, 80)
    hard_button = pygame.Rect(250, 400, 200, 80)

    pygame.draw.rect(screen, BLACK, easy_button, border_radius=10)
    pygame.draw.rect(screen, BLACK, medium_button, border_radius=10)
    pygame.draw.rect(screen, BLACK, hard_button, border_radius=10)

    easy_text = LETTER_FONT.render("Easy", True, WHITE)
    medium_text = LETTER_FONT.render("Medium", True, WHITE)
    hard_text = LETTER_FONT.render("Hard", True, WHITE)
    difficulty_text = TITLE_FONT.render("Choose a Difficulty", True, WHITE)

    screen.blit(easy_text, (easy_button.x + 65, easy_button.y + 20))
    screen.blit(medium_text, (medium_button.x + 45, medium_button.y + 20))
    screen.blit(hard_text, (hard_button.x + 60, hard_button.y + 20))
    screen.blit(difficulty_text, (315, 50))

    goback_button1, goback_button2 = goback_button(hover)

    return easy_button, medium_button, hard_button, goback_button1, goback_button2

def setup_game(difficulty):
    global chosenWord, wrong_guesses

    global revealed_letters, guessed_letters
    revealed_letters = []
    guessed_letters = []

    for letter in button_colors:
        button_colors[letter] = BLACK

    if difficulty == "easy":
        chosenWord = random.choice(easy_words)
    elif difficulty == "medium":
        chosenWord = random.choice(medium_words)
    elif difficulty == "hard":
        chosenWord = random.choice(hard_words)

    starting_parts = {"easy": 0, "medium": 3, "hard": 5}
    guesses = {"easy": 10, "medium": 7, "hard": 5}

    wrong_guesses = starting_parts[difficulty]
    global guess_remain
    guess_remain = guesses[difficulty]

    return chosenWord

def game_screen(chosenWord, guessed_letters, revealed_letters, wrong_guesses, guess_remain, mouse_pos):
    screen.blit(background, (0, 0))

    global gState

    guessbox = pygame.Rect(950, 10, 40, 40)
    pygame.draw.rect(screen, LIGHT_GRAY, guessbox, border_radius=5)
    if guessbox.collidepoint(mouse_pos):
        if gState == "hide":
            screen.blit(check_img, (950, 10))
            screen.blit(SMALLER_FONT.render("Click to show remaining guesses", True, BLACK), (720, 20))
        else:  # gState == "show"
            screen.blit(SMALLER_FONT.render("Click to hide remaining guesses", True, BLACK), (720, 20))
    # Click toggle
    if event.type == pygame.MOUSEBUTTONDOWN and guessbox.collidepoint(mouse_pos):
        if gState == "hide":
            gState = "show"
        else:
            gState = "hide"
    # Display when enabled
    if gState == "show":
        screen.blit(check_img, (950, 10))
        screen.blit(SMALL_FONT.render(f"Guesses remaining: {guess_remain}", True, BLACK), (400, 20))

    # Variables and Dimensions - Row 1 of Keys

    global buttons, button_colors

    # Draw all buttons + letters
    for letter, rect in buttons.items():
        pygame.draw.rect(screen, button_colors[letter], rect, border_radius=5)
        text = LETTER_FONT.render(letter.upper(), True, WHITE)
        screen.blit(text, (rect.x + 15, rect.y + 5))

    draw_hangman(wrong_guesses)

    line_positions = draw_letter_lines(len(chosenWord))

    # Draw letters above their lines
    y_offset = -40
    for i, letter in enumerate(chosenWord):
        if letter in revealed_letters:
            letter_text = LETTER_FONT.render(letter.upper(), True, BLACK)
            x, y = line_positions[i]
            screen.blit(letter_text, (x + 15, y + y_offset))
   
def end_screen(WLstate):

    # draw previous game once (no lag)
    screen.blit(game_snapshot, (0, 0))

    # overlay box
    overlay = pygame.Surface((700, 500), pygame.SRCALPHA)
    overlay.fill((181, 180, 176, 230))
    screen.blit(overlay, (150, 65))

    # win/loss text
    if WLstate == "win":
        text = END_FONT.render("You Win!", True, BLACK)
    else:
        text = END_FONT.render("You Lost!", True, BLACK)
    screen.blit(text, (350, 170))

    # buttons
    playagain_button = pygame.Rect(325, 380, 150, 80)
    mainmenu_button = pygame.Rect(550, 380, 150, 80)

    play_color = WHITE if playagain_button.collidepoint(mouse_pos) else BLACK
    menu_color = WHITE if mainmenu_button.collidepoint(mouse_pos) else BLACK
    play_text = BLACK if playagain_button.collidepoint(mouse_pos) else WHITE
    menu_text = BLACK if mainmenu_button.collidepoint(mouse_pos) else WHITE

    pygame.draw.rect(screen, play_color, playagain_button, border_radius=10)
    pygame.draw.rect(screen, menu_color, mainmenu_button, border_radius=10)

    # text on buttons
    screen.blit(SMALL_FONT.render("Play Again", True, play_text), (playagain_button.x + 15, playagain_button.y + 20))
    screen.blit(LETTER_FONT.render("Menu", True, menu_text), (mainmenu_button.x + 35, mainmenu_button.y + 20))

    # word reveal
    screen.blit(END_FONT2.render("The word was:", True, BLACK), (350, 285))
    screen.blit(END_FONT2.render(chosenWord.upper(), True, BLACK), (555, 285))

    return playagain_button, mainmenu_button


# Drawing Functions

def goback_button(hover):
    global tripoints
    global trirect
    tripoints = [(15, 30), (40, 20), (40, 40)]
    trirect = pygame.Rect(40, 27, 30, 7)
    goback_button1 = pygame.draw.polygon(screen, BLACK, tripoints)
    goback_button2 = pygame.draw.rect(screen, BLACK, trirect, border_radius=1)

    if (hover == 'yes'):
        pygame.draw.polygon(screen, WHITE, tripoints)
        pygame.draw.rect(screen, WHITE, trirect, border_radius=1)

    return goback_button1, goback_button2

def draw_base1(x=325, y=380):
    base1 = pygame.Rect(x, y, 150, 25)#325, 380
    pygame.draw.rect(screen, BROWN, base1, border_radius=3)
    
def draw_base2(x=390, y=100):
    base2 = pygame.Rect(x, y, 25, 300)#390, 100
    pygame.draw.rect(screen, BROWN, base2, border_radius=3)

def draw_base3(x=400, y=100):
    base3 = pygame.Rect(x, y, 150, 25)#400, 100
    pygame.draw.rect(screen, BROWN, base3, border_radius=3)

def draw_base4(x=525, y=120):
    base4 = pygame.Rect(x, y, 25, 50)#525, 120
    pygame.draw.rect(screen, BROWN, base4, border_radius=3)

def draw_head(x=538, y=190):
    head = {"headpos": (x, y), "headrad": 25} #538, 190
    pygame.draw.circle(screen, SKIN, head["headpos"], head["headrad"])

def draw_body(x=528, y=212):
    body = pygame.Rect(x, y, 20, 65) #528, 212
    pygame.draw.rect(screen, SHIRT, body, border_radius=3)

def draw_arm1(x=510, y=225, a=490, b=225):
    arm1_1 = pygame.Rect(x, y, 20, 15) #510, 225
    arm1_2 = pygame.Rect(a, b, 30, 15) #490, 225
    pygame.draw.rect(screen, SHIRT, arm1_1, border_radius=3)
    pygame.draw.rect(screen, SKIN, arm1_2, border_radius=3)

def draw_arm2(x=545, y=225, a=555, b=225):
    arm2_1 = pygame.Rect(x, y, 20, 15) #545, 225
    arm2_2 = pygame.Rect(a, b, 30, 15) #555, 225
    pygame.draw.rect(screen, SHIRT, arm2_1, border_radius=3)
    pygame.draw.rect(screen, SKIN, arm2_2, border_radius=3)

def draw_leg1(x=528, y=274, a=514, b=301):
    leg1_1 = pygame.Rect(x, y, 10, 40) #528, 274
    leg1_2 = pygame.Rect(a, b, 25, 13) #514, 301
    pygame.draw.rect(screen, JEANS, leg1_1, border_radius=3)
    pygame.draw.rect(screen, BLACK, leg1_2, border_radius=6)

def draw_leg2(x=538, y=274, a=535, b=301):
    leg2_1 = pygame.Rect(x, y, 10, 40) #538, 274
    leg2_2 = pygame.Rect(a, b, 25, 13) #535, 301
    pygame.draw.rect(screen, JEANS, leg2_1, border_radius=3)
    pygame.draw.rect(screen, BLACK, leg2_2, border_radius=6)

def draw_hangman(wrong_guesses):
    parts = [draw_base1, draw_base2, draw_base3, draw_base4, draw_head, draw_body, draw_arm1, draw_arm2, draw_leg1, draw_leg2]

    for i in range(min(wrong_guesses, len(parts))):
        parts[i]()

def draw_letter_lines(word_length, y=475, line_width=50, spacing=10):
    # Calculate total width of all lines + spaces
    total_width = word_length * line_width + (word_length - 1) * spacing

    # Center starting X based on screen width
    start_x = (WIDTH - total_width) // 2

    line_positions = []

    for i in range(word_length):
        x = start_x + i * (line_width + spacing)
        rect = pygame.Rect(x, y, line_width, 5)
        pygame.draw.rect(screen, BLACK, rect, border_radius=1)
        line_positions.append((x, y))

    return line_positions

# Main Loop
run = True
htp_button = playgame_button = player_button = None
easy_button = medium_button = hard_button = None
mainmenu_button = playagain_button = None
goback_button1 = goback_button2 = None
chosenWord = ""
global difficulty 
global WLstate
global diffState
global hover
hover = 'no'
wrong_guesses = 0

letters = "abcdefghijklmnopqrstuvwxyz"
buttons = {}
button_colors = {}

x, y = 115, 500
spacing = 60
row_height = 75

    # Create button rects and default colors
for i, letter in enumerate(letters):
    if i == 13:  # move to next row after M
        y += row_height
        x = 115
    rect = pygame.Rect(x, y, 50, 50)
    buttons[letter] = rect
    button_colors[letter] = BLACK
    x += spacing    

while run:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Mouse Clicks
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Menu Screen Buttons
            if curr_screen == "menu" and playgame_button and playgame_button.collidepoint(mouse_pos):
                curr_screen = "difficulty"

            # Difficulty Screen Buttons 
            elif curr_screen == "difficulty" and easy_button and easy_button.collidepoint(mouse_pos):
                difficulty = "easy"
                chosenWord = setup_game(difficulty)
                curr_screen = "game"

            elif curr_screen == "difficulty" and medium_button and medium_button.collidepoint(mouse_pos):
                difficulty = "medium"
                chosenWord = setup_game(difficulty)
                curr_screen = "game"

            elif curr_screen == "difficulty" and hard_button and hard_button.collidepoint(mouse_pos):
                difficulty = "hard"
                chosenWord = setup_game(difficulty)
                curr_screen = "game"

            elif curr_screen == "difficulty" and (goback_button1 and goback_button1.collidepoint(mouse_pos) or goback_button2 and goback_button2.collidepoint(mouse_pos)):
                curr_screen = "menu"

            # End Screen Buttons
            elif curr_screen == "end" and mainmenu_button and mainmenu_button.collidepoint(mouse_pos):
                curr_screen = "menu"

            elif curr_screen == "end" and playagain_button and playagain_button.collidepoint(mouse_pos):
                chosenWord = setup_game(difficulty)
                curr_screen = "game"

        # Handle keyboard input separately
        if event.type == pygame.KEYDOWN and curr_screen == "game":
            key_pressed = event.unicode.lower()

            if key_pressed.isalpha() and key_pressed not in guessed_letters:
                guessed_letters.append(key_pressed)

                if key_pressed in chosenWord:
                    revealed_letters.append(key_pressed)
                    button_colors[key_pressed] = GREEN
                else:
                    wrong_guesses += 1
                    guess_remain -= 1
                    button_colors[key_pressed] = RED

                if all(letter in revealed_letters for letter in chosenWord):
                    WLstate = "win"
                    game_snapshot = screen.copy()
                    curr_screen = "end"

                if wrong_guesses >= 10:
                    WLstate = "loss"
                    game_snapshot = screen.copy()
                    curr_screen = "end"

    # Draw current screen
    if curr_screen == "menu":
        playgame_button, htp_button = menu_screen()
        #Hovering
        if htp_button and htp_button.collidepoint(mouse_pos):
            htpscreen()
        if playgame_button and playgame_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, playgame_button, border_radius=10)
            playgame_text = LETTER_FONT.render("Play", True, BLACK)
            screen.blit(playgame_text, (playgame_button.x + 45, playgame_button.y + 20))
    elif curr_screen == "difficulty":
        easy_button, medium_button, hard_button, goback_button1, goback_button2 = difficulty_screen()
        # Hovering Buttons
        if easy_button and easy_button.collidepoint(mouse_pos):
            diffState = 'easy'
            diffdesc(diffState)
        elif medium_button and medium_button.collidepoint(mouse_pos):
            diffState = 'medium'
            diffdesc(diffState)
        elif hard_button and hard_button.collidepoint(mouse_pos):
            diffState = 'hard'
            diffdesc(diffState)
        if goback_button1 and goback_button1.collidepoint(mouse_pos) or goback_button2 and goback_button2.collidepoint(mouse_pos):
            hover = 'yes'
            goback_button(hover)
        else:
            hover = 'no'
    elif curr_screen == "game":
        game_screen(chosenWord, guessed_letters, revealed_letters, wrong_guesses, guess_remain, mouse_pos)
    elif curr_screen == "end":
        playagain_button, mainmenu_button = end_screen(WLstate)     

    pygame.display.update()
    clock.tick(60)   # Cap the game at 60 FPS

pygame.quit()
sys.exit()
