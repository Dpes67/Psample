from tkinter import *
def drag(event):
    widget=event.widget
    widget.startx=event.x
    widget.starty=event.y
def drag_motion(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startx+event.x
    y=widget.winfo_y()-widget.starty+event.y
    widget.place(x=x,y=y)

window=Tk()
label=Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label2=Label(window,bg="purple",width=10,height=5)
label2.place(x=222,y=222)

label.bind("<Button-1>",drag)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag)
label2.bind("<B1-Motion>",drag_motion)
window.mainloop()
