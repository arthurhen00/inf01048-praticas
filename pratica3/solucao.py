from typing import Iterable, Set, Tuple
from collections import deque
import heapq

from scipy.spatial.distance import hamming, cityblock

objective = '12345678_'
objective_char = [ord(char) for char in objective]
class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai: 'Nodo', acao:str, custo:int, heuristica: str = None):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.heuristic = heuristica
        self.hamming_distance = None
        self.manhattan_distance = None
        if self.heuristic is not None:
            if self.heuristic.lower()  == 'hamming':
                self.hamming_distance = hamming(list(self.estado), list(objective))
            elif self.heuristic.lower()  == 'manhattan':
                self.manhattan_distance = cityblock([ord(char) for char in self.estado], objective_char)
            
            
        
        
    def __hash__(self):
        return hash((self.estado))

        
    def __eq__(self, other):
        if not isinstance(other, Nodo):
            return False

        return (
            self.estado == other.estado
        )
        
    
        
    def __lt__(self, other):
        return self.get_cost() < other.get_cost()
        
    def get_cost(self):
        if self.heuristic is not None:
            if self.heuristic.lower()  == 'hamming':
                return self.hamming_distance + self.custo
            elif self.heuristic.lower()  == 'manhattan':
                return self.manhattan_distance + self.custo
        return self.custo


def get_path(nodo: Nodo):
    actions = []
    while (nodo.pai != None):
        actions.insert(0,nodo.acao)
        nodo = nodo.pai
    return actions

def sucessor(estado:str)->Set[Tuple[str,int]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    empty_position = estado.index('_')
    moves = set()
    if empty_position < 6:
        moves.add(('abaixo'  , empty_position + 3))
    if empty_position % 3 != 0:
        moves.add(('esquerda', empty_position - 1))
    if empty_position > 2:
        moves.add(('acima'   , empty_position - 3))
    if empty_position != 2 and empty_position != 5 and empty_position != 8:
        moves.add(('direita' , empty_position + 1))
    

    legal_moves = set()
    for direction, swap_index in moves:
        if swap_index < len(estado) and swap_index >= 0:
            new_state = list(estado)
            new_state[empty_position], new_state[swap_index] = new_state[swap_index], new_state[empty_position]
            new_state = ''.join(new_state)
            legal_moves.add((direction, new_state))

    return legal_moves

def expande(nodo:Nodo,)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    legal_moves = sucessor(nodo.estado)
    new_nodes = set()

    for action, new_state in legal_moves:
        new_nodes.add(Nodo(estado= new_state,
                        pai= nodo,
                        acao= action,
                        custo= nodo.custo + 1,
                        heuristica= nodo.heuristic))
    return new_nodes

def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    current_node = Nodo(estado= estado,
                        pai= None,
                        acao= None,
                        custo= 0,
                        heuristica='hamming')
    return exec_astar(current_node)

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    
    current_node = Nodo(estado= estado,
                        pai= None,
                        acao= None,
                        custo= 0,
                        heuristica='manhattan')
    return exec_astar(current_node)

    
def exec_astar(start_node):
    x = set()
    f = []
    heapq.heappush(f, (start_node.get_cost(), start_node))
    while(f):
        _ , current_node = heapq.heappop(f)
        
        if current_node.estado == objective:
            return get_path(nodo = current_node)
        
        if current_node in x:
            continue

        x.add(current_node)

        
        discovered_nodes = expande(current_node)

        for node in discovered_nodes:
            if node not in x:
                heapq.heappush(f, (node.get_cost(), node))
    return None

#print(astar_hamming('185423_67'))
#print(astar_hamming('123456_78'))
#print(astar_hamming('2_3541687'))
#print(astar_hamming('2_3541687'))

#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    queue = deque([(estado, [])])  # Inicializa a fila com o estado inicial e uma lista vazia de ações

    while queue:
        estado_atual, acoes_realizadas = queue.popleft()

        if(objective == estado_atual):
            return acoes_realizadas

        for acao in expande(estado_atual):
            novo_estado = exec_astar(estado_atual, acao)
            if novo_estado is not None:  # Verifica se a ação é válida
                nova_acao = acoes_realizadas + [acao]
                queue.append((novo_estado, nova_acao))

    return None  # Retorna None se não encontrar solução

#print(bfs('185423_67'))
#print(bfs('123456_78'))
#print(bfs('2_3541687'))
#print(bfs('2_3541687'))

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    def dfs_rec(current_node, acoes_realizadas):
        if current_node.estado == objective:
            return acoes_realizadas  # Retorna a lista de ações quando o objetivo é atingido

        for acao in expande(current_node):
            novo_estado = exec_astar(current_node, acao)  # Implemente a função realizar_acao conforme as regras do seu problema
            if novo_estado is not None:  # Verifica se a ação é válida
                nova_acao = acoes_realizadas + [acao]
                resultado = dfs_rec(novo_estado, nova_acao)
                if resultado is not None:
                    return resultado

        return None  # Retorna None se não encontrar solução a partir do estado atual

#print(dfs('185423_67'))
#print(dfs('123456_78'))
#print(dfs('2_3541687'))
#print(dfs('2_3541687'))

#opcional,extra
def astar_new_heuristic(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """

    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#print(astar_new_heuristic('185423_67'))
#print(astar_new_heuristic('123456_78'))
#print(astar_new_heuristic('2_3541687'))
#print(astar_new_heuristic('2_3541687'))
