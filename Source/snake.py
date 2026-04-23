import tkinter as tk

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS): #initializing the snake at the top left corner
            self.coordinates.append([0, 0])

        for x , y in self.coordinates: #creating the head of the snake at a x, y coordinate
            square = canvas.create_rectangle(
                x,y,
                x + SPACE_SIZE, y + SPACE_SIZE,
                fill= SNAKE_COLOR,
                tag="snake")
            self.squares.append(square)
