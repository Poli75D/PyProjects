from tkinter import Tk, Button, Label, DoubleVar, Entry

c_window_width = int(190)
cww = c_window_width
c_window_height = int(170)
cwh = c_window_height
def f_resolution(x: int,y: int) -> str:
    return str(x) + "x" + str(y)

window = Tk()
window.title("Feet to Meter Converter")
window.configure(background = "dark blue")
window.geometry(f_resolution(cww,cwh))
window.resizable(width=False,height=False)

def f_convert():
    v_value = float(ft_entry.get())
    v_meter = v_value*0.3048
    mt_value.set("%.4f" % v_meter)

def f_clear():
    ft_value.set("")
    mt_value.set("")

c_element_width = int(7)
c_element_height = int(2)
c_element_padx = int(10)
c_element_pady = int(10)

c_element_bg = str("light grey")
c_element_fg = str("dark blue")

c_lbl_width = int(c_element_width*1)
c_lbl_height = int(c_element_height*1)

c_entry_width = int(c_element_width*2)
c_entry_height = int(c_element_height*1)

c_btn_width = int(c_element_width*1)
c_btn_height = int(c_element_height*1)

ft_lbl = Label(window,text="Feet",bg=c_element_bg,fg=c_element_fg, width=c_lbl_width)
ft_lbl.grid(column=0,row=0,padx=c_element_padx,pady=c_element_pady)

ft_value = DoubleVar()
ft_entry = Entry(window,textvariable=ft_value,width=c_entry_width)
ft_entry.grid(column=1,row=0,padx=c_element_padx,pady=c_element_pady)
ft_entry.delete(0,'end')

mt_lbl = Label(window,text="Meters",bg=c_element_bg,fg=c_element_fg, width=c_lbl_width)
mt_lbl.grid(column=0,row=1,padx=c_element_padx,pady=c_element_pady)

mt_value = DoubleVar()
mt_entry = Entry(window,textvariable=mt_value,width=c_entry_width,state="disabled")
mt_entry.grid(column=1,row=1,padx=c_element_padx,pady=c_element_pady)
mt_entry.delete(0,'end')

convert_btn = Button(window,text="Convert",bg=c_element_bg,fg=c_element_fg,width=c_btn_width,command=f_convert)
convert_btn.grid(column=0,row=2,padx=c_element_padx,pady=c_element_pady*2)

clear_btn = Button(window,text="Clear",bg=c_element_bg,fg=c_element_fg,width=c_btn_width,command=f_clear)
clear_btn.grid(column=1,row=2,padx=c_element_padx,pady=c_element_pady*2)

tit_lbl = Label(window,text="® Pol-US Development 2020", bg="dark blue", fg="white", font="arial 10 bold")
tit_lbl.grid(columnspan=2)

window.mainloop()
