trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores_con_sueldo=[]
import csv,random,time,os
sueldo_bajo=[]
sueldo_medio=[]
sueldo_alto=[]

def crear_csv():
    with open("sueldos.csv","w", encoding="utf-8") as archiv_csv:
        archiv_csv.write("nombre,\tsueldo,\tdesc salud,\tdesc afp,\tS. liquido\n")\

def generar_sueldos_aleatorios():
    for indice in trabajadores:
        trabajadores_con_sueldo.append({"nombre":indice,"sueldo":random.randint(300000,2500000)})
    return print("generacion de sueldos exitosa")


def clasificar_sueldos():
    sueldo_menor=0
    sueldo_mediano=0
    sueldo_grande=0
    for datos in trabajadores_con_sueldo:
        if datos["sueldo"]<800000:
            sueldo_menor+=1
            sueldo_bajo.append({"nombre":datos["nombre"],"sueldo":datos["sueldo"]})
        elif datos["sueldo"]>800000 and datos["sueldo"]<2000000:
            sueldo_mediano+=1
            sueldo_medio.append({"nombre":datos["nombre"],"sueldo":datos["sueldo"]})
        elif datos["sueldo"]>2000000:
            sueldo_grande+=1
            sueldo_alto.append({"nombre":datos["nombre"],"sueldo":datos["sueldo"]})
    print("="*50)
    print("sueldos inferiores a 800 mil")
    print("NOMBRE COMPLETO\tSUELDO")
    print("="*50)
    for datos in sueldo_bajo:
        print(f"{datos["nombre"]} ,\t{datos["sueldo"]}")
    print("="*50)
    print("sueldos entre 800 mil y 2 mll:")
    print("NOMBRE COMPLETO\tSUELDO")
    print("="*50)
    for datos in sueldo_medio:
        print(f"{datos["nombre"]} ,\t{datos["sueldo"]}")
    print("="*50)
    print("sueldos superiores a 2 mll")
    print("NOMBRE COMPLETO\tSUELDO")
    print("="*50)
    for datos in sueldo_alto:
        print(f"{datos["nombre"]} ,\t{datos["sueldo"]}")
    return print("\nvista general de los sueldos")


def estadisticas_de_sueldos():
    os.system("cls")
    total=0
    iteraciones=0
    media=1
    print("1) Sueldo más alto")
    print("2) Sueldo más bajo")
    print("3) Promedio de sueldos")
    print("4) Media geométrica")
    print("5) salir al menu")
    while True:
        try:
            menu=int(input("ingrese la opcion solicitadad: "))
        except ValueError:
            print("el valor ingresado es invalido")
        else:
            match menu:
                case 1:
                    try:
                        print(max(trabajadores_con_sueldo,key=lambda x: x["sueldo"]))
                    except ValueError:
                        print("no sen encuentran saldos registrados")
                case 2:
                    try:
                        print(min(trabajadores_con_sueldo,key=lambda x: x["sueldo"]))
                    except ValueError:
                        print("no sen encuentran saldos registrados")
                case 3:
                    try:
                        for sueldos in trabajadores_con_sueldo:
                            total+=sueldos["sueldo"]
                            iteraciones+=1
                        print(f"el promedio de los sueldos es de: {total/iteraciones}")
                    except ZeroDivisionError:
                        print("no es posible generar el promedio sin antes registrar sueldos")
                case 4:
                    try:
                        for sueldos in trabajadores_con_sueldo:
                            media*=sueldos["sueldo"]
                            iteraciones+=1
                        resultado=media**(1/iteraciones)
                        print(f"la media geomtrica es de: {resultado.__trunc__()}")
                    except ZeroDivisionError:
                        print("la media geometrica no se puede solicitar si no se han generado los sueldos anteriormente")
                case 5:
                    break
                case _:
                    print("opcion invalida")
def reporte_sueldos_archivo_csv():
    if len(trabajadores_con_sueldo) ==0:
        return print("archivo creado sin informacion")
    else:
        with open("sueldos.csv","a", encoding="utf-8") as archiv_csv:
            for sueldos in trabajadores_con_sueldo:
                descuento_salud=0.93*sueldos["sueldo"]
                descuento_afp=0.88*sueldos["sueldo"]
                sueldo_liquido=sueldos["sueldo"]-(descuento_salud-descuento_afp)
                archiv_csv.write(f"{sueldos["nombre"]}\t{sueldos["sueldo"]}\t{descuento_salud.__trunc__()}\t{descuento_afp.__trunc__()}\t{sueldo_liquido.__trunc__()}\n")
        return print("archivo creado con exito")



#inicio del menu
crear_csv()
while True:
    os.system("cls")
    print("MENU EXAMEN TRANSVERSAL")
    print("="*50)
    print("1) generar sueldos aleatorios")
    print("2) clasificacion de sueldos")
    print("3) generar un reporte de sueldos")
    print("4) cargar estadisticas de sueldos ")
    print("5) salir")
    print("="*50)
    try:
        menu=int(input("ingrese una opcion: "))
        print("="*50)
    except ValueError:
        print("seleccion invalida")
    else:
        match menu:
            case 1:
                generar_sueldos_aleatorios()
                print("="*50)
                input("enter para continuar")
                os.system("cls")
            case 2:
                clasificar_sueldos()
                print("="*50)
                input("enter para continuar")
                os.system("cls")
            case 3:
                reporte_sueldos_archivo_csv()
                print("="*50)
                input("enter para continuar")
                os.system("cls")
            case 4:
                estadisticas_de_sueldos()
                print("="*50)
                input("enter para continuar")
                os.system("cls")
            case 5:
                print("saliendo del programa.....")
                print("realizado por: LUIS DAVID PAREDES CALDERON")
                print("rut: 20.124.583-4")
                time.sleep(2)
                break
            
            case _:
                print("seleccion invalida")
"""          
 Descuento salud 7%
 Descuento AFP 12%
 Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.
"""


