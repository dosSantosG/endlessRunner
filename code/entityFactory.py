#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image

from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player1':
                return Player('player1', ((WIN_WIDTH / 2), (WIN_HEIGHT / 2)))
            case 'player2':
                return Player('player2', ((WIN_WIDTH / 2) + 400, (WIN_HEIGHT / 2)))
