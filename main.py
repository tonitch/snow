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

        canvas = Canvas(self.master, width=1920, height=1080, bg="black")
        canvas.grid()

        self.setup(canvas)

    def setup(self, canvas):
        canvas.particles = []
        canvas.tick = 0

        self.update(canvas)

    def update(self, canvas):
        canvas.particles.append(
            Particle(
                canvas, random.randrange(1920),
                random.randrange(-10, 10),
                random.randrange(70, 100) / 50))
        canvas.tick = canvas.tick + 1
        canvas.delete(ALL)
        for particle in canvas.particles:
            particle.draw()
            if particle.y > 1080:
                canvas.particles.remove(particle)

        self.after(1, lambda: self.update(canvas))


class Particle():
    def __init__(self, canvas, x, y, speed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = speed
        self.size = map(self.speed, 70/50, 100/50, 1, 10)

    def draw(self):
        self.particle = self.canvas.create_oval(
            self.x-self.size,
            self.y-self.size,
            self.x+self.size,
            self.y+self.size,
            fill="white")
        self.y = self.y + 1 * self.speed


def map(n, start1, stop1, start2, stop2):
    newval = (n - start1) / (stop1 - start1) * (stop2 - start2) + start2
    return newval


if __name__ == "__main__":
    root = Tk()
    App(root)
