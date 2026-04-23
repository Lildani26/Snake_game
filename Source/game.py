import random
import tkinter as tk
from snake import Snake
from food import Food

#game settings
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 150
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#A9A9A9"

#calling tkinker to create a visual representation 
window = tk.Tk()
window.title("Snake game")
window.resizable(False, False)


#start variables
score = 0
direction = 'right'

#creating the gameboard where the snake will move
canvas = tk.Canvas (window, bg = BACKGROUND_COLOR, height= GAME_HEIGHT, width= GAME_WIDTH)
canvas.pack()

#create a lable where it will show the variable 'score' starting at 0
label  = tk.Label(window, text = "Score : {}".format(score),font = ('Impact', 40))
label.pack()


#game funtions
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":   #to tell the game where will be the next coordinate
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    new_head = (x,y)

    snake.coordinates.insert(0, new_head) #create the new head of the snake

    #check if the turn made a collision to end the game
    if check_collision(snake):
        game_over()
        return

    square = canvas.create_rectangle(
        x, y,
        x + SPACE_SIZE,
        y + SPACE_SIZE,
        fill= SNAKE_COLOR,
        tag= "snake"

    )

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score 
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else: 
        del snake.coordinates[-1] #deletes the last coordinate on the list (like the tail)
        canvas.delete(snake.squares[-1])
        del snake.squares [-1]
        
        #repeat the funtion over and over creating this ilusion of moving as long as check collision is false      
    window.after(SPEED, next_turn, snake, food) #the speed of moving is set by the cons SPEED


def change_direction(new_direccion):
    global direction #check what is the current dirrection

    #check what is the new direction and set it as the direction
    if new_direccion == 'left':
        if direction != 'right': #to not make a 180 degrees turn, make no sense
            direction = new_direccion 

    elif new_direccion == 'right':
        if direction != 'left':
            direction = new_direccion

    elif new_direccion == 'up':
        if direction != 'down':
            direction = new_direccion

    elif new_direccion == 'down':
        if direction != 'up':
            direction = new_direccion


def check_collision (snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH: #if the snake goes out of the dimension of the screen = game over
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]: #if the head of the snake is the same as a different part means it collision with its tail= game over
            return True
    
    return False

def game_over():
    canvas.delete("all")
    canvas.create_text (canvas.winfo_width()/2, canvas.winfo_height()/2,
                        font= ('Impact',40),
                        text= "GAME OVER",
                        fill= "red", 
                        tag= "game_over")

#making the window appear in the middle of the screen
window.update()
window.eval('tk::PlaceWindow . center')

#keyboard events
window.bind('<Left>', lambda event : change_direction ('left'))
window.bind('<Right>', lambda event : change_direction ('right'))
window.bind('<Up>', lambda event : change_direction ('up'))
window.bind('<Down>', lambda event : change_direction ('down'))

snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()
