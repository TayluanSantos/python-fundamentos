# Entendendo diferentes tipos de variáveis em Python

# Dicas:
# 01 - Definir nomes descritivos para variáveis
# 02 - O Python é case-sensitive,ou seja,enxerga distinção entre letras maiúsculas e minúsculas
# 03 - Não utilizar palavras reservadas como nome de variáveis

# Convenções de Nomenclatura
# Seguir o padrão snake_case para palavras compostas - Ex: nome_aluno
# Não deve começar com números - Ex: 1aluno
# Pode começar com letra minúscula ou com underscore(_) - Ex: _aluno / aluno01
# Deve conter apenas valores alfanuméricos (a-Z,0-9) e underscore

### DEFININDO VARIÁVEIS ###

nome = "Maria" 
print(nome)  # Output: Maria

print(type(nome)) # O método type() retorna o tipo da variável

mes = "Julho"
print(mes) # Output: Julho

mes = "Dezembro" # Posso atribuir outro valor a mesma variável
print(mes) # Output: Dezembro

mes_do_ano = mes # Posso atribuir uma variável a outra variável
print(mes) # Output: Dezembro

mes_do_ano = 12 # O Python tem tipagem dinâmica,ou seja, posso atribuir outros tipos de dado a uma variável
print(mes) # Output: 12


### ASSINALANDO MÚLTIPLOS VALORES A VARIÁVEIS ###

# Primeira forma
primeiro_estado = "Rio de Janeiro"
segundo_estado = "São Paulo"
terceiro_estado = "Minas Gerais"

print(primeiro_estado)
print(segundo_estado)
print(terceiro_estado)

# Multiplos valores assinalados
time_01,time_02,time_03 = "Fluminense","Flamengo","Vasco"

print(time_01)
print(time_02)
print(time_03)

### ATRIBUINDO O MESMO VALOR A VARIAVEIS DIFERENTES ###  

primeira_cor = segunda_cor = terceira_cor = "azul" # Todas as variáveis terão o mesmo valor

print(primeira_cor)
print(segunda_cor)
print(terceira_cor)

### EXTRAINDO VALORES DE UMA LISTA PARA VARIÁVEIS ###

frutas = ["maçã", "banana", "morango"]
fruta_01, fruta_02, fruta_03 = frutas

print(fruta_01)
print(fruta_02)
print(fruta_03)


