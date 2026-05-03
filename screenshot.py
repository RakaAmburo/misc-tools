import pyscreenshot as ImageGrab
import sys

# Toma el nombre del archivo como parámetro o usa default
nombre = sys.argv[1] if len(sys.argv) > 1 else "captura.png"

# Captura pantalla completa
img = ImageGrab.grab()
img.save("/home/pablo/Images/" + nombre)

# Seleccionar área: bbox = (x1, y1, x2, y2)
# img = ImageGrab.grab(bbox=(100, 100, 800, 600))
