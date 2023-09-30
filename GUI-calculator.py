from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() 
GUI.title('โปรแกรมคำนวณกะปอมของลูน')
GUI.geometry('500x300')

bg = PhotoImage(file= '4k.png')

BG = Label(GUI, image=bg)
BG.pack()

v_lizard = StringVar() # ตัวแปรที่ใช้เก็บข้อความเมื่อพิมเสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable= v_lizard, font=(None,50))
L = Label(GUI,text='กรุณากรอกจำนวนกะปอม (ต่อตัว)',font=(None,40))
L.pack()

def Cal():
	try:
		quan = float(v_lizard.get())
		calc = quan * 20 # ต่อกะปอม 1 ตัว
		messagebox.showinfo('ราคาทั้งหมด','ราคากะปอมทั้งหมด {} บาท'.format(calc))
		v_lizard.set('1')
	except:
		messagebox.showwarning('กรอกเฉพาะตัวเลขเท่านั้น')
		v_lizard.set('1')

B = ttk.Button(GUI, text= 'คำนวณ', command=Cal)
B.pack(ipadx=30,ipady=20)#ipadx ขยายความกว้าง x/y
E1.pack()#แปะสิ่งที่พิมลงไปใน GUI
GUI.mainloop()