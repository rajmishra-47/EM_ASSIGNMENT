from tkinter import *
import math
import tkinter.messagebox as tmsg


root=Tk()
def compute(vo_a,io_b,wo_c,cos_angle):
    rc=vo_a/(io_b*cos_angle)
    sin_angle=math.sqrt(1-math.pow(cos_angle,2))
    
    xm=vo_a/(io_b*sin_angle)
    tmsg.showinfo('open circuit test ', f'the  value of Rc is {rc} and the value of Xm is {xm}')
    



def getans():
    a=vo_value.get()
    b=io_value.get()
    c=wo_value.get()
    vo_a=float(a)
    io_b=float(b)
    wo_c=float(c)
    cos_angle=(wo_c)/(vo_a*io_b)
    
    compute(vo_a,io_b,wo_c,cos_angle)

def getsct():
    a=vsc_value.get()
    b=isc_value.get()
    c=wsc_value.get()
    vsc_a=float(a)
    isc_b=float(b)
    wsc_c=float(c)
    rze=wsc_c/(isc_b*isc_b)
    zze=vsc_a/isc_b
    xze=math.sqrt(((zze*zze)-(rze*rze)))
    tmsg.showinfo('short circuit test ', f'the  value of Rze is {rze} and the value of Xze is {xze}')

    
        


    
root.geometry('600x250')

Label(root,text="open circuit test",font='times 18 bold',pady=15).grid(row=0,column=3)

vo=Label(root,text="Entre Vo",padx=5)
io=Label(root,text="Entre Io")
wo=Label(root,text="Entre Wo")

vo.grid(row=1,column=2)
io.grid(row=2,column=2)
wo.grid(row=3,column=2)

vo_value=StringVar()
io_value=StringVar()
wo_value=StringVar()

vo_entry=Entry(root,textvariable=vo_value)
io_entry=Entry(root,textvariable=io_value)
wo_entry=Entry(root,textvariable=wo_value)

vo_entry.grid(row=1,column=3)
io_entry.grid(row=2,column=3)
wo_entry.grid(row=3,column=3)

Button(text='calculate oct',command=getans).grid(row=7,column=3)


label2=Label(root,text="short circuit test",font='times 18 bold',pady=15).grid(row=0,column=23)

vsc=Label(root,text="Entre Vsc")
isc=Label(root,text="Entre Isc")
wsc=Label(root,text="Entre Wsc")



vsc.grid(row=1,column=22,padx=30)
isc.grid(row=2,column=22)
wsc.grid(row=3,column=22)





vsc_value=StringVar()
isc_value=StringVar()
wsc_value=StringVar()




vsc_entry=Entry(root,textvariable=vsc_value)
isc_entry=Entry(root,textvariable=isc_value)
wsc_entry=Entry(root,textvariable=wsc_value)




vsc_entry.grid(row=1,column=23)
isc_entry.grid(row=2,column=23)
wsc_entry.grid(row=3,column=23)

Button(text='calculate sct',command=getsct).grid(row=7,column=23)



root.mainloop()