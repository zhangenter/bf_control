# -*- coding=utf-8 -*-
import pygame
pygame.init()
screen = pygame.display.set_mode((600,420))

from py_bf_control.bf_button import BFButton

def do_click1(btn):
    pygame.display.set_caption('i click %s,ctl id is %s' % (btn._text,btn.ctl_id))
    btn.text = 'be click'

btn = BFButton(screen, (20,20,160,40),text=u'test',click=do_click1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        btn.update(event)

    screen.fill((255,255,255))
    btn.draw()
   
    pygame.display.update() 