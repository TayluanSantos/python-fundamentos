# Booleanos
# Valores: True e False -> Em letra capitalizada
# Os tipos booleanos, representam um tipo de dados que resultam em dois valores possíveis: True e False
# Valores booleanos e não-booleanos que são falsos = 0,0.0,False,None,"",{},[]

porta_aberta = True
porta_fechada = False

print(porta_aberta) # True


# Operadores Lógicos 
# São utilizados para combinarmos múltiplas expressões
# and , or e not

# Operador and
# É um operador binário e necessita de dois argumentos
# Para o resultado ser True, é necessário que ambos argumentos sejam verdadeiros

a = True
b = True

print(a and b) # True

c = True
d = False

print(c and d) # False


# Operador or
# É um operador binário e necessita de dois argumentos
# Para o resultado ser True, basta que um dos argumentos seja verdadeiro 

e = True
f = True

print(e or f) # True

g = True
h = False

print(g or h) # True


# Operador not
# É um operador que inverte o valor de um argumento

formiga_is_mamifero = True
print(not(formiga_is_mamifero)) # False


# Precedência dos operadores
# Existe uma ordem de precedência dos operadores lógicos, que é a seguinte: not, and e or 

print(False or not False)  # True / Primeiro é resolvido "not False" que resulta em True, depois False or True = True
