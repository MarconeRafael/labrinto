import labirinto
import visualizacao
import time

# Função para salvar a posição do agente em um arquivo para atualizar a visualização
def salvar_posicao(posicao):
    with open("posicao_atual.txt", "w") as arquivo:
        arquivo.write(f"{posicao[0]},{posicao[1]}")

# Função principal para jogar pelo terminal
def main():
    posicao = labirinto.posicao_inicial
    salvar_posicao(posicao)  # Atualiza a posição inicial na visualização

    print("\n🎮 Bem-vindo ao Labirinto! Controle o agente pelo terminal.")
    print("Use as teclas: W (cima), S (baixo), A (esquerda), D (direita)")
    print("Digite 'q' para sair.\n")

    labirinto.mostrar_labirinto(posicao)
    visualizacao.desenhar_labirinto(posicao)

    while True:
        movimento = input("\nDigite seu movimento (WASD ou setas): ").strip().lower()

        # Mapeia os comandos para as direções corretas
        if movimento in ["w", "cima"]:
            nova_posicao = labirinto.mover(posicao, "cima")
        elif movimento in ["s", "baixo"]:
            nova_posicao = labirinto.mover(posicao, "baixo")
        elif movimento in ["a", "esquerda"]:
            nova_posicao = labirinto.mover(posicao, "esquerda")
        elif movimento in ["d", "direita"]:
            nova_posicao = labirinto.mover(posicao, "direita")
        elif movimento == "q":
            print("\n🚪 Saindo do jogo...")
            break
        else:
            print("❌ Movimento inválido! Use W, A, S, D ou 'q' para sair.")
            continue  # Volta para a entrada do usuário

        # Atualiza a posição
        posicao = nova_posicao
        salvar_posicao(posicao)  # Atualiza a posição na visualização
        labirinto.mostrar_labirinto(posicao)
        visualizacao.desenhar_labirinto(posicao)  # Atualiza visualmente após o movimento

        # Verifica se encontrou o tesouro
        if posicao == labirinto.posicao_tesouro:
            print("\n🏆 Parabéns! Você encontrou o tesouro!")
            break

        time.sleep(0.1)  # Pequena pausa para sincronizar com a visualização

if __name__ == "__main__":
    main()
