class Foodandaccelerate():

    def __init__(self):
        pass

    def spawing(self):
        global food_flag
        global food_pos
        if food_flag == 0:
            food_pos = [random.randrange(1, (g_interface_x//10)) * 10, random.randrange(1, (g_interface_y//10)) * 10] 
    def accelerate(self):
        global score
        global speed
        global food_flag
        if speed <= 27 and food_flag == 0 :
        
            speed += 100
    def reset(self):
        global food_flag
        food_flag = 1