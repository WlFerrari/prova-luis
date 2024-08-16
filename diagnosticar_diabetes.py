def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial): # Define a funcao de diagnosticar diabetes com 2 valores internos padroes

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200: # Realiza a condicao de que se a glicemia em jejum for maior ou igual a 126 ou a glicemia pos prandial for maior ou igual a 200
        return "Diabetes" # Retorna o valor Diabetes no terminal
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200: # Realiza a condição de que se a glicemia em jejum for menor ou igual a 100 ou a glicemia pos prandial forn menor ou igual a 140 e menor que 200
        return "Pré-diabetes" # Retorna o valor pre-diabetes no terminal
    else: # Condição final
        return "Normal" # Retorna o valor normal no terminal

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): ")) # Glicemia em jejum recebe um valor float digitado pelo usuario
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): ")) # Glicemia pos prandial recebe um valor float digitado pelo usuario

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial) # a variavel resultado recebe o valor da funcao diagnosticar diabetes
print(f"O diagnóstico é: {resultado}") # Imprime o resultado