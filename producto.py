class Producto:
    def __init__(self, precio, titulo, autor, editorial, año, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año = año
        self.preferencias = preferencias

    def vender(self):
        return f"Producto {self.titulo}: vendido"

    def comprar(self):
        return f"Producto {self.titulo}: comprado"

    def ver_catalogo(self):
        return f"Catálogo mostrando {self.titulo}"
