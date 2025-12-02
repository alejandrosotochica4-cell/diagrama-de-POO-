from servidor import Servidor
from indexador import Indexador
from procesador import Procesador
from recolector import Recolector
from editorial import Editorial
from hilo import Hilo
from usuario import Usuario
from producto import Producto
from libro import Libro
from revista import Revista
from articulo_segunda_mano import ArticuloSegundaMano
from novedades import Novedades
from articulo_online import ArticuloOnline


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Servidor")
        print("2. Usuario")
        print("3. Producto")
        print("4. Procesador")
        print("5. Recolector")
        print("6. Editorial")
        print("7. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            servidor = Servidor()
            print(servidor.muestra_pagina())
            print(servidor.envia_sugerencia())

        elif opcion == "2":
            usuario = Usuario("Ana", "Lopez", 123, "Cra 10", "ana123", "pass")
            print(usuario.comprar())
            print(usuario.leer())

        elif opcion == "3":
            producto = Producto(20, "Libro A", "Autor X", "Planeta", 2020, "Ficción")
            print(producto.ver_catalogo())

        elif opcion == "4":
            procesador = Procesador()
            print(procesador.realizar_pago())

        elif opcion == "5":
            recolector = Recolector()
            print(recolector.envia_novedades())

        elif opcion == "6":
            editorial = Editorial("Planeta", "Calle 123", "5551234")
            print(editorial.vender())

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
