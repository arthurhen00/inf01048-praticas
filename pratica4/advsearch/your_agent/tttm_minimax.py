import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param board: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move

    return minimax_move(state,-1,utility)

def utility(state, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    board = state.board.board
    enemy = 'W' if player == 'B' else 'B'
    
    if player_lost(board, player):
        return -1000
    
    if player_lost(board, enemy): 
        return 1000
    
    return 1

def player_lost(board, player):
    ## checa diagonais
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    ## checa colunas
    for i in range(3): 
        if board[0][i] == board[1][i] == board[2][i] == player: 
            return True
        
     ## checa linhas
    for row in board:
        if row[0] ==  row[1] == row[2] == player:
            return True

    return False
        

