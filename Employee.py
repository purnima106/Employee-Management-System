from tkinter import *
from requests import * 
from sqlite3 import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


def add() : 
	sw.deiconify()
	mw.withdraw()

def back() : 
	mw.deiconify()
	sw.withdraw()

def view() : 
	tw.deiconify()
	mw.withdraw()
	scr_view.delete(1.0 , END)
	con = None
	try : 
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data : 
			info +=  " id: " +   str(d[0])   +   " name: " +    str(d[1])  +   " salary: " +  str(d[2]) +  "\n"
		scr_view.insert(INSERT , info)
	except Exception as e :
		con.rollback()
		showerror("Issue" , e) 
	finally : 
		if con is not None :
			con.close()

def vback() :
	mw.deiconify()
	tw.withdraw()

def update() : 
	fw.deiconify()
	mw.withdraw()

def uback() : 
	mw.deiconify()
	fw.withdraw()

def delete() : 
	nw.deiconify()
	mw.withdraw()

def dback() : 
	mw.deiconify()
	nw.withdraw()

def fback():
	mw.deiconify()
	pw.withdraw()

def fview():
	pw.deiconify()
	mw.withdraw()

mw = Tk( )
mw.title("Employee Management System")
mw.geometry("1000x668+400+50")
mw.iconbitmap(mw ,"work.ico")
mw.configure(bg = "grey")
photo = Image.open('off.jpg')
img = ImageTk.PhotoImage(photo)
lbl_bk=Label(mw, image=img)
lbl_bk.image=img
lbl_bk.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")


btn_add = Button(mw , text = "Add" , font = f , width = 10 , command = add,bg = "grey")
btn_add.pack(pady = 10)

btn_view = Button(mw , text = "View" , font = f , width = 10 , command = view,bg = "grey")
btn_view.pack(pady = 10)

btn_update = Button(mw , text = "Update" , font = f , width = 10 , command = update,bg = "grey" )
btn_update.pack(pady = 10)

btn_delete = Button(mw , text = "Delete" , font = f , width = 10 , command = delete,bg = "grey")
btn_delete.pack(pady = 10)

lab_location = Label(mw , text = "Location :" , font = ("cambria" , 30))
lab_location.place(x = 15 , y = 600)

lab_loc = Label(mw, text = "" , font = ("cambria" , 30 , "bold"), bg = "light grey")
lab_loc.place(x = 190 , y = 600 )
 
wa = "https://ipinfo.io/"
res = get(wa)
data = res.json()
city_name = data["city"]
lab_loc.config(text = city_name)

sw = Toplevel(mw)
sw.title("Add Employee")
sw.geometry("1000x668+400+50")
sw.iconbitmap(sw,"work.ico")
sw.configure(bg = "grey")
photo1 = Image.open('off.jpg')
img1 = ImageTk.PhotoImage(photo1)
lbl_bk1=Label(sw, image=img)
lbl_bk1.image=img1
lbl_bk1.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")

f = ("cambria" , 30 , "bold")

lab_id = Label(sw , text = "Enter id : " , font = f , bg = "#B9D3EE" )
lab_id.pack(pady = 10)

ent_id = Entry(sw , font = f )
ent_id.pack(pady = 10)

lab_name = Label(sw , text = "Enter name : " , font = f , bg = "#B9D3EE" )
lab_name.pack(pady = 10)

ent_name = Entry(sw , font = f )
ent_name.pack(pady = 10)

lab_salary = Label(sw , text = "Enter salary : " , font = f , bg = "#B9D3EE" )
lab_salary.pack(pady = 10)

ent_salary = Entry(sw , font = f )
ent_salary.pack(pady = 10)

def save() : 
	con = None
	try : 
		con = connect("employee.db")
		cursor = con.cursor()  
		sql = "insert into emp values('%d' , '%s' , '%f')"
		eid = ent_id.get()
		eid = eid.strip()              
		if (eid == "") or (eid.strip()== "" ) : 
			showerror("Failed ","Id should not be empty")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		try : 
			id = int(eid) 
		except ValueError : 
			showerror("Failed " , "Id must be integer only")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		if id < 1 : 
			showerror("Failed " ,"Minimum id should be 1")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		name = ent_name.get()
		if (name == "") or (name.strip() == "") : 
			showerror("Failed " ,"Name should not be empty ")
			ent_name.delete(0 , END)
			ent_name.focus()
			return
		if (not name.isalpha()) :
			showerror("Failed " ,"Invalid name")
			ent_name.delete(0 , END)
			ent_name.focus()
			return
			
		esalary = (ent_salary.get())
		if (esalary == "" ) or (esalary.strip() == "") : 
			showerror("Failed " ,"Salary should not be empty")
			ent_salary.delete(0 , END)
			ent_salary.focus()
			return
		try : 
			salary = float(esalary)
		except : 
			showerror("Failed " ,"Invalid salary")
			ent_salary.delete(0 , END)
			ent_salary.focus()
			return
		cursor.execute(sql%(id,name,salary))
		con.commit()
		showinfo("Success" , "Records saved ")
		ent_id.delete(0 , END)
		ent_name.delete(0, END)
		ent_salary.delete(0 , END)
		ent_id.focus()
		return
		
	except Exception as e :
		con.rollback()
		showerror("Failed ", e)
		ent_id.delete(0 , END)
		ent_name.delete(0, END)
		ent_salary.delete(0 , END)
		ent_id.focus()
		return

	finally : 
		if con is not None :
			con.close()		

btn_save = Button(sw , text = "Save " , font = f , width = 10 , command = save,bg = "grey")
btn_save.pack(pady = 10)

btn_back = Button(sw , text = "Back " , font = f , width = 10 , command = back,bg = "grey" )
btn_back.pack(pady = 10) 
sw.withdraw()

tw = Toplevel(mw)
tw.title("View Employee")
tw.geometry("1000x668+400+50")
tw.iconbitmap(tw,"work.ico")
tw.configure(bg = "grey")
f = ("cambria" , 30 , "bold")
photo2 = Image.open('off.jpg')
img2 = ImageTk.PhotoImage(photo2)
lbl_bk2=Label(tw, image=img2)
lbl_bk2.image=img2
lbl_bk2.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")

scr_view = ScrolledText(tw , font = f , width = 32 , height = 8 , bg = "#FFE7BA", relief="solid" )
scr_view.pack(pady = 20)

btn_backv = Button(tw , text = "Back" , font = f , width = 10 , command = vback,bg = "grey")
btn_backv.place(x = 250 , y = 500 )

tw.withdraw()



fw = Toplevel(mw)
fw.title("Update Employee")
fw.geometry("1000x668+400+50")
fw.iconbitmap(fw,"work.ico")
fw.configure(bg = "grey")
f = ("cambria" , 30 , "bold")
photo3 = Image.open('off.jpg')
img3 = ImageTk.PhotoImage(photo3)
lbl_bk3=Label(fw, image=img3)
lbl_bk3.image=img
lbl_bk3.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")

uw_lab_id = Label(fw , text = "Enter id : " , font = f , bg = "#FFEFDB" )
uw_lab_id.pack(pady = 10)

uw_ent_id = Entry(fw , font = f )
uw_ent_id.pack(pady = 10)

uw_lab_name = Label(fw , text = "Enter name : " , font = f  , bg = "#FFEFDB" )
uw_lab_name.pack(pady = 10)

uw_ent_name = Entry(fw , font = f )
uw_ent_name.pack(pady = 10)

uw_lab_salary = Label(fw , text = "Enter salary : ", font = f , bg = "#FFEFDB" )
uw_lab_salary.pack(pady = 10)

uw_ent_salary = Entry(fw , font = f )
uw_ent_salary.pack(pady = 10)

def usave() : 
	con = None
	try  :
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "update emp set name ='%s' , salary='%f' where id = '%d' "
		id = uw_ent_id.get()
		id = id.strip()    
		if (id == "") or (id.strip() == "" ) : 
			showerror("Failed " , "Id should not be empty")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return
		try : 
			id = int(id)
		except ValueError : 
			showerror("Failed" , "Id must be integer only")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return

		if (id < 1) : 
			showerror("Failed" , "Minimum id should be 1 ")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return

		name = uw_ent_name.get()
		if (name == "") or (name.strip() == "") : 
			showerror("Failed" , "Name should not be empty")
			uw_ent_name.delete(0 , END)
			uw_ent_name.focus()
			return

		if (not name.isalpha()) : 
			showerror("Failed" , "Invalid name")
			uw_ent_name.delete(0 , END)
			uw_ent_name.focus()
			return
		
		salary = uw_ent_salary.get()
		if (salary == "") or (salary.strip() == "") : 
			showerror("Failed" , "Salary should not be empty")
			uw_ent_salary.delete(0 , END)
			uw_ent_salary.focus()
			return
		try :
			salary = float(salary)
		except ValueError :
			showerror("Failed" , "Invalid salary" )
			uw_ent_salary.delete(0 , END)
			uw_ent_salary.focus()
			return
		cursor.execute(sql%(name,salary,id))
		if cursor.rowcount == 1 : 
			con.commit()
			showinfo("Success" , "Records updated")
			uw_ent_id.delete(0 , END)
			uw_ent_name.delete(0 , END)
			uw_ent_salary.delete(0 , END)
			uw_ent_id.focus()
			return
		else : 
			showerror("Failed" , "Record does not exists ")
			uw_ent_id.delete(0 , END)
			uw_ent_name.delete(0 , END)
			uw_ent_salary.delete(0 , END)
			uw_ent_id.focus()
			return

	except Exception as e : 
		con.rollback()
		showerror("Issue" , e )
		uw_ent_id.delete(0 , END)
		uw_ent_name.delete(0 , END)
		uw_ent_salary.delete(0 , END)
		uw_ent_id.focus()
		return
	
	finally  :
		if con is not None : 
			con.close()


btn_usave = Button(fw , text = "Save" , font = f , width = 10 , command = usave,bg = "grey")
btn_usave.pack(pady = 10)

btn_uback = Button(fw , text = "Back" , font = f , width = 10 , command = uback,bg = "grey")
btn_uback.pack(pady = 10)

fw.withdraw()

nw = Toplevel(mw)
nw.title("Delete Employee")
nw.geometry("1000x668+400+50")
nw.iconbitmap(nw,"work.ico")
nw.configure(bg = "grey")
f = ("cambria" , 30 , "bold")
photo4 = Image.open('off.jpg')
img4 = ImageTk.PhotoImage(photo4)
lbl_bk4=Label(nw, image=img4)
lbl_bk4.image=img4
lbl_bk4.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")

dw_lab_id = Label(nw , text = "Enter id : " , font =  f , bg = "#00EEEE")
dw_lab_id.pack(pady = 10)

dw_ent_id = Entry(nw , font = f )
dw_ent_id.pack(pady = 10)

def dsave() : 
	con = None 
	try :
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "delete from emp where id = '%d' "
		id = dw_ent_id.get()
		if (id == "") or (id.strip() == "") : 
			showerror("Failed" , "Id should not be empty") 	
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		try : 
			id = int(id)
		except : 
			showerror("Failed" , "Id must be integer only") 	
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		cursor.execute(sql %(id))
		if cursor.rowcount == 1 :
			con.commit()
			showinfo("Success" , "Record deleted")
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		else :
			showerror("Failed" , "Record does not exists ")
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
	except Exception as e :
		con.rollback()
		showerror("Issue" , e)
		dw_ent_id.delete(0 , END)
		dw_ent_id.focus()
		return

	finally : 
		if con is not None :
			con.close()

btn_dsave = Button(nw , text = "Save" , font = f , width = 10 , command = dsave,bg = "grey" )
btn_dsave.pack(pady = 10)

btn_dback = Button(nw , text = "Back" , font = f , width = 10 , command = dback,bg = "grey")
btn_dback.pack(pady = 10)

nw.withdraw()

def chart():
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = '''SELECT name, salary FROM emp ORDER BY salary DESC LIMIT 5'''
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		salary = []
		for i in data:
			name.append(i[0])
			salary.append(i[1])
		plt.figure(figsize=(8,6))
		c = ['red', 'yellow', 'black', 'blue' , 'orange' ]
		plt.rcParams.update({'text.color': "red", 'axes.labelcolor': "green"})
		ax = plt.axes()
		ax.set_facecolor("lightblue")  # Setting the background color of the plot using facecolor
		
		
		plt.bar(name, salary ,  color= c)
		plt.xlabel("Names of Employee" , fontsize = 15)
		plt.ylabel("Salary of Employee", fontsize = 15)
		plt.title("Top 5 Highest Salaried Employee", fontsize = 15)
		plt.grid()
		plt.show()
	except Exception as e:
        	showerror("issue ", e)
	        con.rollback()
	finally:
		if con is not None:
			con.close()

btn_charts = Button(mw , text = "Charts" , font = f , width = 10 , command = chart,bg = "grey" )
btn_charts.pack(pady = 10)

btn_feedback= Button(mw ,text = "feedback on app",font = ("cambria",15,"bold"),bg = "light grey",command = fview)
btn_feedback.place(x = 800,y = 600)

def on_closing():
    if askyesno("Quit", "Do you want to quit?"):
        mw.destroy()

def fbsave():
	try:
		con = None
		con = connect("employee.db")
		cursor = con.cursor()
		name = fb_name_ent.get()
		if (name == "") or (name.strip() == ""):
			showerror("Issue", "Invalid Name")
			fb_name_ent.delete(0, END)
			fb_name_ent.focus()
			return
		if (not name.isalpha()):
			showerror("Issue", "Invalid Name")
			fb_name_ent.delete(0, END)
			fb_name_ent.focus()
			return

		email = fb_email_ent.get()
		if (email == "") or (email.strip() == ""):
			showerror("Issue", "Inavlid Email")
			fb_email_ent.delete(0, END)
			fb_email_ent.focus()
			return
		if "@gmail.com" not in email:
			showerror("Issue", "Invalid email format")
			fb_email_ent.delete(0, END)
			fb_email_ent.focus()
			return

		feedback = fb_src.get(1.0, END)
		if (feedback.strip() == ""):
			showerror("Issue", "Cannot be empty!")
			fb_src.delete(0, END)
			fb_src.focus()
			return

		sql = "insert into records values('%s','%s','%s')"
		cursor.execute(sql%(name,email,feedback))
		con.commit()
		showinfo("Success", "Response Submitted")
		fb_name_ent.delete(0, END)
		fb_email_ent.delete(0, END)
		fb_src.delete(1.0, END)
		fb_name_ent.focus()
		return

	except Exception as e:
		showerror("Issue", e)
		fb_name_ent.delete(0, END)
		fb_email_ent.delete(0, END)
		fb_src.delete(1.0, END)
		fb_name_ent.focus()
		return
	finally:
		if con is not None:
			con.close()

pw = Toplevel(mw)
pw.title("Feedback")
pw.geometry("1000x668+400+50")
pw.iconbitmap(nw,"work.ico")
pw.configure(bg = "grey")
f = ("cambria" , 30 , "bold")
photo5 = Image.open('off.jpg')
img5 = ImageTk.PhotoImage(photo5)
lbl_bk5=Label(pw, image=img5)
lbl_bk5.image=img5
lbl_bk5.place(relx=0.5,rely=0.5,anchor='center')
f = ("cambria" , 30 , "bold")

fb_name = Label(pw,text = "Enter Name",font = f,bg = "light blue") 
fb_name.place(x = 50,y = 20)

fb_name_ent = Entry(pw,text = "",font = f)
fb_name_ent.place(x =400,y = 20)

fb_email = Label(pw,text = "Enter Email",font = f,bg = "light blue")
fb_email.place(x = 50,y = 100)

fb_email_ent = Entry(pw,text = "",font = f)
fb_email_ent.place(x =400,y = 100)

fb_back = Button(pw,text = "Back",font = f,bg = "grey",command = fback)
fb_back.place(x = 400,y= 550)

fb_fb = Label(pw,text = "Enter Feedback",font = f,bg = "light blue")
fb_fb.place(x = 50, y=180)

fb_src = ScrolledText(pw,font = f,height=5,width = 20)
fb_src.place(x = 400,y = 180)

fb_save = Button(pw,text = "Save",font = f,bg = "grey",command=fbsave)
fb_save.place(x = 400, y = 450)

pw.withdraw()


mw.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)
tw.protocol("WM_DELETE_WINDOW", on_closing)
fw.protocol("WM_DELETE_WINDOW", on_closing)
nw.protocol("WM_DELETE_WINDOW", on_closing)
pw.protocol("WM_DELETE_WINDOW", on_closing)


mw.mainloop()




