import pygame
import time
from singleton import Singleton
from gamestatemachine import GameStateMachine
from gamestate import MainMenuState, GameOverState
from inputhandler import TheInputHandler

class TheGame(metaclass=Singleton):
    window_x: int = 720
    window_y: int = 480
    surface: pygame.Surface
    clock: pygame.time.Clock
    score: int
    
    score: int
    running: bool

    font: pygame.font.Font
    gameStateMachine: GameStateMachine

    def init(self):
        pygame.init()
        TheInputHandler().init()
        self.surface = pygame.display.set_mode((self.window_x, self.window_y))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 64)
        self.gameStateMachine = GameStateMachine()
        self.gameStateMachine.pushState(MainMenuState())
        self.running = True
        self.score = 0

    def handleEvents(self):
        TheInputHandler().update()

    def update(self):
        self.handleEvents()
        self.surface.fill(pygame.Color(0, 0, 0))
        self.gameStateMachine.update()

    def quit(self):
        self.running = False

    def gameOver(self):
        self.gameStateMachine.changeState(GameOverState())

    def gameLoop(self):
        while(self.running):
            self.update()
            pygame.display.flip()

# Initialise game window

#snake = Snake(window_x / 2, window_y / 2)

#fruit = Fruit(random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10)
#score = 0

# Implement this into TheGame class

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont("times new roman", 50)
    game_over_surface = my_font.render("Your Score is : " + str(score), True, (235, 0, 3))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)

    game_window.fill((0, 0, 0))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(10)
    pygame.quit()
    quit()

def check_collision():
    if snake.get_head().x == 0 \
        or snake.get_head().x == window_x  \
        or snake.get_head().y == 0 \
        or snake.get_head().y == window_y\
        or snake.check_own_collision():
            game_over()

def fruit_collision():
    if fruit.position.x == snake.get_head().x and fruit.position.y == snake.get_head().y:
        fruit.set_random_position(window_x, window_y)
        snake.add_segment()
        globals()["score"] += 10

def loop():
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.move_to("UP")
                if event.key == pygame.K_DOWN:
                    snake.move_to("DOWN")
                if event.key == pygame.K_LEFT:
                    snake.move_to("LEFT")
                if event.key == pygame.K_RIGHT:
                    snake.move_to("RIGHT")

        fruit_collision()
        check_collision()
        game_window.fill((0, 0, 0))
        snake.move()
        show_score((255, 0, 0), "Times New Roman", 18)
        fruit.draw(game_window)
        snake.draw(game_window)
        pygame.display.flip()
