import numpy as np

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    sum = 0
    for row in data:
        h = b + w * row[0]
        sum += (h - row[1]) ** 2
 
    mse = sum/len(data)
    return mse

    
def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    m = len(data)

    # Inicialização dos gradientes
    grad_b = 0
    grad_w = 0
    # Loop através dos exemplos no conjunto de dados
    for i in range(m):
        x = data[i, 0]
        y = data[i, 1]
        
        grad_b +=  2 * ((w * x + b) - y)
        grad_w +=  (2 * x) * ((w * x + b) - y)
    
    grad_b = (1 / m) * grad_b
    grad_w = (1 / m) * grad_w
    
    # Atualização dos parâmetros usando a taxa de aprendizado
    b -= alpha * grad_b
    w -= alpha * grad_w

    return b, w

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    b_history = []
    w_history = []
    for i in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        print(compute_mse(b,w,data))
        b_history.append(b)
        w_history.append(w)
        
    return b_history,w_history
