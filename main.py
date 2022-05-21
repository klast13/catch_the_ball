import tkinter
from decimal import Decimal

import cv2

xSpeed = 10  # Decimal('3')
ySpeed = 1  # Decimal('3')
gravity = 0.1  # Decimal('0.05')
energy_loss = 0.85  # Decimal('0.85')

WIDTH, HEIGHT = 600, 600

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

window.title('Catch the ball')
window.resizable(False, False)

# canvas.create_line(WIDTH // 3, 2, WIDTH // 3 * 2, 2, fill="red")
# canvas.create_line(WIDTH // 3, HEIGHT, WIDTH // 3 * 2, HEIGHT, fill="red")
canvas.create_line(WIDTH // 3, 0, WIDTH // 3, HEIGHT, fill="red")
canvas.create_line(WIDTH // 3 * 2, 0, WIDTH // 3 * 2, HEIGHT, fill="red")
canvas.create_line(0, HEIGHT // 2, WIDTH, HEIGHT // 2, fill="green")


def main():

    #  ball = canvas.create_oval(WIDTH // 2 - 10, HEIGHT // 2 - 10, WIDTH // 2 + 10, HEIGHT // 2 + 10, fill='black')
    ball = canvas.create_oval(5, 5, 15, 15, fill='black')

    # move the ball
    def move_ball():

        global xSpeed, ySpeed, gravity
        ySpeed += gravity
        #canvas.move(ball, xSpeed, ySpeed)

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
        print(xSpeed, rightPos)
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
    main()
