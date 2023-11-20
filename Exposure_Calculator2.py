import pygame
import sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
font = pygame.font.SysFont('Arial', 20)

objects = []

BST = {-10:12,-20:6,-30:3,-40:1,-50:0}
temp = -10

##############|COLORS|##############
color_black = (0,0,0)
color_select = (30,30,30)
color_dark = (60,60,60)
color_light = (90,90,90)
color_border = (170,170,170)
color_white = (255,255,255)

##############|GEOMETRY VARIABLES|##############
width = screen.get_width()
height = screen.get_height()
rect_width = 200
rect_height = 40

PCs = []

CST = {
    'old':1,
    'basic':2,
    'advanced':3,
    'padded':1,
    'leather':3
}

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, args=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.args = args
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': color_light,
            'hover': color_dark,
            'pressed': color_select,
            'empty': color_black
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(screen,color_dark,[x,y,rect_width,rect_height],0,20)
        #pygame.draw.rect(screen,color_border,[x,y,rect_width,rect_height],3,20)

        self.buttonSurf = font.render(buttonText, True, color_white)
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    if self.args: self.onclickFunction(self.args)
                    else: self.onclickFunction()
                elif not self.alreadyPressed:
                    if self.args: self.onclickFunction(self.args)
                    else: self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

class PC:
    def __init__(self,Name,gear,fortitude):
        self.time = 0
        self.Name = Name
        #CLOTHES SURVIVAL TIME
        self.CST = CST[gear]
        self.fort = fortitude

        PCs.append(self)
        
    def adv(self,h):
        self.time-=1
        ST = 6+self.CST+self.fort+self.time+BST[temp]
        if ST < 0:
            ST = 0
        x=600
        pygame.draw.rect(screen,color_black,[x,h,rect_width,rect_height],0,20)
        screen.blit(font.render('Time '+self.Name + ': ' + str(ST), False, color_white),(x,h+7))

    def reset(self,h):
        self.time=0
        ST = 6+self.CST+self.fort+self.time+BST[temp]
        x=600
        pygame.draw.rect(screen,color_black,[x,h,rect_width,rect_height],0,20)
        screen.blit(font.render('Time '+self.Name + ': ' + str(ST), False, color_white),(x,h+7))

    def temp(self,h):
        ST = 6+self.CST+self.fort+self.time+BST[temp]
        if ST < 0:
            ST = 0
        x=600
        pygame.draw.rect(screen,color_black,[x,h,rect_width,rect_height],0,20)
        screen.blit(font.render('Time '+self.Name + ': ' + str(ST), False, color_white),(x,h+7))
        
chars = {
    'Sam':['basic',1],
    'Chan-Chan':['old',0],
    'Artyom':['basic',0],
    'Raldo':['basic',2],
    'Bridgewater':['basic',1],
    'Strelnikov':['basic',2],
    'Semyon':['basic',1],
    'Otto':['basic',1],
    'Alexi':['basic',1]
}

for i in chars:
    PC(i,chars[i][0],chars[i][1])

def update_temp(t):
    global temp
    temp = t
    x,y = width-200,20
    pygame.draw.rect(screen,color_black,[x,y,rect_width,rect_height],0,20)
    screen.blit(font.render(f'Temp: {t} C', False, color_white),(x,y+rect_height/4))
    update('temp')

def update(a):
    dh = height/(len(PCs)+1)
    h = -20
    for i in PCs:
        h += dh
        if a == 'adv':
            i.adv(h)
        if a == 'reset':
            i.reset(h)
        if a == 'temp':
            i.temp(h)
    
for t,h in [(-10,20),(-20,80),(-30,140),(-40,200),(-50,260)]:
    Button(30, h, rect_width-100, rect_height, str(t)+' C', update_temp,t)
Button(30,320,rect_width-100,rect_height,"Adv. All", update,'adv')
Button(30,380,rect_width-100,rect_height,"Reset All", update, 'reset')

dh = height/(len(PCs)+1)
h = -20
for i in PCs:
    h += dh
    Button(150, h, rect_width, rect_height, 'Advance '+i.Name, i.adv,h)
    Button(375, h, rect_width, rect_height, 'Reset '+i.Name, i.reset,h)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    for object in objects: object.process()
    update_temp(temp)
    pygame.display.update()