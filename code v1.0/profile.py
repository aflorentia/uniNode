from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import csv

class Profile:
    def delete1(self):
        screen2.destroy()
    
    def delete2(self):
        screen3.destroy()



    def cn(self):
        nc = sirname_entry.get()
        nm = surname
        text = open('C:\\Users\\Στελιος\\Desktop\\TN\\profiles.csv', "r")
        text = ''.join([i for i in text]) \
                .replace(nm, nc)
        x = open('C:\\Users\\Στελιος\\Desktop\\TN\\profiles.csv',"w")
        x.writelines(text)
        x.close()
        self.delete1()
    def name_change(self):
        global screen2
        screen2 = Toplevel(screen)
        screen2.title("Edit")
        screen2.geometry("250x250")
        screen2.configure(background="white")
        nc=StringVar()
        global sirname_entry


        Label(screen2, text = "Please enter the name you wish to use",background="white").pack()
        Label(screen2, text = "",background="white").pack()
        Label(screen2, text = "Sirname * ",background="white").pack()
        sirname_entry = Entry(screen2, textvariable = nc)
        sirname_entry.pack()
        Label(screen2, text = "",background="white").pack()
        Button(screen2, text = "Done", width = 8 ,height = 2 ,fg ="#800000", command = self.cn).pack()
    def dc(self):
        nc = depname_entry.get()
        nm = dep
        text = open('C:\\Users\\Στελιος\\Desktop\\TN\\profiles.csv', "r")
        text = ''.join([i for i in text]) \
                .replace(nm, nc)
        x = open('C:\\Users\\Στελιος\\Desktop\\TN\\profiles.csv',"w")
        x.writelines(text)
        x.close()
        self.delete2()
    def dep_change(self):
        global screen3
        screen3 = Toplevel(screen)
        screen3.title("Edit Department")
        screen3.geometry("250x250")
        screen3.configure(background="white")
        dc=StringVar()
        global depname_entry


        Label(screen3, text = "Please enter the Department",background="white").pack()
        Label(screen3, text = "",background="white").pack()
        Label(screen3, text = "Department * ",background="white").pack()
        depname_entry = Entry(screen3, textvariable = dc)
        depname_entry.pack()
        Label(screen3, text = "",background="white").pack()
        Button(screen3, text = "Done", width = 8 ,height = 2 ,fg ="#800000", command = self.dc).pack()
        

    def main_screen(self,username):
        global screen
        global custFont
        global my_img
        global user
        global pic
        global surname
        global dep
        global friends
        screen = Tk()
        screen.geometry("600x600")
        screen.configure(background = "white")
        screen.title("Profile")
        custFont =Font(
        family = "Helvetica",
        size = 16,
        weight = "bold"
        )
        screen.iconbitmap("C:\\Users\\Στελιος\\Desktop\\TN\\logo.ico")
        my_img=ImageTk.PhotoImage(Image.open("C:\\Users\\Στελιος\\Desktop\\TN\\logo.png"))
        my_label=Label(image=my_img,background="white")
        my_label.pack()
        with open('C:\\Users\\Στελιος\\Desktop\\TN\\profiles.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
      
            for row in reader:
                if row["username"]==username:
                    pic = row["picture"]
                    surname = row["Surname"]
                    user = row["Name"]
                    dep = row["Department"]
                    friends = row["Friends"]
                else:
                    print("error")
        Label(text="",background="white").pack()
        my_img1=Image.open(pic)
        image = my_img1.resize((150, 150), Image.ANTIALIAS)
        my_img1 = ImageTk.PhotoImage(image)
        my_label1=Label(image=my_img1,background="white")
        my_label1.pack()
        my_label1.place(relx = 0.0,
                  rely = 0.2)
        Label(text="",background="white").pack()
        Label(text="Name: "+user,background="white",font=custFont).pack()
        Label(text="",background="white").pack()
        Label(text="Sirname: "+surname,background="white",font=custFont).pack()
        Label(text="",background="white").pack()
        Label(text="Department: "+dep,background="white",font=custFont).pack()
        Label(text="",background="white").pack()
        Label(text="Friends: "+friends,background="white",font=custFont).pack()
        Label(text="",background="white").pack()
        Button(text = "Change Sirname",width = 12 ,height = 2 ,fg ="#800000", command = self.name_change).pack()
        Label(text="",background="white").pack()
        Button(text = "Change Department",width = 15 ,height = 2 ,fg ="#800000",command = self.dep_change).pack()
        Label(text="",background="white").pack()
        Button(text = "Add Friends",width = 12 ,height = 2 ,fg ="#800000").pack()

        screen.mainloop()

iter = Profile()
iter.main_screen("stelios")