from textwrap import wrap
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import mysql.connector


#------------------------------------------------------------------------------------------------------------------------------------------------------------
#TKINTER Initialisation Statements-For 1st Window
root = Tk()
root.title("Epiphany-A Diary that loves you")
root.iconbitmap('img/icon.png')
root.resizable(False, False)
bg = PhotoImage(file = "img/bg.png")
back = Label(root, image=bg)
back.place(x=0,y=0,relwidth=1,relheight=1)

# BG setup For 2nd Window
bg1 = PhotoImage(file = "img/bg3.png")


#------------------------------------------------------------------------------------------------------------------------------------------------------------

#DB Initialisation Statements
db = mysql.connector.connect(host="localhost",user="root",passwd="",database="Diary")
c = db.cursor()  


#Functions------------------------------------------------------------------------------------------------------------------------------------------------------------

#Databases-Functions:

#Create Database & Table
def create_table():
 
    c.execute('''
    CREATE TABLE Story (
        StoryNum int Primary Key Not Null AUTO_INCREMENT,
        StoryContent LONGTEXT,
        StoryDate datetime DEFAULT CURRENT_TIMESTAMP);
    )
    ''')
    
    db.close()
    print("Database Created")

#Delete Database
def delete_table():
 
    c.execute('''
    DROP TABLE Story;
    ''')
    
    db.close()
    print("Database Created")

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Display Func
def display(t,u):

    #TKINTER Initialisation Statements-For 2nd Window
    top = Toplevel()
    top.title('Your Precious Words')
    top.iconbitmap('img/icon.png')
    top.resizable(False, False)
    
    back1 = Label(top, image=bg1)
    back1.place(x=0,y=0,relwidth=1,relheight=1)
    

    head = Label(top,text="Previous Entries").grid(row=0,column=2,padx=10,pady=10)

    displayer = ScrolledText(top)
    displayer.insert(END,t)
    displayer.grid(row=1,column=1,columnspan=2,padx=20)
    displayer.config(state= DISABLED)

    head2=Label(top,text="Date").grid(row=0,column=4,padx=10,pady=10)
    date = Label(top,text=u)
    date.grid(row=1,column=4,padx=10,pady=10)

   


#------------------------------------------------------------------------------------------------------------------------------------------------------------
#GUI-Functions:

#View Func
def view():
    c.execute(''' 
    SELECT * FROM Story;''')
    records = c.fetchall()
    sno=''
    print_records='' 
    date_records='' 
    for record in records:
        print_records += str(record[0]) +".  "+ str(record[1]) +'\n\n\n\n'
        date_records += str(record[0]) +".  "+str(record[2]) +'\n\n\n\n'
    display(print_records,date_records)
        

#Save Func
def save():
    sql = ('''
    INSERT INTO Story (StoryContent)
    VALUES ("%s")
    ''')
    val = (str(input1.get("1.0",'end-1c')),)
    c.execute(sql, val)

    db.commit()
    input1.delete("1.0",'end-1c')
    label2 = Label(root,text="SAVED!")
    label2.grid(row=10,column=2)
    

#Rewrite Func
def rewrite():
    input1.delete("1.0",'end-1c')
    label2 = Label(root,text="NEW ENTRY")
    label2.grid(row=10,column=2)

#-GUI-Components-----------------------------------------------------------------------------------------------------------------------------------------------------------  

# Header
head_img = PhotoImage(file="img/head.png")
myLabel = Label(root,image=head_img)
myLabel.grid(row=0,column=2,pady=10)

#Input
input1 = ScrolledText(root,width=100,borderwidth=0)
input1.grid(row=1,column=2,padx=10,ipady=10)


# View
view_img = PhotoImage(file="img/1.png")
btn1 = Button(root,image=view_img ,command=view ,borderwidth=0 )
btn1.grid(row=2,column=2,pady=10)

# Save
save_img = PhotoImage(file="img/2.png")
btn2 = Button(root,image=save_img ,command=save ,borderwidth=0 )
btn2.grid(row=3,column=2,pady=10)

# Rewrite
re_img = PhotoImage(file="img/3.png")
btn3 = Button(root,image=re_img ,command=rewrite ,borderwidth=0 )
btn3.grid(row=4,column=2,pady=10)


#DB-Table-Initialisation-and-Deletion---------------------------------------------------------------------------------------------------------------------------------------------------------
# create_table()
# delete_table()
#------------------------------------------------------------------------------------------------------------------------------------------------------------



#Main GUI Loop--------------------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
