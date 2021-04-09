from random import randint
import turtle

fleets = [
    [2],
    [2, 3],
    [2, 3, 4],
    [2, 3, 3, 4],
    [2, 3, 4, 5],
    [2, 3, 3, 4, 5]
]

def start_menu():
    turtle.hideturtle()
    turtle.color("white")
    turtle.penup()
    turtle.speed(0)
    turtle.goto(0, 0)

    blast_screen("black")
    turtle.write("WELCOME TO BATTLESHIP",
                 align="center",
                 font=("Impact", 50, "normal"))
    turtle.goto(0, -20)
    turtle.write("Please use the console to select the size of your sea.",
                 align="center",
                 font=("Courier New", 15, "bold"))
    map_size = input("Please choose the size of your sea.\n"
                     "Type a number from 5-10: ")
    if map_size.isdigit():
        map_size = int(map_size)
        if 5 <= map_size <= 10:
            turtle.clear()
            blast_screen("black")
            print("Generating game.")
            draw_legend(map_size, 15, (0, 195), "ENEMY SEA", "red")
            draw_legend(map_size, 15, (0, -195), "YOUR SEA", "green")
            draw_sea(map_size, 15, (0, 195))
            draw_sea(map_size, 15, (0, -195))
            print("Game generated succesfully!")
            input("")
        else:
            print("Silly, that won't work!")
            start_menu()
    else:
        print("Silly, that won't work!")
        start_menu()


def place_boats(diameter):
    print()


def blast_screen(color):
    # fill the whole screen with light grey color
    last_pos = turtle.position()
    turtle.goto(500, 500)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.right(90)
        turtle.forward(1000)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(last_pos)


def draw_legend(size, scaling_factor, anchor, title, color):
    # unpack anchor coordinates
    x, y = anchor[0], anchor[1]
    tile = scaling_factor * 2

    # draw the outer boundary square
    turtle.color("black")
    radius = (size * scaling_factor)
    turtle.goto(x + radius, y + radius + tile)
    turtle.pendown()
    turtle.fillcolor("dark grey")
    turtle.begin_fill()
    for i in range(4):
        turtle.right(90)
        turtle.forward((radius * 2) + tile)
    turtle.end_fill()
    turtle.penup()
    turtle.color("white")

    # Write title
    turtle.goto(x - radius - tile, y + radius + tile - 5)
    turtle.color(color)
    turtle.write(title, font=("Impact", 20, "normal"))
    turtle.color("black")

    # Write alphabetical, horizontal coordinate axis
    turtle.goto(x + (radius * -1) + scaling_factor, y + radius)
    turtle.setheading(0)
    for i in range(size):
        turtle.write(chr(65 + i), align="center", font=("Courier New", 20, "normal"))
        turtle.forward(tile)

    # Write numerical, vertical coordinate axis
    turtle.goto(x + (radius * -1) - scaling_factor, y + radius - tile)
    turtle.setheading(-90)
    for i in range(size):
        turtle.write(str(i + 1), align="center", font=("Courier New", 20, "normal"))
        turtle.forward(tile)
    turtle.setheading(0)

def draw_sea(size, scaling_factor, anchor):
    # This function uses turtle to draw the boundaries of the game board.
    # The boundaries are a 600 x 600 square centered on the origin.
    # Therefore the corners are at (300, 300), (300, -300), (-300, -300),
    # and (-300, 300).
    # The value zero for turtle.speed actually makes the turtle move
    # infinitely quickly.

    # unpack anchor coordinates
    x, y = anchor[0], anchor[1]

    # draw the outer boundary square
    turtle.color("white")
    radius = size * scaling_factor
    turtle.goto(x + radius, y + radius)
    turtle.pendown()
    turtle.fillcolor("light blue")
    turtle.begin_fill()
    for i in range(4):
        turtle.right(90)
        turtle.forward(radius * 2)
    turtle.end_fill()
    turtle.penup()

    # draw the vertical grid lines
    for i in range(size):
        turtle.goto((radius * -1) + (scaling_factor * 2 * i) + x, radius + y)
        turtle.pendown()
        turtle.goto((radius * -1) + (scaling_factor * 2 * i) + x, (radius * -1) + y)
        turtle.penup()

    # draw the horizontal grid lines
    for i in range(size):
        turtle.goto(radius + x, (radius * -1) + (scaling_factor * 2 * i) + y)
        turtle.pendown()
        turtle.goto((radius * -1) + x, (radius * -1) + (scaling_factor * 2 * i) + y)
        turtle.penup()


def initialize_player_board():
    # initialize the user's board and make it 10 x 10. The board is a list
    # of 10 rows, with each row being a list of 10 zeros.
    user_board = []
    for i in range(10):
        user_board.append([0] * 10)


def initialize_enemy_board():
    # initialize the enemy's board and make it 10 x 10. The board is a list
    # of 10 rows, with each row being a list of 10 zeros.
    enemy_board = []
    for i in range(10):
        enemy_board.append([0] * 10)


# BEGIN THE GAME
start_menu()
