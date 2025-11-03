# Listas

# As listas são utilizadas para armazenarem uma coleção de elementos
# Principais Características
# - As listas são mutáveis
# - Podemos armazenar mais de um tipo de dados em uma lista
# - As listas são ordenadas. Dessa forma, podemos acessar os elementos por meio de seu índice
# - Uma lista é representada pelo símbolo de colchetes [] e seus elementos são separados por vírgula

# Criando uma lista
estados_sudeste = ["Rio de Janeiro","São Paulo","Minas Gerais","Espírito Santo"]

# Inicializando uma lista vazia
estados_sul = []

# Criando uma lista com um único tipo de dado
lista_homogenia = ["Python","Java","C#","C++","Go"]

# Criando uma lista com vários tipos de dados
lista_heterogenia = ["Python",1,True,2.0,None]

# Acessando um elemento por meio do índice
estados_sudeste [0] # Output : Rio de Janeiro

# Acessando um elemento da lista de trás para frente
estados_sudeste [-1] # Output : Espírito Santo / O índice do primeiro elemento de trás para frente é -1

# Assinalando um novo valor a um elemento da lista
estados_sudeste [0] = "RJ" # Output : ["RJ","São Paulo","Minas Gerais","Espírito Santo"]
