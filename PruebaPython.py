class Animal:
    def operation1(self, params):
        # Implementar la funcionalidad según sea necesario
        pass

    def operation2(self):
        # Implementar la funcionalidad según sea necesario
        pass

class Vertebrado(Animal):
    def __init__(self):
        self.attribute1 = 'defaultValue'
        self.attribute2 = 'type'
        self.attribute3 = 'type'

    def operation1(self, params):
        # Implementar la funcionalidad según sea necesario
        pass

    def operation2(self, params):
        # Implementar la funcionalidad según sea necesario
        pass

class Mamiferos(Vertebrado):
    def __init__(self):
        super().__init__()

class Aves(Vertebrado):
    def __init__(self):
        super().__init__()

class Reptiles(Vertebrado):
    def __init__(self):
        super().__init__()

# Ejemplo de creación de un objeto
mi_mamifero = Mamiferos()
mi_ave = Aves()
mi_reptil = Reptiles()
