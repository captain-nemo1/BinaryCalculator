#Simple Binary calculator for values less than 10
import random
import pygame
import sys
import time
#A,B,C,D,x for coordinates
A=100
B=20
C=25
D=30
x=50
E=0
s="" #string to store expression
i=0#check value to clear string
pygame.init()
screen=pygame.display.set_mode((300,300))
black=(0,0,0)
pygame.display.set_caption("Binary Calculator")
screen.fill((black))
font = pygame.font.SysFont('Times New Roman', 22)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b            

#to evaluate expression
def calc():
    global s,i
    #to find operator location
    for k in range(len(s)):
        if(s[k]=='+' or s[k]=='-' or s[k]=='*' or s[k]=='/'):
            break
    #if invalid expression        
    try:        
        a=int(s[:k])#stores first number
        b=int(s[k+1:])#stores second number
        msg=s[k]#stores operator
    except:
           text = font.render("Invalid Input", True, (0, 0, 255))     
           screen.blit(text,(0,0))     
           pygame.display.update()
           return
    if msg is '+':
        k=add(a,b)
    if msg is '-':
        k=sub(a,b)
    if msg is '*':
        k=mul(a,b)
    if msg is '/':
        k=div(a,b)
    text = font.render(str(k), True, (0, 0, 255))     
    screen.blit(text,(200,250))
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    i=1#so that for calculating next expression we go to string start in button_num    
    
#to get result    
def button_equal(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global E
    text = font.render(msg, True, (0, 0, 0)) 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)
        if(click[0]==1):
            pygame.draw.rect(screen, (225,0,0),(x,y,w,h), 0)
            calc()#function to calculate
            E=0#so next time displays answer values from the start
    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)
    #draw text on button
    screen.blit(text,(x+3,y+3))
    
#to clear screen    
def button_clear(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    text = font.render(msg, True, (0, 0, 0)) 
    global s
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)
        if(click[0]==1):
            pygame.draw.rect(screen, (225,0,0),(x,y,w,h), 0)
            screen.fill(black)
            s=""#clearing string
    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)
    #draw text on button    
    screen.blit(text,(x+3,y+3))

#for drawing mathematical symbols
def button_symbol(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global E,s
    text = font.render(msg, True, (0, 255, 0)) 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)
        if(click[0]==1):
            pygame.draw.rect(screen, (225,0,0),(x,y,w,h), 0)
            time.sleep(.1)
            s=s+msg#add symbol to string
            screen.blit(text,(100+E,250))
            E=E+10            
    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)
    #draw text on button
    screen.blit(text,(x+3,y+3))

#for click on numbers
def button_num(msg,x,y,w,h):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    global E,i,s 
    text = font.render(msg, True, (0, 255, 0)) 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:   #if mouse pointer is over button
        pygame.draw.rect(screen, (225,225,225),(x,y,w,h), 0)
        
        if(click[0]==1):
            pygame.draw.rect(screen, (225,0,0),(x,y,w,h), 0)
            if i!=1: #will be 1 if prior calculations done so reset string s to 0 in else case
                s=s+msg         
            else:
                s=msg
                i=0
            time.sleep(.1)
            screen.blit(text,(100+E,250))
            E=E+10
            return    
            
    else:
        pygame.draw.rect(screen, (200,127,168),(x,y,w,h), 0)
    #draw text on button
    screen.blit(text,(x+3,y+3))
    
#draw all buttons    
def draw():
    button_num('1',A,B,C,D)
    button_num('2',A+x,B,C,D) 
    button_num('3',A+2*x,B,C,D)
    button_num('4',A,B+x,C,D)
    button_num('5',A+x,B+x,C,D) 
    button_num('6',A+2*x,B+x,C,D)
    button_num('7',A,B+2*x,C,D)
    button_num('8',A+x,B+2*x,C,D) 
    button_num('9',A+2*x,B+2*x,C,D)
    button_num('0',A+x,B+3*x,C,D)
    button_symbol('+',A-x,B,C,D)
    button_symbol('-',A-x,B+x,C,D)
    button_symbol('*',A-x,B+2*x,C,D)
    button_symbol('/',A-x,B+3*x,C,D)
    button_clear('C',A+2*x,B+3*x,C,D)
    button_equal('=',A,B+3*x,C,D)
    
while True:
    draw()    
    pygame.display.update()    
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
    
    
    
    
    
    
                

