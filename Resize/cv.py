import cv2
import glob
import os

# Ruta donde están las imágenes
ruta_imagenes = "imgs/*.jpg"  # Cambia la extensión según tus imágenes
ruta_salida = 'resize_imgs/'  # Ruta donde guardar las imágenes redimensionadas

# Crear la carpeta de salida si no existe
os.makedirs(ruta_salida, exist_ok=True)

# Leer todas las imágenes en la ruta especificada
imagenes = [cv2.imread(imagen) for imagen in glob.glob(ruta_imagenes)]

# Redimensionar y guardar las imágenes
for i, img in enumerate(imagenes):
    # Redimensionar la imagen a 100x100
    img_redimensionada = cv2.resize(img, (100, 100))
    
    # Guardar la imagen redimensionada
    nombre_archivo = os.path.basename(glob.glob(ruta_imagenes)[i])  # Obtener el nombre del archivo original
    cv2.imwrite(os.path.join(ruta_salida, nombre_archivo), img_redimensionada)

print("Imágenes redimensionadas y guardadas en:", ruta_salida)