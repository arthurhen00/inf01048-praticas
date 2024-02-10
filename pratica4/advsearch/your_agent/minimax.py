from typing import Tuple, Callable
def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    _, move = MAX(state,max_depth,eval_func, float('-inf'), float('inf'))
    
    return move

def MAX(state, max_depth, eval_func, alpha, beta):
    if state.is_terminal() or max_depth == 0:
        if state.player is None:
            return 0, None
        return eval_func(state, state.player), None
        
    v = float('-inf')
    a = None
    legal_moves = state.legal_moves()
    
    for move in legal_moves:
        new_state = state.next_state(move)
        min_v, _ = MIN(new_state, max_depth - 1, eval_func, alpha, beta)
        if min_v > v :
            v = min_v
            a = move
            
        alpha = max(alpha, min_v)
        if alpha >= beta:
            break
    return v,a
        
        
def MIN(state, max_depth, eval_func, alpha, beta):
    if state.is_terminal() or max_depth == 0:
        if state.player is None:
            return 0, None
        return eval_func(state, state.board.opponent(state.player)), None
        
    v = float('inf')
    a = None
    
    legal_moves = state.legal_moves()
    
    for move in legal_moves:
        new_state = state.next_state(move)
        max_v, _ = MAX(new_state, max_depth - 1, eval_func, alpha, beta)
        if max_v < v :
            v = max_v
            a = move
        beta = min(beta, max_v)
        if beta <= alpha:
            break
    return v,a

def get_opponent(player):
    return 'B' if player == 'W' else 'W'