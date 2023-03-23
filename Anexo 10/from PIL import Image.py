from PIL import Image
import numpy as np

# Definir el tamaño de la imagen y la escala de valores
size = (256, 256)
min_val = 20
max_val = 45

# Crear una matriz con los valores de la escala de colores
x, y = np.meshgrid(np.linspace(0, 1, size[0]), np.linspace(0, 1, size[1]))
value_range = np.linspace(min_val, max_val, size[0])
value_mat = np.tile(value_range, (size[1], 1)).T
rgb_mat = np.zeros((size[0], size[1], 3))
rgb_mat[:, :, 0] = np.interp(value_mat, [min_val, max_val], [0, 1]) * (y**2) * 255 # R
rgb_mat[:, :, 1] = np.interp(value_mat, [min_val, max_val], [0, 1]) * (1-y) * (1-x) * 255 # G
rgb_mat[:, :, 2] = np.interp(value_mat, [min_val, max_val], [0, 1]) * x**2 * 255 # B

# Convertir la matriz en una imagen y guardarla en formato png
img = Image.fromarray(rgb_mat.astype(np.uint8))
img.save('escala_de_colores.png')