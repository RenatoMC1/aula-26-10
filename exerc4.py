Dados_pessoa = {}
listaNomes = []

for i in range(1,6):
    Nome = input(f"Digite o {i}º nome: ")
    Idade = int(input(f"Digite a {i}ª idade: "))
    Dados_pessoa[Nome] = Idade
    listaNomes.append(Nome)

print("-"*50)
for chave, valor in Dados_pessoa.items():
    if valor >=18:
        print("Os maiores de idade são:", chave)
print("-"*50)
