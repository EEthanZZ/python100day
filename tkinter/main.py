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
    return sum


print(add(3, 4, 5))


def cal(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


cal(n=3, add=2, mul=5)


class Car:
    def __init__(self, **kwargs):
        self.model = kwargs["make"]
        self.make = kwargs["model"]


my_car = Car(make="Toyota", model="Rav4")
print(my_car.model)

window.mainloop()
