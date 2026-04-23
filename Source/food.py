import random
class Food:
    def __init__(self):

        valid_x = GAME_WIDTH//SPACE_SIZE #to make sure the food is drop ina  exact cell.
        valid_y = GAME_HEIGHT//SPACE_SIZE

        x = random.randint(0, valid_x -1) * SPACE_SIZE
        y = random.randint(0, valid_y -1) * SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_rectangle(
            x,y,
            x+SPACE_SIZE, y+SPACE_SIZE, 
            fill= FOOD_COLOR, 
            tag="food")
