# 1. Importando as bibliotecas
import imageio
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

# 2. Declaração de Variáveis
tamanho_imagem = 256
numero_frame = 24


# 3. Definindo as funções
def gerar_imagens_aleatorias():
    for step in range(1000, 1000 + numero_frame):
        matriz_aleatoria = np.random.rand(tamanho_imagem, tamanho_imagem).round()
        arquivo = 'gerador' + str(step) + '.png'
        plt.imshow(matriz_aleatoria, interpolation='nearest')
        plt.savefig(arquivo)


def gerar_imagens_aleatorias_sns():
    for step in range(2000, 2000 + numero_frame):
        matriz_aleatoria = np.random.rand(tamanho_imagem, tamanho_imagem).round()
        arquivo = 'gerador' + str(step) + '.png'
        sns.heatmap(matriz_aleatoria,cbar=False)
        plt.savefig(arquivo)


def gerar_gif():
    arquivos_gerados = ['gerador' + str(x) + '.png' for x in range(1000, 1000 + numero_frame)]
    with imageio.get_writer('Gerador_G1.gif', mode='I') as writer:
        for arquivos_gerado in arquivos_gerados:
            image = imageio.imread(arquivos_gerado)
            writer.append_data(image)

def gerar_gif_sns():
    arquivos_gerados = ['gerador' + str(x) + '.png' for x in range(2000, 2000 + numero_frame)]
    with imageio.get_writer('Gerador_sns_G1.gif', mode='I') as writer:
        for arquivos_gerado in arquivos_gerados:
            image = imageio.imread(arquivos_gerado)
            writer.append_data(image)

# 4. Rodar programas
gerar_imagens_aleatorias()
gerar_imagens_aleatorias_sns()
gerar_gif()
gerar_gif_sns()
