#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_BLACK, WIN_WIDTH, C_BLUE, C_WHITE, C_YELLOW, MENU_OPTION, WIN_HEIGHT, MUSIC_VOLUME
from code.entity import Entity
from code.entityFactory import EntityFactory


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/menuBg/menuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option: int = 0
        pygame.mixer_music.load('./assets/audio/music/menuMusic.WAV')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(MUSIC_VOLUME)
        while True:
            # Draw images
            self.window.blit(source=self.surf, dest=self.rect, )
            # Title of the game
            self.menu_text(152, 'Ships and Rocks', C_WHITE, (WIN_WIDTH / 2, 90))
            self.menu_text(150, "Ships and Rocks", C_BLUE, (WIN_WIDTH/2, 90))
            # self.menu_text(100, "Escape", C_WHITE, (340, 120))
            # self.menu_text(102, "Escape", C_BLUE, (340, 120))
            # Menu itens
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(60, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 300 + 60 * i))

                else:
                    self.menu_text(60, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 300 + 60 * i))

            pygame.display.flip()

            # checks for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # closes window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:  # DOWN KEY
                    if event.key == pygame.K_DOWN:
                        if menu_option < (len(MENU_OPTION) - 1):
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
