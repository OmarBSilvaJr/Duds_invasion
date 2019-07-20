'''
JOGO: DUDS INVASION X SPACESHIP GUTO

by Omar Júnior for my kids: Guto & Dudu

Descrição: 
- O jogador controla uma espaçonave (Spaceship Guto) que aparece na parte inferior 
  central da tela. 
- O jogador pode mover a nave para a direita e para a esquerda usando as teclas de
  direção e atirar usando a barra de espaço.
- Quando o jogo começa, uma frota de alienígenas (Duds) enche o céu e se desloca na
  tela para os lados e para baixo.
- O jogador atira nos alienígenas e os destrói.
- Se o jogador atingir todos os alienígenas, uma nova frota, que se moverá mais 
  rapidamente que a frota anterior, aparecerá.
- Se algum alienígena atingir a espaçonave do jogador ou alcançar a parte inferior
  da tela, o jogador perderá uma nave.
- Se o jogador perder 03 (três) espaçonaves, o jogo terminará.
'''
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from moon import Moon
from button import Button
import game_functions as gf
from game_stats import GameStats
from scoreboard import Scoreboard

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    #escolha = int(input("Escolha a Nave: 1 - Guto; 2 - Dudu: "))
    pygame.init()
    di_settings = Settings()
    screen = pygame.display.set_mode((di_settings.screen_width, di_settings.screen_height))
    pygame.display.set_caption("""
            DUDS INVASION X SPACE GUTO                  by Omar Jr                  Pressione 'q' para sair""")

    # Cria uma espaçonave, lua, um grupo de projéteis e um grupo de alienígenas
    """
    if escolha == 2:
        nave = 'Figuras/nave0.bmp' #Nave Dudu
    else:
        nave = 'Figuras/nave4.bmp' #Default nave Guto
    """
    ship = Ship(di_settings, screen)
    moon = Moon(di_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()
    
    # Cria a frota de alienígenas
    gf.create_fleet(di_settings, screen, ship, aliens)

    # Cria um céu estrelado
    gf.create_sky(di_settings, screen, stars)

    # Cria o botão Play
    play_button = Button(di_settings, screen, "Jogar")

    # Cria uma instância para armazenar estatísticas do jogo e cria painel de pontuação.
    stats = GameStats(di_settings)
    sb = Scoreboard(di_settings, screen, stats)
        
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(di_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(di_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(di_settings, stats, screen, ship, aliens, bullets)

        #moon.blitme()
        gf.update_screen(di_settings, screen, stats, sb, ship, aliens, bullets, moon, stars, play_button)

run_game()
