# main.py
from algoritimos import Biblioteca

# Exemplo de uso
algoritimos = Biblioteca()

# Adicionando mais livros
algoritimos.adicionar_livro("História Antiga", "Ana Oliveira", 789)
algoritimos.adicionar_livro("O Mundo Moderno", "Carlos Santos", 101)
algoritimos.adicionar_livro("Aventuras Submarinas", "Mariana Lima", 222)

# Busca por número de identificação
num_identificacao_procurado = 222
livro_encontrado = algoritimos.buscar_livro_por_identificacao(num_identificacao_procurado)

# Verifica se o livro foi encontrado e imprime as informações
if livro_encontrado:
    print("Livro encontrado:", livro_encontrado['titulo'], "por", livro_encontrado['autor'])
else:
    print("Livro não encontrado.")
