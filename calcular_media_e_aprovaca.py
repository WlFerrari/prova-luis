def calcular_media_e_aprovacao(notas, nota_minima_aprovacao): # Cria a funcao de calcular media e aprovacao com dois valores internos padroes
    total_notas = 0 # total notas recebe valor inicial 0
    num_alunos = len(notas) # numero de alunos recebe o tamanho da quantidade de notas
    aprovados = [] # Cria uma lista com os aprovados
    reprovados = [] # Cria uma lista com os reprovados

    for aluno, nota in notas.items(): # Repeticacao para cada aluno e nota em notas
        total_notas += nota # total notas recebe a soma da nota
    if nota >= nota_minima_aprovacao: # Condicao para ver se nota e maior ou igual a nota minima 
        aprovados.append(aluno) # Adiciona o aluno a lista de aprovados
    else: # Condicao senao
        reprovados.append(aluno) # Adiciona o aluno a lista de reprovados

    media_turma = total_notas / num_alunos # Media da turma recebe o calculo do total de notas dividido pelo numero de alunos

    return media_turma, aprovados, reprovados # Retorna os valores da media da turma, aprovados e reprovados

    notas = { # notas recebe um dicionario padrao com alunos e suas notas
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
    }

nota_minima_aprovacao = 70 # Valor padrao para aprovacao e o valor inteiro 70

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao) # valores da media da turma, aprovados e reprovados vao receber os valores retornados pela funcao

print(f"Média da turma: {media_turma:.2f}") # Imprime a media da turma com 2 casas decimais formatadas
print(f"Alunos aprovados: {', '.join(aprovados)}") # Imprime os aprovados em uma unica string
print(f"Alunos reprovados: {', '.join(reprovados)}") # Imprime os reprovados em uma unica string
