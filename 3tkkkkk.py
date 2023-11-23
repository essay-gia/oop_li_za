import tkinter
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
#
# # # кнопочка тык
# # def clickknopka():
# #     label["text"] = txt.get()
#
# # новое окно для добавления новой машинки
# def neww():
#     newwc=Tk()
#     newwc.title("Добавление нового автомобиля")
#     newwc.geometry("500x400")
#     newwc.configure(bg="khaki")
#
#     def clickknopka():
#         label["text"] = txt.get()
#
#     # res= "Ввод номера автомобиля {}".format(txt.get())
#     # lbl.configure(text=res)
#     lbl = Label(newwc, text="Номер автомобиля:",fg="gray42",bg="honeydew3")
#     lbl.place(x=10, y=50)
#     txt = ttk.Entry(newwc, width=10)
#     txt.place(x=165, y=50)
#     click=ttk.Button(text="Click", command=clickknopka)
#     click.place(x=200, y=50)
#     label = ttk.Label()
#     label.place(x=200, y=50)
#
#     newwc.mainloop()
#
#
# # главное окно
# window = Tk()
# window.title("Добро пожаловать в автопарк")
# window.geometry('600x500')
# window.configure(bg="palegoldenrod")
# nad=Label(window, text="Добро пожаловать в автопарк!",font=("Times New Roman",20), bg="khaki3", fg="gray40").pack(side='top')
#
#
# # добавление новой машинки нажатием на картинку
# newcar= 'newcar.jpg'
# new=Image.open(newcar)
# newcar=ImageTk.PhotoImage(new)
# Button(window, image=newcar, command=neww).place(x=10, y=110)
# dob=Label(window, text="Добавление машины", font=("Times New Roman",10),bg="papayawhip",fg="gray36").place(x=10,y=80)
#
#
#
#
#
# # lbl=Label(window, text="")
# # lbl.grid(column=1,row=0)
# # proba=Button(window, text='Тык, чтобы начать',command=clicked, bg="pink", fg="black")
# # proba.grid(column=0, row=0)
#
# window.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Car:
    def __init__(self, number, make, model, year, dvigat, horse, color, expense, windows, doors, brake, kasko):
        self.number = number
        self.make = make
        self.model = model
        self.year = year
        self.dvigat = dvigat
        self.horse = horse
        self.color = color
        self.expense = expense
        self.windows = windows
        self.doors = doors
        self.brake = brake
        self.kasko = kasko

cars = []

def add_car(number, make, model, year, dvigat, horse, color, expense, windows, doors, brake, kasko):
    car = Car(number, make, model, year,dvigat, horse, color, expense, windows, doors, brake, kasko)
    cars.append(car)

def open_new_window():
    new_window = Toplevel(window)
    new_window.title("Добавление новой машины")
    new_window.geometry("400x500")
    new_window.configure(bg="khaki")

    lbl = Label(new_window, text="Номер автомобиля:", fg="gray42", bg="honeydew3")
    lbl.place(x=10, y=50)
    txt_number = ttk.Entry(new_window, width=10)
    txt_number.place(x=165, y=50)

    lbl_make = Label(new_window, text="Марка:", fg="gray42", bg="honeydew3")
    lbl_make.place(x=10, y=80)
    txt_make = ttk.Entry(new_window, width=10)
    txt_make.place(x=165, y=80)

    lbl_model = Label(new_window, text="Модель:", fg="gray42", bg="honeydew3")
    lbl_model.place(x=10, y=110)
    txt_model = ttk.Entry(new_window, width=10)
    txt_model.place(x=165, y=110)

    lbl_year = Label(new_window, text="Год выпуска:", fg="gray42", bg="honeydew3")
    lbl_year.place(x=10, y=140)
    txt_year = ttk.Entry(new_window, width=10)
    txt_year.place(x=165, y=140)
    label = ttk.Label()

    lbl_dvigat = Label(new_window, text="Объем двигателя:", fg="gray42", bg="honeydew3")
    lbl_dvigat.place(x=10, y=170)
    txt_dvigat = ttk.Entry(new_window, width=10)
    txt_dvigat.place(x=165, y=170)

    lbl_horse = Label(new_window, text="Количество л.с.:", fg="gray42", bg="honeydew3")
    lbl_horse.place(x=10, y=200)
    txt_horse = ttk.Entry(new_window, width=10)
    txt_horse.place(x=165, y=200)

    lbl_color = Label(new_window, text="Цвет автомобиля:", fg="gray42", bg="honeydew3")
    lbl_color.place(x=10, y=230)
    txt_color = ttk.Entry(new_window, width=10)
    txt_color.place(x=165, y=230)

    lbl_expense = Label(new_window, text="Расход топлива:", fg="gray42", bg="honeydew3")
    lbl_expense.place(x=10, y=260)
    txt_expense = ttk.Entry(new_window, width=10)
    txt_expense.place(x=165, y=260)

    lbl_windows = Label(new_window, text="Положение окон:", fg="gray42", bg="honeydew3")
    lbl_windows.place(x=10, y=290)
    txt_windows = ttk.Entry(new_window, width=10)
    txt_windows.place(x=165, y=290)

    lbl_doors = Label(new_window, text="Положение дверей:", fg="gray42", bg="honeydew3")
    lbl_doors.place(x=10, y=320)
    txt_doors = ttk.Entry(new_window, width=10)
    txt_doors.place(x=165, y=320)

    lbl_brake = Label(new_window, text="Ручной тормоз:", fg="gray42", bg="honeydew3")
    lbl_brake.place(x=10, y=350)
    txt_brake = ttk.Entry(new_window, width=10)
    txt_brake.place(x=165, y=350)

    lbl_kasko = Label(new_window, text="Каско:", fg="gray42", bg="honeydew3")
    lbl_kasko.place(x=10, y=380)
    txt_kasko = ttk.Entry(new_window, width=10)
    txt_kasko.place(x=165, y=380)



    def clickknopka():
        add_car(txt_number.get(), txt_make.get(), txt_model.get(), txt_year.get(), txt_dvigat.get(), txt_horse.get(), txt_color.get(), txt_expense.get(), txt_windows.get(), txt_doors.get(), txt_brake.get(), txt_kasko.get())
        label["text"] = "Машина добавлена: " + txt_number.get()

    click = ttk.Button(new_window, text="Добавить", command=clickknopka)
    click.place(x=270, y=390)

def open_all_window():
    all_window = Toplevel(window)
    all_window.title("Список всех машин")
    all_window.geometry("400x400")
    all_window.configure(bg="khaki")

    lbl = Label(all_window, text="Список всех машин:", fg="gray42", bg="honeydew3")
    lbl.pack()

    for car in cars:
        car_info = f"Номер: {car.number}; \n Марка: {car.make}; \n Модель: {car.model}; \n Год: {car.year}; \n Объем двигателя: {car.dvigat}; \n Количество л. с.: {car.horse}: \n Цвет автомобиля: {car.color}: \n Расход топлива: {car.expense}; \n Положение окон: {car.windows}; \n Положение дверей: {car.doors}; \n Ручной тормоз: {car.brake}; \n Каско: {car.kasko} \n\n\n"
        lbl_car = Label(all_window, text=car_info, fg="gray42", bg="blanchedalmond")
        lbl_car.pack()


def open_create_window():
    create_window = Toplevel(window)
    create_window.title("Изменение машин")
    create_window.geometry("400x500")
    create_window.configure(bg="khaki")

    lbl = Label(create_window, text="Выберите машину по номеру:", fg="gray42", bg="honeydew3")
    lbl.place(x=10, y=50)
    selected_number = ttk.Combobox(create_window, values=[car.number for car in cars])
    selected_number.place(x=190, y=50)

    lbl_make = Label(create_window, text="Новая марка:", fg="gray42", bg="honeydew3")
    lbl_make.place(x=10, y=80)
    txt_make = ttk.Entry(create_window, width=10)
    txt_make.place(x=190, y=80)

    lbl_model = Label(create_window, text="Новая модель:", fg="gray42", bg="honeydew3")
    lbl_model.place(x=10, y=110)
    txt_model = ttk.Entry(create_window, width=10)
    txt_model.place(x=190, y=110)

    lbl_year = Label(create_window, text="Новый год выпуска:", fg="gray42", bg="honeydew3")
    lbl_year.place(x=10, y=140)
    txt_year = ttk.Entry(create_window, width=10)
    txt_year.place(x=190, y=140)

    lbl_dvigat = Label(create_window, text="Новый объем двигателя:", fg="gray42", bg="honeydew3")
    lbl_dvigat.place(x=10, y=170)
    txt_dvigat = ttk.Entry(create_window, width=10)
    txt_dvigat.place(x=190, y=170)

    lbl_horse = Label(create_window, text="Новое количество л.с.:", fg="gray42", bg="honeydew3")
    lbl_horse.place(x=10, y=200)
    txt_horse = ttk.Entry(create_window, width=10)
    txt_horse.place(x=190, y=200)

    lbl_color = Label(create_window, text="Новый цвет машины:", fg="gray42", bg="honeydew3")
    lbl_color.place(x=10, y=230)
    txt_color = ttk.Entry(create_window, width=10)
    txt_color.place(x=190, y=230)

    lbl_expense = Label(create_window, text="Новый расход топлива:", fg="gray42", bg="honeydew3")
    lbl_expense.place(x=10, y=260)
    txt_expense = ttk.Entry(create_window, width=10)
    txt_expense.place(x=190, y=260)

    lbl_windows = Label(create_window, text="Новое положение окон:", fg="gray42", bg="honeydew3")
    lbl_windows.place(x=10, y=290)
    txt_windows = ttk.Entry(create_window, width=10)
    txt_windows.place(x=190, y=290)

    lbl_doors = Label(create_window, text="Новое положение дверей:", fg="gray42", bg="honeydew3")
    lbl_doors.place(x=10, y=320)
    txt_doors = ttk.Entry(create_window, width=10)
    txt_doors.place(x=190, y=320)

    lbl_brake = Label(create_window, text="Новое положение ручного тормоза:", fg="gray42", bg="honeydew3")
    lbl_brake.place(x=10, y=350)
    txt_brake = ttk.Entry(create_window, width=10)
    txt_brake.place(x=190, y=350)

    lbl_kasko = Label(create_window, text="Новый статус Каско:", fg="gray42", bg="honeydew3")
    lbl_kasko.place(x=10, y=380)
    txt_kasko = ttk.Entry(create_window, width=10)
    txt_kasko.place(x=190, y=380)


    label = ttk.Label()

    def click_create():
        for car in cars:
            if car.number == selected_number.get():
                car.make = txt_make.get()
                car.model = txt_model.get()
                car.year = txt_year.get()
                label["text"] = f"Характеристики машины {car.number} изменены"

    click_create = ttk.Button(create_window, text="Изменить", command=click_create)
    click_create.place(x=270, y=400)


window = Tk()
window.title("Добро пожаловать в автопарк")
window.geometry('600x500')
window.configure(bg="palegoldenrod")
nad = Label(window, text="Добро пожаловать в автопарк!", font=("Times New Roman", 20), bg="khaki3", fg="gray40").pack(side='top')

newcar = 'newcar.jpg'
new = Image.open(newcar)
newcar = ImageTk.PhotoImage(new)

allcar = 'allcar.jpg'
new = Image.open(allcar)
allcar = ImageTk.PhotoImage(new)

creatcar = 'creat.jpg'
new = Image.open(creatcar)
creatcar = ImageTk.PhotoImage(new)

Button(window, image=newcar, command=open_new_window).place(x=10, y=110)
dob = Label(window, text="Добавление машины", font=("Times New Roman", 10), bg="papayawhip", fg="gray36").place(x=10,y=80)

Button(window, image=allcar, command=open_all_window).place(x=170, y=110)
dob = Label(window, text="Список машин", font=("Times New Roman", 10), bg="papayawhip", fg="gray36").place(x=180,y=80)

Button(window, image=creatcar, command=open_create_window).place(x=320, y=110)
dob = Label(window, text="Изменение машин", font=("Times New Roman", 10), bg="papayawhip", fg="gray36").place(x=310,y=80)
window.mainloop()


import unittest

class TestCarFunctions(unittest.TestCase):
    def test_add_multiple_cars(self):
        add_car("A591KM", "Ford", "Focus", "2022", "1.6L", "120", "синий", "7L/100км", "опущены", "открыты", "выключен", "нет")
        add_car("X723MC", "Honda", "Civic", "2023", "1.8L", "140", "серебристый", "6.5L/100км", "подняты", "закрыты", "включен", "да")
        self.assertEqual(len(cars), 3)
        self.assertEqual(cars[1].make, "Honda")

    def test_add_invalid_car(self):
        add_car("33333", "", "Accord", "2021", "2.0L", "190", "красный", "7.5L/100км", "опущены", "закрыты", "выключен", "нет")
        self.assertEqual(len(cars), 2)










