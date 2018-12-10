from tkinter import *
import random
import math


class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main()
        self.mainloop()

    def main(self):
        self.master.title("Particules")
        self.master.resizable(width=False, height=False)

        canvas = Canvas(self.master, width=800, height=800, bg="black")
        canvas.grid()

        self.setup(canvas)

    def setup(self, canvas):
        canvas.particles = []
        canvas.tick = 0

        self.update(canvas)

    def update(self, canvas):
        canvas.particles.append(Particle(canvas, random.randrange(800), random.randrange(-10, 10), 3, random.randrange(70,100)/100))
        canvas.tick = canvas.tick + 1
        canvas.delete(ALL)
        for particle in canvas.particles:
            particle.draw()
            if particle.y > 800:
                canvas.particles.remove(particle)

        self.after(1, lambda: self.update(canvas))


class Particle():
    def __init__(self, canvas, x, y, size, speed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def draw(self):
        self.particle = self.canvas.create_oval(
            self.x-self.size,
            self.y-self.size,
            self.x+self.size,
            self.y+self.size,
            fill="white")
        self.y = self.y + 1 * self.speed


if __name__ == "__main__":
    root = Tk()
    App(root)
