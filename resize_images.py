#%%
import os
import os.path
from PIL import Image
import shutil

def resizing(f,f_saved):
    """
    recibe dos rutas como parámetros, donde se encuentran las imágenes a utilizar
    y les realiza un resizing, ya hardcodeado en 50x50 pixels
    """
    for file in os.listdir(f):
        f_img = f + "/" + file
        f_img_save = f_saved + "/" + file
        img = Image.open(f_img)
        img = img.resize((80,80))
        f_img_save = f_img_save.strip(".jpg") + ".png" if ".jpg" in f_img_save else f_img_save
        img.save(f_img_save)
        shutil.move(r'Sin procesar' + '\\' + file,r'Ya usado y procesado' + '\\' + file )

f_SP = r'C:\Users\Lucia\Desktop\Ingeniería biomédica\Algoritmos 1\Imagenes\Sin procesar'
f_saved = r'C:\Users\Lucia\Desktop\Ingeniería biomédica\Algoritmos 1\Imagenes\Procesadas'

#resizing(f_SP,f_saved)
# %%
