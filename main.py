from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk

BACKGROUND_COLOR = "#F7F7FF"
BUTTON_COLOR = "#279AF1"
EXIT_COLOR = "#C14953"


def exit_program():
    window.destroy()


def watermark_text():
    filename = filedialog.askopenfilename(initialdir='/Desktop', title='Select an Image: ',
                                          filetypes=(("JPG File", "*.jpg"),
                                                     ("PNG file", "*.png"),
                                                     ("All Files", "*.*")))
    img = Image.open(filename)
    width, height = img.size

    draw = ImageDraw.Draw(img)
    text = "Sample Text Watermark"

    font = ImageFont.truetype('arial.ttf', 42)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 100
    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)

    # Save watermarked image
    img.save('watermark.jpg')

    # Show img in gui
    img = Image.open("watermark.jpg")
    img.thumbnail((450, 450))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


def watermark_image():
    filename = filedialog.askopenfilename(initialdir='/Desktop', title='Select an Image: ',
                                          filetypes=(("JPG File", "*.jpg"),
                                                     ("PNG file", "*.png"),
                                                     ("All Files", "*.*")))
    base_image = Image.open(filename)
    watermark = Image.open("water_logo.png")

    base_image.paste(watermark, (100, 100), mask=watermark)
    base_image.save("watermark.jpg")

    img = Image.open("watermark.jpg")
    img.thumbnail((450, 450))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


def result():
    filename = filedialog.askopenfilename(initialdir='/Desktop', title='Select an Image: ',
                                          filetypes=(("JPG File", "*.jpg"),
                                                     ("PNG file", "*.png"),
                                                     ("All Files", "*.*")))
    img = Image.open(filename)
    img.thumbnail((450, 450))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


window = Tk()
window.title("Watermark App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(window, width=700, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(columnspan=3, rowspan=3)


logo = Image.open("logo.png")
logo = logo.resize((400, 400))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bd=0)
logo_label.image = logo
logo_label.grid(column=1, row=1)


lbl = Label(window)
lbl.grid(column=1, row=1)

text_btn = Button(window, text="Mark Text", font=('verdana', 10), width=10, height=1, bg=BUTTON_COLOR, fg='white',
                  command=watermark_text)
text_btn.grid(column=0, row=3)

image_btn = Button(window, text="Mark Image", font=('verdana', 10), width=10, height=1, bg=BUTTON_COLOR, fg='white',
                  command=watermark_image)
image_btn.grid(column=1, row=2)

result_btn = Button(window, text="Show image", font=('verdana', 10), width=10, height=1, bg=BUTTON_COLOR, fg='white',
                  command=result)
result_btn.grid(column=1, row=0)

quit_btn = Button(window, text="Exit", font=('verdana', 10), width=10, height=1, bg=EXIT_COLOR, fg="white", command=exit_program)
quit_btn.grid(column=2, row=3)



window.mainloop()
