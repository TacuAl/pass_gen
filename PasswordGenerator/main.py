import tkinter
import customtkinter
from password_gen import generate_password
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def gen_but():
    pswd.delete(1.0,"end")
    err_msg.pack_forget()
    try:
        min_len=int(len.get())
    except:
        err_msg.configure(text="Error, not a number!",text_color="red")
        err_msg.pack()
    has_capital = cap.get().lower() == "y"
    has_number = nr.get().lower() == "y"
    has_special = spe.get().lower() == "y"
    pswd.insert(1.0,generate_password(min_len,has_number,has_special,has_capital))
    
#Main window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Password Generator")

#Length of the password
title = customtkinter.CTkLabel(app,text="What is the minimum length?")
title.pack(padx=10,pady=10)
len_var=tkinter.IntVar()
len= customtkinter.CTkEntry(app,width=350,height=40,textvariable=len_var)
len.pack()

#Capital letters y/n
title = customtkinter.CTkLabel(app,text="Do you want to have capital letters (y/n)?")
title.pack(padx=10,pady=10)
cap_var=tkinter.StringVar()
cap= customtkinter.CTkEntry(app,width=350,height=40,textvariable=cap_var)
cap.pack()

#Number y/n
title = customtkinter.CTkLabel(app,text="Do you want to have numbers (y/n)?")
title.pack(padx=10,pady=10)
nr_var=tkinter.StringVar()
nr= customtkinter.CTkEntry(app,width=350,height=40,textvariable=nr_var)
nr.pack()

#Special character y/n
title = customtkinter.CTkLabel(app,text="Do you want to have special characters (y/n)?")
title.pack(padx=10,pady=10)
spe_var=tkinter.StringVar()
spe= customtkinter.CTkEntry(app,width=350,height=40,textvariable=spe_var)
spe.pack()

#Button for generating
generate_button=customtkinter.CTkButton(app,text="Generate",command=gen_but)
generate_button.pack(padx=10,pady=10)

#Finished product
pswd = customtkinter.CTkTextbox(app,height=1,border_width=1)
pswd.pack()

#Error msg
err_msg=customtkinter.CTkLabel(app)

app.mainloop()
