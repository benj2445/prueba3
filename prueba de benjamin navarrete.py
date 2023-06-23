import random
def Grabar_Vehiculo(vehiculos):
    tipo = input("Tipo de Vehiculos:")
    patente= input("Patente:")
    marca = input("Marca:")
    precio =float(input("Precio:"))
    multas = []
    while True:
        opcion = input("¿Agregar multa?(S/N):")
        if opcion.lower()=="S":
            monto = float(input("Monto de la Multa:"))
            fecha = input("Fecha de la Multa:")
            multas.append((monto,fecha))
        else:
            break
        fecha_registro=input("Fecha de Registro del Vehiculo:")
        nombre_dueño=input("Nombre del Dueño:")
        vehiculos[patente]={"Tipo":tipo,"Marca":marca,"Precio":precio,"Multas":multas,"Fecha_Registro":fecha_registro,"Nombre_Dueño":nombre_dueño}
        print("Vehiculo Registrado Correctamente.")
        def buscar_vehiculo(vehiculos):
            patente=input("Ingrese la Patente del Vehiculo:")
            if patente in vehiculos:
                vehiculos=vehiculos[patente]
                print("Informacion del Vehiculo:")
                print("Tipo:",vehiculos["Tipo"])
                print("Patente:",patente)
                print("Marca:",vehiculos["Marca"])
                print("Precio:",vehiculos["Precio"])
                print("Multas:")
                for monto, fecha in vehiculos["Multas"]:
                    print("-Monto:",monto)
                    print("-Fecha:",fecha)
                    print("Fecha de Registro:",vehiculos["Fecha_Registro"])
                    print("Dueño:",vehiculos["Nombre_Dueño"])
                else:
                    print("no se encontro ningun Vehiculos con esa Patente.")
                    def imprmir_certificado(vehiculos):
                        for patente,vehiculos in vehiculos():
                            certificado_contaminates = 5000
                            random.randint(1.500,3.500)
                            certificado_anotaciones = 10000
                            random.randint(1.500,3.500)
                            certificado_multas = 15000
                            random.randint(1.500,3.500)
                            print("Certificados para el Vehiculos con Patente",patente)
                            print("-Certificado de Emision de Contaminantes:",certificado_contaminates)
                            print("-Certificado de Anotaciones Vigentes:",certificado_anotaciones)
                            print("-Certificado de Multas:",certificado_multas)
                            print("Datos del Dueño:")
                            print("-Nombre:",vehiculos["Nombre_Dueño"])
                            print("-Patente del Vehiculos:",patente)
                            print()
                            def menu():
                                vehiculos={}
                                nombre=input("Ingrese su Nombre:")
                                apellido=input("Ingrese su Apellido:")
                                version="1.0"
                                while True:
                                    print("\n---Menu---")
                                    print("1.Grabar Vehiculos")
                                    print("2.Buscar Vehiculos")
                                    print("3.Imprimir Certificados")
                                    print("4.Salir")
                                    opcion=input("Seleccione una Opcion (1-4):")
                                    if opcion =="1":
                                        Grabar_Vehiculo(vehiculos)
                                    elif opcion =="2":
                                        buscar_vehiculo(vehiculos)
                                    elif opcion =="3":
                                        imprmir_certificado(vehiculos)
                                    elif opcion =="4":
                                        print("Gracias por Utilizar este Programa.")
                                        print("Nombre:{}{}",format(nombre,apellido))
                                        print("programa version 1.0")
                                        
                                        







                