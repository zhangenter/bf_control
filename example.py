# -*- coding=utf-8 -*-
import pygame
from bf_edit import BFEdit
from bf_button import BFButton
from bf_panel import BFPanel

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

btn_panel = BFPanel()
btn_panel.add_control(BFButton(screen, (120,20,160,40),text='Play',click=do_click1))
btn_panel.add_control(BFButton(screen, (120,70,160,40),text='Hide',click=do_click2))
btn_panel.add_control(BFButton(screen, (120,120,160,40),text='Quit',click=do_click3))
edit1 = BFEdit(screen, (120,170,160,40),text='test1')
btn_panel.add_control(edit1)
edit2 = BFEdit(screen, (120,220,160,40),text='test2')
btn_panel.add_control(edit2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        btn_panel.update(event)

    screen.fill((255,255,255))
    btn_panel.draw()
   
    pygame.display.update() 