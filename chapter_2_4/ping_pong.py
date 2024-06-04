import turtle
from random import choice, randint

WINDOWS_BG_COLOR: str = "gray"

GAME_BOARD_WIDTH: int = 600
GAME_BOARD_HEIGHT: int = 300

STRETCH_LEN: int = 1
STRETCH_WID: int = 5

PLAYER_1_COLOR: str = "yellow"
PLAYER_2_COLOR: str = "black"

PLAYER_1_SIDE: int = -GAME_BOARD_WIDTH + 50
PLAYER_2_SIDE: int = GAME_BOARD_WIDTH - 50

player_1_score: int = 0
player_2_score: int = 0

GAME_BOARD_BG_COLOR: str = "green"
GAME_BOARD_ELEMENTS_COLOR: str = "white"

FONT: tuple[str, int, str] = ("Arial", 44, "bold")

# Основное окно
window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=0.8, height=0.8)
window.bgcolor(WINDOWS_BG_COLOR)
window.tracer(1)

# Игровое поле
border = turtle.Turtle()
border.speed(0)
border.color(GAME_BOARD_BG_COLOR)
border.begin_fill()
border.goto(-GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
border.goto(GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
border.goto(GAME_BOARD_WIDTH, -GAME_BOARD_HEIGHT)
border.goto(-GAME_BOARD_WIDTH, -GAME_BOARD_HEIGHT)
border.goto(-GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
border.end_fill()

# Элементы игрового поля
border.goto(0, GAME_BOARD_HEIGHT)
border.color(GAME_BOARD_ELEMENTS_COLOR)
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

# Игрок 1
rocket_a = turtle.Turtle()
rocket_a.color(PLAYER_1_COLOR)
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
rocket_a.penup()
rocket_a.goto(PLAYER_1_SIDE, 0)

player_1_score = 0
s1 = turtle.Turtle(visible=False)
s1.color(PLAYER_1_COLOR)
s1.penup()
s1.setposition(-GAME_BOARD_WIDTH + GAME_BOARD_WIDTH // 2, GAME_BOARD_HEIGHT)
s1.write(player_1_score, font=FONT)

# Игрок 2
rocket_b = turtle.Turtle()
rocket_b.speed(3)
rocket_b.color(PLAYER_2_COLOR)
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=STRETCH_LEN, stretch_wid=STRETCH_WID)
rocket_b.penup()
rocket_b.goto(PLAYER_2_SIDE, 0)

player_2_score = 0
s2 = turtle.Turtle(visible=False)
s2.color(PLAYER_2_COLOR)
s2.penup()
s2.setposition(GAME_BOARD_WIDTH - GAME_BOARD_WIDTH // 2, GAME_BOARD_HEIGHT)
s2.write(player_1_score, font=FONT)


def move_up():
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


# Мяч
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.dx = 3
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

# window.mainloop()

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        player_2_score += 1
        s2.clear()
        s2.write(player_2_score, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        player_1_score += 1
        s1.clear()
        s1.write(player_1_score, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if (
            ball.ycor() >= rocket_b.ycor() - 50
            and ball.ycor() <= rocket_b.ycor() + 50
            and ball.xcor() >= rocket_b.xcor() - 5
            and ball.xcor() <= rocket_b.xcor() + 5
    ):
        ball.dx = -ball.dx

    if (
            ball.ycor() >= rocket_a.ycor() - 50
            and ball.ycor() <= rocket_a.ycor() + 50
            and ball.xcor() >= rocket_a.xcor() - 5
            and ball.xcor() <= rocket_a.xcor() + 5
    ):
        ball.dx = -ball.dx

window.mainloop()
