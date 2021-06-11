from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
import excelProcessing as ep
import staticMaping as sm
import gps as gps
import geo as geo


class map(tk.Tk):

    def __init__(self):
        super().__init__()

        self.name_var = tk.StringVar()

        # configure the root window
        self.title('UniNode')
        self.geometry('600x600')
        self.configure(background="white")

        # uniNode logo
        self.logo = ImageTk.PhotoImage(Image.open("D:/Users/afent/Desktop/techProjectMap/logo/logo.png"))
        self.logo_label = Label(image=self.logo)
        self.logo_label.pack()

        # University Information Map title
        self.custFont = Font(
            family="Helvetica",
            size=24,
            weight="bold"
        )
        self.title = Label(text="University Information Map", font=self.custFont, fg="#800000")
        self.title.place(x=107, y=130)

        # Univeristy Map
        my_img2 = Image.open("papaCirlce.pillow.png")
        resize_image = my_img2.resize((360, 280))
        self.img = ImageTk.PhotoImage(resize_image)
        self.vlabel = tk.Label(self, image=self.img)
        self.vlabel.place(x=10, y=200)

        # Search Classroom
        self.lClassroom = Label(text="Search Classroom", width=18, height=2, fg="#800000")
        self.lClassroom.place(x=380, y=270)
        self.eClassroom = Entry(textvariable=self.name_var, bd=5)
        self.eClassroom.place(x=380, y=300)
        self.sub_btn = tk.Button(text='Submit', command=self.submit)
        self.sub_btn.place(x=520, y=300)

        # station Button
        self.station_btn = Button(self, text="Search Station", width=18, height=2, fg="#800000", command=self.station_button)
        self.station_btn.place(x=380, y=360)

        # quit button
        self.button_quit = Button(self, text="Exit Program", width=18, height=2, fg="#800000", command=self.quit)
        self.button_quit.place(x=220, y=500)

    def submit(self):
        classroom = self.name_var.get()
        self.name_var.set("")
        df = ep.initialize(which=0)     #read classroom excel
        l, r = ep.searchingByName(classroom, df)
        if l is not None:
            sm.staticmap(l, r)
            self.showMap()
        else:
            warning = "The Classroom \"" + classroom + "\" you searched does not exists"
            messagebox.askretrycancel("404 classroom", warning)

    def showMap(self):
        new = Image.open("spot.pillow.png")
        rz = new.resize((360, 280))
        self.imgn = ImageTk.PhotoImage(rz)
        # ml = tk.Label(image=screen.imgn)
        # ml.place(x=70, y=250)
        self.vlabel.configure(image=self.imgn)

    def station_button(self):

        longUser, latUser, distance = gps.gps()
#############################################################################################
#######################Test Bench IF we were inside PAPA#####################################
#############################################################################################
        longUser, latUser = 38.28424, 21.78855

        if longUser is None:
            error = "You are " + str(round(distance,2)) + "km away from University of Patras "
            messagebox.showerror("error", error)

        else:
            info = "You are inside the area of University of Patras"
            messagebox.showinfo("info", info)

            station = "ΠΑΙΔΑΓΩΓΙΚΟ"
            df = ep.initialize(which=1)  # read busStation excel

            coordinatesList = ep.getTheList(df)
            # print(coordinatesList)

            v = {'lat': longUser, 'lon': latUser}
            closestStation = geo.closest(coordinatesList, v)
            # print(closestStation)
            # print(closestStation['name'])
            # print(type(closestStation['name']))

            l, r = ep.searchingByName(closestStation['name'], df)
            sm.staticmapRoute(l, r, longUser, latUser)
            self.showMap()
            messagebox.showinfo("info", "Closest station is " + closestStation['name'])


if __name__ == "__main__":
    app = map()
    app.mainloop()