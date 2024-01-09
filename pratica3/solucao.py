from typing import Iterable, Set, Tuple
import heapq

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai: 'Nodo', acao:str, custo:int):
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
        
    def hamming_distance_to_objective(self, objective : str):
        return hamming_distance(self.estado, objective)


def hamming_distance(string: str, objective):
    if len(string) != len(objective):
        raise ValueError("Input strings must have the same length")
    return sum(c1 != c2 for c1, c2 in zip(string, objective))


def get_path(nodo: Nodo):
    actions = []
    while (nodo.pai != None):
        actions.insert(0,nodo.acao)
        nodo = nodo.pai
    return actions

def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    empty_position = estado.index('_')
    
    moves = {
        ('esquerda', empty_position - 1),
        ('direita' , empty_position + 1),
        ('acima'   , empty_position - 3),
        ('abaixo'  , empty_position + 3)
    }
    

    legal_moves = set()
    for direction, swap_index in moves:
        # movimento valido?
        if swap_index < len(estado) and swap_index >= 0:
            # adicionar movimento no conjunto de tuplas
            new_state = list(estado)
            new_state[empty_position], new_state[swap_index] = new_state[swap_index], new_state[empty_position]
            new_state = ''.join(new_state)
            legal_moves.add((direction, new_state))

    return legal_moves

def expande(nodo:Nodo)->Set[Nodo]:
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
                           custo= nodo.custo + 1))
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
    objective = '12345678_'
    x = set()
    f = []
    
    current_node = Nodo(estado= estado,
                        pai= None,
                        acao= None,
                        custo= 0)
    heapq.heapify(f)
    heapq.heappush(f, ((current_node.hamming_distance_to_objective(objective) + current_node.custo, id(current_node)), current_node))
    
    while(f):
        _, current_node = heapq.heappop(f)
        
        if current_node in x:
            continue
        print(len(f), '  -  ', len(x))
        x.add(current_node)
        
        if current_node.estado == objective:
            return get_path(nodo = current_node)
        
        discovered_nodes = expande(current_node)
        for node in discovered_nodes:
            if node not in x:
                heapq.heappush(f, ((node.hamming_distance_to_objective(objective) + node.custo, id(node)), node))
    
    return None
    
    
    
print(astar_hamming('185423_67'))
#print(astar_hamming('123456_78'))

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

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
