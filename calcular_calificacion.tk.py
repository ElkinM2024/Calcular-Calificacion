import tkinter as tk
from tkinter import simpledialog

# Diccionario para almacenar alumnos
alumnos = {}

# Función para calcular la calificación
def calcular_calificacion(nota):
    if nota < 5:
        return "SS"
    elif 5 <= nota < 7:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    elif nota >= 9:
        return "SB"

# Función para validar entradas
def es_numero(valor):
    return valor.isdigit()

def es_letra(valor):
    return valor.replace(" ", "").isalpha()

# Funciones de gestión
def mostrar_alumnos():
    if not alumnos:
        resultado_label.config(text="No hay alumnos registrados.")
        return
    resultado = "DNI | Apellidos, Nombre | Nota | Calificación\n"
    for dni, datos in alumnos.items():
        resultado += f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}\n"
    resultado_label.config(text=resultado)

def introducir_alumno():
    dni = simpledialog.askstring("Introducir Alumno", "DNI:")
    if not dni or not es_numero(dni):
        resultado_label.config(text="Error: El DNI debe contener solo números.")
        return
    if dni in alumnos:
        resultado_label.config(text="Error: El DNI ya está registrado.")
        return
    apellidos = simpledialog.askstring("Introducir Alumno", "Apellidos:")
    if not apellidos or not es_letra(apellidos):
        resultado_label.config(text="Error: Los apellidos deben contener solo letras.")
        return
    nombre = simpledialog.askstring("Introducir Alumno", "Nombre:")
    if not nombre or not es_letra(nombre):
        resultado_label.config(text="Error: El nombre debe contener solo letras.")
        return
    nota = simpledialog.askstring("Introducir Alumno", "Nota:")
    if not nota or not es_numero(nota) or not (0 <= float(nota) <= 10):
        resultado_label.config(text="Error: Nota inválida. Introduzca un número entre 0 y 10.")
        return
    nota = float(nota)
    calificacion = calcular_calificacion(nota)
    alumnos[dni] = {"apellidos": apellidos, "nombre": nombre, "nota": nota, "calificacion": calificacion}
    resultado_label.config(text="Alumno introducido correctamente.")

def eliminar_alumno():
    dni = simpledialog.askstring("Eliminar Alumno", "DNI del alumno a eliminar:")
    if not dni or not es_numero(dni):
        resultado_label.config(text="Error: El DNI debe contener solo números.")
        return
    if dni in alumnos:
        del alumnos[dni]
        resultado_label.config(text="Alumno eliminado correctamente.")
    else:
        resultado_label.config(text="Error: DNI no encontrado.")

def consultar_alumno():
    dni = simpledialog.askstring("Consultar Alumno", "DNI del alumno:")
    if not dni or not es_numero(dni):
        resultado_label.config(text="Error: El DNI debe contener solo números.")
        return
    if dni in alumnos:
        datos = alumnos[dni]
        resultado = (f"DNI: {dni}\nApellidos: {datos['apellidos']}\nNombre: {datos['nombre']}\n"
                     f"Nota: {datos['nota']}\nCalificación: {datos['calificacion']}")
        resultado_label.config(text=resultado)
    else:
        resultado_label.config(text="Error: DNI no encontrado.")

def modificar_nota():
    dni = simpledialog.askstring("Modificar Nota", "DNI del alumno:")
    if not dni or not es_numero(dni):
        resultado_label.config(text="Error: El DNI debe contener solo números.")
        return
    if dni in alumnos:
        nueva_nota = simpledialog.askstring("Modificar Nota", "Nueva nota:")
        if not nueva_nota or not es_numero(nueva_nota) or not (0 <= float(nueva_nota) <= 10):
            resultado_label.config(text="Error: Nota inválida. Introduzca un número entre 0 y 10.")
            return
        nueva_nota = float(nueva_nota)
        alumnos[dni]["nota"] = nueva_nota
        alumnos[dni]["calificacion"] = calcular_calificacion(nueva_nota)
        resultado_label.config(text="Nota modificada correctamente.")
    else:
        resultado_label.config(text="Error: DNI no encontrado.")

def mostrar_suspensos():
    suspensos = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
                 for dni, datos in alumnos.items() if datos["nota"] < 5]
    if suspensos:
        resultado_label.config(text="\n".join(suspensos))
    else:
        resultado_label.config(text="No hay alumnos suspensos.")

def mostrar_aprobados():
    aprobados = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
                 for dni, datos in alumnos.items() if datos["nota"] >= 5]
    if aprobados:
        resultado_label.config(text="\n".join(aprobados))
    else:
        resultado_label.config(text="No hay alumnos aprobados.")

def mostrar_mh():
    mh = [f"{dni} | {datos['apellidos']}, {datos['nombre']} | {datos['nota']} | {datos['calificacion']}" 
          for dni, datos in alumnos.items() if datos["nota"] == 10]
    if mh:
        resultado_label.config(text="\n".join(mh))
    else:
        resultado_label.config(text="No hay candidatos a matrícula de honor.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Calificaciones de Alumnos")
root.geometry("800x500")

# Etiqueta para mostrar los resultados
resultado_label = tk.Label(root, text="", justify="left", anchor="w", width=80, height=15, bg="white", relief="solid")
resultado_label.pack(pady=10)

# Frame para los botones
frame = tk.Frame(root)
frame.pack(pady=10)

# Botones con colores y disposición horizontal
botones = [
    ("Mostrar Alumnos", mostrar_alumnos, "lightpink"),
    ("Introducir Alumno", introducir_alumno, "lightgreen"),
    ("Eliminar Alumno", eliminar_alumno, "lightcoral"),
    ("Consultar Alumno", consultar_alumno, "khaki"),
    ("Modificar Nota", modificar_nota, "lightorange"),
    ("Mostrar Suspensos", mostrar_suspensos, "plum"),
    ("Mostrar Aprobados", mostrar_aprobados, "lightyellow"),
    ("Candidatos a MH", mostrar_mh, "lightsalmon")
]

for idx, (texto, comando, color) in enumerate(botones):
    tk.Button(frame, text=texto, command=comando, width=20, bg=color).grid(row=idx // 4, column=idx % 4, padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()
