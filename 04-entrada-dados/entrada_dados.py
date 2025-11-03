# Entrada de Dados

# Método: input()
# Explicação: O método input() é um método utilizado em Python para recebermos dados digitados pelo usuário
# A função uma vez iniciada, fica aguardando a entrada de dados do usuário e  que o mesmo pressione o Enter 

print('Informe seu nome:')
nome = input() # método que recebe a entrada de dados 

print(f'Olá,{nome}')

# Também podemos passar a mensagem como argumento da função. A resposta será na mesma linha da mensagem
idade = input('Insira a sua idade:')
print(idade)

input.s

# IMPORTANTE!

print(type(idade)) # <class 'str'> O método input() assimila qualquer entrada como uma string. Portanto, se quisermos um valor numérico, devemos fazer o type casting

primeiro_numero = int(input('Insira o primeiro número: ')) # convertendo de string para int
segundo_numero = int(input('Insira o segundo número: ')) # convertendo de string para int

resultado_soma = primeiro_numero + segundo_numero

print(f'O resultado da soma de {primeiro_numero} + {segundo_numero} é igual a: {resultado_soma} ')


