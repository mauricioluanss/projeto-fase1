# Constante com os nomes do meses para usar como refeência no laço principal.
MESES = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

# Variaveis de escopo global (vaolres vão mudar no decorrer do script)
qtd_meses_escaldantes = 0
maior_temp_max = None
menor_temp_max = None
mes_mais_escaldante = ""
mes_menos_quente = ""
soma_temp_max = 0

# Loop principal. Ele solicita a temperatura de cada mês, valida a entrada,
# e todas as verificações.
for mes in MESES:
    while True:
        try:
            temp_max = float(input(f"Informe a temperatura máxima de {mes}: "))

            if temp_max < -60 or temp_max > 50:
                print("A temperatura deve estar entre -60°C e 50°C.")
            else:
                soma_temp_max += temp_max

                # armazena a qtd de meses escaldantes
                if temp_max > 33:
                    qtd_meses_escaldantes += 1

                # captura a temperatura e mês mais escaldante
                if maior_temp_max is None or temp_max > maior_temp_max:
                    maior_temp_max = temp_max
                    mes_mais_escaldante = mes

                # captura temperatura e mês menos quente
                if menor_temp_max is None or temp_max < menor_temp_max:
                    menor_temp_max = temp_max
                    mes_menos_quente = mes

                break

        except ValueError:
            print("Entrada inválida... Tu precisa informar um número.")


# Parte final que informa os dados pro usuário
print("\nRELATÓRIO METEOROLÓGICO ANUAL")
print(f"Temperatura média máxima anual: {soma_temp_max / len(MESES):.1f}°C")

if qtd_meses_escaldantes < 1:
    quente_escaldante = "quente"
    print("Não houveram meses escaldantes no ano.")
else:
    quente_escaldante = "escaldante"
    print(f"Quantidade de meses escaldantes no ano: {qtd_meses_escaldantes}")

print(
    f"Mês mais {quente_escaldante} do ano: {mes_mais_escaldante} {maior_temp_max:.1f}°C"
)
print(f"Mês menos quente do ano: {mes_menos_quente} {menor_temp_max:.1f}°C")
print("\n")
