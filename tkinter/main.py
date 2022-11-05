import tkinter

window = tkinter.Tk()
window.title("Window 1")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="label 1", font=("Arial", 24, "bold"))
my_label.pack(side="left")


def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(3,4,5)











window.mainloop()