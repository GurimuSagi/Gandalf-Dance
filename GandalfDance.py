import sys
import os

import pygame
import pyganim
import pygame_textinput
from pygame.locals import *

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

path = resource_path(os.path.join('Files','bgMenu.png'))
bgMenu = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgCredits.png'))
bgCredits = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgPause.png'))
bgPause = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgChoose.png'))
bgChoose = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgGame1.png'))
bgGame = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgGameUp.png'))
bgGameUp = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgGameOver.png'))
bgGameOver = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgWinNext.png'))
bgWinNext = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgWin.png'))
bgWin = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgTutorial1.png'))
bgTutor1 = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgTutorial2.png'))
bgTutor2 = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgGameEnd.png'))
bgGameEnd = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgSaveF.png'))
bgSaveF = pygame.image.load(path)
path = resource_path(os.path.join('Files','bgSaveT.png'))
bgSaveT = pygame.image.load(path)
path = resource_path(os.path.join('Files','button1.png'))
button1 = pygame.image.load(path)
path = resource_path(os.path.join('Files','button2.png'))
button2 = pygame.image.load(path)
path = resource_path(os.path.join('Files','button3.png'))
button3 = pygame.image.load(path)
path = resource_path(os.path.join('Files','buttonYes.png'))
buttonYes = pygame.image.load(path)
path = resource_path(os.path.join('Files','buttonNo.png'))
buttonNo = pygame.image.load(path)
path = resource_path(os.path.join('Files','lvl1.png'))
buttonLvL_1 = pygame.image.load(path)
path = resource_path(os.path.join('Files','lvl2.png'))
buttonLvL_2 = pygame.image.load(path)
path = resource_path(os.path.join('Files','lvl3.png'))
buttonLvL_3 = pygame.image.load(path)
path = resource_path(os.path.join('Files','back.png'))
buttonBack =  pygame.image.load(path)
path = resource_path(os.path.join('Files','lvl2block.png'))
buttonLvL_2X = pygame.image.load(path)
path = resource_path(os.path.join('Files','lvl3block.png'))
buttonLvL_3X = pygame.image.load(path)
path = resource_path(os.path.join('Files','note.png'))
note = pygame.image.load(path)
path = resource_path(os.path.join('Files','click.png'))
panel = pygame.image.load(path)
path = resource_path(os.path.join('Files','click2.png'))
panelTap = pygame.image.load(path)

path1 = resource_path(os.path.join('Files','G01.png'))
path2 = resource_path(os.path.join('Files','G03.png'))
Anim = pyganim.PygAnimation([(path1, 460), (path2, 460)])
Anim.play()
clickTap = pyganim.PygAnimation([(panelTap, 460)])
clickTap.play()

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

path = resource_path(os.path.join('Files','save.txt'))
save = open(path)
path = resource_path(os.path.join('Files','lvl1.txt'))
lvl1 = open(path)
path = resource_path(os.path.join('Files','lvl2.txt'))
lvl2 = open(path)
path = resource_path(os.path.join('Files','lvl3.txt'))
lvl3 = open(path)

FLAG_LVL2 = False
FLAG_LVL3 = False
FLAG_WIN = False
FLAG_ACC = False
FLAG_START = False

mainClock = pygame.time.Clock()

pygame.init()
textinput = pygame_textinput.TextInput()
pygame.display.set_caption('Gandalf Dance!')
screen = pygame.display.set_mode((500, 700),0,32)
path = resource_path(os.path.join('Files','pixel.ttf'))
font = pygame.font.Font(path,50)
fontName = pygame.font.Font(path,70)
fontScore = pygame.font.Font(path, 120)

class Note(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        width = 57
        height = 58
        self.image = note
        self.startX = x
        self.startY = y
        self.xvel = speed
        self.rect = Rect(x, y, width, height)

    def update(self, Click):
        if Click == False:           
            self.rect.y += self.xvel
        if Click:
            self.rect.y = 0
            
    def draw(self, screen):      
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    path = resource_path(os.path.join('Files','Epic Sax Guy - 8-bit Remix.mp3'))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(loops=-1)
    global FLAG_START
    while True:  
        screen.blit(bgMenu, (0, 0))
        
        draw_text(None, font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(227, 382, 246, 77)
        button_2 = pygame.Rect(227, 482, 246, 76)
        button_3 = pygame.Rect(227, 582, 246, 76)

        screen.blit(button1, (225,380))
        screen.blit(button2, (225,480))
        screen.blit(button3, (225,580))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_1.collidepoint((mx, my)):
            if click:
                if FLAG_START == False:
                    createAccount()
                if FLAG_START == True:
                    choose()
        if button_2.collidepoint((mx, my)):
            if click:
                creditspage()
        if button_3.collidepoint((mx, my)):
            if click:
                running = False
                pygame.quit()
                sys.exit()
                    
        pygame.display.update()
        mainClock.tick(60)

def createAccount():
    running = True
    global FLAG_LVL2
    global FLAG_LVL3
    global FLAG_START
    while running:
        path = resource_path(os.path.join('Files','save.txt'))
        with open(path, "r") as file:
            name = file.read().splitlines()
            str1 = name[0]
            if str1 == "NULLisTrueNull":
                account = False
            else:
                account = True
                str2 = name[1]
                str3 = name[2]
        mx, my = pygame.mouse.get_pos()
        button_Back = pygame.Rect(46, 660, 75, 30)
        button_Next = pygame.Rect(391, 660, 75, 30)    
        if account == False:
            screen.blit(bgSaveF,(0,0))      
            draw_text('Input your name:', font, (255, 255, 255), screen, 125, 210)
            events = pygame.event.get()
            for event in events:
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True    
            textinput.update(events)
            draw_text(textinput.get_text(), font, (0, 0, 0), screen, 125, 295)

            if button_Next.collidepoint((mx, my)):
                if click:
                    if len(textinput.get_text())>=1:
                        path = resource_path(os.path.join('Files','save.txt'))
                        with open(path, "w") as file:
                            file.write(textinput.get_text())
                            file.write('\nFalse')
                            file.write('\nFalse')
                        FLAG_START = True
                        running = False
                        choose()
            
        if account == True:
            screen.blit(bgSaveT,(0,0))
            draw_text(("Hello, " + str1 + '!'), font, (255, 255, 255), screen, 80, 240)
            if str2 == "True":
                FLAG_LVL2 = True
                draw_text('Level 2 is unlocked!', font, (255, 255, 255), screen, 125, 310)
            else:
                draw_text('Level 2 is locked.', font, (255, 255, 255), screen, 125, 310)
            if str3 == "True":
                FLAG_LVL3 = True
                draw_text('Level 3 is unlocked!', font, (255, 255, 255), screen, 125, 340)
            else:
                draw_text('Level 3 is locked.', font, (255, 255, 255), screen, 125, 340)
            if button_Next.collidepoint((mx, my)):
                if click:
                    FLAG_START = True
                    running = False
                    choose()

        click = False
        events = pygame.event.get()
        for event in events:
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True    
        
        if button_Back.collidepoint((mx, my)):
            if click:
                running = False
            
        pygame.display.update()
        mainClock.tick(60)


def choose():
    running = True
    
    while running:
        screen.blit(bgChoose, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        button_LvL1 = pygame.Rect(172, 302, 161, 65)
        button_LvL2 = pygame.Rect(172, 382, 161, 65)
        button_LvL3 = pygame.Rect(172, 462, 161, 65)
        button_Back = pygame.Rect(172, 542, 161, 65)

        screen.blit(buttonLvL_1, (170,300))
        screen.blit(buttonBack, (170,540))

        if FLAG_LVL2 == False:
            screen.blit(buttonLvL_2X, (170,380))
        elif FLAG_LVL2 == True:
            screen.blit(buttonLvL_2, (170,380))
        if FLAG_LVL3 == False:
            screen.blit(buttonLvL_3X, (170,460))
        elif FLAG_LVL3 == True:
            screen.blit(buttonLvL_3, (170,460))

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if click:
            if button_LvL1.collidepoint((mx, my)):
                tutorial()
                running = False
            elif button_LvL2.collidepoint((mx, my)):
                if FLAG_LVL2 == True:
                    game(lvl2)
                    running = False
            elif button_LvL3.collidepoint((mx, my)):
                if FLAG_LVL3 == True:
                    game(lvl3)
                    running = False
            elif button_Back.collidepoint((mx, my)):
                running = False
            else:
                click = False

        pygame.display.update()
        mainClock.tick(60)    


def tutorial():
    running = True
    click = False
    FLAG_SCREEN = 1
    while running:
        if FLAG_SCREEN == 1:
            screen.blit(bgTutor1, (0,0))
        else:
            screen.blit(bgTutor2, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        button_Menu = pygame.Rect(46, 660, 75, 30)
        button_1 = pygame.Rect(161, 660, 75, 30)
        button_2 = pygame.Rect(276, 660, 75, 30)
        button_Play = pygame.Rect(391, 660, 75, 30)

        if click:
            if button_Menu.collidepoint((mx, my)):
                running = False
            elif button_1.collidepoint((mx, my)):
                FLAG_SCREEN = 1
            elif button_2.collidepoint((mx, my)):
                FLAG_SCREEN = 2
            elif button_Play.collidepoint((mx, my)):
                running = False
                game(lvl1)
            else:
                click = False
                
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)    
        
    
def game(lvl):
    running = True
    path = resource_path(os.path.join('Files','music.mp3'))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    panelA = pygame.Rect(55, 602, 57, 58)
    panelW = pygame.Rect(155, 602, 57, 58)
    panelK = pygame.Rect(255, 602, 57, 58)
    panelL = pygame.Rect(355, 602, 57, 58)

    entities = pygame.sprite.Group()

    platforms = []
    speed = 0
    if lvl == lvl1:
        y = 400
        speed = 2
        path = resource_path(os.path.join('Files','lvl1.txt'))
        with open(path, 'r') as f:
            notes = f.read().splitlines()
    elif lvl == lvl2:
        y = 400
        speed = 3
        path = resource_path(os.path.join('Files','lvl2.txt'))
        with open(path, 'r') as f:
            notes = f.read().splitlines()
    elif lvl == lvl3:
        y = 400
        path = resource_path(os.path.join('Files','lvl3.txt'))
        with open(path, 'r') as f:
            notes = f.read().splitlines()
        speed = 4
        
    for row in notes:
        colInd = 0
        for col in row:
            colInd += 1
            if col == '1':
                if colInd == 1:
                    pf = Note(55, y, speed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 2:
                    pf = Note(155, y, speed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 3:
                    pf = Note(255, y, speed)
                    platforms.append(pf)
                    entities.add(pf)
                if colInd == 4:
                    pf = Note(355, y, speed)
                    platforms.append(pf)
                    entities.add(pf)
        if lvl == lvl1:
            y -= 30
        else:
            y -= 26
    
    points = 0 
    badFlag = 0
    HP = 7
    while running:        
        start_ticks=0
        Click = False
        breakFlag = False
        mainClock.tick(60)
        
        screen.blit(bgGame, (0, 0))        
        
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                pygame.mixer.music.stop()
                win(lvl, points, badFlag)
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.pause()
                    result = pause()
                    if result == True:
                        pygame.mixer.music.unpause()
                    else:
                        running = False
                        path = resource_path(os.path.join('Files','Epic Sax Guy - 8-bit Remix.mp3'))
                        pygame.mixer.music.load(path)
                        pygame.mixer.music.play(loops=-1)
            if event.type == KEYDOWN:
                noteClick = False
                if event.key == K_a:
                    for note in platforms:
                        if panelA.colliderect(note) == True:
                            points += 10
                            noteClick = True
                            platforms.remove(note)
                    if noteClick == False:
                        path = resource_path(os.path.join('Files','sound.wav'))
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(path), maxtime=200)
                        badFlag += 1
                        HP -= 1
                    clickTap.blit(screen, (55,602))
                        
                if event.key == K_s:
                    for note in platforms:
                        if panelW.colliderect(note) == True:
                            points += 10
                            noteClick = True
                            platforms.remove(note)
                    if noteClick == False:
                        path = resource_path(os.path.join('Files','sound.wav'))
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(path), maxtime=200)
                        badFlag += 1
                        HP -= 1
                    clickTap.blit(screen, (155,602))
                        
                if event.key == K_k:
                    for note in platforms:
                        if panelK.colliderect(note) == True:
                            points += 10
                            noteClick = True
                            platforms.remove(note)
                    if noteClick == False:
                        path = resource_path(os.path.join('Files','sound.wav'))
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(path), maxtime=200)
                        badFlag += 1
                        HP -= 1
                    clickTap.blit(screen, (255,602))

                if event.key == K_l:
                    for note in platforms:
                        if panelL.colliderect(note) == True:
                            points += 10
                            noteClick = True
                            platforms.remove(note)
                    if noteClick == False:
                        path = resource_path(os.path.join('Files','sound.wav'))
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound(path), maxtime=200)
                        badFlag += 1
                        HP -= 1
                    clickTap.blit(screen, (355,602))

        for note in platforms:
            if note.rect.bottom == 700:
                path = resource_path(os.path.join('Files','sound.wav'))
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(path), maxtime=200)
                badFlag += 1
                HP -= 1

        if badFlag >= 7:
                pygame.mixer.music.stop()
                gameOver()
                running = False
                
        screen.blit(panel, (55,602))
        screen.blit(panel, (155,602))
        screen.blit(panel, (255,602))
        screen.blit(panel, (355,602))

        for e in platforms:
            screen.blit(e.image, e.rect)
            e.update(Click)
        screen.blit(bgGameUp, (0, 0))
        
        
        if lvl == lvl1:
            draw_text('lvl1', font, (255, 255, 255), screen, 25, 20)
            draw_text(str(points), font, (255, 255, 255), screen, 25, 60)
            draw_text('HP', font, (255, 255, 255), screen, 25, 100)
            draw_text(str(HP), font, (255, 255, 255), screen, 65, 100)
        elif lvl == lvl2:
            draw_text('lvl2', font, (255, 255, 255), screen, 25, 20)
            draw_text(str(points), font, (255, 255, 255), screen, 25, 60)
            draw_text('HP', font, (255, 255, 255), screen, 25, 100)
            draw_text(str(HP), font, (255, 255, 255), screen, 65, 100)
        elif lvl == lvl3:
            draw_text('lvl3', font, (255, 255, 255), screen, 25, 20)
            draw_text(str(points), font, (255, 255, 255), screen, 25, 60)
            draw_text('HP', font, (255, 255, 255), screen, 25, 100)
            draw_text(str(HP), font, (255, 255, 255), screen, 65, 100)
        
        Anim.blit(screen, (20,20))

        pygame.display.update()
        pygame.display.flip()
 
def creditspage():
    running = True
    click = False
    while running:
        
        screen.blit(bgCredits,(0,0))
        
        mx, my = pygame.mouse.get_pos()
        
        button_Back = pygame.Rect(172, 552, 161, 65)
        screen.blit(buttonBack, (170,550))

        if click:
            if button_Back.collidepoint((mx, my)):
                running = False
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def gameOver():
    running = True
    path = resource_path(os.path.join('Files','Game Over.mp3'))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    click = False
    while running:
        
        screen.blit(bgGameOver, (0,0))

        mx, my = pygame.mouse.get_pos()

        button_Back = pygame.Rect(172, 552, 161, 65)
        screen.blit(buttonBack, (170,550))

        if click:
            if button_Back.collidepoint((mx, my)):
                running = False
                path = resource_path(os.path.join('Files','Epic Sax Guy - 8-bit Remix.mp3'))
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(loops=-1)
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    choose()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)


def win(lvl, point, miss):
    running = True
    path = resource_path(os.path.join('Files','HeatleyBros - 8 Bit Win.mp3'))
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(loops=-1)
    global FLAG_LVL2
    global FLAG_LVL3
    global FLAG_WIN
    click = False
    while running:

        if lvl == lvl1:
            if FLAG_LVL2 == False:
                screen.blit(bgWinNext, (0,0))
            else:
                screen.blit(bgWin, (0,0))
        if lvl == lvl2:
            if FLAG_LVL3 == False:
                screen.blit(bgWinNext, (0,0))
            else:
                screen.blit(bgWin, (0,0))
        if lvl == lvl3:
            if FLAG_WIN == False:
                screen.blit(bgGameEnd,(0,0))
            else:
                screen.blit(bgWin, (0,0))

        mx, my = pygame.mouse.get_pos()

        if lvl == lvl3 and FLAG_WIN == False:
            button_Back = pygame.Rect(172, 572, 161, 65)
            screen.blit(buttonBack, (170,570))
            draw_text(str(point), fontScore, (255, 255, 255), screen, 270, 369)
            draw_text(str(miss), fontScore, (255,255,255), screen, 340, 449)
        else:
            button_Back = pygame.Rect(172, 552, 161, 65)
            screen.blit(buttonBack, (170,550))
            draw_text(str(point), fontScore, (255, 255, 255), screen, 270, 298)
            draw_text(str(miss), fontScore, (255,255,255), screen, 340, 400)

        if click:
            if button_Back.collidepoint((mx, my)):
                if lvl == lvl1:
                    FLAG_LVL2 = True
                    path = resource_path(os.path.join('Files','save.txt'))
                    with open(path, "r") as file:
                        name = file.read().splitlines()
                    with open(path, "w") as file:
                        file.write(name[0])
                        file.write('\nTrue')
                        file.write('\n')
                        file.write(name[2])
                if lvl == lvl2:
                    FLAG_LVL3 = True
                    path = resource_path(os.path.join('Files','save.txt'))
                    with open(path, "r") as file:
                        name = file.read().splitlines()
                    with open(path, "w") as file:
                        file.write(name[0])
                        file.write('\n')
                        file.write(name[1])
                        file.write('\nTrue')
                if lvl == lvl3:
                    FLAG_WIN = True
                running = False
                choose()
                path = resource_path(os.path.join('Files','Epic Sax Guy - 8-bit Remix.mp3'))
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(loops=-1)
            else:
                click = False

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.display.update()
        mainClock.tick(60)

def pause():
    running = True
    click = False

    while running:
        screen.blit(bgPause, (0, 0))
        
        mx, my = pygame.mouse.get_pos()

        button_Yes = pygame.Rect(172, 482, 161, 65)
        button_No = pygame.Rect(172, 577, 161, 65)
        
        if button_Yes.collidepoint((mx, my)):
            if click:
                running = False
                return False
        if button_No.collidepoint((mx, my)):
            if click:
                running = False
                return True
    
        screen.blit(buttonYes, (170,480))
        screen.blit(buttonNo, (170,575))
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
