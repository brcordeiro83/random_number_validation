# 1. Importando as bibliotecas

import imageio
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# 2. Definindo as funções
def gerar_imagens_aleatorias(tamanho_imagem, nome_arquivo, numero_frame):
    for step in range(1000, 1000 + numero_frame):
        matriz_aleatoria = np.random.rand(tamanho_imagem, tamanho_imagem).round()
        arquivo = nome_arquivo + str(step) + '.png'
        plt.imshow(matriz_aleatoria, interpolation='nearest')
        plt.savefig(arquivo)


def gerar_imagens_aleatorias_sns(tamanho_imagem, nome_arquivo, numero_frame):
    for step in range(2000, 2000 + numero_frame):
        matriz_aleatoria = np.random.rand(tamanho_imagem, tamanho_imagem).round()
        arquivo = nome_arquivo + str(step) + '.png'
        sns.heatmap(matriz_aleatoria, cbar=False)
        plt.savefig(arquivo)


def gerar_gif(numero_frame, nome_arquivo):
    arquivos_gerados = [nome_arquivo + str(x) + '.png' for x in range(1000, 1000 + numero_frame)]
    with imageio.get_writer(nome_arquivo + '.gif', mode='I') as writer:
        for arquivos_gerado in arquivos_gerados:
            image = imageio.imread(arquivos_gerado)
            writer.append_data(image)


def gerar_gif_sns(numero_frame, nome_arquivo):
    arquivos_gerados = [nome_arquivo + str(x) + '.png' for x in range(2000, 2000 + numero_frame)]
    with imageio.get_writer(nome_arquivo + '_sns.gif', mode='I') as writer:
        for arquivos_gerado in arquivos_gerados:
            image = imageio.imread(arquivos_gerado)
            writer.append_data(image)

# if(__name__ == '__main__'):
#    gerador_v1()
