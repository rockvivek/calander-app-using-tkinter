#calendar program in python..........

from tkinter import *
import calendar as c

def showCal():
    new_window = Tk()
    new_window.config(background = 'white')
    new_window.title("Calendar")
    new_window.geometry('550x600')
    fetch_year = int(year_field.get())
    print(fetch_year)
    cal_content = c.calendar(fetch_year,2,1,6)
    cal_year  = Label(new_window,text=cal_content,font = "Consolas 14 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_window.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.config(background = "white")
    root.title("Home")
    root.geometry("500x400")

    cal = Label(root,text="Welcome to Calendar Application",font=("times",20,'bold'))

    year = Label(root,text="Pleace enter a year",font=("times",10,'bold'))

    year_field = Entry(root)

    show = Button(root,text = "show Calendar",fg ="Black",bg="light Green"
                  ,command=showCal)
    exit = Button(root,text = "Exit",fg ="Black",bg="light Green"
                  ,command=root.quit)

    cal.place(x=0,y=0)

    year.place(x=40,y=70)

    year_field.place(x=170,y=70)

    show.place(x=80,y=110)

    exit.place(x=190,y=110)

    root.mainloop()