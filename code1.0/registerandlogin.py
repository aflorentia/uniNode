from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
import csv
class RegisterLogin:
  
  def delete7(self):
    screen1.destroy()
  
  def delete2(self):
    screen3.destroy()

  def delete3(self):
    screen4.destroy()

  def delete4(self):
    screen5.destroy()
    
  def login_sucess(self):
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Sucess",background="white").pack()
    Button(screen3, text = "OK", command = self.delete2).pack()

  def password_not_recognised(self):
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error",background="white").pack()
    Button(screen4, text = "OK", command =self.delete3).pack()

  def user_not_found(self):
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found",background="white").pack()
    Button(screen5, text = "OK", command =self.delete4).pack()

    
  def register_user(self):
    print("working")
    
    username_info = username.get()
    password_info = password.get()

    with open('C:\\Users\\Στελιος\\Desktop\\TN\\users.csv', mode="a",newline='') as csvfile:
      f = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      f.writerow([username_info,password_info])

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration Sucess", fg = "green" ,font = custFont,background="white").pack()
    Button(screen1, text = "Done", width = 8 ,height = 2 ,fg ="#800000", command = self.delete7).pack()


  def login_verify(self):
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    global flag
    flag = 1
    with open('C:\\Users\\Στελιος\\Desktop\\TN\\users.csv', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      
      for row in reader:
        if row["username"] == username1:
          flag=0
          if row["password"] == password1:
            self.login_sucess()
            break
          else:
            self.password_not_recognised()
            break
    
    if flag == 1:
      self.user_not_found()
        
          





  def register(self):
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x600")
    screen1.configure(background="white")
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below",background="white").pack()
    Label(screen1, text = "",background="white").pack()
    Label(screen1, text = "Username * ",background="white").pack()
  
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ",background="white").pack()
    password_entry =  Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "",background="white").pack()
    Button(screen1, text = "Register", width = 8 ,height = 2 ,fg ="#800000", command = self.register_user).pack()

  def login(self):
    global screen2
    screen2 = Toplevel(screen)
    screen2.configure(background = "white")
    screen2.title("Login")
    screen2.geometry("600x600")
    Label(screen2, text = "Please enter details below to login",background="white").pack()
    Label(screen2, text = "",background="white").pack()

    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2, text = "Username * ",background="white").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "",background="white").pack()
    Label(screen2, text = "Password * ",background="white").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "",background="white").pack()
    Button(screen2, text = "Login",width = 8 ,height = 2 ,fg ="#800000", command = self.login_verify).pack()
    
    
  def main_screen(self):
    global screen
    global custFont
    global my_img
    screen = Tk()
    screen.geometry("600x600")
    screen.configure(background = "white")
    screen.title("Welcome")
    custFont =Font(
    family = "Helvetica",
    size = 24,
    weight = "bold"
    )
    screen.iconbitmap("C:\\Users\\Στελιος\\Desktop\\TN\\logo.ico")
    my_img=ImageTk.PhotoImage(Image.open("C:\\Users\\Στελιος\\Desktop\\TN\\logo.png"))
    my_label=Label(image=my_img,background="white")
    my_label.pack()
    Label(text="",background="white").pack()
    Button(text = "Login", width = 8 ,height = 2 ,fg ="#800000", command = self.login).pack()
    Label(text="",background="white").pack()
    Button(text = "Register",width = 8 ,height = 2 ,fg ="#800000", command = self.register).pack()

    screen.mainloop()
  

iter = RegisterLogin()
iter.main_screen()
  
