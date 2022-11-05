import tkinter

window = tkinter.Tk()
window.title("Window 1")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="label 1", font=("Arial", 24, "bold"))
my_label.pack(side="top")


my_label["text"] = "XXXXXX"


def button_click():
    my_label.config(text="YYYYYY")


button = tkinter.Button(text="button", command=button_click)
button.pack()



def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(3, 4, 5))


def cal(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


cal(n=3, add=2, mul=5)


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")


my_car = Car(make="1010", model="ccc")
print(my_car.make)

window.mainloop()
