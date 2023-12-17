Atividade 1
    b=-3.78, w=1.18, alpha=0.01, num_iterations=10000
    EQM final: 6.474774735674796

Atividade 2
    CIFAR-10
        60000 imagens coloridas (3 canais de cor) 32x32 separadas em 10 classes, cada uma com 6000 imagens. No total são 50000 imagens de treinamento e 10000 de teste.

        A complexidade da análise desse conjunto de dados reside na dificuldade de distinguir algumas classes. Por exemplo, gatos e cachorros são animais muito semelhantes, sendo necessário diferenciar detalhes sutis para classificá-los corretamente. Além disso, as imagens podem conter informações adicionais além das classes desejadas, as quais precisam ser ignoradas.

        A abordagem proposta consiste em utilizar múltiplas camadas convolucionais para detectar primeiro detalhes sutis e, em seguida, detalhes mais gerais.

        Iniciando com 2 camadas de convolução, 2 de max pooling e uma camada oculta com 32 neurônios, obtivemos uma acurácia no conjunto de testes de 63,65%, com um pequeno overfitting. Nesse modelo inicial, a intenção era avaliar o desempenho apenas na detecção de detalhes sutis.

        Ao ajustar a primeira convolução para 32 filtros, a segunda para 64 e adicionar mais duas camadas com 128 filtros, alcançamos uma acurácia de 68,79%, porém com um overfitting significativo. Aqui, além de detectar detalhes sutis, a ideia foi fazer com que o modelo aprendesse detalhes mais complexos das imagens, mas o aumento na complexidade resultou em um maior overfitting.

        Para lidar com o overfitting, decidimos desligar aleatoriamente neurônios durante o treinamento utilizando a camada dropout. Com essa modificação, obtivemos uma acurácia de 71,65%, com um pequeno overfitting.

    CIFAR-100
        60000 imagens coloridas (3 canais de cor) 32x32 separadas em 100 classes, cada uma com 600 imagens. No total são 50000 imagens de treinamento e 10000 de teste.

        A complexidade da análise desse conjunto de dados reside na diferença na quantidade de imagens por classe em relação aos outros datasets, 10 vezes menos imagens por classe, o que resulta na rede ter dificuldades em classificar corretamente as imagens.

        Nesse caso, foi utilizada uma rede semelhante a rede do CIFAR-10 com variações na quantidade dos filtros, com (32,32,64,64), (128,128,256,256):
            Duas camadas de convolução com 32 (128) filtros 3x3
            Uma camada com max pooling 2x2
            Duas camadas de convolução com 32 (128) filtros 3x3
            Uma camada com max pooling 2x2

            Duas camadas de convolução com 64 (256) filtros 3x3
            Uma camada com max pooling 2x2
            Duas camadas de convolução com 64 (256) filtros 3x3
            Uma camada com max pooling 2x2

            Uma camada flatten
            Uma camada com 256 neuronios densamente conectada
            Uma camada com 128 neuronios densamente conectada
            Uma camada com 100 (número de classes) neuronios densamente conectada
        
        Quantidades de filtros maiores não foram testados devido a demora no treinamento. Entranto ambas ficaram com a precisão no conjunto de treinamento perto dos 78% e 28% no conjunto de teste, sintomas de overfitting. Foram adicionadas camadas de Dropout ao fim de cada bloco de convolução para tentar ajustar o overfitting resultando em uma acurácia de 31%.

    MNIST


    Fashion MNIST
        60000 imagens em preto e branco 28×28 separadas em 10 classes, cada uma com 7000 imagens. No total são 60000 imagens de treinamento e 10000 de teste.

        Uma dificuldade percebida é que alguma classes possuem elementos muito parecidos, como as T-shirt/top, Pullover, Coat e Shirt.

        Para esse conjunto iniciou-se com a rede a seguir:
            Uma camada de convolução com 32 filtros 3x3
            Uma camada max pooling tamanho 2x2

            Uma camada de convolução com 64 filtros 3x3
            Uma camada max pooling tamanho 2x2

            Uma camada densamente conectada com 128 neuronios
            Uma camada densamente conectada com 10 (número de classes) neuronios

        Essa rede obteve 93% de acurácia no conjunto de treinamento e 89% no conjunto de teste

        Testou-se também adicionar esse bloco logo antes das camadas densas:
            Uma camada de convolução com 128 filtros 3x3
            Uma camada max pooling tamanho 2x2

        Porem isso diminuiu a acurácia para 91% no conjunto de treinamento e 87% no conjunto de teste.

        Foi feito ainda mais um teste baseada na primeira rede apresentada para este problema adicionando o seguinte bloco logo no começo da rede:
            Uma camada de convolução com 16 filtros 3x3
            Uma camada max pooling tamanho 2x2

        E mais uma vez a acurácia diminuiu, 90% no conjunto de treinamento e 87% no conjunto de teste.

        Ao final, a primeira rede testada saiu como a melhor performante podendo-se concluir que como as imagens possuiam somente uma camada de cor elas possuiam menos características, logo menos filtros se fazem necessários.