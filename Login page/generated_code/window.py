from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 621, y = 488,
    width = 145,
    height = 38)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 771, y = 389,
    width = 80,
    height = 38)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    651.0, 408.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e1cece",
    highlightthickness = 0)

entry0.place(
    x = 555.0, y = 389,
    width = 192.0,
    height = 36)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    693.5, 230.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e1cece",
    highlightthickness = 0)

entry1.place(
    x = 555.0, y = 211,
    width = 277.0,
    height = 36)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    693.5, 319.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e1cece",
    highlightthickness = 0)

entry2.place(
    x = 555.0, y = 300,
    width = 277.0,
    height = 36)

window.resizable(False, False)
window.mainloop()
