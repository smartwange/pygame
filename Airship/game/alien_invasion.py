import pygame
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    ''' 初始化游戏并创建一个屏幕对象'''
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion1.1")
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    '''开始游戏的主循环'''
    while True:
        # 事件循环
        gf.check_events(ship)
        ship.update()
        '''每次循环时都重绘屏幕，让最近绘制的屏幕可见'''
        gf.update_screen(ai_settings, screen, ship)
run_game()
