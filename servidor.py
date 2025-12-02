class Servidor:
    def __init__(self):
        self.estado = "activo"

    def muestra_pagina(self):
        return "Servidor: mostrando página"

    def envia_sugerencia(self):
        return "Servidor: enviando sugerencia"

    def envia_datos_de_compra(self):
        return "Servidor: enviando datos de compra"

    def envia_datos_de_venta(self):
        return "Servidor: enviando datos de venta"
