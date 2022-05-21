import time
import tkinter
from decimal import Decimal
from time import sleep
import get_screenshots_of_window
from multiprocessing import Process

import cv2

from ball import Ball

xSpeed = 30  # Decimal('3')
ySpeed = 1  # Decimal('3')
gravity = 0.1  # Decimal('0.05')
energy_loss = 0.85  # Decimal('0.85')

WIDTH, HEIGHT = 600, 300

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

window.title('Catch the ball')
window.resizable(False, False)

# canvas.create_line(WIDTH // 3, 2, WIDTH // 3 * 2, 2, fill="red")
# canvas.create_line(WIDTH // 3, HEIGHT, WIDTH // 3 * 2, HEIGHT, fill="red")
canvas.create_line(WIDTH // 3, 0, WIDTH // 3, HEIGHT, fill="red")
canvas.create_line(WIDTH // 3 * 2, 0, WIDTH // 3 * 2, HEIGHT, fill="red")
# canvas.create_line(0, HEIGHT // 2, WIDTH, HEIGHT // 2, fill="green")

ball = Ball(canvas=canvas,
            x=WIDTH // 2 - 5,
            y=HEIGHT // 2 - 5,
            diameter=10,
            xvelocity=xSpeed,
            yvelocity=ySpeed,
            color='black',
            width=WIDTH,
            height=HEIGHT)


def main():
    # ball = canvas.create_oval(WIDTH // 2 - 5, HEIGHT // 2 - 5, WIDTH // 2 + 5, HEIGHT // 2 + 5, fill='black')
    # ball = canvas.create_oval(5, 5, 15, 15, fill='black')

    # move the ball
    ball.move_ball(gravity=gravity)
    # ball.canvas.after(20, ball.move_ball(gravity=gravity))
    canvas.after(20, ball.move_ball(gravity=gravity))
    window.mainloop()


if __name__ == '__main__':
    main()
    '''
    while p1.is_alive():
        frame = get_screenshots_of_window.get_screen()
        cv2.waitKey(1)
        cv2.imshow('frame', frame)
    '''
