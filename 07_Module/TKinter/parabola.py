from tkinter import *
import math

def circle(canvas: Canvas, r: int, g: int, h: int, color='red'):
    """Draw a circle on canvas

    Args:
        canvas (Canvas): The canvas to draw the graph.
        r (int): The radius of the circle
        g (int): 圓心的x座標
        h (int): 圓心的y座標
    """
    h *= -1
    canvas.create_oval(g + r, h + r, g - r, h - r, outline=color, width=2)
    # for i in range(g - r, g + r):
    #     x0 = i
    #     y0 = math.sqrt(r ** 2 - (x0 - g) ** 2) + h
    #     x1 = i + 1
    #     y1 = math.sqrt((r ** 2) - ((x1 - g) ** 2)) + h
    #     draw_line(canvas, x0, y0, x1, y1)
    #     y0b = y0 - 2 * (y0 - h)
    #     y1b = y1 - 2 * (y1 - h)
    #     draw_line(canvas, x0, y0b, x1, y1b)        


def parabola(canvas: Canvas, size: int):
    for i in range(size + 1):
        x0 = i
        y0 = x0 ** 2 / size
        x1 = i + 1
        y1 = x1 ** 2 / size
        draw_line(canvas, x0, y0, x1, y1)
        draw_line(canvas, -x0, y0, -x1, y1)


def draw_axis(canvas: Canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.config(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(x_origin, 0, -x_origin, 0, fill='black')
    canvas.create_line(0, y_origin, 0, -y_origin, fill='black')


def draw_line(canvas: Canvas, x0: int, y0: int, x1: int, y1: int):
    canvas.create_line(x0, -y0, x1, -y1, fill='red')


mainWindow = Tk()
mainWindow.title('Parablola')
mainWindow.geometry('640x480')

mainCanvas = Canvas(mainWindow, width=640, height=480)
mainCanvas.grid(column=0, row=0)

draw_axis(mainCanvas)

# for i in range(1, 100):
#     parabola(mainCanvas, i)
circle(mainCanvas, 125, 50, 50, 'blue')

mainWindow.mainloop()