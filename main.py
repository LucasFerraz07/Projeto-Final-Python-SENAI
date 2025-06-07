import pygame
import pygame_gui
from faseJogando import FaseJogando

pygame.init()

score_label = None
voltar_menu_button = None

largura_tela = 800
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('quickly')

manager = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')

logo_image = pygame.image.load("images/logo_quicly.png").convert_alpha()
logo_image = pygame.transform.scale(logo_image, (400, 200))
logo_rect = logo_image.get_rect(center=(largura_tela // 2, 200)) 


tela.fill((255, 255, 255))

# Estado e dificuldade
estado = 'menu'
dificuldade = 'FACIL'
fase_jogando = None

# Botões de menu
menu_button_facil = pygame_gui.elements.UIButton(
    pygame.Rect(350, 350, 100, 50), 'FÁCIL', manager=manager
)
menu_button_medio = pygame_gui.elements.UIButton(
    pygame.Rect(350, 410, 100, 50), 'MÉDIO', manager=manager
)
menu_button_dificil = pygame_gui.elements.UIButton(
    pygame.Rect(350, 470, 100, 50), 'DIFÍCIL', manager=manager
)

inicio_button = None
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000  # 100 segundos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if estado == 'menu':
                if event.ui_element == menu_button_facil:
                    dificuldade = 'FACIL'
                elif event.ui_element == menu_button_medio:
                    dificuldade = 'MEDIO'
                elif event.ui_element == menu_button_dificil:
                    dificuldade = 'DIFICIL'

                menu_button_facil.kill()
                menu_button_medio.kill()
                menu_button_dificil.kill()

                inicio_button = pygame_gui.elements.UIButton(
                    pygame.Rect(350, 350, 100, 50), 'START GAME', manager=manager
                )

                voltar_menu_button = pygame_gui.elements.UIButton(
                pygame.Rect(300, 400, 200, 50),
                text='Voltar ao Menu',
                manager=manager
                )
                estado = 'inicio'
            
            elif estado == 'inicio' and event.ui_element == voltar_menu_button:
                inicio_button.kill()
                voltar_menu_button.kill()
                
                # Recria botões do menu
                menu_button_facil = pygame_gui.elements.UIButton(
                    pygame.Rect(350, 350, 100, 50), 'FÁCIL', manager=manager
                )
                menu_button_medio = pygame_gui.elements.UIButton(
                    pygame.Rect(350, 410, 100, 50), 'MÉDIO', manager=manager
                )
                menu_button_dificil = pygame_gui.elements.UIButton(
                    pygame.Rect(350, 470, 100, 50), 'DIFÍCIL', manager=manager
                )
                
                estado = 'menu'

            elif estado == 'inicio' and event.ui_element == inicio_button:
                inicio_button.kill()
                voltar_menu_button.kill()
                fase_jogando = FaseJogando(manager, dificuldade)
                estado = 'jogando'

            elif estado == 'jogando' and fase_jogando is not None:
                fase_jogando.responder(event.ui_element)

            elif estado == 'score':
                if event.ui_element == voltar_menu_button:
                    score_label.kill()
                    voltar_menu_button.kill()
                    # Recria botões do menu
                    menu_button_facil = pygame_gui.elements.UIButton(
                        pygame.Rect(350, 350, 100, 50), 'FÁCIL', manager=manager
                    )
                    menu_button_medio = pygame_gui.elements.UIButton(
                        pygame.Rect(350, 410, 100, 50), 'MÉDIO', manager=manager
                    )
                    menu_button_dificil = pygame_gui.elements.UIButton(
                        pygame.Rect(350, 470, 100, 50), 'DIFÍCIL', manager=manager
                    )
                    fase_jogando = None
                    estado = 'menu'


    tela.fill((255, 255, 255))

    if estado in ('menu', 'inicio'):
        tela.blit(logo_image, logo_rect)


    if estado == 'jogando' and fase_jogando is not None:
        fase_jogando.atualizar_tempo(time_delta)

        if fase_jogando.finalizado:
            # Cria os elementos da tela de score
            score_label = pygame_gui.elements.UILabel(
                pygame.Rect(250, 300, 300, 50),
                text=f'Sua pontuação: {fase_jogando.pontuacao}',
                manager=manager
            )
            voltar_menu_button = pygame_gui.elements.UIButton(
                pygame.Rect(300, 400, 200, 50),
                text='Voltar ao Menu',
                manager=manager
            )
            estado = 'score'

    
    manager.update(time_delta)
    manager.draw_ui(tela)
    pygame.display.flip()

pygame.quit()
