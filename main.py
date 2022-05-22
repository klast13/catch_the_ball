import timeit
import tkinter
from multiprocessing import Process
from time import sleep

import cv2
import numpy as np

import get_screenshots_of_window

xSpeed = 10
ySpeed = 1
gravity = 0.1
energy_loss = 0.85

WIDTH, HEIGHT = 600, 600

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

window.title('Catch the ball')
window.resizable(False, False)

# canvas.create_line(WIDTH // 3, 2, WIDTH // 3 * 2, 2, fill="red")
# canvas.create_line(WIDTH // 3, HEIGHT, WIDTH // 3 * 2, HEIGHT, fill="red")
# canvas.create_line(WIDTH // 3, 0, WIDTH // 3, HEIGHT, fill="red")
# canvas.create_line(WIDTH // 3 * 2, 0, WIDTH // 3 * 2, HEIGHT, fill="red")
# canvas.create_line(0, HEIGHT // 2, WIDTH, HEIGHT // 2, fill="green")


def main():

    #  ball = canvas.create_oval(WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10, fill='black')
    ball = canvas.create_oval(0, 0, 10, 10, fill='black')  # d ~= 14.14

    # move the ball
    def move_ball():

        global xSpeed, ySpeed, gravity
        ySpeed += gravity

        (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

        # костыль, чтобы шар не завис в границах
        if bottomPos + ySpeed > HEIGHT:
            canvas.move(ball, xSpeed, HEIGHT - bottomPos)
        elif topPos + ySpeed < 0:
            canvas.move(ball, xSpeed, 0 - topPos)
        elif rightPos + xSpeed > WIDTH:
            canvas.move(ball, WIDTH - rightPos, ySpeed)
        elif leftPos + xSpeed < 0:
            canvas.move(ball, 0 - leftPos, ySpeed)
        else:
            canvas.move(ball, xSpeed, ySpeed)

        #print(ySpeed, bottomPos)
        #print(xSpeed, rightPos)
        (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

        # при любом касании уменьшаем скорость и направление
        if leftPos <= 0 or rightPos >= WIDTH:
            xSpeed = -xSpeed * energy_loss
            ySpeed *= energy_loss
        if topPos <= 0 or bottomPos >= HEIGHT:
            ySpeed = -ySpeed * energy_loss
            xSpeed *= energy_loss

        canvas.after(20, move_ball)

    canvas.after(20, move_ball)
    window.mainloop()


if __name__ == '__main__':
    proc1 = Process(target=main)
    proc1.start()
    sleep(0.5)
    prev_time, prev_x, prev_y = 0, 0, 0
    while proc1.is_alive():
        frame = get_screenshots_of_window.get_screen()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, 1, 1000, param1=100, param2=1, maxRadius=20)
        if circles is None:
            print('None')
            prev_time, prev_x, prev_y = 0, 0, 0
        else:
            #circles = np.uint16(np.around(circles))
            print('coords:', circles[0][0], 'time:', (timeit.default_timer() - prev_time) if prev_time else None,
                  'Vx =', ((circles[0][0][0] - prev_x) / (timeit.default_timer() - prev_time)) if prev_x else None,
                  'Vy =', ((circles[0][0][1] - prev_y) / (timeit.default_timer() - prev_time)) if prev_y else None)
            prev_time = timeit.default_timer()
            prev_x = circles[0][0][0]
            prev_y = circles[0][0][1]
        cv2.waitKey(10)
        cv2.imshow('frame', frame)



