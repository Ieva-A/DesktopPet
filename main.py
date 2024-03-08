import tkinter as tk
import time
import random

filename = "cat_idle_64.gif"
petOnTop = True
numberOfFrames = 3
secondsPerFrame = 0.1
updateFrequency = 20 #lower = faster
spriteX = 64
spriteY = 64

class pet():
    x = 0
    def __init__(self, i):
        print(i)
        #create window
        self.window = tk.Tk()
        #img = tk.PhotoImage(file=filename) #for static image
        self.idle = [tk.PhotoImage(file=filename, format='gif -index %i' % (i)) for i in range(numberOfFrames)]
        self.frame_index = 0
        self.img = self.idle[self.frame_index]
        #check if advance frame
        self.timestamp = time.time()

        #make window transparent
        #focuslight to black when window doesn't have focus
        self.window.config(highlightbackground="#000001") #colour set to #000001 so pure black can be used in sprite
        #make window frameless
        self.window.overrideredirect(True)
        #make window pop out on top 
        self.window.attributes("-topmost", petOnTop)
        #turn blue into transparent
        self.window.wm_attributes("-transparentcolor", "#000001")

        #create label to contain image
        self.label = tk.Label(self.window, bd=0, bg="#000001")
        self.window.geometry("{spriteX}x{spriteY}+{x}+0".format(x=str(self.x), spriteX = spriteX, spriteY = spriteY))
        self.label.configure(image=self.img)
        self.label.pack()

        #run self.update() when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()
    
    def update(self):
        self.x += 2

        if time.time() > self.timestamp + secondsPerFrame:
            self.timestamp = time.time()
            #advance frame by 1, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % numberOfFrames
            self.img = self.idle[self.frame_index]

        #update window if moving
        self.window.geometry("{spriteX}x{spriteY}+{x}+0".format(x=str(self.x), spriteX = spriteX, spriteY = spriteY)) #EDIT RESOLUTION OF SPRITE HERE
        self.label.configure(image=self.img)
        self.label.pack

        self.window.after(updateFrequency, self.update)

pet(10)
