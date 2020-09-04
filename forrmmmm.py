#registration form using tkinter
#data is stored in mysql via connection method


from tkinter import * 
from tkinter import ttk, messagebox
from PIL import Image,ImageTk 
import pymysql

#getting the screen
root = Tk()
root.title("Registeration window")
root.geometry("1600x900")
root.config(bg="white")

#clearing registration form after registration is done
def clear():
	Name_entry.delete(0,END)
	Email_entry.delete(0,END)
	contact_entry.delete(0,END)
	alternate_contact_entry.delete(0,END)
	State_entry.current(0)
	Nationality_entry.current(0)
	Institute_entry.delete(0,END)
	Course_entry.current(0)

#registering data
def register_data():
	if Name_entry.get()=="" or Email_entry.get()=="" or contact_entry.get()=="" or State_entry.get()=="Select" or Nationality_entry.get()=="Select" or Institute_entry.get()=="" or Course_entry.get()=="Select" :
		messagebox.showerror("Error" , "All fiels are required", parent=root)
	elif var1.get()==0:
		messagebox.showerror("Error","Please agree our terms and conditions", parent=root)
	elif contact_entry.get()==alternate_contact_entry.get():
		messagebox.showerror("Error" , "Alternate Contact should be different", parent=root)
	else:
		try:
			con=pymysql.connect(host="localhost",user="root",password="kun@ls@h.6841",database="registration")
			cur=con.cursor()
			cur.execute("select * from registration_request where Email_entry=%s",Email_entry.get())
			row=cur.fetchone()
			if row!=None:
				messagebox.showerror("Error","User already Exist, Please try with another email",parent=root)
			else:
				try:
					int(contact_entry.get())
					int(alternate_contact_entry.get())
					cur.execute("insert into registration_request(Name_entry,Email_entry,contact_entry,alternate_contact_entry,State_entry,Nationality_entry,Institute_entry,Course_entry) values (%s,%s,%s,%s,%s,%s,%s,%s)",
									(Name_entry.get(),
									 Email_entry.get(),
									 contact_entry.get(),
									 alternate_contact_entry.get(),
									 State_entry.get(),
									 Nationality_entry.get(),
									 Institute_entry.get(),
									 Course_entry.get()
									))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Register Successful", parent=root)
					clear()
					print("Full name : ", Name_entry.get(),"\n",
						"Email :", Email_entry.get(),"\n", 
						"Contact no. :", contact_entry.get(),"\n",
						"Alternate Contact no. :", alternate_contact_entry.get(),"\n",
						"State :", State_entry.get(),"\n",
						"Nationality :", Nationality_entry.get(),"\n",
						"Institute :", Institute_entry.get(),"\n",
						"Course :", Course_entry.get(),"\n")
				except:
					messagebox.showerror("Error","Contact and Alternate contact should be a number")


		except Exception as es:
			messagebox.showerror("Error",f"Error dur to: {str(es)}",parent=root)
			print("Full name : ", Name_entry.get(),"\n",
				"Email :", Email_entry.get(),"\n", 
				"Contact no. :", contact_entry.get(),"\n",
				"Alternate Contact no. :", alternate_contact_entry.get(),"\n",
				"State :", State_entry.get(),"\n",
				"Nationality :", Nationality_entry.get(),"\n",
				"Institute :", Institute_entry.get(),"\n",
				"Course :", Course_entry.get(),"\n")



#bg image
bg_img=ImageTk.PhotoImage(file="red-blue-hd-bg.jpg")
bg=Label(root, image=bg_img).place(x=0,y=0,width=1600,height=900)
		
#creating frame 2
frame2=Frame(root,bg="white")
frame2.place(x=570,y=120,width=901,height=684)
#creating frame 3 inside frame 2
frame3=Frame(root,bg="black")
frame3.place(x=573,y=122,width=896,height=680)

#creating frame 1
frame1=Frame(root,bg="white")
frame1.place(x=78,y=88,width=504,height=754)

#adding image to frame 1
frm_bg=ImageTk.PhotoImage(file="frame1_img.jpeg")
bg=Label(root,image=frm_bg).place(x=80,y=90,width=500,height=750)

####adding text to frame 3####
#adding label

Name=Label(root,text="Full Name", bg="black", fg="white", font=("Times new roman", 20, "normal"))
Name.place(x= 600,y= 135)

#adding entry box
Name_entry=Entry(root, width=30, bg="white" , fg="black", font=("none 16 normal"))
Name_entry.place(x=600, y= 180)

#adding label
Email=Label(root,text="Email", bg="black", fg="white", font=("Times new roman", 20, "normal"))
Email.place(x= 1092,y= 135)

#adding entry box
Email_entry=Entry(root, width=30, bg="white" , fg="black", font=("none 16 normal"))
Email_entry.place(x= 1092, y= 180)

#adding label
contact=Label(root,text="Contact", bg="black", fg="white",font=("Times new roman", 20, "normal"))
contact.place(x= 600,y= 245)

#adding entry box
contact_entry=Entry(root, width=30, bg="white" , fg="black", font=("none 16 normal"))
contact_entry.place(x= 600, y= 290)

#adding label
alternate_contact=Label(root,text="Alternate_contact", bg="black", fg="white", font=("Times new roman", 20, "normal"))
alternate_contact.place(x= 1092,y= 245)

#adding entry box
alternate_contact_entry=Entry(root, width=30, bg="white" , fg="black", font=("none 16 normal"))
alternate_contact_entry.place(x= 1092, y= 290)

#adding label
State=Label(root,text="State", bg="black", fg="white", font=("Times new roman", 20, "normal"))
State.place(x= 600,y= 355)

#adding combo box
State_entry=ttk.Combobox(root, width=28,state='readonly', justify=CENTER, font=("Times new roman", 18, "normal"))
State_entry['values']=('Select','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal')
State_entry.current(0)
State_entry.place(x= 600, y= 400)

#adding label
Nationality=Label(root,text="Nationality", bg="black", fg="white", font=("Times new roman", 20, "normal"))
Nationality.place(x= 1092,y= 355)

#adding entry box
Nationality_entry=ttk.Combobox(root, width=28,state='readonly', justify=CENTER, font=("Times new roman", 18, "normal"))
Nationality_entry['values']=('Select','Afghan','Albanian','Algerian','Argentine','Argentinian','Australian','Austrian','Bangladeshi','Belgian','Bolivian','Batswana','Brazilian','Bulgarian','Cambodian','Cameroonian','Canadian','Chilean','Chinese','Colombian','Costa Rican','Croatian','Cuban','Czech','Danish','Dominican','Ecuadorian','Egyptian','Salvadorian','English','Estonian','Ethiopian','Fijian','Finnish','French','German','Ghanaian','Greek','Guatemalan','Haitian','Hungarian','Icelandic','Indian','Indonesian','Iranian','Iraqi','Irish','Israeli','Italian','Jamaican','Japanese','Jordanian','Kenyan','Kuwaiti','Lao','Latvian','Lebanese','Libyan','Lithuanian','Malagasy','Malaysian','Malian','Maltese','Mexican','Mongolian','Moroccan','Mozambican','Namibian','Nepalese','Dutch','New Zealand','Nicaraguan','Nigerian','Norwegian','Pakistani','Panamanian','Paraguayan','Peruvian','Polish','Portuguese','Romanian','Russian','Saudi','Scottish','Senegalese','Serbian','Singaporean','Slovak','South African','Korean','Spanish','Sri Lankan','Sudanese','Swedish','Swiss','Syrian','Taiwanese','Tajikistani','Thai','Tongan','Tunisian','Turkish','Ukrainian','Emirati','British','American','Uruguayan','Venezuelan','Vietnamese','Welsh','Zambian','Zimbabwean')
Nationality_entry.place(x= 1092, y= 400)
Nationality_entry.current(0)

#adding label
Institute=Label(root,text="Institute", bg="black", fg="white", font=("Times new roman", 20, "normal"))
Institute.place(x= 600,y= 465)

#adding entry box
Institute_entry=Entry(root, width=30, bg="white" , fg="black", font=("none 16 normal"))
Institute_entry.place(x= 600, y= 510)

#adding label
Course=Label(root,text="Course", bg="black", fg="white", font=("Times new roman", 20, "normal"))
Course.place(x= 1092,y= 465)

#adding entry box
Course_entry=ttk.Combobox(root, width=28,state='readonly', justify=CENTER, font=("Times new roman", 18, "normal"))
Course_entry['values']=('Select','Management MBA/BBA','Engineering B.Tech and B.Arch, M.Tech, ME, BE','Computer Application-BCA/MCA','Designing - Fashion/Interior/Web','Mass-communication/Journalism BJMC','Hospitality (Hotel) - Hotel Management','Medical-BDS and MBBS','Finance -B.Com/CA','Arts Psychology and Sociology','Law B.ALLB/LLB','Education Teaching-B.Ed/M.Ed','Pharmacy B.Pharma/M.Pharma','Tourism management - B.Sc.','Fine Arts B.F.A','Nursing B.Sc. and M.Sc. in Nursing')
Course_entry.place(x= 1092, y= 510)
Course_entry.current(0)

#term and condition check button
var1= IntVar()
Checkbutton(root, text="i agree with the terms and conditions.",cursor="hand2",onvalue=1,offvalue=0,variable=var1, width=40, bg="black", fg="red", font=("Times new roman", 20 , "italic")).place(x=700, y=570)

#creating Submittion Button
Submittionbutton=Button(root,text="Register",cursor="hand2",command=register_data,width=40, bg="green", fg="white", font=("Times new roman", 20, "normal"))
Submittionbutton.place(x=710,y=630)

#creating exit function
def close_window():
	root.destroy()
	exit()
#creating exit button
exitbutton=Button(root,text="QUIT",cursor="hand2",width=20,bg="red", fg="white", command=close_window,font=("Times new roman", 20 , "normal"))
exitbutton.place(x=850,y=720)

#creating sign in
singin=Button(root,text="Sign In",width="10", bg="white",fg="Grey",cursor="hand2",font=("Times new roman", 18 , "bold"))
singin.place(x=250,y=750)

root.mainloop()