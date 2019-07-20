import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, di_settings, screen):
        """Inicializa a estrela e define sua posição inicial."""
        super(Star, self).__init__()
        self.screen = screen
        self.di_settings = di_settings

        # Carrega a imagem da estrela e obtém seu rect
        self.image = pygame.image.load('Figuras/star.bmp')
        self.rect = self.image.get_rect()
                
        # Inicia a estrela na parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """Desenha a lua em sua posição atual."""
        self.screen.blit(self.image, self.rect)
