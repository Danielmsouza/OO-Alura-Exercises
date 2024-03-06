class Book:
    def __init__(self, title='', author='', pages=0):
        self.titulo = title
        self.autor = author
        self.paginas = pages

    def __str__(self):
        return f'{self.title} for {self.author} - {self.pages} pages'

    @property
    def titulo_author(self):
        return f'{self.title} for {self.author}'

    def increase_pages(self, amount):
        self.pages += amount

