def calcular_area_comodos(): # Cria a função de calcular a area dos comodos
    total_area = 0 # A area total tem valor inicial 0
    while True: # Inicia uma condição 

        largura = float(input("Digite a largura do cômodo (em metros): ")) # Largura vai receber um dado float digitado pelo usuario
        comprimento = float(input("Digite o comprimento do cômodo (em metros): ")) # Comprimento ira receber um dado float digitado pelo usuario 

        area_comodo = largura * comprimento # area do comodo recebe o calcula da largura vezes comrpimento
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.") # Imprime o valor da area do comodo formatado em 2 casas decimais

        total_area += area_comodo # A area total recebe o valor da area do comodo toda vez que é chamada assim fazendo uma soma

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower() # Imprime uma pergunta ao usuario formatando a resposta em minusculo e sem espaços
        if mais_comodos != 's': # Realiza a condição se o usuario digitar uma respota diferente de "s"
            break # Encerra a função

        return total_area # Retorna a area total

area_total = calcular_area_comodos() # A variavel area_total recebe o valor do calculo realizado na funcao da area dos comodos
print(f"A área total da casa é: {area_total:.2f} metros quadrados.") # Imprime a area total com a formatacao de 2 casas decimais