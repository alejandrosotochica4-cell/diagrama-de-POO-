class Usuario:
    def __init__(self, nombre, apellido, cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta
        self.direccion = direccion
        self.login = login
        self.password = password

    def enviar_sugerencia(self):
        return "Usuario: enviando sugerencia"

    def leer(self):
        return "Usuario: leyendo producto"

    def comprar(self):
        return "Usuario: comprando producto"

    def vender(self):
        return "Usuario: vendiendo producto"

    def realizar_reclamacion(self):
        return "Usuario: realizando reclamación"
