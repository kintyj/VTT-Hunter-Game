from SockLib.Input import intput
from character import CharacterOption,CharacterSheet,Character
import pygame, pygame_gui


if __name__ == "__main__":
    
    #region initalize Pygame
    pygame.init()
    screen = pygame.display.set_mode((1920,1080))
    pygame.display.set_caption("Hunter Game")
    clock = pygame.time.clock()
    gui_manager = pygame_gui.UIManager((1920,1080))
    font = pygame.font.Font(None, 20)
    #endregion

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()