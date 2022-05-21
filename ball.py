import tkinter


class Ball:

    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color, width, height):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, x + diameter, y + diameter, fill=color)
        self.xSpeed = xvelocity
        self.ySpeed = yvelocity
        self.energy_loss = 0.85
        self.WIDTH = width
        self.HEIGHT = height

    def move_ball(self, gravity):
        self.ySpeed += gravity

        (leftPos, topPos, rightPos, bottomPos) = self.canvas.coords(self.image)

        # костыль, чтобы шар не завис в границах
        if bottomPos + self.ySpeed > self.HEIGHT:
            self.canvas.move(self.image, self.xSpeed, self.HEIGHT - bottomPos)
        elif topPos + self.ySpeed < 0:
            self.canvas.move(self.image, self.xSpeed, 0 - topPos)
        elif rightPos + self.xSpeed > self.WIDTH:
            self.canvas.move(self.image, self.WIDTH - rightPos, self.ySpeed)
        elif leftPos + self.xSpeed < 0:
            self.canvas.move(self.image, 0 - leftPos, self.ySpeed)
        else:
            self.canvas.move(self.image, self.xSpeed, self.ySpeed)

        (leftPos, topPos, rightPos, bottomPos) = self.canvas.coords(self.image)
        # print(ySpeed, bottomPos)
        # print(xSpeed, rightPos)

        # при любом касании уменьшаем скорость и направление
        if leftPos <= 0 or rightPos >= self.WIDTH:
            self.xSpeed = -self.xSpeed * self.energy_loss
            self.ySpeed *= self.energy_loss
        if topPos <= 0 or bottomPos >= self.HEIGHT:
            self.ySpeed = -self.ySpeed * self.energy_loss
            self.xSpeed *= self.energy_loss

        self.canvas.after(20, self.move_ball(gravity))


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
print(ball.image)
print(ball.xSpeed)
