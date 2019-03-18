import re


class ListaArticulo:
    def __init__(self, **kwargs):
        self.nombre = kwargs.get('nombre', 'default')

    def __open__(self, mode):
        return open(self.__str__(), mode)

    def __close__(self, archivo):
        return archivo.close()

    def __str__(self):
        return '{}.txt'.format(self.nombre)

    def ver_articulos(self):
        archivo = self.__open__('r')
        for i, art in enumerate(archivo.readlines()):
            print("{}.- {}".format(i + 1, art[:-1]))
        self.__close__(archivo)

    def agregar_articulo(self, articulo):
        archivo = self.__open__('a')
        try:
            archivo.write('{}\n'.format(articulo))
        except Exception as e:
            print("Error tratando de agregar el articulo.")
        else:
            print("Articulo {} agregado correctamente".format(articulo))
            self.__close__(archivo)

    def buscar_articulo(self):
        archivo = self.__open__('r')
        articulo = input("Nombre del articulo que desee buscar: \n")
        for i, v in enumerate(
                re.findall(r'({})\w+'.format(articulo), archivo.read())):
            print("{}.- {}".format(i + 1, v))
        self.__close__(archivo)

    def eliminar_articulo(self):
        self.ver_articulos()
        try:
            articulo = int(
                input("Indique el numero del articulo que desea eliminar: \n"))
        except ValueError:
            print("Ingrese un numero")
            self.eliminar_articulo()
        else:
            archivo = self.__open__('r')
            texto = archivo.readlines()
            self.__close__(archivo)
            archivo = self.__open__('w')
            nombre_art = ''
            for i, art in enumerate(texto):
                if not articulo - 1 == i:
                    archivo.write(art)
                else:
                    nombre_art = art
            self.__close__(archivo)
            if nombre_art:
                print("El articulo {} fue eliminado.".format(nombre_art[:-1]))

    def ver_articulo(self):
        pass
