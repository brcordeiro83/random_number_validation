# 1. Importando as bibliotecas
import imageio
import numpy as np
from matplotlib import pyplot as plt

# 2. Declaração de Variáveis
tamanho_imagem = 255
numero_frame: int = 24


# 3. Definindo as funções
def gerar_imagens_aleatorias(tamanho_imagem):
    for step in range(1000, 1000 + numero_frame):
        matriz_aleatoria = np.random.rand(tamanho_imagem, tamanho_imagem).round()
        arquivo = 'gerador' + str(step) + '.png'
        plt.imshow(matriz_aleatoria, interpolation='nearest')
        plt.savefig(arquivo)

def gerar_gif():
    arquivos_gerados = ['gerador' + str(x) + '.png' for x in range(1000, 1000 + numero_frame)]
    with imageio.get_writer('GeradorG1.gif', mode='I') as writer:
        for arquivos_gerado in arquivos_gerados:
            image = imageio.imread(arquivos_gerado)
            writer.append_data(image)


# 4. Rodar programas
gerar_imagens_aleatorias(tamanho_imagem)
gerar_gif()
