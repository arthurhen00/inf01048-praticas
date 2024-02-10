Arthur Hendges da silva, 00332968, Turma B  
Gabriel Antônio Pereira, 00324449, Turma B  
Everton Fritsch de Lima, 00334801, Turma A  

TTTM  

1. 
Minimax jogando como player 1: de 12 partidas jogadas o minimax empatou 4 partidas e ganhou 8.  
Minimax jogando como player 2: de 12 partidas jogadas o minimax ganhou 12.  

2.
Sim, para 24 partidas entre Minimax x Minimax, 24 empataram. O algoritmo está encontrado um equilíbrio entre atacar e defender.  

3.
Minimax jogando como player 1:  de 6 partidas jogadas 6 empataram.  
Minimax jogando como player 2:  de 6 partidas jogadas 6 empataram.  

Othello  

1. 
|        | Count | Mask | Custom |
| ------ | ----- | ---- | ------ |
| Count  |   1   |  -1  |   1    |
| Mask   |   1   |  -1  |   1    |
| Custom |   1   |  -1  |   -1   |

2. e 3.   
A heurística com melhor desempenho foi a de valor posicional, já que ela leva em consideração a posição específica das peças no tabuleiro e atribui valores diferentes a cada posição. Isso permite uma avaliação mais refinada das posições das peças em comparação com a heurística simples de contagem de peças e a heurística personalizada que assume que ter mais opções de movimento é uma vantagem. A heurística baseada na contagem de peças teve um resultado medio. Sua limitação em considerar a posição específica das peças no tabuleiro pode resultar em avaliações menos precisas.  


Feedback:  
O trabalho foi na sua maior parte fácil devido ao algoritmo estar descrito nos slides e as heurísticas serem simples. O único problema que tomou um tempo considerável, apesar de estar escrito no enunciado, foi que o min tinha que inverter o player para calcular a utilidade com se fosse o player que iria jogar.  

Quanto ao uso de IA, ao perceber que o erro estava no algoritmo do minimax tentamos usar tanto o ChatGPT e o chat do Bing para ver se algum encontrava a solução, nenhum encontrou. Também usamos o GPT para gerar a heuristica custom que foi a mais simples mas com o pior resultado.  
