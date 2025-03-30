#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_BLACK, WIN_WIDTH, C_BLUE, C_WHITE, C_YELLOW, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/menuBg/menuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/audio/music/menuMusic.WAV')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.2)
        while True:
            self.window.blit(source=self.surf, dest=self.rect, )
            # Title of the game
            self.menu_text(205, "Mafia", C_WHITE, ((WIN_WIDTH / 2), 120))
            self.menu_text(200, "Mafia", C_BLUE, ((WIN_WIDTH / 2), 120))
            self.menu_text(205, "Assault", C_WHITE, ((WIN_WIDTH / 2), 230))
            self.menu_text(200, "Assault", C_BLUE, ((WIN_WIDTH / 2), 230))
            # Menu itens
            for i in range(len(MENU_OPTION)):
                self.menu_text(55, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 400 + 60 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
