import pygame
import labirinto
import os

# Inicializa o Pygame
pygame.init()

# Configurações básicas
TAMANHO_BLOCO = 50
LARGURA = labirinto.labirinto.shape[1] * TAMANHO_BLOCO
ALTURA = labirinto.labirinto.shape[0] * TAMANHO_BLOCO

# Carregamento das imagens
def carregar_imagem(nome_arquivo):
    caminho = os.path.join("images", nome_arquivo)
    try:
        img = pygame.image.load(caminho)
        return pygame.transform.scale(img, (TAMANHO_BLOCO, TAMANHO_BLOCO))
    except pygame.error:
        print(f"Erro ao carregar imagem: {caminho}")
        return None

img_grama = carregar_imagem("grama.png")
img_tijolo = carregar_imagem("tijolo.png")
img_tesouro = carregar_imagem("tesouro.png")
img_agente = carregar_imagem("agente.png")

# Criando a janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto com Tesouro")

# Relógio para controlar a taxa de atualização
clock = pygame.time.Clock()

# Função para desenhar o labirinto
def desenhar_labirinto(posicao_agente):
    tela.fill((0, 0, 0))  # Fundo preto

    for i in range(labirinto.labirinto.shape[0]):
        for j in range(labirinto.labirinto.shape[1]):
            if labirinto.labirinto[i, j] == 1 and img_tijolo:  # Parede
                tela.blit(img_tijolo, (j * TAMANHO_BLOCO, i * TAMANHO_BLOCO))
            elif labirinto.labirinto[i, j] == 2 and img_tesouro:  # Tesouro
                tela.blit(img_tesouro, (j * TAMANHO_BLOCO, i * TAMANHO_BLOCO))
            elif img_grama:  # Caminho livre
                tela.blit(img_grama, (j * TAMANHO_BLOCO, i * TAMANHO_BLOCO))

    # Desenha o agente na posição atual, se a imagem for válida
    if img_agente:
        tela.blit(img_agente, (posicao_agente[1] * TAMANHO_BLOCO, posicao_agente[0] * TAMANHO_BLOCO))
    else:
        pygame.draw.rect(
            tela, (0, 255, 0),
            (posicao_agente[1] * TAMANHO_BLOCO, posicao_agente[0] * TAMANHO_BLOCO, TAMANHO_BLOCO, TAMANHO_BLOCO)
        )

    pygame.display.flip()  # Atualiza a tela

# Loop principal
def iniciar_visualizacao():
    posicao_agente = labirinto.posicao_inicial
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Atualiza a posição do agente a partir do arquivo externo
        try:
            with open("posicao_atual.txt", "r") as arquivo:
                linha = arquivo.readline().strip()
                if linha:
                    nova_posicao = tuple(map(int, linha.split(",")))
                    if (
                        0 <= nova_posicao[0] < labirinto.labirinto.shape[0]
                        and 0 <= nova_posicao[1] < labirinto.labirinto.shape[1]
                    ):
                        posicao_agente = nova_posicao
        except (FileNotFoundError, ValueError):
            pass  # Evita erro se o arquivo ainda não existir ou a leitura falhar

        desenhar_labirinto(posicao_agente)
        clock.tick(30)  # Controla a taxa de atualização para evitar uso excessivo de CPU

    pygame.quit()

if __name__ == "__main__":
    iniciar_visualizacao()

