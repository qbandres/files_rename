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


from tkinter import filedialog
import os
import csv

#Funciones para el listado de files
def listar_documentos(carpeta):
    documentos = []
    for root, _, files in os.walk(carpeta):
        for file in files:
            documentos.append(file)
    return documentos

def generar_csv(carpeta, archivo_csv):
    documentos = listar_documentos(carpeta)
    with open(archivo_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Numero","Documento"])
        for i, documento in enumerate(documentos,start=1):
            csvwriter.writerow([i,documento])

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    carpeta_seleccionada.set(carpeta)

def guardar_csv():
    carpeta = carpeta_seleccionada.get()
    if carpeta:
        archivo_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        if archivo_csv:
            generar_csv(carpeta, archivo_csv)
            mensaje_estado.set("CSV generado con éxito.")

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


#Codigo primera pestaña
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

#codigo segunda pestaña

carpeta_seleccionada = tk.StringVar()
mensaje_estado = tk.StringVar()


tk.Label(my_frame2, text="Carpeta:").grid(row=0, column=0)
tk.Entry(my_frame2, textvariable=carpeta_seleccionada).grid(row=0, column=1)
tk.Button(my_frame2, text="Seleccionar Carpeta", command=seleccionar_carpeta).grid(row=0, column=2)

tk.Button(my_frame2, text="Generar CSV", command=guardar_csv).grid(row=1, column=0, columnspan=3)

tk.Label(root, textvariable=mensaje_estado).pack()

root.mainloop()
