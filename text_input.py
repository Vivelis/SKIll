import pygame

def enter_text():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    text = ""
    done = False
    white=(255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)

    bg = (0,0,0) 
    while not done:
        for event in pygame.event.get():
            screen.fill(bg)
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                else:
                    text += event.unicode
            font = pygame.font.SysFont("Arial", 30)
        screen.fill(bg)
        txtsurf = font.render(text, True, white)
        screen.blit(txtsurf,(200 - txtsurf.get_width() // 2, 150 - txtsurf.get_height() // 2))
        pygame.display.update()
    return text
