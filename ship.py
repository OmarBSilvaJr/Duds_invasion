import pygame

class Ship():
    def __init__(self, di_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.di_settings = di_settings

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('Figuras/nave4.bmp') #Default nave Guto - nave4.bmp 
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect.top = self.rect.top
        self.rect.centery = self.rect.centery

        # Armazena um valor decimal para o centro da espaçonave
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        # Atualiza o valor do do centro da espaçonave. e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.di_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.di_settings.ship_speed_factor
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.di_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <=  self.screen_rect.bottom:
            self.y += self.di_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.x
        self.rect.centery = self.y      

    def blitme(self):
        """Desenha a espaçonave em sua posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaçonave na tela."""
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.bottom-(self.rect.height / 2)
        
