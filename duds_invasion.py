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
import game_functions as gf

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    di_settings = Settings()
    screen = pygame.display.set_mode((di_settings.screen_width, di_settings.screen_height))
    pygame.display.set_caption("Duds Invasion x Space Guto                     by Omar Jr")

    # Cria uma espaçonave
    ship = Ship(di_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
        
    # Inicia o laço principal do jogo
    while True:
        gf.check_events(di_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(di_settings, screen, ship, bullets)

run_game()
