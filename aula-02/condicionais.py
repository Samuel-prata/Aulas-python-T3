'''    IF, ELSE ELIF  '''

email = 'samutigrao@gmail.com'
email_digitado = input('Digite seu email: ')
email_digitado = email_digitado.lower()
senha = 'Samu123'
senha_digitada = input('Digite sua senha: ')

''' OPERADORES DE COMPARAÇÃO
== -> IGUAIS
!= -> DIFERENTE
< -> MENOR
> -> MAIOR
<= MENOR OU IGUAL
>= -> MAIOR OU IGUAL
'''

''' OPERADORES BOOLEANOS
E = && = AND
OU = || = OR
NAO = ! = NOT
'''

if email_digitado == email and senha_digitada == senha: #True
    print('Logado com sucesso!')
elif senha_digitada != senha:
    print('Senha invalida. O usuário Edu@gmail.com ja contem essa senha!')
else: 
    print('Credenciais invalidas')
print('Terminamos')