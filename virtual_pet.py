import tkinter as tk
import time
from pet import Pet


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pet = Pet(
            name="Никита",
            fullness=100,
            health=100,
            mood=100,
            cleanness=100,
            energy=100
        )
        self.geometry("512x512")
        self.name_lbl = tk.Label(self, text=f"имя: {self.pet.name}")
        self.name_lbl.pack()
        self.fullness_lbl = tk.Label(self, text=f"сытость: {self.pet.fullness}")
        self.fullness_lbl.pack()
        self.health_lbl = tk.Label(self, text=f"здоровье: {self.pet.health}")
        self.health_lbl.pack()
        self.mood_lbl = tk.Label(self, text=f"настроение: {self.pet.mood}")
        self.mood_lbl.pack()
        self.cleanness_lbl = tk.Label(self, text=f"чистота: {self.pet.cleanness}")
        self.cleanness_lbl.pack()
        self.energy_lbl = tk.Label(self, text=f"бодрость: {self.pet.energy}")
        self.energy_lbl.pack()


        self.canvas = tk.Canvas(self, width=256, height=256)
        self.canvas.pack()
        self.img = tk.PhotoImage(file="assets/calm.png")
        self.img = self.img.subsample(2)
        self.canvas.create_image(128, 128, image=self.img, anchor=tk.CENTER)


        self.feed_btn = tk.Button(self, text="покормить", command=lambda: self.pet.feed(5))
        self.feed_btn.pack()

    def my_update(self):
            self.pet.decrease_stats()
            self.fullness_lbl.config(text=f"сытость: {self.pet.fullness}")
            self.health_lbl.config(text=f"здоровье: {self.pet.health}")
            self.mood_lbl.config(text=f"настроение: {self.pet.mood}")
            self.cleanness_lbl.config(text=f"чистота: {self.pet.cleanness}")
            self.energy_lbl.config(text=f"энергия: {self.pet.energy}")
            self.after(1000, self.my_update)




if __name__ == '__main__':
    window = App()
    window.my_update()
    window.mainloop()
