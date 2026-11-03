import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Trap Motel-Hotel")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((25, 10, 25))  # Fill the screen with black color

    # Update the display
    pygame.display.flip()

pygame.quit()

