import tkinter as tk
from pet import Pet

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, height=512, width=512)
        self.canvas.pack()
        self.img = tk.PhotoImage(file = "assert/calm.png") 
        self.canvas.create_image(20, 20,image=self.img)
if __name__ == '__main__':
    window = App()
    pet = Pet(
        name="Вася",
        fullness=100,
        health=100,
        mood=100,
        cleanness=100,
        energy=100
    )
    


    window.mainloop()

