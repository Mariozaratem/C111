import os
import shutil

from_dir = r"C:\\Users\\mzara\\OneDrive\\Documentos\\BYJU\\Python\\Python 4\\Imagenes_Archivos"
to_dir = r"C:\\Users\\mzara\\OneDrive\\Documentos\\BYJU\\Python\\Python 4\\Documentos_Archivos"

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    file_path = os.path.join(from_dir, file)  # Ruta completa del archivo de origen
    destination_path = os.path.join(to_dir, file)  # Ruta completa del archivo de destino
    shutil.move(file_path, destination_path)

print("Archivos movidos correctamente.")