from typing import Iterable, Set, Tuple
from collections import deque
import heapq
from scipy.spatial.distance import hamming, cityblock
import time

objective = '12345678_'
objective_char = [ord(char) for char in objective]
expanded_nodes = 0
solution_cost = 0
astar_type = None

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
        self.bfs = bfs
        self.dfs = dfs
        
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
            if self.heuristic.lower() == 'hamming':
                return self.hamming_distance + self.custo
            elif self.heuristic.lower() == 'manhattan':
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
    global astar_type
    astar_type = 'astar_hamming'
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
    global astar_type
    astar_type= 'astar_manhattan'
    current_node = Nodo(estado= estado,
                        pai= None,
                        acao= None,
                        custo= 0,
                        heuristica='manhattan')
    return exec_astar(current_node)

    
def exec_astar(start_node):
    global expanded_nodes, solution_cost
    expanded_nodes = 0
    solution_cost = 0

    start_time = time.time()

    x = set()
    f = []
    heapq.heappush(f, (start_node.get_cost(), start_node))
    while f:
        _, current_node = heapq.heappop(f)
        
        if current_node.estado == objective:
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Métricas
            print(f"{astar_type} - Nós expandidos: {expanded_nodes}")
            print(f"{astar_type} - Tempo decorrido: {elapsed_time} segundos")
            print(f"{astar_type} - Custo da solução: {solution_cost}")
            return get_path(nodo=current_node)

        if current_node in x:
            continue

        x.add(current_node)

        expanded_nodes += 1
        solution_cost = current_node.get_cost()

        discovered_nodes = expande(current_node)

        for node in discovered_nodes:
            if node not in x:
                heapq.heappush(f, (node.get_cost(), node))

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Métricas
    print(f"{astar_type} - Nós expandidos: {expanded_nodes}")
    print(f"{astar_type} - Tempo decorrido: {elapsed_time} segundos")
    print(f"{astar_type} - Custo da solução: {solution_cost}")

    return None

#opcional,extra
def bfs(estado: str)->list[str]:
    global expanded_nodes, solution_cost
    expanded_nodes = 0
    solution_cost = 0
    start_time = time.time()

    queue = deque([Nodo(estado=estado, pai=None, acao=None, custo=0)])

    visitados = set()

    while queue:
        nodo_atual = queue.popleft()

        if nodo_atual.estado == objective:
            end_time = time.time()
            elapsed_time = end_time - start_time
            # Métricas
            print(f"BFS - Nós expandidos: {expanded_nodes}")
            print(f"BFS - Tempo decorrido: {elapsed_time} segundos")
            print(f"BFS - Custo da solução: {solution_cost}")
            return get_path(nodo_atual)

        visitados.add(nodo_atual.estado)

        expanded_nodes += 1
        solution_cost = nodo_atual.get_cost()

        sucessores = expande(nodo_atual)

        for sucessor in sucessores:
            if sucessor.estado not in visitados:
                queue.append(sucessor)

    end_time = time.time()
    elapsed_time = end_time - start_time
    # Métricas
    print(f"BFS - Nós expandidos: {expanded_nodes}")
    print(f"BFS - Tempo decorrido: {elapsed_time} segundos")
    print(f"BFS - Custo da solução: {solution_cost}")

    return None

#opcional,extra
def dfs(estado: str)->list[str]:
    global expanded_nodes, solution_cost
    expanded_nodes = 0
    solution_cost = 0
    start_time = time.time()

    stack = [Nodo(estado=estado, pai=None, acao=None, custo=0)]

    visitados = set()

    while stack:
        nodo_atual = stack.pop()

        if nodo_atual.estado == objective:
            end_time = time.time()
            elapsed_time = end_time - start_time
            # Métricas
            print(f"DFS - Nós expandidos: {expanded_nodes}")
            print(f"DFS - Tempo decorrido: {elapsed_time} segundos")
            print(f"DFS - Custo da solução: {solution_cost}")
            return get_path(nodo_atual)

        visitados.add(nodo_atual.estado)

        expanded_nodes += 1
        solution_cost = nodo_atual.get_cost()

        sucessores = expande(nodo_atual)

        for sucessor in sucessores:
            if sucessor.estado not in visitados:
                stack.append(sucessor)

    end_time = time.time()
    elapsed_time = end_time - start_time
    # Métricas
    print(f"DFS - Nós expandidos: {expanded_nodes}")
    print(f"DFS - Tempo decorrido: {elapsed_time} segundos")
    print(f"DFS - Custo da solução: {solution_cost}")

    return None

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
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

#print(astar_hamming('2_3541687'))
#print(astar_manhattan('2_3541687'))
#print(bfs('2_3541687'))
#print(dfs('2_3541687'))

