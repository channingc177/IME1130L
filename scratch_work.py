import turtle
from sys import exit
from random import randint

player_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    (-150, -330),
]
enemy_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    (-150, 30),
]

player_fleet = [
    ["Patrol Boat", ["k0", "k0"], [1, 1], False],
    ["Destroyer", ["k0", "k0", "k0"], [1, 1, 1], False],
    ["Cruiser", ["k0", "k0", "k0", "k0"], [1, 1, 1, 1], False],
    ["Battleship", ["k0", "k0", "k0", "k0", "k0"], [1, 1, 1, 1, 1], False],
    ["Submarine", ["k0", "k0", "k0"], [1, 1, 1], False],
]

enemy_fleet = [
    ["Patrol Boat", ["k0", "k0"], [1, 1], False],
    ["Destroyer", ["k0", "k0", "k0"], [1, 1, 1], False],
    ["Cruiser", ["k0", "k0", "k0", "k0"], [1, 1, 1, 1], False],
    ["Battleship", ["k0", "k0", "k0", "k0", "k0"], [1, 1, 1, 1, 1], False],
    ["Submarine", ["k0", "k0", "k0"], [1, 1, 1], False],
]
player_guesses, enemy_guesses = [], []
enemy_brain = [
    ["k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0"],
    ["k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0", "k0"]
]


def draw_menu(anchor):
    turtle.goto(anchor)


def print_board(board):
    for row in board:
        print(row)
    print()


def reset_board(board):
    for i in range(0, 10):
        board[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def index_to_tag(row, col):
    tag = ""
    tag += chr(65 + row)
    tag += str(col + 1)
    return tag


def check_tile(board, tag):
    # unpack tag into alphabetical and numerical component
    tag_let = tag[0]
    tag_num = int(tag[1:])

    # check board state at corresponding index
    row = ord(tag_let) - 65
    col = tag_num - 1
    tile_state = board[row][col]
    return tile_state


def change_tile(board, tag, value):
    # unpack tag into alphabetical and numerical component
    tag_let = tag[0]
    tag_num = int(tag[1:])

    # check board state at corresponding index
    row = ord(tag_let) - 65
    col = tag_num - 1
    board[row][col] = value


def draw_menu():
    turtle.showturtle()
    turtle.hideturtle()
    turtle.pensize(1)
    turtle.color("white")
    turtle.speed(0)
    ts = turtle.getscreen()
    ts.bgcolor("black")
    turtle.write("WELCOME TO BATTLESHIP", font=("Impact", 70, "normal"), align="Center")