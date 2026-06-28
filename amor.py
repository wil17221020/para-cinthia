import tkinter as tk
import math

def dibujar_corazon():
    # Ocultar el botón después de presionarlo
    btn_abrir.destroy()
    
    # Parámetros del corazón
    x_offset = 300
    y_offset = 250
    escala = 15
    
    # Ecuación paramétrica para dibujar el corazón
    puntos = []
    for t in range(0, 629):
        t = t / 100
        x = 16 * math.sin(t)**3
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        puntos.append((x * escala + x_offset, y * escala + y_offset))

    # Dibujar la figura
    canvas.create_polygon(puntos, fill="#FF1493", outline="white", width=3)

    # Añadir el texto
    canvas.create_text(
        300, 250, 
        text="Del odio al amor,\nsolo con mi reina", 
        fill="white", 
        font=("Georgia", 18, "bold"), 
        justify="center"
    )

# Configuración de la ventana principal
root = tk.Tk()
root.title("Una sorpresa para ti")
root.geometry("600x600")
canvas = tk.Canvas(root, width=600, height=600, bg="#4B0082")
canvas.pack()

# Creación del botón "Abrir"
btn_abrir = tk.Button(root, text="Abrir", font=("Arial", 16), command=dibujar_corazon, bg="white", fg="#4B0082")
# Colocamos el botón en el centro del lienzo
canvas.create_window(300, 300, window=btn_abrir)

root.mainloop()