# Enunciado da fase 1
# Implemente um programa que leia, valide e analise dados informados pelo usuário. Os dados são meteorológicos e referem-se aos dados de 2021 (de janeiro a dezembro) registrados em uma cidade.
# Toda entrada de dados deve ser validada. No caso de valor inválido, informe ao usuário o erro e permita que ele redigite o dado.

# Seu programa deve coletar os seguintes dados:

# • Mês: use valor numérico de 1 a 12 (janeiro a dezembro) para se referir aos meses do ano.

# Para cada mês do ano, informe:
# • Temperatura máxima do mês: devem estar em Celsius, garanta que estejam dentro de um intervalo válido para temperaturas, tal como: -60 graus à +50 graus.

# A seguir, seu programa deve calcular e exibir:
# • Temperatura média máxima anual: exibe a média das temperaturas máximas informadas.
# • Quantidade de meses escaldantes: quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
# • Mês mais escaldante do ano: mês que registrou a maior temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).
# • Mês menos quente do ano: mês que registrou a menor temperatura máxima dentre todos os informados. O mês deve ser escrito na tela por extenso (janeiro a dezembro).

# Antes de enviar, teste o seu programa com os seguintes dados:
import string
import math
import random

mes = 0
temp_max_mes = 0

for cont in range(1, 13):
    mes = int(input("Digite o mês: "))
    if mes in range(1, 13):
        temp_max_mes = float(input(f"Digite a temperatura do mês {mes}: "))


temp_media_max_anual = 0
qtd_meses_escaldantes = 0
mes_mais_escaldante = 0
mes_menos_escaldante = 0
