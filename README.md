# Validação dos geradores de números aleatórios

## Motivação

Os geradores de números aleatórios são classificados mais precisamente como pseudoaleatórios nos manuais de programação. A razão deste prefixo está na origem de sua obtenção, que é gerado a partir do truncamento de algum cálculo numérico. 

Estes números são essenciais para as simulações computacionais de modelos físicos, como na mecânica estatística, climatologia dentre outros, porque são através deles que os físicos testam os seus modelos teóricos.

É possível que em sistemas físicos pequenos os números pseudoaleatórios satisfaçam a exigência do físico/programador, mas a medida que o sistema cresce em tamanho será possível observar alguns padrões que podem introduzir tendências indesejadas nos resultados, não por culpa do modelo físico, mas sim no número aleatório para testá-lo.

Proponho desenvolver uma metodologia que teste a qualidade do gerador de números aleatórios através do python.


## Metodologia

