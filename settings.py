class Settings():
    """Uma classe para armazenar todas as configurações do jogo Duds Invasion."""

    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (65, 105, 225)

        # Configurações da espaçonave
        self.ship_limit = 3

        # Configurações dos alienígenas
        self.fleet_drop_speed = 10
        
        # Configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        # A taxa com que a velocidade do jogo aumenta
        self.speed_scale = 1.1

        # A taxa com que os pontos para cada alienígena aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Inicializa as configurações que mudam no decorrer do jogo."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        self.alien_points = 50

        # fleet_direction = 1 representa a direita; -1 a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        """Aumenta as configurações de velocidade e os pontos para cada alienígena."""
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
