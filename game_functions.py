import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, di_settings, screen, ship, bullets):
    """Responde a pressionar a tecla."""
    if event.key == pygame.K_RIGHT:
            ship.moving_right = True
    elif event.key == pygame.K_LEFT:
            ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        fire_bullet(di_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Responde a soltar a tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(di_settings, screen, ship, bullets):
    """Dispara um projétil se o limete ainda não foi alcançado."""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < di_settings.bullets_allowed:
        new_bullet = Bullet(di_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(di_settings, screen, ship, bullets):
    """Responde a eventos de pressionar teclas e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, di_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(di_settings, screen, ship, bullets):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(di_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()

    # Apaga os projéteis que desapareceem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) # Verifica se os projéteis estão sendo apagados