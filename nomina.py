
    import time
import contextlib
import re


def nomina():
    # Declaracion de las variables
    su_name = input("Digite Su Nombre: ")
    su_last = input("Digite Su Apellido: ")

    su_Documento = input("Ingrese su numero de Documento")
    sueldo_base = int(input("Digite Su Salario: "))
    su_Diastrabajados = int(input("Digite dia trabajados: "))
    print("\n")

    # subcidio de trasmporte
    if sueldo_base < 2000001:
        excedente =  117172
    else:
        excedente = 0
    st = int(excedente)

    # Calculo del Salud
    ss = int(sueldo_base * 0.04)
    # Pension
    ps = int(sueldo_base * 0.12)

    # Total de Descuento
    total_descuento = ss + ps
    # Sueldo Neto
    sueldo_neto = sueldo_base + st - total_descuento

    # Salida de Valores
    print("[~] Realizando los calculos.......")
    print("[~] Imprimiendo los resultados.......")
    print("\n")
    time.sleep(1)
    print("[+] Su Sueldo Bruto es: " + str(sueldo_base))
    print("[+] Sueldo mas gasto de presentacion: " + str(sueldo_base))
    print("[+] Salud: " + str(ss))
    print("[+] Pension: " + str(ps))
    print("[+] Total de retenciones: " + str(total_descuento))
    print("[+] Sueldo Neto: " + str(sueldo_neto))
