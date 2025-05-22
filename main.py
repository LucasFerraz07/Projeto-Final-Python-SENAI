import pygame
import pygame_gui
import pygame_gui.ui_manager

pygame.init()

largura_tela = 800
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da cobrinha')

# criando manager para o pygame_gui
gerente_menu = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')
gerente_inicio = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')
gerente_jogando = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')
gerente_score = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')

# pinta a tela
# Usa o RGB como padrão 
tela_cor = (0, 0, 0)
tela.fill(tela_cor)

#Criação botão menu:
menu_button_facil = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 350), (100, 50)]),
        text='FÁCIL',
        manager = gerente_menu
    )

menu_button_medio = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 401), (100, 50)]),
        text='MÉDIO',
        manager = gerente_menu
    )

menu_button_dificil = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 451), (100, 50)]),
        text='DIFÍCIL',
        manager = gerente_menu
    )

#Criação botão inicio:
start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect([(350, 350), (100, 50)]),
        text='Start Game',
        manager = gerente_inicio
    )

# estados do jogo:
# menu, inicio, jogando, score, fim
estado = 'menu'

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        gerente_menu.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                estado = 'jogando'