import tkinter

window = tkinter.Tk()
window.title("Window 1")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

my_label = tkinter.Label(text="label 1", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


my_label["text"] = "XXXXXX"


def button_click():
    new_text = input_text.get()
    my_label.config(text=new_text)
    with open("file1.txt", mode="a") as file:
        file.write(f'{new_text}\n')


button = tkinter.Button(text="button", command=button_click)
button.grid(column=1, row=1)
button_2 = tkinter.Button(text="button2", command=button_click)
button_2.grid(column=2, row=0)

input_text = tkinter.Entry(width=20)
input_text.grid(column=3, row=2)



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
