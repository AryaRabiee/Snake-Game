import pygame
import random


class Snake:
    def __init__(self, window):
        self.window = window
        self.snake_size = 17
        self.x = 300  
        self.y = 200 
        self.direction = "RIGHT"
        self.width = 640
        self.height = 480
        self.fruit_x = random.randint(0, 630)
        self.fruit_y = random.randint(0, 470)
        self.body = [(self.x , self.y)] 
        self.score = 0
        self.speed = 10

    def reset_game(self):
        self.x = 300  
        self.y = 200 
        self.direction = "RIGHT"
        self.body = [(self.x, self.y)]
        self.fruit_x = random.randint(0, 630)
        self.fruit_y = random.randint(0, 470)
        self.score = 0
        self.speed = 10

    def move(self):
        if self.direction == "LEFT":
            self.x -= 15
        elif self.direction == "RIGHT":
            self.x += 15
        elif self.direction == "UP":
            self.y -= 15
        elif self.direction == "DOWN":
            self.y += 15

        if self.x < 0:
            self.x = self.width - 15
        elif self.x > self.width:
            self.x = 0
        elif self.y < 0:
            self.y = self.height - 15
        elif self.y > self.height:
            self.y = 0

        self.body.insert(0, (self.x, self.y))

        if (self.x, self.y) in self.body[1:]:
            self.game_over()

        if len(self.body) > 1:
            self.body.pop()

    def spawn_snake(self):
        snake_color = (255, 255, 0)
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.snake_size, self.snake_size)
            pygame.draw.rect(self.window, snake_color, rect)

    def fruit(self):
        fruit_color = (255, 0, 0)
        rec = pygame.Rect(self.fruit_x, self.fruit_y, self.snake_size - 7, self.snake_size - 7)
        pygame.draw.rect(self.window, fruit_color, rec)

    def check_snake(self):
        if self.x <= self.fruit_x + self.snake_size and self.x + self.snake_size >= self.fruit_x and self.y <= self.fruit_y + self.snake_size and self.y + self.snake_size >= self.fruit_y:
            self.fruit_x = random.randint(0, 630)
            self.fruit_y = random.randint(0, 470)
            self.body.append(self.body[-1])
            return True
        return False

    def game_over(self):
        font = pygame.font.SysFont(None, 35)  
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 0, 0))
        

        game_over_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 3))
        restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 30))


        self.window.blit(game_over_text, game_over_rect)
        self.window.blit(restart_text, restart_rect)
        
        pygame.display.update()


        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return
                    elif event.key == pygame.K_r:
                        self.reset_game() 
                        waiting_for_input = False  


pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Snake_Game")
font = pygame.font.SysFont('None' , 25)

snake = Snake(window)

clock = pygame.time.Clock()

while True:
    window.fill((0, 128, 64)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if snake.direction == "RIGHT":
                if event.key == pygame.K_UP:
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.direction = "DOWN"
            elif snake.direction == "LEFT":
                if event.key == pygame.K_UP:
                    snake.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    snake.direction = "DOWN"
            elif snake.direction == "DOWN":
                if event.key == pygame.K_RIGHT:
                    snake.direction = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    snake.direction = "LEFT"
            elif snake.direction == "UP":
                if event.key == pygame.K_LEFT:
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    snake.direction = "RIGHT"
    score_text = font.render(f'Score:{snake.score}' , True , (0,0,0))
    window.blit(score_text , (10,10))
    if snake.check_snake():
        snake.score+=1
        snake.speed +=1
        if snake.speed > 30:
            snake.speed = 30
    
    snake.move()   
    snake.spawn_snake()
    snake.fruit()
    pygame.display.update()  
    clock.tick(snake.speed)  
