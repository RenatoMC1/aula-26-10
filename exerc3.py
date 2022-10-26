Dados_pessoa = {}
lista_idades = []

for i in range(1,11):
    Nome = input(f"Digite o {i}º nome: ")
    Idade = int(input(f"Digite a {i}ª idade: "))
    Dados_pessoa[Nome] = Idade
    lista_idades.append(Idade)

print("-"*50)
print(Dados_pessoa)
print("-"*50)
print("A Lista das idades são: ", lista_idades)
print("-"*50)
print("o valor mínimo é: ", min(lista_idades))
print("-"*50)
print("o valor máximo é: ", max(lista_idades))
print("-"*50)
print("o valor da soma é: ", sum(lista_idades))
print("-"*50)
print("o valor da média é: ", sum(lista_idades)/len(lista_idades))
print("-"*50)
lista_idades.sort()
print("A ordem crescente é: ", (lista_idades))
print("-"*50)
lista_idades.reverse()
print("A ordem decrescente é: ", (lista_idades))
print("-"*50)