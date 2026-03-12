# DESAFIO 3 
"""
– Média Salarial no Departamento de Engenharia de Dados
Você recebeu uma lista de dicionários com informações sobre funcionárias.
Sua tarefa:
Calcular a média salarial das mulheres do departamento Engenharia de Dados.
Dica: percorra a lista, filtre pelo departamento, some os salários e calcule a média.
Lista fornecida:
funcionarias = [
    {"nome": "Beatriz", "departamento": "Análise de BI", "salario": 7000},
    {"nome": "Helena", "departamento": "Engenharia de Dados", "salario": 9500},
    {"nome": "Isabela", "departamento": "Ciência de Dados", "salario": 11000},
    {"nome": "Laura", "departamento": "Engenharia de Dados", "salario": 8500},
    {"nome": "Mariana", "departamento": "Engenharia de Software", "salario": 7500}
]
"""


# Lista de funcionárias com nome, departamento e salário
funcionarias = [
    {"nome": "Beatriz", "departamento": "Análise de BI", "salario": 7000},
    {"nome": "Helena", "departamento": "Engenharia de Dados", "salario": 9500},
    {"nome": "Isabela", "departamento": "Ciência de Dados", "salario": 11000},
    {"nome": "Laura", "departamento": "Engenharia de Dados", "salario": 8500},
    {"nome": "Mariana", "departamento": "Engenharia de Software", "salario": 7500}
]

print("===  Média Salarial no Departamento de Engenharia de Dados ===")

# Departamento que queremos filtrar
departamento = "Engenharia de Dados"

#somar salários e contar quantas funcionárias são do departamento
soma_salarios = 0
quantidade = 0

# Percorrer (loop) cada funcionária da lista
for func in funcionarias:
    # Verifica se o departamento da funcionária é o que queremos
    if func["departamento"] == departamento:
        # Se for, somamos o salário dela
        soma_salarios = soma_salarios + func["salario"]
    
        quantidade = quantidade + 1

# calcula e imprime a média se encontrou pelo menos 1 funcionária
if quantidade > 0:
    media = soma_salarios / quantidade
   
    print(f"Média salarial em '{departamento}': R$ {round(media, 2)}")
else:
    print(f"Não há funcionárias no departamento '{departamento}'.")