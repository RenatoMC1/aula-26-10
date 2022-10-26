Dados_pessoa = {}

for i in range(1,11):
    Nome = input("Digite o nome: ")
    Idade = int(input("Digite a idade: "))
    Dados_pessoa[Nome] = Idade

print(Dados_pessoa)
print("-"*50)

for item in Dados_pessoa.items():
    print(item)
print("-"*50)
for chave in Dados_pessoa.keys():
    print(chave)
print("-"*50)
for valor in Dados_pessoa.values():
    print(valor)
print("-"*50)