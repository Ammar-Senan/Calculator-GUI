import tkinter as tk
import random

# إعداد النافذة
root = tk.Tk()
root.title("لعبة الحنش 🐍")
root.resizable(False, False)

# إعداد القماش (Canvas)
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100     # سرعة اللعبة (كلما قل الرقم زادت السرعة)
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#2ecc71"
FOOD_COLOR = "#e74c3c"
BACKGROUND_COLOR = "#2c3e50"

canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# متغيرات اللعبة
snake = []
snake_coordinates = []
food = None
score = 0

# صندوق النقاط
label = tk.Label(root, text=f"النقاط: {score}", font=("Arial", 16), bg="#34495e", fg="white")
label.pack(fill="x")

# دوال اللعبة
def create_snake():
    global snake, snake_coordinates
    snake = []
    snake_coordinates = []
    for i in range(BODY_PARTS):
        snake_coordinates.append([0, 0])
        part = canvas.create_rectangle(0, 0, SPACE_SIZE, SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
        snake.append(part)

def create_food():
    global food
    x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
    y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
    food = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn():
    global food, score

    x, y = snake_coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake_coordinates.insert(0, (x, y))
    part = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.insert(0, part)

    # أكل التفاحة
    if x == canvas.coords(food)[0] and y == canvas.coords(food)[1]:
        score += 1
        label.config(text=f"النقاط: {score}")
        canvas.delete(food)
        create_food()
    else:
        del snake_coordinates[-1]
        canvas.delete(snake[-1])
        del snake[-1]

    if check_collisions():
        game_over()
    else:
        root.after(SPEED, next_turn)

def change_direction(new_direction):
    global direction
    if new_direction == "left" and direction != "right":
        direction = new_direction
    elif new_direction == "right" and direction != "left":
        direction = new_direction
    elif new_direction == "up" and direction != "down":
        direction = new_direction
    elif new_direction == "down" and direction != "up":
        direction = new_direction

def check_collisions():
    x, y = snake_coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake_coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete("all")
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2,
                       text=f"انتهت اللعبة!\nالنقاط: {score}",
                       fill="white", font=("Arial", 24, "bold"))

# بداية اللعبة
direction = "right"
create_snake()
create_food()
next_turn()

# التحكم
root.bind("<Left>", lambda e: change_direction("left"))
root.bind("<Right>", lambda e: change_direction("right"))
root.bind("<Up>", lambda e: change_direction("up"))
root.bind("<Down>", lambda e: change_direction("down"))

root.mainloop()
