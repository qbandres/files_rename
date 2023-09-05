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
ventana.title("Aplicación de Renombrar Archivos")

# Crear un widget Notebook (pestañas)
notebook = tk.ttk.Notebook(ventana)

# Pestaña "rename"
frame_rename = tk.Frame(notebook)
notebook.add(frame_rename, text="Rename")

# Etiqueta y entrada para el nuevo nombre base en la pestaña "rename"
lbl_nuevo_nombre = tk.Label(frame_rename, text="Nuevo Nombre Base:")
lbl_nuevo_nombre.pack()
entry_nuevo_nombre = tk.Entry(frame_rename)
entry_nuevo_nombre.pack()

# Botón para seleccionar archivos en la pestaña "rename"
btn_seleccionar = tk.Button(frame_rename, text="Seleccionar Archivos", command=seleccionar_archivos)
btn_seleccionar.pack()

# Etiqueta para mostrar el estado en la pestaña "rename"
lbl_estado = tk.Label(frame_rename, text="")
lbl_estado.pack()

# Agregar el widget Notebook a la ventana
notebook.pack()

ventana.mainloop()
