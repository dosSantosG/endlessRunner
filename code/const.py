# C
import pygame

C_BLACK = (0, 0, 0)
C_YELLOW = (255, 180, 0)
C_BLUE = (0, 80, 122)
C_WHITE = (255, 255, 255)
# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENEMY_SPAWN_TIME = 1000
ENTITY_SPEED = {
    'level1Bg0': 1,
    'level1Bg1': 2,
    'level1Bg2': 3,
    'level1Bg3': 4,
    'level1Bg4': 5,
    'level1Bg5': 0,
    'level2Bg0': 0,
    'level2Bg1': 1,
    'level2Bg2': 1,
    'level2Bg3': 1,
    'level2Bg4': 2,
    'level2Bg5':0,
    'player1': 15,
    'player2': 15,
    'enemy1': 8,
    'enemy2': 6,
    'enemy3': 13,

}
# M
MENU_OPTION = (
    '1P - ARCADE (PVE)',
    '2P - ARENA (PVP)',
    'SCORE',
    'EXIT')
MUSIC_VOLUME = 0.1
# P
PLAYER_KEY_UP = {'player2': pygame.K_UP,
                 'player1': pygame.K_w}
PLAYER_KEY_DOWN = {'player2': pygame.K_DOWN,
                   'player1': pygame.K_s}
PLAYER_KEY_LEFT = {'player2': pygame.K_LEFT,
                   'player1': pygame.K_a}
PLAYER_KEY_RIGHT = {'player2': pygame.K_RIGHT,
                    'player1': pygame.K_d}
PLAYER_KEY_SHOOT = {'player2': pygame.K_RCTRL,
                    'player1': pygame.K_LCTRL}

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

