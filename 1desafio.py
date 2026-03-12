# DESAFIO 1
"""
– Métrica de Diversidade na Liderança
Como analista de dados em uma empresa de tecnologia, você precisa criar uma função para calcular uma métrica simples de diversidade de gênero na liderança.
A função deve receber:

Número total de líderes
Número de líderes mulheres

Após calcular a porcentagem de mulheres na liderança, retorne:

Abaixo de 30%: "A empresa está abaixo da meta de diversidade."
Entre 30% e 50%: "A empresa está na meta de diversidade."
Acima de 50%: "A empresa excedeu a meta de diversidade.

 """

print("=== Cálculo de Diversidade na Liderança ===")

# 1. O usuário informa o total de líderes
total_lideres = int(input("Digite o TOTAL de líderes da empresa: "))

# 2. O usuário informa quantas líderes são mulheres
lideres_mulheres = int(input("Digite o número de líderes MULHERES: "))

# 3. Calculando o percentual de mulheres
percentual = (lideres_mulheres / total_lideres) * 100

# 4. Mostrando o valor calculado
print(f"\nPercentual de mulheres na liderança: {round(percentual, 1)}%")

# critérios do desafio
if percentual < 30:
    print("A empresa está abaixo da meta de diversidade.")
elif percentual <= 50:
    print("A empresa está na meta de diversidade.")
else:
    print("A empresa excedeu a meta de diversidade.")