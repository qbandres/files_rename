import tkinter as tk
from tkinter import ttk
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
root = tk.Tk()
root.title("Renombrar Archivos")
root.geometry("380x420+560+240")

# Se configura la funcion para crear la pestaña
my_notebook = ttk.Notebook(root,width=500,height = 500)
my_notebook.pack()

#Se confirgua la primera pestaña
my_frame1 = tk.Frame(my_notebook)
my_frame1.pack(fill = 'both',expand=1)
my_notebook.add(my_frame1,text='rename_files')

#Se confirgua la segunda pestaña
my_frame2 = tk.Frame(my_notebook)
my_frame2.pack(fill = 'both',expand=1)
my_notebook.add(my_frame2,text='list_files')

# Etiqueta y entrada para el nuevo nombre base
lbl_nuevo_nombre = tk.Label(my_frame1, text="Nuevo Nombre Base:")
lbl_nuevo_nombre.pack()
entry_nuevo_nombre = tk.Entry(my_frame1)
entry_nuevo_nombre.pack()

# Botón para seleccionar archivos
btn_seleccionar = tk.Button(my_frame1, text="Seleccionar Archivos", command=seleccionar_archivos)
btn_seleccionar.pack()

# Etiqueta para mostrar el estado
lbl_estado = tk.Label(my_frame1, text="")
lbl_estado.pack()

root.mainloop()
