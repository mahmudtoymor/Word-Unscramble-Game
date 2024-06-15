import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Word Unscramble Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# List of meaningful words
meaningful_word = ['dog', 'cow', 'cat']

def generate_letters(meaningful_word):
    word = random.choice(meaningful_word)
    letters = list(word)
    random.shuffle(letters)
    return letters, word

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

point = 0
wrong = 0

# Game loop
while True:
    letters, correct_word = generate_letters(meaningful_word)
    input_word = ''
    game_over = False

    while not game_over:
        screen.fill(white)
        draw_text(' '.join(letters), font, black, screen, 100, 150)
        draw_text(f'Score: {point}', small_font, black, screen, 10, 10)
        draw_text(f'Your guess: {input_word}', small_font, black, screen, 100, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_word.lower() == correct_word:
                        point += 1
                        game_over = True
                    else:
                        wrong += 1
                        if wrong == 3:
                            draw_text(f'Game over! Final score: {point}', small_font, black, screen, 100, 350)
                            pygame.display.update()
                            pygame.time.wait(2000)
                            game_over = True
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                else:
                    input_word += event.unicode
        
        pygame.display.update()

    # Check if the player wants to continue
    if wrong == 3:
        screen.fill(white)
        draw_text(f'Game over! Final score: {point}', small_font, black, screen, 100, 150)
        draw_text('Do you want to continue? (Y/N)', small_font, black, screen, 100, 250)
        pygame.display.update()
        
        continue_game = False
        while not continue_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        point = 0
                        wrong = 0
                        continue_game = True
                    if event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()
