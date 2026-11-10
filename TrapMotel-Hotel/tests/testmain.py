import pygame

#main game file
pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Trap Motel-Hotel")

clock = pygame.time.Clock()
FPS = 60

#colors
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)
RED = (180, 35, 45)

#fonts
title_font = pygame.font.Font(None, 72)
subtitle_font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 40)

#render static text once, before the loop 
title_text = title_font.render("Trap Motel-Hotel", True, RED)
instructions = button_font.render("press ENTER to start", True, WHITE)
playing_message = button_font.render("Welcome to the Trap....... press ESC for the menu", True, WHITE)

game_running = True
game_state = ("MAIN MENU")

while game_running:
        clock.tick(FPS)

        for event in pygame.event.get():

                if event.type == pygame.quit:
                        game_running = False

                if event.type == pygame.KEYDOWN:                        
                        if game_state == "MAIN_MENU":
                                if event.key == pygame.K_RETURN:
                                        game_state = "PLAYING"
                        elif game_state == "PLAYING":
                                if event.key == pygame.K_ESCAPE:
                                        game_state == "MAIN_MENU"


        if game_state == "MAIN_MENU":
                screen.bilt(title_text, title_text.get_rect(center=(SCREEN_WIDTH // 2, 250)))
                screen.bilt(instructions, instructions.get_rect(center=(SCREEN_WIDTH // 2, 350)))

        elif game_state == "PLAYING":
                screen.bilt(playing_message, playing_message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

        screen.fill((50, 0, 0))
        print(game_state)
                
        pygame.display.flip()

pygame.quit()
