# -*- coding=utf-8 -*-
import pygame
from bf_button import BFButton,BFButtonGroup

pygame.init()
screencaption = pygame.display.set_caption('bf control')
screen = pygame.display.set_mode((400,400))

def do_click1(btn):
    pygame.display.set_caption('i click %s,ctl id is %s' % (btn._text,btn.ctl_id))
    btn.text = 'be click'

def do_click2(btn):
    btn.visible = False

def do_click3(btn):
    pygame.quit()
    exit()

btn_group = BFButtonGroup()
btn_group.make_button(screen, (120,100,160,40),text='Play',click=do_click1)
btn_group.make_button(screen, (120,180,160,40),text='Hide',click=do_click2)
btn_group.make_button(screen, (120,260,160,40),text='Quit',click=do_click3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        btn_group.update(event)

    screen.fill((255,255,255))
    btn_group.draw()
   
    pygame.display.update() 