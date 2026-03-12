# DESAFIO 2 
"""
– Sistema de Login Simples
Para acessar a plataforma do bootcamp, as participantes precisam realizar um login simples.
Crie um programa que:

Use um usuário e senha pré-definidos
Solicite login e senha
Informe se o acesso foi permitido ou negado

"""

print("=== Sistema de Login Simples ===")
# usuário e senha corretos (pré-definidos)
usuario_correto = "WoMakers"
senha_correta = "Code@123"

# A pessoa digita o usuário e a senha
# A função input lê o que o usuário digitar no teclado como texto (string)
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")

# Comparar o que foi digitado com o que é correto
# '==' para verificar se os textos são exatamente iguais
if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    # Se as duas comparações forem verdadeiras, o acesso é permitido
    print("Acesso permitido.")
else:
    # Caso contrário (qualquer um estiver errado), acesso negado
    print("Acesso negado.")
