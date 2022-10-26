# Titulo = {}
# Autor = {}
# Data_lancamento = {}
# Edicao = {}
# Editora = {}
# ISBN = {}

Titulo = input("Digite o título do livro: ")
Autor = input("Digite o autor do livro: ")
Data_lancamento = input("Digite a Data de Lançamento do livro: ")
Edicao = input("Digite a edição do livro: ")
Editora = input("Digite a Editora: ")
ISBN = input("Digite o ISBN: ")

Dados_Livro = {
    'Título': Titulo,
    'Autor': Autor,
    'Data de Lançamento': Data_lancamento,
    'Edição': Edicao,
    'Editora': Editora,
    'ISBN': ISBN

}

print(Dados_Livro)
