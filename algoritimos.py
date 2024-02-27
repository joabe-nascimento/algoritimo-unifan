class Biblioteca:
    def __init__(self):
        # Inicializa o catálogo como um dicionário vazio
        self.catalogo = {}

    def adicionar_livro(self, titulo, autor, num_identificacao):
        # Verifica se o número de identificação já existe no catálogo
        if num_identificacao in self.catalogo:
            print(f"Erro: Já existe um livro com o número de identificação {num_identificacao}")
        else:
            # Adiciona o livro ao catálogo
            self.catalogo[num_identificacao] = {'titulo': titulo, 'autor': autor}

    def buscar_livro_por_identificacao(self, num_identificacao):
        # Busca um livro no catálogo pelo número de identificação
        livro = self.catalogo.get(num_identificacao, None)
        return livro

