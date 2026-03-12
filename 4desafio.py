# DESAFIO 4 
""" 
– Remover Valores Duplicados de uma Lista
Durante a consolidação de dados, foram encontrados números repetidos em uma lista.
Crie um programa que:

Receba uma lista de números
Gere uma nova lista sem valores duplicados
 """

print("=== Remover Valores Duplicados de uma Lista ===")

lista_numeros = [5, 2, 8, 5, 3, 2, 9]

lista_sem_duplicados = []

# Percorre cada número da lista original
for numero in lista_numeros:
    # Se o número AINDA NÃO está na nova lista, adicionamos
    if numero not in lista_sem_duplicados:
        lista_sem_duplicados.append(numero)

print("Lista original:       ", lista_numeros)
print("Sem valores repetidos:", lista_sem_duplicados)
