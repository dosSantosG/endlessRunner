#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, MENU_OPTION
from code.entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if self.name == "player1":
            # moves player 1 up OR down
            if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
                self.rect.centery -= ENTITY_SPEED[self.name]
            elif pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
                self.rect.centery += ENTITY_SPEED[self.name]
            # moves player 1 left OR right
            if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
                self.rect.centerx -= ENTITY_SPEED[self.name]
            elif pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < (WIN_WIDTH/2)-90:
                self.rect.centerx += ENTITY_SPEED[self.name]
        elif self.name == 'player2':
            # moves player 2 up OR down
            if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
                self.rect.centery -= ENTITY_SPEED[self.name]
            elif pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
                self.rect.centery += ENTITY_SPEED[self.name]
            # moves player2 left OR right
            if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > (WIN_WIDTH/2)+90:
                self.rect.centerx -= ENTITY_SPEED[self.name]
            elif pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
                self.rect.centerx += ENTITY_SPEED[self.name]

