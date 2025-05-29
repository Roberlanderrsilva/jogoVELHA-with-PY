# -*- coding: utf-8 -*-

# Definições de cores ANSI (podem não funcionar em todos os terminais)
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET_COR = '\033[0m'

# Mapeamento dos jogadores para suas cores e símbolos
JOGADOR_X = {'simbolo': 'X', 'cor': VERDE}
JOGADOR_O = {'simbolo': 'O', 'cor': AMARELO}

tabuleiro = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

jogador_atual = JOGADOR_X
vencedor = None
jogo_terminou = False

def exibir_tabuleiro(estado_final=None, cor_estado_final=None):
    """Exibe o tabuleiro no terminal."""
    print("\n")
    for i in range(1, 10):
        simbolo = tabuleiro[i]
        cor = RESET_COR
        if estado_final and cor_estado_final:
            cor = cor_estado_final
        elif simbolo == JOGADOR_X['simbolo']:
            cor = JOGADOR_X['cor']
        elif simbolo == JOGADOR_O['simbolo']:
            cor = JOGADOR_O['cor']
        
        print(f" {cor}{simbolo if simbolo != ' ' else str(i)}{RESET_COR} ", end="")
        if i % 3 == 0:
            print("\n" + "-----------")
    print("\n")

def registrar_jogada(posicao):
    """Registra a jogada do jogador atual no tabuleiro."""
    global tabuleiro
    if tabuleiro[posicao] == ' ':
        tabuleiro[posicao] = jogador_atual['simbolo']
        return True
    return False

def mudar_jogador():
    """Alterna o jogador atual."""
    global jogador_atual
    if jogador_atual == JOGADOR_X:
        jogador_atual = JOGADOR_O
    else:
        jogador_atual = JOGADOR_X

def verificar_vencedor():
    """Verifica se há um vencedor."""
    global vencedor, jogo_terminou
    
    combinacoes_vitoria = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Linhas
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Colunas
        [1, 5, 9], [3, 5, 7]             # Diagonais
    ]

    for combo in combinacoes_vitoria:
        if (tabuleiro[combo[0]] == tabuleiro[combo[1]] == tabuleiro[combo[2]] and
                tabuleiro[combo[0]] != ' '):
            vencedor = tabuleiro[combo[0]]
            jogo_terminou = True
            return

def verificar_empate():
    """Verifica se o jogo empatou."""
    global jogo_terminou
    if ' ' not in tabuleiro.values() and not vencedor:
        jogo_terminou = True
        return True
    return False

def exibir_mensagem_final():
    """Exibe a mensagem final do jogo."""
    if vencedor:
        cor_vitoria = JOGADOR_X['cor'] if vencedor == JOGADOR_X['simbolo'] else JOGADOR_O['cor']
        exibir_tabuleiro(estado_final=True, cor_estado_final=cor_vitoria)
        print(f"{cor_vitoria}O JOGADOR {vencedor} VENCEU!{RESET_COR}")
    elif verificar_empate(): # Chamada redundante, mas garante a lógica de empate
        exibir_tabuleiro(estado_final=True, cor_estado_final=VERMELHO)
        # Simular texto grande para "VELHOU ! , TENTEM OUTRA VEZ !"
        print(f"{VERMELHO}")
        print(r" __      __   _______   _        _          ____    _   _    ")
        print(r" \ \    / /  | ______| | |      | |        / __ \  | | | |   ")
        print(r"  \ \  / /   | |__     | |      | |       | |  | | | | | |   ")
        print(r"   \ \/ /    |  __|    | |      | |       | |  | | | | | |   ")
        print(r"    \  /     | |____   | |____  | |____   | |__| | | |_| |   ")
        print(r"     \/      |______|  |______| |______|   \____/   \___/    ")
        print(r"                                                             ")
        print(r"  _______   _______   _   _   _______   _______   __   __    ")
        print(r" |__   __| |__   __| | \ | | |__   __| |__   __|  \ \ / /    ")
        print(r"    | |       | |    |  \| |    | |       | |      \ V /     ")
        print(r"    | |       | |    | . ` |    | |       | |       > <      ")
        print(r"    | |       | |    | |\  |    | |       | |      / . \     ")
        print(r"    |_|       |_|    |_| \_|    |_|       |_|     /_/ \_\    ")
        print(f"{RESET_COR}")

def reiniciar_jogo():
    """Reinicia o estado do jogo."""
    global tabuleiro, jogador_atual, vencedor, jogo_terminou
    tabuleiro = {i: ' ' for i in range(1, 10)}
    jogador_atual = JOGADOR_X
    vencedor = None
    jogo_terminou = False

def loop_jogo():
    """Loop principal do jogo."""
    global jogo_terminou
    while not jogo_terminou:
        exibir_tabuleiro()
        print(f"Jogador atual: {jogador_atual['cor']}{jogador_atual['simbolo']}{RESET_COR}")
        
        try:
            posicao = int(input("Escolha uma posição (1-9): "))
            if not 1 <= posicao <= 9:
                print("Posição inválida. Escolha um número entre 1 e 9.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        if registrar_jogada(posicao):
            verificar_vencedor()
            if not jogo_terminou: # Se não houve vencedor, verifica empate
                if verificar_empate():
                    jogo_terminou = True # Garante que o jogo termine em empate
            
            if not jogo_terminou: # Se não terminou (nem vitória nem empate), muda jogador
                mudar_jogador()
        else:
            print("Posição já ocupada. Tente outra.")

    exibir_mensagem_final()

    while True:
        jogar_novamente = input("Jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente == 's':
            reiniciar_jogo()
            loop_jogo()
            break 
        elif jogar_novamente == 'n':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")


if __name__ == "__main__":
    loop_jogo()
    