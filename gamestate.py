from menubutton import MenuButton
from typing import List, Callable
from abc import ABC, abstractmethod
from gameobject import GameObject, GameObjectLoader
from snake import Snake
from fruit import Fruit

class GameState(ABC):
    gameObjects: List[GameObject]

    def __init__(self) -> None:
        super().__init__()
        self.gameObjects = list[GameObject]()

    @abstractmethod
    def onEnter(self):
        pass

    @abstractmethod
    def onExit(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

class MenuState(GameState):
    callbacks: List[Callable]

    def addCallback(self, cb:Callable):
        self.callbacks.append(cb)

    def executeCallback(self, index:int):
        self.callbacks[index]()

class MainMenuState(MenuState):
    def onEnter(self):
        playButton = MenuButton("Play", 0, 0, 0)
        playButton.load(GameObjectLoader(100, 100, 200, 80, 255, 0, 0))
        playButton.setCallback(self.menuToPlay)
        playButton.setHoverBackground(0, 255, 0)

        exitButton = MenuButton("Exit", 0, 0, 0)
        exitButton.load(GameObjectLoader(100, 300, 200, 80, 255, 0, 0))
        exitButton.setCallback(self.exit)
        exitButton.setHoverBackground(200, 50, 50)

        self.gameObjects.append(playButton)
        self.gameObjects.append(exitButton)

        print("Entering Main Menu")
    
    def onExit(self):
        print("Exiting Main Menu")

    def update(self):
        for gameObj in self.gameObjects:
            gameObj.update()

    def menuToPlay(self):
        from game import TheGame
        TheGame().gameStateMachine.changeState(PlayState())

    def exit(self):
        from game import TheGame
        self.onExit()
        TheGame().quit()

class PauseState(MenuState):
    def onEnter(self):
        mainBtn = MenuButton("Menu", 0, 0, 0)
        mainBtn.load(GameObjectLoader(100, 100, 200, 80, 255, 0, 0))
        mainBtn.setHoverBackground(0, 255, 0)
        mainBtn.setCallback(self.toMenu)

        resumeBtn = MenuButton("Resume", 0, 0, 0)
        resumeBtn.load(GameObjectLoader(100, 300, 200, 80, 255, 0, 0))
        resumeBtn.setHoverBackground(0, 255, 0)
        resumeBtn.setCallback(self.resume)

        self.gameObjects.append(mainBtn)
        self.gameObjects.append(resumeBtn)

        print("Entering Pause Menu")
    
    def onExit(self):
        print("Exiting PauseMenu")

    def toMenu(self):
        from game import TheGame
        TheGame().gameStateMachine.popState()
        TheGame().gameStateMachine.changeState(MainMenuState())

    def resume(self):
        from game import TheGame
        TheGame().gameStateMachine.popState()
    
    def update(self):
        for gameObj in self.gameObjects:
            gameObj.update()

class PlayState(GameState):
    snake: Snake
    fruit: Fruit

    def onEnter(self):
        from game import TheGame

        self.snake = Snake()
        self.fruit = Fruit()

        self.fruit.load(GameObjectLoader(0, 0, 10, 10, 0, 0, 255))
        self.fruit.setRandomPosition(TheGame().window_x, TheGame().window_y)

        self.gameObjects.append(self.snake)
        self.gameObjects.append(self.fruit)

        print("Entering Play State")
    
    def onExit(self):
        print("Exiting Play State")
    
    def handleEvents(self):
        from inputhandler import TheInputHandler, Keyboard
        from game import TheGame
        if TheInputHandler().keyDown[Keyboard.ESC]:
            TheGame().gameStateMachine.pushState(PauseState())

    def objCollision(self, p1:GameObject, p2:GameObject) -> bool:
        leftA = p1.getX()
        rightA = p1.getX() + p1.width
        topA = p1.getY()
        bottomA = p1.getY() + p1.height

        leftB = p2.getX()
        rightB = p2.getX() + p2.width
        topB = p2.getY()
        bottomB = p2.getY() + p2.height

        if bottomA <= topB:
            return False
        if topA >= bottomB:
            return False
        if rightA <= leftB:
            return False
        if leftA >= rightB:
            return False
        
        return True

    def update(self):
        from game import TheGame
        self.handleEvents()

        if(self.objCollision(self.fruit, self.snake)):
            self.fruit.setRandomPosition(TheGame().window_x, TheGame().window_y)
            self.snake.addSegment()
            TheGame().score += 10

        for gameObj in self.gameObjects:
            gameObj.update()
    
class GameOverState(MenuState):
    def onEnter(self):
        from game import TheGame
        gameOverText = MenuButton("GAME OVER!", 255, 0, 0)
        gameOverText.load(GameObjectLoader(100, 10, 500, 80, 0, 0, 0))

        score = MenuButton(f"Your score is: {str(TheGame().score)}", 255, 0, 0)
        score.load(GameObjectLoader(100, 200, 500, 80, 0, 0, 0))

        menuBtn = MenuButton("Menu", 0, 0, 0)
        menuBtn.setHoverBackground(0, 255, 0)
        menuBtn.load(GameObjectLoader(100, 100, 300, 80, 255, 0, 0))
        menuBtn.setCallback(self.toMenu)

        playBtn = MenuButton("Play again", 0, 0, 0)
        playBtn.setHoverBackground(0, 255, 0)
        playBtn.load(GameObjectLoader(100, 300, 300, 80, 255, 0, 0))
        playBtn.setCallback(self.toPlay)

        self.gameObjects.append(menuBtn)
        self.gameObjects.append(playBtn)
        self.gameObjects.append(score)
        self.gameObjects.append(gameOverText)

        print("Entering GameOver Menu")
    
    def toMenu(self):
        from game import TheGame
        TheGame().gameStateMachine.changeState(MainMenuState())

    def toPlay(self):
        from game import TheGame
        TheGame().gameStateMachine.changeState(PlayState())

    def onExit(self):
        print("Exiting GameOver Menu")
    
    def update(self):
        for gameObj in self.gameObjects:
            gameObj.update()