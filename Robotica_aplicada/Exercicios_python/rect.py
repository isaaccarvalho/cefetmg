# Criando a classe Rect
class Rect:

    def __init__(self, width, height): # Construtor da Classe
        self.width = width
        self.height = height

    def area(self): # Calcula Área do Retângulo
        return self.width*self.height

    def per(self): # Calcula Perímetro do Retângulo
        return (2*self.width)+(2*self.height)
