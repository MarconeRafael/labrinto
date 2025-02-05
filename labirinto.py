import numpy as np

# Novo labirinto 10x10 (0 = caminho livre, 1 = parede, 2 = tesouro)
labirinto = np.array([
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 2, 1, 1, 1, 0, 0, 1, 1, 1],  # Tesouro na posição (4,1)
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Posições iniciais
posicao_inicial = (0, 0)
posicao_tesouro = (4, 1)  # Posição do tesouro

# Função para exibir o labirinto formatado
def mostrar_labirinto(posicao):
    lab_copy = np.where(labirinto == 1, "#", ".")  # Caminhos e paredes
    lab_copy = np.where(labirinto == 2, "T", lab_copy)  # Tesouro
    x, y = posicao
    lab_copy[x, y] = "A"  # Agente
    print("\n".join([" ".join(row) for row in lab_copy]))  # Exibe o labirinto formatado
    print("\n")

# Função para mover o agente
def mover(posicao, acao):
    movimentos = {"cima": (-1, 0), "baixo": (1, 0), "esquerda": (0, -1), "direita": (0, 1)}
    
    ALTURA, LARGURA = labirinto.shape  # Obtém dimensões do labirinto
    nova_posicao = (posicao[0] + movimentos[acao][0], posicao[1] + movimentos[acao][1])

    # Verifica se a posição é válida (dentro dos limites e sem parede)
    if 0 <= nova_posicao[0] < ALTURA and 0 <= nova_posicao[1] < LARGURA and labirinto[nova_posicao] != 1:
        return nova_posicao
    return posicao  # Se for inválida, mantém a posição

# Testando controle manual pelo terminal
def controlar_agente():
    posicao = posicao_inicial
    mostrar_labirinto(posicao)
    
    while True:
        movimento = input("\nDigite seu movimento (WASD ou 'cima', 'baixo', 'esquerda', 'direita'): ").strip().lower()
        
        if movimento in ["w", "cima"]:
            posicao = mover(posicao, "cima")
        elif movimento in ["s", "baixo"]:
            posicao = mover(posicao, "baixo")
        elif movimento in ["a", "esquerda"]:
            posicao = mover(posicao, "esquerda")
        elif movimento in ["d", "direita"]:
            posicao = mover(posicao, "direita")
        elif movimento == "q":
            print("\n🚪 Saindo do jogo...")
            break
        else:
            print("❌ Movimento inválido! Use W, A, S, D ou 'q' para sair.")
            continue
        
        mostrar_labirinto(posicao)
        
        if posicao == posicao_tesouro:
            print("\n🏆 Parabéns! Você encontrou o tesouro!")
            break

if __name__ == "__main__":
    controlar_agente()
