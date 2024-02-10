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
A heurística com melhor desempenho foi a de valor posicional. Ela considera a posição das peças no tabuleiro e isso permite avaliações mais precisas. A heurística é eficaz ao atribuir valores diferentes às posições ocupadas pelas peças.

Heurística de contagem de peças: Essa heurística usa a contagem de peças e essa simplicidade pode levar a avaliações menos refinadas. Ao focar apenas na diferença entre o número de peças do jogador e do oponente, ela não considera a posição específica das peças no tabuleiro, o que pode limitar sua capacidade de avaliação estratégica.

Heurística personalizada assume que ter mais opções de movimento é uma vantagem. Ela é simples e eficiente, mas sua limitação na avaliação estratégica pode resultar em uma falta de discriminação entre diferentes estados. 

Feedback:  
O trabalho foi na sua maior parte fácil devido ao algoritmo estar descrito nos slides e as heurísticas serem simples. O único problema que tomou um tempo considerável, apesar de estar escrito no enunciado, foi que o min tinha que inverter o player para calcular a utilidade com se fosse o player que iria jogar.  

Quanto ao uso de IA, ao perceber que o erro estava no algoritmo do minimax tentamos usar tanto o ChatGPT e o chat do Bing para ver se algum encontrava a solução, nenhum encontrou. Também usamos o GPT para gerar uma heuristica custom que foi a mais simples mas com o pior resultado.  
