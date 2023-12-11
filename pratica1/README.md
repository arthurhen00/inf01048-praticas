Atividade 1


Atividade 2  
CIFAR-10  
60000 imagens coloridas (3 canais de cor) 32x32 separadas em 10 classes, cada uma com 6000 imagens. 5000 imagens de treinamento e 1000 de teste.  

A complexidade da análise desse conjunto de dados reside na dificuldade de distinguir algumas classes. Por exemplo, gatos e cachorros são animais muito semelhantes, sendo necessário diferenciar detalhes sutis para classificá-los corretamente. Além disso, as imagens podem conter informações adicionais além das classes desejadas, as quais precisam ser ignoradas.  

A abordagem proposta consiste em utilizar múltiplas camadas convolucionais para detectar primeiro detalhes sutis e, em seguida, detalhes mais gerais.  

Iniciando com 2 camadas de convolução, 2 de max pooling e uma camada oculta com 32 neurônios, obtivemos uma acurácia no conjunto de testes de 63,65%, com um pequeno overfitting. Nesse modelo inicial, a intenção era avaliar o desempenho apenas na detecção de detalhes sutis.  

Ao ajustar a primeira convolução para 32 filtros, a segunda para 64 e adicionar mais duas camadas com 128 filtros, alcançamos uma acurácia de 68,79%, porém com um overfitting significativo. Aqui, além de detectar detalhes sutis, a ideia foi fazer com que o modelo aprendesse detalhes mais complexos das imagens, mas o aumento na complexidade resultou em um maior overfitting.  

Para lidar com o overfitting, decidimos desligar aleatoriamente neurônios durante o treinamento utilizando a camada dropout. Com essa modificação, obtivemos uma acurácia de 71,65%, com um pequeno overfitting.  

CIFAR-100  


MNIST  


Fashion MNIST  

    
