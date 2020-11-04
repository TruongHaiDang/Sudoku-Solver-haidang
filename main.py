import module_vision
# import module_rubik
import tkinter as tk
from tkinter import *
import cube_interactive
import matplotlib.pyplot as plt

vision = module_vision.module_vision(0)
cube_drawing = cube_interactive.Cube(3)
# rubik = module_rubik.module_rubik()


def start_with_camera():
    while True:
        if vision.camera_capture_active():
            break


main_form = tk.Tk()
main_form.title("Rubik Solver")
main_form.geometry("600x600")
main_form.iconbitmap("./img/rubik.ico")
main_form.configure(background="#505160")
main_form.resizable(0, 0)

header_frame = Frame(main_form).pack()
Label(header_frame, text="Rubik Solver", font=('Itim', 28), bg="#505160", fg="#AEBD38").place(x=600 / 3, y=0)
Button(header_frame, text="Start with camera", font=('Itim', 20), bg="#68829E",
       fg="#AEBD38", relief=FLAT, activeforeground="#68829E",
       activebackground="#AEBD38", command=start_with_camera).place(width=600, x=0, y=50)

workspace_frame = Frame(main_form).pack()
crossword0 = Entry(workspace_frame).place(width=30, height=30, x=130, y=120)
crossword1 = Entry(workspace_frame).place(width=30, height=30, x=170, y=120)
crossword2 = Entry(workspace_frame).place(width=30, height=30, x=210, y=120)
crossword3 = Entry(workspace_frame).place(width=30, height=30, x=130, y=160)
crossword4 = Entry(workspace_frame).place(width=30, height=30, x=170, y=160)
crossword5 = Entry(workspace_frame).place(width=30, height=30, x=210, y=160)
crossword6 = Entry(workspace_frame).place(width=30, height=30, x=130, y=200)
crossword7 = Entry(workspace_frame).place(width=30, height=30, x=170, y=200)
crossword8 = Entry(workspace_frame).place(width=30, height=30, x=210, y=200)

crossword9 = Entry(workspace_frame).place(width=30, height=30, x=10, y=240)
crossword10 = Entry(workspace_frame).place(width=30, height=30, x=50, y=240)
crossword11 = Entry(workspace_frame).place(width=30, height=30, x=90, y=240)
crossword12 = Entry(workspace_frame).place(width=30, height=30, x=10, y=280)
crossword13 = Entry(workspace_frame).place(width=30, height=30, x=50, y=280)
crossword14 = Entry(workspace_frame).place(width=30, height=30, x=90, y=280)
crossword15 = Entry(workspace_frame).place(width=30, height=30, x=10, y=320)
crossword16 = Entry(workspace_frame).place(width=30, height=30, x=50, y=320)
crossword17 = Entry(workspace_frame).place(width=30, height=30, x=90, y=320)

crossword18 = Entry(workspace_frame).place(width=30, height=30, x=130, y=240)
crossword19 = Entry(workspace_frame).place(width=30, height=30, x=170, y=240)
crossword20 = Entry(workspace_frame).place(width=30, height=30, x=210, y=240)
crossword21 = Entry(workspace_frame).place(width=30, height=30, x=130, y=280)
crossword22 = Entry(workspace_frame).place(width=30, height=30, x=170, y=280)
crossword23 = Entry(workspace_frame).place(width=30, height=30, x=210, y=280)
crossword24 = Entry(workspace_frame).place(width=30, height=30, x=130, y=320)
crossword25 = Entry(workspace_frame).place(width=30, height=30, x=170, y=320)
crossword26 = Entry(workspace_frame).place(width=30, height=30, x=210, y=320)

crossword27 = Entry(workspace_frame).place(width=30, height=30, x=250, y=240)
crossword28 = Entry(workspace_frame).place(width=30, height=30, x=290, y=240)
crossword29 = Entry(workspace_frame).place(width=30, height=30, x=330, y=240)
crossword30 = Entry(workspace_frame).place(width=30, height=30, x=250, y=280)
crossword31 = Entry(workspace_frame).place(width=30, height=30, x=290, y=280)
crossword32 = Entry(workspace_frame).place(width=30, height=30, x=330, y=280)
crossword33 = Entry(workspace_frame).place(width=30, height=30, x=250, y=320)
crossword34 = Entry(workspace_frame).place(width=30, height=30, x=290, y=320)
crossword35 = Entry(workspace_frame).place(width=30, height=30, x=330, y=320)

crossword36 = Entry(workspace_frame).place(width=30, height=30, x=370, y=240)
crossword37 = Entry(workspace_frame).place(width=30, height=30, x=410, y=240)
crossword38 = Entry(workspace_frame).place(width=30, height=30, x=450, y=240)
crossword39 = Entry(workspace_frame).place(width=30, height=30, x=370, y=280)
crossword40 = Entry(workspace_frame).place(width=30, height=30, x=410, y=280)
crossword41 = Entry(workspace_frame).place(width=30, height=30, x=450, y=280)
crossword42 = Entry(workspace_frame).place(width=30, height=30, x=370, y=320)
crossword43 = Entry(workspace_frame).place(width=30, height=30, x=410, y=320)
crossword44 = Entry(workspace_frame).place(width=30, height=30, x=450, y=320)

crossword45 = Entry(workspace_frame).place(width=30, height=30, x=130, y=360)
crossword46 = Entry(workspace_frame).place(width=30, height=30, x=170, y=360)
crossword47 = Entry(workspace_frame).place(width=30, height=30, x=210, y=360)
crossword48 = Entry(workspace_frame).place(width=30, height=30, x=130, y=400)
crossword49 = Entry(workspace_frame).place(width=30, height=30, x=170, y=400)
crossword50 = Entry(workspace_frame).place(width=30, height=30, x=210, y=400)
crossword51 = Entry(workspace_frame).place(width=30, height=30, x=130, y=440)
crossword52 = Entry(workspace_frame).place(width=30, height=30, x=170, y=440)
crossword53 = Entry(workspace_frame).place(width=30, height=30, x=210, y=440)

result = StringVar()
result.set("result")
Label(header_frame, textvariable=result, font=('Itim', 28), bg="#505160", fg="yellow").place(x=600 / 2.5, y=500)

main_form.mainloop()

# cube_drawing.draw_interactive()
# plt.show()
