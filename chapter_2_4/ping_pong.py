import turtle
from random import choice, randint

WINDOWS_BG_COLOR: str = "#013220"
WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 600
GAME_BOARD_WIDTH: int = (WINDOW_WIDTH // 2) - 60
GAME_BOARD_HEIGHT: int = (WINDOW_HEIGHT // 2) - 60
STRETCH_LEN: int = 1
STRETCH_WID: int = 5
PLAYER_1_COLOR: str = "#ddd"
PLAYER_2_COLOR: str = "orange"
PLAYER_1_SIDE: int = -GAME_BOARD_WIDTH + 50
PLAYER_2_SIDE: int = GAME_BOARD_WIDTH - 50
GAME_BOARD_BG_COLOR: str = "#44944A"
GAME_BOARD_ELEMENTS_COLOR: str = "white"
FONT: tuple[str, int, str] = ("Arial", 36, "bold")
BALL_COLOR: str = "red"
BALL_SHAPE: str = "circle"
INITIAL_BALL_DX: int = 5
INITIAL_BALL_DY: int = -5
SPEED_INCREMENT: int = 10
BALL_SPEEDS: list[int | float] = [-6, 5.5, 5.5, 6]
ROCKET_SPEED: int = 20
ROCKET_SHAPE: str = "square"
MAX_Y: int = GAME_BOARD_HEIGHT - 10
MIN_Y: int = -GAME_BOARD_HEIGHT + 10
MAX_X: int = GAME_BOARD_WIDTH - 10
MIN_X: int = -GAME_BOARD_WIDTH + 10
ROCKET_MAX_Y: int = GAME_BOARD_HEIGHT - 50
ROCKET_MIN_Y: int = -GAME_BOARD_HEIGHT + 50
ROCKET_HALF_HEIGHT: int = 50
ROCKET_HALF_WIDTH: int = 10


def create_game_board():
    game_board = turtle.Turtle()
    game_board.speed(0)
    game_board.color(GAME_BOARD_BG_COLOR)
    game_board.begin_fill()
    game_board.goto(-GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
    game_board.goto(GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
    game_board.goto(GAME_BOARD_WIDTH, -GAME_BOARD_HEIGHT)
    game_board.goto(-GAME_BOARD_WIDTH, -GAME_BOARD_HEIGHT)
    game_board.goto(-GAME_BOARD_WIDTH, GAME_BOARD_HEIGHT)
    game_board.end_fill()

    # Элементы игрового поля
    game_board.goto(0, GAME_BOARD_HEIGHT)
    game_board.color(GAME_BOARD_ELEMENTS_COLOR)
    game_board.setheading(270)
    for i in range(25):
        if i % 2 == 0:
            game_board.forward(24)
        else:
            game_board.up()
            game_board.forward(24)
            game_board.down()
    game_board.hideturtle()


def create_rocket(color, x_pos):
    rocket = turtle.Turtle()
    rocket.color(color)
    rocket.shape(ROCKET_SHAPE)
    rocket.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
    rocket.penup()
    rocket.goto(x_pos, 0)
    rocket.setheading(0)
    return rocket


def score_display(color, x_pos):
    score_field = turtle.Turtle(visible=False)
    score_field.color(color)
    score_field.penup()
    score_field.setposition(x_pos, GAME_BOARD_HEIGHT)
    score_field.write(0, font=FONT)
    return score_field


def move_rocket(rocket, direction):
    y = rocket.ycor() + direction * ROCKET_SPEED
    if y > ROCKET_MAX_Y:
        y = ROCKET_MAX_Y
    elif y < ROCKET_MIN_Y:
        y = ROCKET_MIN_Y
    rocket.sety(y)


def move_up():
    move_rocket(rocket_a, 1)


def move_down():
    move_rocket(rocket_a, -1)


def move_up_b():
    move_rocket(rocket_b, 1)


def move_down_b():
    move_rocket(rocket_b, -1)


def update_score(score_field, score):
    score_field.clear()
    score_field.write(score, font=FONT)


def check_collision(rocket, curr_ball):
    rocket_b_top = rocket.ycor() + ROCKET_HALF_HEIGHT
    rocket_b_bottom = rocket.ycor() - ROCKET_HALF_HEIGHT
    rocket_a_right = rocket.xcor() + ROCKET_HALF_WIDTH
    rocket_a_left = rocket.xcor() - ROCKET_HALF_WIDTH

    return (
            rocket_b_bottom < curr_ball.ycor() < rocket_b_top
            and rocket_a_left < curr_ball.xcor() < rocket_a_right
    )


def game_loop():
    global player_1_score, player_2_score

    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= MAX_Y:
        ball.dy *= -1

    if ball.ycor() <= MIN_Y:
        ball.dy *= -1

    if ball.xcor() >= MAX_X:
        player_1_score += 1
        update_score(player_1_score_info, player_1_score)
        reset_ball()

    if ball.xcor() <= MIN_X:
        player_2_score += 1
        update_score(player_2_score_info, player_2_score)
        reset_ball()

    if check_collision(rocket_b, ball):
        ball.dx *= -1

    if check_collision(rocket_a, ball):
        ball.dx *= -1

    window.ontimer(game_loop, SPEED_INCREMENT)


def reset_ball():
    ball.goto(0, randint(-WINDOW_HEIGHT // 2, WINDOW_HEIGHT // 2))
    ball.dx = choice(BALL_SPEEDS)
    ball.dy = choice(BALL_SPEEDS)


if __name__ == "__main__":
    # Инициализация окна
    window = turtle.Screen()
    window.title("Ping-Pong")
    window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    window.bgcolor(WINDOWS_BG_COLOR)
    window.tracer(1)

    create_game_board()

    rocket_a = create_rocket(PLAYER_1_COLOR, PLAYER_1_SIDE)
    rocket_b = create_rocket(PLAYER_2_COLOR, PLAYER_2_SIDE)

    player_1_score = 0
    player_2_score = 0
    player_1_score_info = score_display(
        PLAYER_1_COLOR, -GAME_BOARD_WIDTH + GAME_BOARD_WIDTH // 2
    )
    player_2_score_info = score_display(
        PLAYER_2_COLOR, GAME_BOARD_WIDTH - GAME_BOARD_WIDTH // 2
    )

    # Инициализация мяча
    ball = turtle.Turtle()
    ball.shape(BALL_SHAPE)
    ball.speed(0)
    ball.color(BALL_COLOR)
    ball.dx = INITIAL_BALL_DX
    ball.dy = INITIAL_BALL_DY
    ball.penup()

    # Запуск прослушивателя событий
    window.listen()
    window.onkeypress(move_up, "w")
    window.onkeypress(move_down, "s")
    window.onkeypress(move_up_b, "Up")
    window.onkeypress(move_down_b, "Down")

    # Запуск игрового процесса
    game_loop()
    window.mainloop()
