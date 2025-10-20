#primeros datos
agenda={
    "jose": {
        "telefono": 302944,
        "correo": "jo@.com",
        "direccion": "Paris"  },
    "mario": {
        "telefono": 829455,
        "correo": "jo@.com",
        "direccion": "espa"},

    "angel": {
        "telefono": 829405,
        "correo": "jo@.com",
        "direccion": "florida"},
    "luis": {
        "telefono": 930594,
        "correo": "jo@.com",
        "direccion": "barranquilla"},
}
# funciones reutilizables
#1
def consulta(nombre):
    if nombre in agenda:
        datos = agenda[nombre]
        print(f"\n{nombre}:")
        print(f"Teléfono: {datos['telefono']}")
        print(f"Correo: {datos['correo']}")
        print(f"Direccion: {datos['direccion']}\n")
    else:
        print("\nno existe el nombre buscado\n")
#2
def agregar(nombre,telefono,correo,direccion):
    if nombre in agenda:
        print("\n el nombre ya existe")
    else:
        agenda[nombre] = {
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion,
        }
#3
def modificar(nombre,telefono,correo,direccion):
    if nombre in agenda:
        agenda[nombre] ["telefono"] = telefono
        agenda[nombre] ["correo"] = correo
        agenda[nombre] ["direccion"] = direccion
        print(" modificacion exitosa")
    else:
        print("\nno existe el nombre buscado\n")
#4
def eliminar(nombre,telefono,correo,direccion):
    if nombre in agenda:
        del agenda[nombre]
        print(" eliminacion exitosa")
    else:
        print("\nno existe el nombre buscado\n")
#5
def buscarnumero(numero):
    for nombre, datos in agenda.items():
        if datos["telefono"] == numero:
           print(f"\n nuero encontrado:{nombre}")
           print(f"telefono : {datos['telefono']}\n")
           print(f"correo : {datos['correo']}\n")
           print(f"direccion : {datos['direccion']}\n")
           return nombre
        print("\nno existe el nombre buscado\n")
        return None
consultando= True
"""
Actúa como una bandera de control.
Mientras su valor sea True, el ciclo se seguirá ejecutando.
"""

#creacion del menu

while consultando:
    print()
    print("Agenda")
    print("--------------------")
    print("1. consulta \n2. añadir \n3. modificar\n4. eliminar \n5. busacar numero\n6. agenda \n7. salir")


    opcion=""
#Define un ciclo while y compruebe si la persona ha seleccionado o no

    while opcion not in ["1","2","3","4","5"]:
        opcion = input("Selecciona una opción (1-5): ")


        if opcion == "1":
            nombre = input("Ingresa el nombre del cliente: ")
            consulta(nombre)

        elif opcion == "2":
            nombre = input("Ingresa el nombre del cliente: ")
            try:
                telefono = int(input("Ingresa el telefono del cliente: "))
                correo = input("Ingresa el correo del cliente: ")
                direccion = input("Ingresa la direccion del cliente: ")
                agregar(nombre,telefono,correo,direccion)
            except ValueError:
                print("\nnumero no valido\n")

        elif opcion == "3":
            nombre = input("Ingresa el nombre del cliente: ")
            try:
                telefono = int(input("Ingresa el nuevo telefono del cliente: "))
                correo = input("Ingresa el nuevo correo del cliente: ")
                direccion = input("Ingresa la nuevo direccion del cliente: ")
                modificar(nombre, telefono, correo, direccion)
            except ValueError:
                print("\nnumero no valido\n")

        elif opcion == "4":
            nombre = input("Ingresa el nombre del cliente: ")
            eliminar(nombre)

        elif opcion == "5":
            nombre = input("Ingresa el nuemero del cliente: ")
            buscarnumero(nombre)

        elif opcion == "6":
            print("AGENDA COMPLETA")
            for nombre, datos in agenda.items():
                print(f" {nombre}: Telefono: {datos['telefono']}, Correo: {datos['correo']}, Direccion: {datos['direccion']}")
                print()

        elif opcion == "7":
            consultando = False
            print("\n", "\n")
            print(" gracias por buscar")
            print("\n", "\n")