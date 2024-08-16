def calcular_imc(peso, altura): # Cria a funcao para calcular o imc com 2 valores internos

    imc = peso / (altura ** 2) # Imc recebe o calculo do peso vezes altura elevado ao quadrado
    return imc # retorna o valor do imc

def classificar_imc(imc): # Cria a funcao classificar imc com valor interno do imc

    if imc < 18.5: # Condicao se imc for menor que 18.5
        return "Abaixo do peso" # retorna abaixo do peso
    elif 18.5 <= imc < 24.9: # outra condicao se imc estiver entre 18.5 e 24.9
        return "Peso normal" # retorna peso normal
    elif 25 <= imc < 29.9: # outra condicao se imc estiver entre 25 e 29.9
        return "Sobrepeso" # retorna sobrepeso
    elif 30 <= imc < 34.9: # outra condicao se imc estiver entre 30 e 34.9
        return "Obesidade grau 1" # retorna obesidade grau 1
    elif 35 <= imc < 39.9: # outra condicao se imc estiver entre 35 e 39.9
        return "Obesidade grau 2" # retorna obesidade grau 2
    else: # senao
        return "Obesidade grau 3" # retorna obesidade grau 3
        
def sugestao_atividade_fisica(classificacao_imc): # funcao com valor interno da funcao classificacao imc

    if classificacao_imc == "Abaixo do peso": # condicao se classificacao imc tiver valor igual a abaixo do peso
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
        proteínas e calorias." # retorna uma frase
    elif classificacao_imc == "Peso normal": # outra condicao
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
        natação, junto a um treino de força moderado." # retorna frase
    elif classificacao_imc == "Sobrepeso": # outra condicao
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
        de exercícios de resistência." # retorna frase
    elif classificacao_imc == "Obesidade grau 1": # outra condicao
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
        programa de reeducação alimentar." # retorna frase
    elif classificacao_imc == "Obesidade grau 2": # outra condicao
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
        acompanhamento nutricional." # retorna frase
    else: # senao
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
        fisioterapia, e consultas regulares com um nutricionista." # retorna frase

peso = float(input("Digite seu peso (em kg): ")) # input para peso com valor float
altura = float(input("Digite sua altura (em metros): ")) # input para altura com valor float

imc = calcular_imc(peso, altura) # imc recebe o calcular imc dos valores fornecidos acima
classificacao_imc = classificar_imc(imc) # classificacao imc recebe o valor da funcao classficar imc
sugestao = sugestao_atividade_fisica(classificacao_imc) # sugestao recebe o valor da funcao sugestao...

print(f"Seu IMC é: {imc:.2f}") # Imprime o imc com formatacao de 2 casas decimais
print(f"Classificação: {classificacao_imc}") # Imprime a classificacao
print(f"Sugestão de atividade física: {sugestao}") # Imprime a sugestao