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
        if self.dificuldade == "facil":
            self.tempo_total = 150
        elif self.dificuldade == "medio":
            self.tempo_total = 120
        elif self.dificuldade == "dificil":
            self.tempo_total = 90
        else:
            self.tempo_total = 120  # valor padrão caso a dificuldade seja desconhecida

        self.tempo_restante = self.tempo_total
        self.criando_barra_tempo()
        self.exibir_pergunta()

    def carregar_perguntas(self):
        todas = {
            'FACIL': [
                Pergunta('Quanto é 4 + 3?', ['6', '5', '7', '8', '9'], 2),
                Pergunta('Quanto é 7 + 3?', ['11', '9', '8', '10', '12'], 3),
                Pergunta('Quanto é 11 + 5?', ['14', '15', '11', '13', '16'], 4),
                Pergunta('Quanto é 20 - 7?', ['11', '27', '13', '15', '10'], 2),
                Pergunta('Quanto é 14 + 6?', ['21', '18', '23', '19', '20'], 4),
                Pergunta('Quanto é 14 - 7?', ['6', '8', '7', '3', '5'], 2),
                Pergunta('Quanto é 13 + 11?', ['23', '25', '26', '27', '24'], 4),
                Pergunta('Quanto é 15 - 6?', ['8', '5', '9', '7', '10'], 2),
                Pergunta('Quanto é 10 + 15?', ['25', '30', '35', '20', '15'], 0),
                Pergunta('Quanto é 7 - 6?', ['2', '1', '3', '13', '4'], 1),
                Pergunta('Quanto é 20 + 2?', ['21', '24', '23', '22', '18'], 3),
                Pergunta('Quanto é 15 - 10?', ['10', '15', '25', '5', '20'], 3),
                Pergunta('Quanto é 23 + 7?', ['31', '29', '33', '31', '30'], 4),
                Pergunta('Quanto é 12 - 4?', ['16', '8', '4', '10', '9'], 1),
                Pergunta('Quanto é 34 + 11?', ['40', '50', '43', '45', '48'], 2),
            ],
            'MEDIO': [
                Pergunta('Quanto é 32 + 18?', ['22', '14', '44', '50', '49'], 3),
                Pergunta('Quanto é 95 - 55?', ['150', '135', '40', '50', '65'], 2),
                Pergunta('Quanto é 45 + 35?', ['10', '80', '75', '85', '90'], 1),
                Pergunta('Quanto é 25 x 2?', ['50', '27', '30', '23', '40'], 0),
                Pergunta('Quanto é 67 + 23?', ['100', '88', '93', '87', '90'], 4),
                Pergunta('Quanto é 10 x 5?', ['15', '50', '25', '35', '20'], 1),
                Pergunta('Quanto é 20 x 3?', ['60', '23', '17', '6', '40'], 0),
                Pergunta('Quanto é 88 + 12?', ['100', '98', '96', '93', '99'], 0),
                Pergunta('Quanto é 29 + 54?', ['78', '83', '82', '79', '86'], 1),
                Pergunta('Quanto é 60 - 30?', ['90', '30', '40', '50', '80'], 1),
                Pergunta('Quanto é 75 - 25?', ['50', '100', '95', '45', '70'], 0),
                Pergunta('Quanto é 15 x 4?', ['19', '20', '60', '50', '45'], 2),
                Pergunta('Quanto é 85 - 45?', ['130', '40', '120', '100', '50'], 1),
                Pergunta('Quanto é 100 - 60?', ['30', '160', '100', '40', '50'], 3),
                Pergunta('Quanto é 30 x 3?', ['33', '30', '60', '29', '90'], 4),
            ],
            'DIFICIL': [
                Pergunta('Quanto é 5 x 10?', ['45', '50', '60', '70', '55'], 1),
                Pergunta('Quanto é 75 - 25?', ['50', '100', '95', '45', '70'], 0),
                Pergunta('Quanto é 12 + 34?', ['46', '56', '48', '38', '26'], 0),
                Pergunta('Quanto é 24 / 3?', ['8', '9', '10', '11', '7'], 0),
                Pergunta('Quanto é 8 x 5?', ['40', '50', '60', '30', '20'], 0),
                Pergunta('Quanto é 56 + 29?', ['85', '75', '65', '95', '15'], 0),
                Pergunta('Quanto é 88 - 32?', ['46', '66', '26', '56', '76'], 3),
                Pergunta('Quanto é 15 x 3?', ['45', '55', '35', '25', '15'], 0),
                Pergunta('Quanto é 49 / 7?', ['7', '6', '5', '4', '8'], 0),
                Pergunta('Quanto é 7 x 6?', ['42', '52', '32', '22', '12'], 0),
                Pergunta('Quanto é 9 x 8?', ['72', '82', '62', '52', '42'], 0),
                Pergunta('Quanto é 91 - 47?', ['54', '34', '44', '24', '64'], 2),
                Pergunta('Quanto é 7 x 6?', ['42', '52', '32', '22', '12'], 0),
                Pergunta('Quanto é 9 x 8?', ['72', '82', '62', '52', '42'], 0),
                Pergunta('Quanto é 55 - 23?', ['42', '22', '12', '52', '32'], 4),
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
                    self.pontuacao += 0

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
