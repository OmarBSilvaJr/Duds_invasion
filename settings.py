class Settings():
    """Uma classe para armazenar todas as configurações do jogo Duds Invasion."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (65, 105, 225)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3



