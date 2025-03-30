#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_WHITE, WIN_WIDTH, C_BLACK, WIN_HEIGHT, MUSIC_VOLUME, MENU_OPTION
from code.entityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 100000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if game_mode == MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('player2'))

    def run(self, ):
        pygame.mixer_music.fadeout(400)

        pygame.mixer_music.load(f'./assets/audio/music/{self.name}.wav')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(MUSIC_VOLUME)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # printed text
            self.level_text(40, f'{self.name} - TIMEOUT: {self.timeout / 1000:.1f}s ', C_WHITE, (10, 5))
            self.level_text(40, f'FPS: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 60))
            self.level_text(40, f'Entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 30))
            pygame.display.flip()

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
