import pygame
import pygame_gui
import pygame_gui.ui_manager

pygame.init()

largura_tela = 800
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da cobrinha')

# criando manager para o pygame_gui
gerente = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')

# pinta a tela
# Usa o RGB como padrão 
tela_cor = (0, 0, 0)
tela.fill(tela_cor)

#Criação botão menu:
menu_button_facil = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 350), (100, 50)]),
        text='FÁCIL',
        manager = gerente
    )

menu_button_medio = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 401), (100, 50)]),
        text='MÉDIO',
        manager = gerente
    )

menu_button_dificil = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 451), (100, 50)]),
        text='DIFÍCIL',
        manager = gerente
    )


# estados do jogo:
# menu, #inicio, jogando, score, fim
estado = 'menu'

#dificuldade do jogo:
#facil, medio, dificil
dificuldade = 'FACIL'

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        gerente.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == menu_button_facil:
                estado = 'inicio'
                dificuldade = 'FACIL' 
                menu_button_facil.kill()
                menu_button_medio.kill()
                menu_button_dificil.kill()
                #botão start
                inicio_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect([(350, 350), (100, 50)]),
                text='START GAME',
                manager = gerente
                )
            elif event.ui_element == menu_button_medio:
                estado = 'inicio'
                dificuldade = 'MEDIO' 
                menu_button_facil.kill()
                menu_button_medio.kill()
                menu_button_dificil.kill()
                #botão start
                inicio_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect([(350, 350), (100, 50)]),
                text='START GAME',
                manager = gerente
                )
            elif event.ui_element == menu_button_dificil:
                estado = 'inicio'
                dificuldade = 'DIFICIL' 
                menu_button_facil.kill()
                menu_button_medio.kill()
                menu_button_dificil.kill()
                #botão start
                inicio_button = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect([(350, 350), (100, 50)]),
                text='START GAME',
                manager = gerente
                )
            elif event.ui_element == inicio_button:
                estado = 'jogando'
                inicio_button.kill()

    tela.fill(tela_cor)


    # estou pedindo para atualizar os elementos do pygame_gui    
    gerente.update(1 / 60.0)
    gerente.draw_ui(tela)
    
    pygame.display.flip()

pygame.quit()