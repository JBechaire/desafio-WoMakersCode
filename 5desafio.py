# DESAFIO 5 
"""
– Dias Restantes para Entrega de Projetos
A gerente de projetos Letícia precisa saber quantos dias faltam para cada entrega.
Crie um programa que:

Importe o módulo datetime
Peça uma data no formato DD/MM/AAAA
Calcule e exiba quantos dias faltam para o prazo
 """

# Importacao datetime 
from datetime import datetime, date

print("=== Dias Restantes para Entrega de Projetos ===")

# Pedir data 
data_str = input("Digite a data de entrega (DD/MM/AAAA): ")

#    Transformamos o texto (string) em uma data de verdade
#    Usamos datetime.strptime para "interpretar" a string conforme o formato indicado
#    Exemplo: "25/12/2026" vira um objeto datetime; depois pegamos só a parte 'date'
data_entrega = datetime.strptime(data_str, "%d/%m/%Y").date()

# Pegamos a data de hoje
hoje = date.today()

#    Calculamos a diferença entre as datas (entrega - hoje)
#    O resultado é um objeto 'timedelta'; para obter os dias inteiros, usamos .days
dias_restantes = (data_entrega - hoje).days

#  Mostramos o resultado de forma amigável
if dias_restantes > 0:
    print(f"Faltam {dias_restantes} dia(s) para a entrega.")
elif dias_restantes == 0:
    print("A entrega é hoje!")
else:
    # dias_restantes é negativo -> prazo já passou
    print(f"O prazo já passou há {abs(dias_restantes)} dia(s).")