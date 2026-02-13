class NO:
    def __init__(self,palavra,linha):
        self.palavra = palavra
        self.linhas = {linha}
        self.altura = 1
        self.esquerda = None
        self.direita = None
