import pygame

W, H = 1280, 720
WHITE, RED, YELLOW, GRAY = (240, 240, 240), (180, 35, 45), (255, 210, 80), (160, 160, 160)

ROWS = ["Volume", "Sound", "Go Back"]


def draw_text(screen, text, font, color, center):
    """Draw text centered on a point and return its rect."""
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=center)
    screen.blit(surf, rect)
    return rect


def change(options, row, delta):
    """Change the value(s) of one settings row."""
    if row == "Volume":
        options["volume"] = max(0, min(10, options["volume"] + delta))
    elif row == "Sound":
        options["sound"] = not options["sound"]


def run(screen, options):
    """Show the settings screen until Tim goes back, because we're all Tim."""
    clock = pygame.time.Clock()
    title_font = pygame.font.Font(None, 72)
    small_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 48)

    selected = 0
    rects = []

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                row = ROWS[selected]
                if event.key == pygame.K_ESCAPE:
                    return "back"
                elif event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(ROWS)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(ROWS)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    change(options, row, -1)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    change(options, row, +1)
                elif event.key == pygame.K_RETURN:
                    if row == "Go Back":
                        return "back"
                    change(options, row, +1)

            elif event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                for i, rect in enumerate(rects):
                    if rect.collidepoint(event.pos):
                        selected = i
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            if ROWS[i] == "Go Back":
                                return "back"
                            change(options, ROWS[i], +1)

        # ---------- drawing ----------
        screen.fill((0, 0, 0))
        draw_text(screen, "Settings", title_font, RED, (W // 2, 180))

        rects = []
        for i, row in enumerate(ROWS):
            is_sel = i == selected
            color = YELLOW if is_sel else WHITE
            y = 330 + i * 70

            if row == "Go Back":
                label = "> Go Back <" if is_sel else "Go Back"
                draw_text(screen, label, button_font, color, (W // 2, y))
            else:
                if row == "Volume":
                    value = f"< {options['volume']} >"
                else:
                    value = "< ON >" if options["sound"] else "< OFF >"
                draw_text(screen, row, button_font, color, (W // 2 - 150, y))
                draw_text(screen, value, button_font, color, (W // 2 + 150, y))

            rects.append(pygame.Rect(W // 2 - 350, y - 25, 700, 50))

        draw_text(screen, "UP / DOWN to move    LEFT / RIGHT to change    ESC to go back",
                  small_font, GRAY, (W // 2, H - 50))

        pygame.display.flip()