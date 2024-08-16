def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso): # Define a função calcular_juros_atraso com valores internos
    taxa_juros_diaria = taxa_juros_anual / 365 / 100 # A variavel taxa_juros_diaria recebe uma conta

    juros = valor_principal * taxa_juros_diaria * dias_atraso # A variavel juros ira receber im calculo

    valor_total = valor_principal + juros # valor_total ira receber a soma entre o valor_principal e juros
    return valor_total, juros # retorna o valor total e o juros calculados dentro da função


valor_principal = 1000.00 # A variavel recebe valor padrao 1000 em float
taxa_juros_anual = 5.0 # A variavel recebe o valor padrao 5 em float
dias_atraso = 30 # A variavel recebe o valor inteiro 30 como padrao
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso) # As variaveis valor_total e juros recebem o valor retornado pela funcao
print(f"Valor total a ser pago: R${valor_total:.2f}") # Imprime o valor total formatado em djuas casas decimais
print(f"Valor dos juros: R${juros:.2f}") # Imprime os juros formatado em 2 casas deciamsi
