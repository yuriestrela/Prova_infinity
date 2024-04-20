class Material:
    def __init__(self, titulo, autor_ou_editora):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        print(f'Titulo: {self.titulo} \nAutor ou editora: {self.autor_ou_editora}')


class Livro(Material):
    def __init__(self, titulo, autor_ou_editora, genero):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Gênero: {self.genero}')


class Revista(Material):
    def __init__(self, titulo, autor_ou_editora, edicao):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Edição: {self.edicao}')


livro = Livro("Dom Casmurro", "Machado de Assis", "Romance")
revista = Revista("Veja", "Editora Abril", "Edição 2345")

livro.exibir_informacoes()
revista.exibir_informacoes()