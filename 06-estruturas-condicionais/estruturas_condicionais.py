# Estruturas Condicionais  - If / Elif / else
# If:  É executado se o resultado da expressão for True
# Elif: # É executado se o resultado da primeira expressão for False
# Else: É executado se ambas as expressões anteriores forem falsas
# O bloco de código é definido por : e a identação

media_escolar = 7.0
media_aluno = 4.5

if media_aluno >= media_escolar : 
    print("Aprovado")

elif media_aluno >= 5.0 :
    print("Recuperação")

else : 
    print("Reprovado") 


time = "Fluminense"
times_rj = ["Fluminense","Flamengo","Botafogo","Vasco"]

if time in times_rj:
    print(f"O {time} é um time do Rio de Janeiro")

else: 
    print(f"O {time} não é um time do Rio de Janeiro")


# If ternário

idade = 18
print("Maior de idade" if idade >= 18 else "Menor de idade")