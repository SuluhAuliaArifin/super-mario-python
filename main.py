import pygame
from classes.Dashboard import Dashboard
from classes.Level import Level
from classes.Menu import Menu
from classes.Sound import Sound
from entities.Mario import Mario


windowSize = 640, 480


def main():
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    dashboard = Dashboard("./img/font.png", 8, screen)
    sound = Sound()
    level = Level(screen, sound, dashboard)
    menu = Menu(screen, dashboard, level, sound)

    while not menu.start:
        menu.update()

    mario = Mario(0, 0, level, screen, dashboard, sound)
    clock = pygame.time.Clock()

    while not mario.restart:
        pygame.display.set_caption("Super Mario running with {:d} FPS".format(int(clock.get_fps())))
        if mario.pause:
            mario.pauseObj.update()
        else:
            level.drawLevel(mario.camera)
            dashboard.update()
            mario.update()
        pygame.display.update()
        clock.tick(max_frame_rate)
    return 'restart'


if __name__ == "__main__":
    exitmessage = 'restart'
    while exitmessage == 'restart':
        exitmessage = main()

font = pygame.font.SysFont("Arial", 26)

def draw_hud(screen, dashboard, level):
    lives_text = font.render(f"Lives: {level.mario.lives}", True, (255, 255, 255))
    score_text = font.render(f"Score: {dashboard.points}", True, (255, 255, 0))
    coin_text = font.render(f"Coins: {dashboard.coins}", True, (255, 255, 0))
    level_text = font.render(f"Level: {level.world}", True, (0, 255, 255))

    screen.blit(lives_text, (20, 15))
    screen.blit(score_text, (20, 45))
    screen.blit(coin_text, (20, 75))
    screen.blit(level_text, (20, 105))
