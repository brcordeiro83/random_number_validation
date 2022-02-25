# 1. Importando as bibliotecas

import funcoes as fc

# 2. Declaração de Variáveis
tamanho_imagem = 256
numero_frame = 2
nome_arquivo = 'Imagens/gerador'

# 3. Rodar programas
fc.gerar_imagens_aleatorias(tamanho_imagem, nome_arquivo, numero_frame)
fc.gerar_imagens_aleatorias_sns(tamanho_imagem, nome_arquivo, numero_frame)
fc.gerar_gif(numero_frame, nome_arquivo)
fc.gerar_gif_sns(numero_frame, nome_arquivo)
