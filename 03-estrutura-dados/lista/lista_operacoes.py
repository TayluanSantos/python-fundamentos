# Operações em listas

linguagens_programacao = ["Python","Java"]

# Adicionando um elemento ao final da lista -> append()
linguagens_programacao.append("C#") # Output : ["Python","Java","C#"]

# Inserindo um elemento em uma posição específica da lista. Isso não substitui o item que estava na posição anteriormente -> insert()
linguagens_programacao.insert(1,"C++") # Output: ["Python","C++","Java","C#"]

# Removendo um elemento da lista -> remove()
linguagens_programacao.remove("C#") # Output : ["Python","C++","Java","C#"]

# Descobrindo o índice de um elemento -> index()
linguagens_programacao.index("Python") # Output : 0

# Verificando o tamanho de uma lista -> len()
len(linguagens_programacao) # Output : 4 

# Contando a ocorrência de um item -> count()
linguagens_programacao.count("Python") # Output : 1 

# Removendo e retornando um item da lista / Por padrão remove o último item, mas podemos especificar um índice específico
item_removido = linguagens_programacao.pop() 
print(item_removido) # Output : Java


