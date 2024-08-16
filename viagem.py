def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio): # Cria a funcao calcular custo viagem com valores internos

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel # Variavel recebe o valor de um calculo

    custo_pedagio_total = numero_pedagios * custo_pedagio # Variavel recebe o valor de um calculo

    custo_total = custo_combustivel_total + custo_pedagio_total # Variavel recebe o valor de um calculo

    return custo_total, custo_combustivel_total, custo_pedagio_total # Retorna os 3 valores das variaveris

distancia = float(input("Digite a distância da viagem (em km): ")) # Le a distancia digitado pelom usuario
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): ")) # Le valor digitado pelo usuario
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): ")) # Le valor digitado pelo usuario
numero_pedagios = int(input("Digite o número de pedágios no percurso: ")) # Le valor digitado pelo usuario
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): ")) # Le valor digitado pelo usuario

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,
custo_combustivel,
consumo_veiculo, numero_pedagios, 

custo_pedagio) # AS 3 variaveis recebem os valores para serem feitos na funcao

print(f"Custo total da viagem: R${custo_total:.2f}") # Imrprime mensagem
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}") # Imrprime mensagem
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}") # Imrprime mensagem