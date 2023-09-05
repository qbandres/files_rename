import tkinter as tk
from tkinter import filedialog
import os

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(
        title="Selecciona archivos para renombrar",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivos:
        # Obtener el nuevo nombre base del usuario
        nuevo_nombre_base = entry_nuevo_nombre.get()
        
        # Carpeta de destino (la misma carpeta donde están los archivos originales)
        carpeta_destino = os.path.dirname(archivos[0])
        
        # Ciclo para renombrar los archivos
        for i, archivo_original in enumerate(archivos):
            nombre, extension = os.path.splitext(archivo_original)
            nuevo_nombre = f"{nuevo_nombre_base}_{i+1}{extension}"
            nuevo_path = os.path.join(carpeta_destino, nuevo_nombre)
            
            # Renombrar el archivo
            os.rename(archivo_original, nuevo_path)
        
        lbl_estado.config(text="Archivos renombrados exitosamente")

# Crear la ventana de tkinter
ventana = tk.Tk()
ventana.title("Renombrar Archivos")

# Etiqueta y entrada para el nuevo nombre base
lbl_nuevo_nombre = tk.Label(ventana, text="Nuevo Nombre Base:")
lbl_nuevo_nombre.pack()
entry_nuevo_nombre = tk.Entry(ventana)
entry_nuevo_nombre.pack()

# Botón para seleccionar archivos
btn_seleccionar = tk.Button(ventana, text="Seleccionar Archivos", command=seleccionar_archivos)
btn_seleccionar.pack()

# Etiqueta para mostrar el estado
lbl_estado = tk.Label(ventana, text="")
lbl_estado.pack()

ventana.mainloop()
