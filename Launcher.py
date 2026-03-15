import sys

import pygame
from pygame import *
WIDTH, HEIGHT = 500, 500

mixer.init()
clicksound = pygame.mixer.Sound("Assets/Sounds/click.mp3")
clicksound.set_volume(0.3)
def launcher():
    init()
    screen = display.set_mode((WIDTH, HEIGHT))
    display.set_caption("Mike Launcher")

    font_title = font.Font(None, 56)
    font_btn = font.Font(None, 42)
    font_input = font.Font(None, 36)

    turnonmusic = True
    mode = "Main"

    while True:
        if mode == "Main":
            screen.fill((50,50,0))

            title = font_title.render("Mini Mike Deltarune Battle", True, (255, 255, 255))
            screen.blit(title, title.get_rect(center=(WIDTH / 2, 40)))

            play_btn = Rect(100, 100, 300, 70)
            settings_btn = Rect(100, 200, 300, 70)
            exit_btn = Rect(100, 300, 300, 70)

            draw.rect(screen, (0, 180, 0), play_btn, border_radius=12)
            draw.rect(screen, (18, 180, 0), settings_btn, border_radius=12)
            draw.rect(screen, (180, 0, 0), exit_btn, border_radius=12)

            screen.blit(font_btn.render("ГРАТИ", True, (0, 0, 0)),
                        font_btn.render("ГРАТИ", True, (0, 0, 0)).get_rect(center=play_btn.center))
            screen.blit(font_btn.render("НАЛАШТУВАННЯ", True, (0, 0, 0)),
                        font_btn.render("НАЛАШТУВАННЯ", True, (0, 0, 0)).get_rect(center=settings_btn.center))
            screen.blit(font_btn.render("ВИХІД", True, (0, 0, 0)),
                        font_btn.render("ВИХІД", True, (0, 0, 0)).get_rect(center=exit_btn.center))

            for e in event.get():
                if e.type == QUIT:
                    quit()

                if e.type == MOUSEBUTTONDOWN:
                    if play_btn.collidepoint(e.pos):
                        clicksound.play()
                        return turnonmusic

                    if exit_btn.collidepoint(e.pos):
                        quit()

                    if settings_btn.collidepoint(e.pos):
                        clicksound.play()
                        mode = "Settings"

            display.update()
        elif mode == "Settings":
            screen.fill((50,40,50))

            title = font_title.render("НАЛАШТУВАННЯ", True, (180, 50, 0))
            screen.blit(title, title.get_rect(center=(WIDTH / 2, 40)))

            exitsettings_btn = Rect(100, 100, 300, 70)

            volume_btn = Rect(150, 240, 200, 70)

            draw.rect(screen, (180, 80, 0), exitsettings_btn, border_radius=12)

            if turnonmusic == True:
                draw.rect(screen, (150, 0, 0), volume_btn, border_radius=12)
            else:
                draw.rect(screen, (0, 150, 0), volume_btn, border_radius=12)

            screen.blit(font_btn.render("ПОВЕРНУТИСЯ", True, (0, 0, 0)),
                        font_btn.render("ПОВЕРНУТИСЯ", True, (0, 0, 0)).get_rect(center=exitsettings_btn.center))

            if turnonmusic == True:
                screen.blit(font_btn.render("ВИМКНУТИ", True, (0, 0, 0)),
                            font_btn.render("ВИМКНУТИ", True, (0, 0, 0)).get_rect(center=volume_btn.center))
            else:
                screen.blit(font_btn.render("УВІМКНУТИ", True, (0, 0, 0)),
                            font_btn.render("УВІМКНУТИ", True, (0, 0, 0)).get_rect(center=volume_btn.center))


            tc = 0, 150, 0
            tt = "Аудіо: Увімкнено"
            if turnonmusic == False:
                tc = 150, 0, 0
                tt = "Аудіо: Вимкнено"

            screen.blit(font_input.render(tt, True, tc), (100, 200))

            for e in event.get():
                if e.type == QUIT:
                    quit()

                if e.type == MOUSEBUTTONDOWN:
                    if exitsettings_btn.collidepoint(e.pos):
                        clicksound.play()
                        mode = "Main"


                    if volume_btn.collidepoint(e.pos):
                        clicksound.play()
                        if turnonmusic == True:
                            turnonmusic = False
                        else:
                            turnonmusic = True

            display.update()