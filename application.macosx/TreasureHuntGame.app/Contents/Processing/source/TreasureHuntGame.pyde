add_library('minim')
player = Minim(this)

import random

class Creature:
   
    def __init__(self,x,y,g,r,obstruction, frameNum):
   
        self.x=x
        self.y=y
        self.g=g
        self.r= r
        self.vx=0
        self.vy=1
        self.obstruction = obstruction
        self.frame= 0 #frame being displayed
        self.frameNum = frameNum
        self.alive = 1
 

class Player(Creature):
   
    def __init__(self,x,y,g,r,obstruction, frameNum, br , bl,imgNum):
        Creature.__init__(self,x,y,g,r,obstruction, frameNum)
        self.keyHandler = { LEFT:False, UP:False, RIGHT:False }
        self.br = br
        self.bl = bl
        self.powerJump = 0
        self.imgNum = imgNum
       
       
                               
    def display1(self):

        if self.keyHandler[RIGHT] == False and self.keyHandler[LEFT] == False:
            image(imageCh1,self.x - 40 , self.y + 20 , 100, 100, self.frame * 280, 0, (self.frame + 1) * 280, 330)
       
       
        elif self.keyHandler[RIGHT] == True:
            image(imageCh1,self.x - 40 , self.y  + 20, 100, 100 , self.frame * 280, 0, (self.frame + 1) * 280, 330)

        elif self.keyHandler[LEFT] == True:
            image(imageCh1, self.x - 40 , self.y + 20 , 100,100, (self.frame + 1) * 280, 0, self.frame * 280,330)
           
    def display2(self):

        if self.keyHandler[RIGHT] == False and self.keyHandler[LEFT] == False:
            image(imageCh2,self.x - 40 , self.y + 20 , 100, 120, self.frame * 250, 0, (self.frame + 1) * 250, 330)
       
       
        elif self.keyHandler[RIGHT] == True:
            image(imageCh2,self.x - 40 , self.y  + 20, 100, 120 , self.frame * 250, 0, (self.frame + 1) * 250, 330)

        elif self.keyHandler[LEFT] == True:
            image(imageCh2, self.x - 40 , self.y + 20 , 100,120, (self.frame + 1) * 250, 0, self.frame * 250,330)    
           
   
       
        #rect(self.x,self.y, 100 , 100)
       
    def gravity(self):
       
        if self.y + 100 < self.g :
            self.vy=self.vy+0.5
           
        else:
            self.vy=0
           
        for p in self.obstruction:
            if p.x <= self.x < p.x + p.w and self.y + 100 <= p.y:
                self.g = p.y
                return
           
           
        global currentLevel
       
        if currentLevel == 1:
            self.g = game.g
           
        else:
            self.g = game2.g
       
   
    def update(self):
       
            self.gravity()
               
               
            if self.keyHandler[RIGHT]== True and  self.bl  < self.x + self.r < self.br - self.r:
                self.vx+=0.25
               
            elif self.keyHandler[LEFT]== True and  self.bl  < self.x  - self.r < self.br - self.r:
                self.vx-=0.25
               
            else:
                self.vx=0
           
            if self.keyHandler[UP] and 100 + self.y == self.g and  self.bl  + self.r < self.x < self.br - self.r:
                self.vy = -12 + self.powerJump
               
            self.y=self.y + self.vy
            self.x=self.x + self.vx
           
            if self.y + 100 > self.g :
                self.y= self.g - 100
               
            if frameCount%5 == 0 and self.vx != 0 and self.vy == 0:
                self.frame = (self.frame + 1) % self.frameNum
            elif self.vx == 0:
                #no animation if character stands still
                self.frame = 0    
               
               
class Monster(Creature):
   
    def __init__(self,x,y,g,r, obstruction , frameNum, br, bl, imgNum):
        Creature.__init__(self,x,y,g,r,obstruction, frameNum)
        self.movement = 1
        self.br=br
        self.bl=bl
        self.imgNum = imgNum
        #self.alive = 0

       
    def display1(self):
       
        if self.movement == 0:
            image(imageM1,self.x - 75 , self.y  - 80, 80, 100 , self.frame * 154, 0, (self.frame + 1) * 150, 191)

        elif self.movement == 1:
            image(imageM1, self.x - 75 , self.y - 80 , 80, 100, (self.frame + 1) * 154, 0, self.frame * 150,191)
           
        #rect(self.x - 40 ,self.y - 50,80,100)
           
    def display2(self):

        if self.movement == 0:
            image(imageM2,self.x - 100 , self.y  - 115, 100, 100 , self.frame * 200, 0, (self.frame + 1) * 200, 230)

        elif self.movement == 1:
            image(imageM2, self.x - 100 , self.y - 115 , 100, 100, (self.frame + 1) * 200, 0, self.frame * 200, 230)
         
       


    def gravity(self):
             
        if self.y + self.r < self.g :
            self.vy=self.vy+0.5
           
        else:
            self.vy=0
           
        for p in self.obstruction:
            if p.x <= self.x < p.x + p.w and self.y + self.r <= p.y:
                self.g = p.y
                return
           
        global currentLevel
       
        if currentLevel == 1:
            self.g = game.g
           
        else:
            self.g = game2.g
       
    def update(self):
   
        self.gravity()
        self.speed = 1
       
        self.y=self.y + self.vy
        self.x=self.x + self.vx
           
        if self.y + self.r > self.g :
            self.y = self.g - self.r
           

        #self.x = self.x + self.speed
       
       
        if self.x > self.br :
            self.movement = 0
           
        if self.x < self.bl :
            self.movement = 1
         
        if (self.x < self.br + 50 and self.movement == 1):
            self.x +=  self.speed
   
       
        if (self.x > self.bl - 50 and self.movement == 0):
            self.x -= self.speed
           
        if frameCount%10 == 0 and self.vx == 0 and self.vy == 0:
            self.frame = (self.frame + 1) % self.frameNum
        #elif self.vx == 0:
            #no animation if character stands still
            #self.frame = 0
           
           
class Assets:
   
        def __init__(self,x,y,g, obstruction, r):
       
            self.x=x
            self.y=y
            self.g=g
            self.vx=0
            self.vy=1
            self.obstruction=obstruction
            self.r =r
       
            self.pcoin= random.randint(10, 690)
   
class Coin(Assets):

    def __init__(self,x,y,g, obstruction, r):
        Assets.__init__(self,x,y,g, obstruction, r)
       
   
    def display(self):
       
        image(imageCoin, self.x ,self.y,self.r,self.r)
       

        #ellipse(self.pcoin,self.y,2*self.r,2*self.r)
       
    def gravity(self):
       
        if self.y + self.r < self.g :
            self.vy=self.vy+0.5
           
        else:
            self.vy=0
           
        for p in self.obstruction:
            if p.x <= self.x < p.x + p.w and self.y + self.r <= p.y:
                self.g = p.y
                return
           
        global currentLevel
       
        if currentLevel == 1:
            self.g = game.g
           
        else:
            self.g = game2.g
           
   

    def update(self):
   
        self.gravity()

       
        self.y=self.y + self.vy
        self.x=self.x + self.vx
           
        if self.y + self.r > self.g :
            self.y = self.g - self.r
           
class Power_Ups(Assets):

    def __init__(self,x,y,g, obstruction, r):
        Assets.__init__(self,x,y,g, obstruction, r)
       
   
    def display(self):
       
        image(imagePU1, self.x ,self.y,self.r,self.r)

       
    def gravity(self):
       
        if self.y + self.r < self.g :
            self.vy=self.vy+0.5
           
        else:
            self.vy=0
           
        for p in self.obstruction:
            if p.x <= self.x < p.x + p.w and self.y + self.r <= p.y:
                self.g = p.y
                return
           
        global currentLevel
       
        if currentLevel == 1:
            self.g = game.g
           
        else:
            self.g = game2.g
       
   

    def update(self):
   
        self.gravity()

       
        self.y=self.y + self.vy
        self.x=self.x + self.vx
           
        if self.y + self.r > self.g :
            self.y = self.g - self.r        

class Obstruction:
    def __init__(self,x,y,w,h, isMoving=False):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.isMoving= isMoving
        self.speed = 1
       
        global currentLevel
       
   
    def display(self):
        #rect(self.x,self.y,self.w,self.h)
        #image(imageTree, -30,500, 180, 180)
        image(imageP1,self.x,self.y,self.w + 1.75*self.w ,self.h)
       
        if self.isMoving and currentLevel==1 : 
            self.x = self.x + self.speed
            if (self.x > 200):
                self.speed = - self.speed
            if (self.x < 50):
                self.speed = - self.speed
               
        ''' if self.isMoving and currentLevel==2:
            self.y = self.y + self.speed
            if (self.y > 450):
                self.speed = - self.speed
            if (self.y < 300):
                self.speed = - self.speed'''

class Game:
    
    score1= 0
    score2= 0
    
    def __init__(self, w, h, g, obstructionList , level):
        self.w = w
        self.h = h
        self.g = g
        self.g1 = g
        self.level = level
        self.obstructionList = obstructionList
       
           
        if self.level == 1:
            self.player1=Player(100,600,self.g,35,self.obstructionList, 5 , 700, 0,1 )
            self.player2=Player(50,600,self.g,35,self.obstructionList, 5 , 700, 0,2 )
            self.Players =[self.player1,self.player2]
           
            self.monster1=Monster(270,100, self.g, 14,self.obstructionList, 4, 500, 70,1)
            self.monster2=Monster(300,500, self.g, 14,self.obstructionList, 4, 560, 200,1)
            self.monster3=Monster(200,100, self.g, 14,self.obstructionList, 3, 650, 50,2)
            self.Monsters = [self.monster1, self.monster2 , self.monster3]
           
            self.potion1= Power_Ups(300, 450, self.g, self.obstructionList, 40)
            self.Potions = [self.potion1]
           
            self.coin1 = Coin(random.randint(50, 650), 100, self.g, self.obstructionList, 30)
            self.coin2 = Coin(random.randint(50, 650), 100, self.g, self.obstructionList, 30)
            self.coin3 = Coin(random.randint(50, 650), 100, self.g, self.obstructionList, 30)
            self.coin4 = Coin(random.randint(50, 650), 100, self.g, self.obstructionList, 30)
            self.Coin = [self.coin1, self.coin2, self.coin3, self.coin4]
           
           
       
        else:
           
            self.player1=Player(650,500,self.g,35,self.obstructionList, 5 , 700, 0,1 )
            self.player2=Player(670,500,self.g,35,self.obstructionList, 5 , 700, 0,2 )
            self.Players =[self.player1,self.player2]
       
            self.monster1=Monster(330,450, self.g, 14,self.obstructionList, 4, 490, 268,1)
            #self.monster2=Monster(500,50, self.g, 14,self.obstructionList, 4, 650, 50,1)
            self.monster3=Monster(200,180, self.g, 14,self.obstructionList, 3, 440, 200,2)
            self.Monsters = [self.monster1, self.monster3]
           
            self.potion1= Power_Ups(350, 450, self.g, self.obstructionList, 40)
            self.Potions = [self.potion1]
           
           
            self.coin1 = Coin(640, 100, self.g, self.obstructionList, 30)
            self.coin2 = Coin(250, 300, self.g, self.obstructionList, 30)
            self.coin3 = Coin( 390, 100, self.g, self.obstructionList, 30)
            self.coin4 = Coin(180, 130, self.g, self.obstructionList, 30)
            self.Coin = [self.coin1, self.coin2, self.coin3, self.coin4]
       
        #self.potion1= Power_Ups(random.randint(50, 650), 100, self.g, self.obstructionList, 40)
        #self.Potions = [self.potion1]
       
    def display(self):
        #stroke(0)
        #line(0,self.g, self.w, self.g)
        i=0
        for i in range(len(self.obstructionList)):
            self.obstructionList[i].display()
         
           
        for p in self.Players:
            if p.alive == 1:
                if p.imgNum == 1:
                    p.display1()
                elif p.imgNum == 2:
                    p.display2()
                p.update()
       
        check = 0
        #players dying
        for m in self.Monsters:
            for p in self.Players:
                if p.x < m.x < p.x + 100 and p.y + 30 < m.y  < p.y + 170 and m.alive == 1 and p.alive == 1:
                    p.alive = 0
                    check = 1
                    die.play()
                    die.rewind()
                   
                elif p.y > 700 and p.alive == 1:
                    p.alive = 0
                    check = 1
                    die.play()
                    die.rewind()
                   
        #displaying monsters
        for m in self.Monsters:
            if m.alive == 1:
                if m.imgNum == 1:
                    m.display1()
                elif m.imgNum == 2:
                    m.display2()
            m.update()
       
        #displaying coins    
        for c in self.Coin:
            c.display()
            c.update()
           
        #collecting coins
        for c in self.Coin:
            for p in self.Players:
                if p.x - 50 < c.x < p.x + 40 and  p.y  < c.y  < p.y + 100:
                    self.Coin.remove(c)
                    if p == self.player1:
                        Game.score1 +=1
                    elif p == self.player2:
                        Game.score2 +=1
                    #print(score)
                    c.display()
                    c.update()
                   
        #displaying potions
        for p in self.Potions:
            p.display()
            p.update()
           
           
        #jumping power up
        for pu in self.Potions:
            for p in self.Players:
                if p.alive == 1:
                    if p.x - 50 < pu.x < p.x + 40 and  p.y  < pu.y  < p.y + 100:
                        self.Potions.remove(pu)
                        p.powerJump = -3
                       
         
                                       
        #both players died
        check = 0
        for p in self.Players:
            if p.alive== 1:
                check = 1
                    
        if check == 0:
            if self.level == 1:
                image(imageBackground, 0,0)
            else:
                image(imageBackground2,0,0)
            textSize(17)
            image(imageLost, 215, 200, 300, 300)
            fill(127,0,0)
            text("CLICK ANYWHERE TO RESTART", 240, 450)
            


            #return

obstruction1 = Obstruction(150,550,500, 300)
obstruction2 = Obstruction(600,450,100, 300)
obstruction3 = Obstruction(0,380,600, 300)
obstruction4 = Obstruction(150,250,150, 300,True)
obstruction5 = Obstruction(350,150,150, 300)
obstruction8 = Obstruction(600,100,100, 300)
obstructionList1=[obstruction8, obstruction5, obstruction4, obstruction3,obstruction2, obstruction1]

obstruction9 = Obstruction(600,600,100, 300)
obstruction10 = Obstruction(250,500,250, 300)
obstruction11 = Obstruction(0,450,150, 300, True)
obstruction12 = Obstruction(220,330,250, 300)
obstruction13 = Obstruction(550,250,150, 300)
obstruction14 = Obstruction(150,200,300, 300)
obstruction15= Obstruction(0,100,100, 300)
obstructionList2=[obstruction15, obstruction11, obstruction14, obstruction13, obstruction12, obstruction10, obstruction9]          
 
global imageBackground

game = Game(700,700,655, obstructionList1 , 1)    
game2 = Game(700,700,900, obstructionList2 , 2)                                                                                                                                                
 
Games = [game, game2]

currentLevel = 1                                                                                  
                                                                                                                                                                                                                                                         
def keyPressed():
   
    if keyCode==LEFT:
        if currentLevel ==1:
            game.player1.keyHandler[LEFT]=True
        else:
            game2.player1.keyHandler[LEFT]=True
       
    elif keyCode==RIGHT:
        if currentLevel ==1:
            game.player1.keyHandler[RIGHT]=True
           
        else:
            game2.player1.keyHandler[RIGHT]=True
       
    elif keyCode== UP:
        if currentLevel ==1:
            game.player1.keyHandler[UP] = True
            jump.rewind()
            jump.play()
        else:
            game2.player1.keyHandler[UP] = True
            jump.rewind()
            jump.play()
           
       
    if key=='a':
        if currentLevel ==1:
            game.player2.keyHandler[LEFT]=True
        else:
            game2.player2.keyHandler[LEFT]=True
           
       
    elif key=='d':
        if currentLevel ==1:
            game.player2.keyHandler[RIGHT]=True
        else:
            game2.player2.keyHandler[RIGHT]=True
           
       
    elif key== 'w':
        if currentLevel ==1:
            game.player2.keyHandler[UP] = True
            jump.rewind()
            jump.play()
        else:
            game2.player2.keyHandler[UP] = True
            jump.rewind()
            jump.play()
           
       
def keyReleased():
   
    if keyCode==LEFT:
        if currentLevel ==1:
            game.player1.keyHandler[LEFT]= False
        else:
            game2.player1.keyHandler[LEFT]= False
       
    elif keyCode==RIGHT:
        if currentLevel ==1:
            game.player1.keyHandler[RIGHT]= False
        else:
            game2.player1.keyHandler[RIGHT]= False
       
    elif keyCode== UP:
        if currentLevel ==1:
            game.player1.keyHandler[UP] = False
        else:
            game2.player1.keyHandler[UP] = False
           
    if key=='a':
        if currentLevel ==1:
            game.player2.keyHandler[LEFT]= False
        else:
            game2.player2.keyHandler[LEFT]= False
       
           
    elif key=='d':
        if currentLevel ==1:
            game.player2.keyHandler[RIGHT]= False
        else:
            game2.player2.keyHandler[RIGHT]= False
           
    elif key== 'w':
        if currentLevel ==1:
            game.player2.keyHandler[UP] = False
        else:
            game2.player2.keyHandler[UP] = False


def setup():
        size(game.w,game.h)
        global imageBackground, imageP1, imageGround, imageCh1, imageCh2, imageM1, imageM2, imageCoin, imageTree, imagePU1 , imageBackground2, imageWIN, imageDoor, imageLost, imageGAMEWIN
        imageBackground = loadImage("data/Images/img1.png")
        imageP1 = loadImage("data/Images/platform1.png")
        imageGround = loadImage("data/Images/ground.png")
        imageCh1= loadImage("data/Images/character1.png")
        imageCh2= loadImage("data/Images/character2.png")
        imageM1= loadImage("data/Images/monster1.png")
        imageM2= loadImage("data/Images/monster2.png")
        imageCoin= loadImage("data/Images/coin.png")
        imagePU1= loadImage("data/Images/jumping_powerup.png")
        imageBackground2 = loadImage("data/Images/img2.png")
        imageWIN = loadImage("data/Images/treasure.png")
        imageDoor= loadImage("data/Images/door.png")
        imageLost=loadImage("data/Images/gameover.png")
        imageGAMEWIN=loadImage("data/Images/win.png") 
        #imageTree = loadImage("data/Images/tree.png")
       
        bg_music = player.loadFile("data/Sounds/background.mp3")
        bg_music.loop()    
       
        global jump
        jump = player.loadFile("data/Sounds/jump.wav")
       
        global die
        die = player.loadFile("data/Sounds/die1.mp3")

      
       
def draw():
    background(255,255,255)
    global imageBackground, imageGround, imgaeBackGround2, currentLevel, imageDoor, imageGAMEWIN, checkAlive
   
    if currentLevel == 1:
        image(imageBackground, 0,0)
        image( imageDoor, 615, 5, 70, 100)
       
       
    else:
        image(imageBackground2,0,0)
        image(imageWIN,15,45, 70, 60)
        image( imageDoor, 615, 505, 70, 100)
       
   
    if currentLevel == 1:
        image(imageGround,0,540,700,200)
       
   
       
    #check if any player is alive
    checkAlive = 0
    for g in Games:
        for p in g.Players:
            if p.alive== 0:
                checkAlive = 1
                
    #if both players reached door, we switch to level 2
    if checkAlive == 0:
        if game.player1.g == 100 and game.player2.g == 100:
            currentLevel = 2
            
    #if 1 dead, other at door
    if checkAlive == 1:
        for g in Games:      
            for p in g.Players:
                if p.g == 100:
                    currentLevel = 2
    
    if currentLevel == 1:
        game.display()
       
    else:
        game2.display()
        
    #player reached treasure
    global WIN
    WIN = 0
    if currentLevel == 2:
        if checkAlive == 1:
            #for g in Games:      
            for p in g.Players:
                if p.g == 100:
                    image(imageBackground2,0,0)
                    textSize(17)
                    image(imageGAMEWIN,215, 200, 300, 300)
                    fill(127,0,0)
                    text("CLICK ANYWHERE TO RESTART", 240, 540)
                    WIN = 1
                        

            
        
    testScore1 = "Player1 : " + str(Game.score1)
    testScore2 = "Player2 : " + str(Game.score2)
    fill(0)
    textSize(15)
    text(testScore2, 370, 40)
    text(testScore1, 250, 40)


#restart game
  
def mouseClicked():
    global currentLevel , game , game2, Games, WIN
    
    checkDead = 0
    
    if currentLevel == 1:
        if game.player1.alive == 1 or game.player2.alive == 1:
                checkDead = 1
                
    if currentLevel == 2:
        if game2.player1.alive == 1 or game2.player2.alive == 1:
                checkDead = 1
                    
    if checkDead == 0 or WIN == 1:
        currentLevel = 1
        Game.score1 = 0
        Game.score2 = 0
        game = Game(700,700,655, obstructionList1 , 1)
        game2 = Game(700,700,900, obstructionList2 , 2)
        Games = [game , game2]
                #also add this option for when game is won.
