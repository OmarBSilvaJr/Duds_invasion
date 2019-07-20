import pygame

class Moon():
    def __init__(self, di_settings, screen):
        """Inicializa a lua e define sua posição inicial."""
        self.screen = screen
        self.di_settings = di_settings

        # Carrega a imagem da lua e obtém seu rect
        self.image = pygame.image.load('Figuras/moon.bmp')
        self.rect = self.image.get_rect()
                
        # Inicia a lua na parte superior direito da tela
        self.rect.x = di_settings.screen_width - self.rect.width
        self.rect.y = 0
        
    def blitme(self):
        """Desenha a lua em sua posição atual."""
        self.screen.blit(self.image, self.rect)
