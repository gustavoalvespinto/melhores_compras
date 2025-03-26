import statistics

titulo = "Calcula o valor médio de avaliação do produto"
print(f'{titulo:^50}')

nota1 = int(input("Digite a primeira nota avaliada do produto pelo cliente: "))

nota2 = int(input("Digite a segunda nota avaliada do produto pelo cliente: "))

media = [nota1, nota2]

media = statistics.mean(media)

print("A média alcançada foi: {}".format(media))

if media > 6:
    print("Parabéns, produto adequado aos clientes!")
else:
    print("Que pena, esse produto inadequado e com muitas reclamações!")
	
		   