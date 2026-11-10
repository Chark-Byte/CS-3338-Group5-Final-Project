import pygame

pygame.init()
W, H = 1280, 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Trap Motel-Hotel")
clock = pygame.time.Clock()

# colors
WHITE, RED, YELLOW, GRAY = (240, 240, 240), (180, 35, 45), (255, 210, 80), (160, 160, 160)

# fonts
title_font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 48)

# menu options, and the message shown on each screen they open
OPTIONS = ["NEW GAME", "CONTINUE", "SETTINGS", "LEAVE GAME"]
SCREENS = {
    "NEW GAME": "Welcome to the Trap Motel-Hotel.......",
    "CONTINUE": "No saved games found yet.",
    "SETTINGS": "Settings coming soon.",
}


def draw_text(text, font, color, y):
    """Draw centered text at height y and return its rect."""
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(W // 2, y))
    screen.blit(surf, rect)
    return rect


state = "MENU"      # "MENU", or the name of the option that was picked
selected = 0
rects = []          # clickable areas of the menu options
running = True

while running:
    clock.tick(60)
    choice = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if state != "MENU":
                if event.key == pygame.K_ESCAPE:
                    state = "MENU"
            elif event.key in (pygame.K_UP, pygame.K_w):
                selected = (selected - 1) % len(OPTIONS)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                selected = (selected + 1) % len(OPTIONS)
            elif event.key == pygame.K_RETURN:
                choice = OPTIONS[selected]

        elif state == "MENU" and event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
            for i, rect in enumerate(rects):
                if rect.collidepoint(event.pos):
                    selected = i
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        choice = OPTIONS[i]

    if choice == "LEAVE GAME":
        running = False
    elif choice:
        state = choice

    # ---------- main menu drawing ----------
    screen.fill((0, 0, 0))

    if state == "MENU":
        draw_text("Trap Motel-Hotel", title_font, RED, 180)
        rects = []
        for i, text in enumerate(OPTIONS):
            is_sel = i == selected
            label = f"> {text} <" if is_sel else text
            rect = draw_text(label, button_font, YELLOW if is_sel else WHITE, 330 + i * 70)
            rects.append(rect.inflate(60, 20))
        draw_text("UP / DOWN to move    ENTER to select", small_font, GRAY, H - 50)
    else:
        draw_text(SCREENS[state], button_font, WHITE, H // 2)
        draw_text("Press ESC to go back to the menu", small_font, GRAY, H - 50)

    pygame.display.flip()

pygame.quit()