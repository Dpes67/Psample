from tkinter import *
import time
WIDTH=1000
HEIGHT=600
xVelocity=1
yVelocity=1
window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
bck_photo=PhotoImage(file="logo.png")#add bg picture
bck_image=canvas.create_image(0,0,image=bck_photo,anchor=NW)

photo=PhotoImage(file="zombie.png")#add pic for animation
image=canvas.create_image(0,0,image=photo,anchor=NW)



image_width=photo.width()
image_height=photo.height()

while TRUE:
    coordinates=canvas.coords(image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity=-xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity=-yVelocity
    canvas.move(image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
window.mainloop()