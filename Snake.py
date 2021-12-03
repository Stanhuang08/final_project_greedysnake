class Snake():
    def __init__(self):
        pass

    def turn_around(self):
        global direction 
        global change_to 
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
            
    
    def growing(self):
        global snake_body
        global score
        global food_flag
        snake_body.insert(0, list(snake_head))
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
           score += 1
           food_flag = 0
        else:
           snake_body.pop()

    def moving(self):
        global direction
        global snack_pos
        if direction == 'UP':
           snake_head[1] -= 10
        if direction == 'DOWN':
           snake_head[1] += 10
        if direction == 'LEFT':
           snake_head[0] -= 10
        if direction == 'RIGHT':
           snake_head[0] += 10