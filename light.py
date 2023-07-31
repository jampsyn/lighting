import tkinter as tk
import random

colors = ['blue', 'green', 'yellow', 'red', 'black', 'pink', 'orange', 'brown', 'purple', 'white']

window = tk.Tk()

canvas = tk.Canvas(window, width=500, height=120)
canvas.pack()

lamp1 = canvas.create_oval(40, 40, 100, 100, fill="gray")
lamp2 = canvas.create_oval(140, 40, 200, 100, fill="gray")
lamp3 = canvas.create_oval(240, 40, 300, 100, fill="gray")
lamp4 = canvas.create_oval(340, 40, 400, 100, fill="gray")
lamp5 = canvas.create_oval(440, 40, 500, 100, fill="gray")

color_count = 0

def color():
    global color_count
    color_count += 1
    lamp_colors = []
    for lamp in [lamp1, lamp2, lamp3, lamp4, lamp5]:
        new_color = random.choice(colors)
        canvas.itemconfig(lamp, fill=new_color)
        lamp_colors.append(new_color)
    print("Coloring button pressed:", color_count, "times")
    print("Colors selected:", lamp_colors)

colorbutton = tk.Button(window, text="Coloring", command=color)
colorbutton.pack()

def reset():
    global color_count
    color_count = 0
    canvas.itemconfig(lamp1, fill="gray")
    canvas.itemconfig(lamp2, fill="gray")
    canvas.itemconfig(lamp3, fill="gray")
    canvas.itemconfig(lamp4, fill="gray")
    canvas.itemconfig(lamp5, fill="gray")

resetbutton = tk.Button(window, text="Reset", command=reset)
resetbutton.pack()

window.mainloop()
