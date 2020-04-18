import pygame, sys

class Game():
    Runners = []
    __starline = 20
    __finishline = 620
    

    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("fondo/playa.png")
        pygame.display.set_caption("Carrera de caballitos")
     
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
        self.__screen.blit(self._background, (0, 0))
        
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()
    
    
if __name__== "__main__":
    game = Game()
    pygame.font.init()
    game.competir()