import sys
from time import sleep
import pygame
from random import randint
from bullet import Bullet
from alien import Alien
from star import Star
from ship import Ship

def check_keydown_events(event, di_settings, screen, ship, bullets):
    """Responde a pressionar a tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        fire_bullet(di_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    
def check_keyup_events(event, ship):
    """Responde a soltar a tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(di_settings, screen, ship, bullets):
    """Dispara um projétil se o limete ainda não foi alcançado."""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(bullets) < di_settings.bullets_allowed:
        new_bullet = Bullet(di_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(di_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responde a eventos de pressionar teclas e mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, di_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(di_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(di_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reinicia as configurações do jogo
        di_settings.initialize_dynamic_setting()

        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True

        # Reinicia as imagens do painel de pontuaçao
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota e centraliza a espaçonave
        create_fleet(di_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(di_settings, screen, stats, sb, ship, aliens, bullets, moon, stars, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(di_settings.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    moon.blitme()
    stars.draw(screen)
    aliens.draw(screen)

    # Desenha a informação sobre a pontuação
    sb.show_score()

    # Desenha o botão Play se o jogo estiver intativo
    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(di_settings, screen, stats, sb, ship, aliens, bullets):
    """Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
    # Atualiza as posições dos projéteis
    bullets.update()
    
    # Livra-se dos projéteis que desapareceem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) # Verifica se os projéteis estão sendo apagados

    check_bullet_alien_collisions(di_settings, screen, stats, sb, ship, aliens, bullets)
 
def get_number_aliens_x(di_settings, alien_width):
    """"Determina o número de alienígenas que cabem em uma linha."""
    number_aliens_x = int(di_settings.screen_width / (2 * alien_width) - 1)
    return number_aliens_x

def get_number_rows(di_settings, ship_height, alien_height):
    """Determina o número de linhas vom alienígenas que cabem na tela."""
    availabel_space_y = (di_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(availabel_space_y / (2 * alien_height))
    return number_rows

def create_alien(di_settings, screen, aliens, alien_number, row_number):
    """Cria um alienígena e o posiciona na linha."""
    alien = Alien(di_settings, screen)
    alien_width = alien.rect.width
    # O espaçamento entre os alienígenas é igual à largura de um alienígena
    alien.x = alien_width + 2 * alien_width * alien_number 
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(di_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas."""
    # Cria um alienígena e calcula o número de alienígenas em uma linha
    alien = Alien(di_settings, screen)
    number_aliens_x = get_number_aliens_x(di_settings, alien.rect.width)
    number_rows = get_number_rows(di_settings, ship.rect.height, alien.rect.height)

    # Cria a frota de alienígenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(di_settings, screen, aliens, alien_number, row_number)

def get_number_stars_x(di_settings, star_width):
    """"Determina o número de estrelas que cabem em uma linha."""
    number_stars_x = int(di_settings.screen_width / (8 * star_width))
    return number_stars_x

def get_number_star_rows(di_settings, star_height):
    """Determina o número de linhas com estrelas que cabem na tela."""
    number_star_rows = int(di_settings.screen_height / (8 * star_height) )
    return number_star_rows

def create_star(di_settings, screen, stars, star_number, row_number):
    """Cria uma estrela e a posiciona na linha."""
    star = Star(di_settings, screen)
    star_width = star.rect.width
    random_number = randint(-25, 25)
    # O espaçamento entre as estrelas é igual à largura de uma estrela
    star.x = star_width + 8 * star_width * star_number + random_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 8 * star.rect.height * row_number + random_number
    stars.add(star)

def create_sky(di_settings, screen, stars):
    """Cria um céu estrelado."""
    # Cria uma estrela e calcula o número de estrelas em uma linha
    star = Star(di_settings, screen)
    number_stars_x = get_number_stars_x(di_settings, star.rect.width)
    number_rows = get_number_star_rows(di_settings, star.rect.height)
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(di_settings, screen, stars, star_number, row_number)

def update_aliens(di_settings, stats, screen, ship, aliens, bullets):
    """
    Verifica se a frota está em uma das bordas e então
    atualiza as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(di_settings, aliens)
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(di_settings, stats, screen, ship, aliens, bullets)

    # Verifica se há algum alienígena que atingiu a parte inferior da tela
    check_aliens_bottom(di_settings, stats, screen, ship, aliens, bullets) 

def check_fleet_edges(di_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(di_settings, aliens)
            break

def change_fleet_direction(di_settings, aliens):
    """Faz a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += di_settings.fleet_drop_speed
    di_settings.fleet_direction *= -1

def check_bullet_alien_collisions(di_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenha colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += di_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Se a frota toda for destruída, inicia um novo nível
        bullets.empty()
        di_settings.increase_speed()

        # Aumenta o nível
        stats.level += 1
        sb.prep_level()

        create_fleet(di_settings, screen, ship, aliens)

def ship_hit(di_settings, stats, screen, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
    if stats.ships_left > 0:
        # Decrementa ships_left
        stats.ships_left -= 1

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()

        # Cria a nova frota e centraliza a espaçonave
        create_fleet(di_settings, screen, ship, aliens)
        ship.center_ship()

        #Faz uma pausa
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(di_settings, stats, screen, ship, aliens, bullets):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(di_settings, stats, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """Verifica se há uma nova pontuação máxima."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()