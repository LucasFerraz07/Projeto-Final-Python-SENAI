import pygame
import pygame_gui
import random


class Pergunta:
    def __init__(self, enunciado, alternativas, correta):
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.correta = correta  # índice da resposta correta (0 a 3)


class FaseJogando:
    def __init__(self, manager, dificuldade):
        self.manager = manager
        self.finalizado = False
        self.dificuldade = dificuldade
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.perguntas = self.carregar_perguntas()
        self.botoes = [] 
        self.tempo_total = 60  # segundos
        self.tempo_restante = self.tempo_total
        self.criando_barra_tempo()
        self.exibir_pergunta()

    def carregar_perguntas(self):
        todas = {
            'FACIL': [
                Pergunta('Quanto é 2 + 3?', ['4', '5', '6', '7'], 1),
                Pergunta('Quanto é 5 + 4?', ['8', '9', '10', '11'], 1),
                Pergunta('Quanto é 6 - 2?', ['2', '3', '4', '5'], 2),
                Pergunta('Quanto é 3 + 3?', ['5', '6', '7', '8'], 1),
                Pergunta('Quanto é 10 - 1?', ['9', '10', '8', '7'], 0),
                Pergunta('Quanto é 4 + 4?', ['6', '7', '8', '9'], 2),
                Pergunta('Quanto é 7 - 5?', ['3', '2', '1', '4'], 1),
                Pergunta('Quanto é 1 + 1?', ['1', '2', '3', '4'], 1),
                Pergunta('Quanto é 9 - 3?', ['5', '6', '7', '8'], 1),
                Pergunta('Quanto é 2 + 6?', ['6', '7', '8', '9'], 2),
                Pergunta('Quanto é 10 - 2?', ['7', '8', '9', '10'], 1),
                Pergunta('Quanto é 3 + 5?', ['7', '8', '9', '10'], 1),
                Pergunta('Quanto é 7 + 1?', ['7', '8', '9', '6'], 1),
                Pergunta('Quanto é 8 - 4?', ['3', '4', '5', '6'], 1),
                Pergunta('Quanto é 6 + 3?', ['9', '8', '7', '6'], 0),
            ],
            'MEDIO': [
                Pergunta('Quanto é 12 x 3?', ['36', '33', '30', '39'], 0),
                Pergunta('Quanto é 45 ÷ 5?', ['9', '7', '10', '8'], 0),
                Pergunta('Quanto é 8 x 4?', ['32', '28', '36', '30'], 0),
                Pergunta('Quanto é 50 - 27?', ['22', '23', '24', '25'], 1),
                Pergunta('Quanto é 72 ÷ 8?', ['8', '9', '10', '11'], 1),
                Pergunta('Quanto é 100 - 43?', ['56', '57', '58', '60'], 1),
                Pergunta('Quanto é 25 + 36?', ['60', '61', '62', '63'], 1),
                Pergunta('Quanto é 7 x 6?', ['40', '42', '45', '48'], 1),
                Pergunta('Quanto é 81 ÷ 9?', ['8', '9', '10', '11'], 1),
                Pergunta('Quanto é 9 x 9?', ['81', '72', '90', '99'], 0),
                Pergunta('Quanto é 120 - 90?', ['20', '30', '40', '50'], 1),
                Pergunta('Quanto é 64 ÷ 8?', ['7', '8', '9', '6'], 1),
                Pergunta('Quanto é 14 x 2?', ['28', '26', '30', '24'], 0),
                Pergunta('Quanto é 90 ÷ 10?', ['9', '8', '10', '11'], 0),
                Pergunta('Quanto é 55 + 22?', ['76', '77', '78', '79'], 1),
            ],
            'DIFICIL': [
                Pergunta('Quanto é (12 + 8) × 2?', ['40', '42', '36', '38'], 0),
                Pergunta('Quanto é 121 ÷ 11?', ['10', '11', '12', '13'], 1),
                Pergunta('Quanto é 144 ÷ 12?', ['10', '11', '12', '13'], 2),
                Pergunta('Quanto é 17 x 3?', ['51', '52', '53', '54'], 0),
                Pergunta('Quanto é 100 - (25 + 35)?', ['40', '50', '45', '60'], 0),
                Pergunta('Quanto é 13 x 4?', ['52', '53', '54', '55'], 0),
                Pergunta('Quanto é 144 - 66?', ['76', '78', '80', '82'], 1),
                Pergunta('Quanto é 88 ÷ 8?', ['10', '11', '12', '13'], 1),
                Pergunta('Quanto é 8²?', ['64', '72', '81', '49'], 0),
                Pergunta('Quanto é √81?', ['7', '8', '9', '10'], 2),
                Pergunta('Quanto é 13 + 27?', ['40', '41', '39', '42'], 0),
                Pergunta('Quanto é 25 x 4?', ['100', '90', '95', '110'], 0),
                Pergunta('Quanto é 10²?', ['100', '110', '120', '130'], 0),
                Pergunta('Quanto é 121 - 22?', ['99', '98', '100', '97'], 0),
                Pergunta('Quanto é 96 ÷ 8?', ['12', '11', '13', '10'], 0),
            ]
        }

        return random.sample(todas[self.dificuldade], 10)

    def exibir_pergunta(self):
        self.enunciado_label = pygame_gui.elements.UILabel(
            pygame.Rect(200, 150, 400, 50),
            text=self.perguntas[self.pergunta_atual].enunciado,
            manager=self.manager
        )

        self.botoes = []
        for i, alternativa in enumerate(self.perguntas[self.pergunta_atual].alternativas):
            botao = pygame_gui.elements.UIButton(
                pygame.Rect(250, 230 + i * 60, 300, 50),
                text=alternativa,
                manager=self.manager,
                object_id=pygame_gui.core.ObjectID(class_id="@alternativa", object_id=f"resp_{i}")
            )
            self.botoes.append(botao)

    def limpar_pergunta(self):
        self.enunciado_label.kill()
        for botao in self.botoes:
            botao.kill()

    def responder(self, botao_clicado):
        if self.pergunta_atual >= len(self.perguntas):
            return 

        for i, botao in enumerate(self.botoes):
            if botao == botao_clicado:

                correta = self.perguntas[self.pergunta_atual].correta
                if i == correta:
                    self.pontuacao += 10
                else:
                    self.pontuacao -= 5

                self.limpar_pergunta()
                self.pergunta_atual += 1

                if self.pergunta_atual < len(self.perguntas):
                    self.exibir_pergunta()
                else:
                    self.encerrar()
                break

    def criando_barra_tempo(self):
        self.barra_tempo = pygame_gui.elements.UIProgressBar(
            pygame.Rect(200, 100, 400, 30),
            manager=self.manager
        )

    def atualizar_tempo(self, tempo_delta):
        self.tempo_restante -= tempo_delta
        progresso = max(0, self.tempo_restante / self.tempo_total)
        self.barra_tempo.set_current_progress(progresso * 100)

        if self.tempo_restante <= 0:
            self.limpar_pergunta()
            self.encerrar()

    def encerrar(self):
        self.limpar_pergunta()
        self.barra_tempo.kill()
        self.finalizado = True
