class GameStats():
    """Armazena dados estatísticos do jogo."""

    def __init__(self, di_settings):
        """Inicializa os dados estatísticos."""
        self.di_settings = di_settings
        self.reset_stats()
        self.high_score = 0

        # Inicia o jogo em um estado ativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.di_settings.ship_limit
        self.score = 0
        self.level = 1

