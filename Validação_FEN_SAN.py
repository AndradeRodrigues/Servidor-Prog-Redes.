import chess

# Função para validar uma jogada no formato FEN
def validar_jogada_fen(fen, board):
    try:
        move = chess.Move.from_uci(fen)  # Converte a jogada para o formato UCI
        if move in board.legal_moves:  # Verifica se a jogada é legal
            board.push(move)  # Aplica a jogada no tabuleiro
            return True  # Jogada válida
        else:
            return False  # Jogada inválida
    except:
        return False  # Jogada inválida (erro de formatação ou exceção)

# Função para validar uma jogada no formato SAN
def validar_jogada_san(san, board):
    try:
        move = board.parse_san(san)  # Converte a jogada para o formato SAN
        if move in board.legal_moves:  # Verifica se a jogada é legal
            board.push(move)  # Aplica a jogada no tabuleiro
            return True  # Jogada válida
        else:
            return False  # Jogada inválida
    except:
        return False  # Jogada inválida (erro de formatação ou exceção)

# Exemplo de uso
board = chess.Board()  # Cria um novo objeto de tabuleiro

while True:
    print(board)  # Exibe o tabuleiro atual

    jogada = input("Digite a jogada: ")  # Solicita a entrada da jogada ao usuário

    if validar_jogada_fen(jogada, board) or validar_jogada_san(jogada, board):
        print('Jogada válida')  # Exibe a mensagem de jogada válida
    else:
        print('Jogada inválida. Tente novamente.')  # Exibe a mensagem de jogada inválida

    print('Jogadas realizadas:', board.move_stack)  # Exibe a lista de jogadas realizadas até o momento
