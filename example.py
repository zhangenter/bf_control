# -*- coding=utf-8 -*-
import pygame

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.scrap.init()

from bf_common import TEXT_ALIGN_LEFT,TEXT_ALIGN_MIDDLE,TEXT_ALIGN_RIGHT
from bf_edit import BFEdit
from bf_button import BFButton
from bf_panel import BFPanel
from bf_label import BFLabel

screencaption = pygame.display.set_caption('bf control')

def do_click1(btn):
    pygame.display.set_caption('i click %s,ctl id is %s' % (btn._text,btn.ctl_id))
    btn.text = 'be click'

def do_click2(btn):
    btn.visible = False

def do_click3(btn):
    pygame.quit()
    exit()

def do_click4(btn):
    bf_lebel.text_align = TEXT_ALIGN_LEFT
def do_click5(btn):
    bf_lebel.text_align = TEXT_ALIGN_MIDDLE
def do_click6(btn):
    bf_lebel.text_align = TEXT_ALIGN_RIGHT


btn_panel = BFPanel()
btn_panel.add_control(BFButton(screen, (20,20,160,40),text=u'测试',click=do_click1))
btn_panel.add_control(BFButton(screen, (200,20,160,40),text='隐藏',click=do_click2))
btn_panel.add_control(BFButton(screen, (380,20,160,40),text='退出',click=do_click3))

bf_lebel = BFLabel(screen, (20,80,160,40),text='文字显示')
bf_lebel.text_align = TEXT_ALIGN_RIGHT
btn_panel.add_control(bf_lebel)
btn21 = BFButton(screen, (200,80,100,40),text=u'靠左',click=do_click4)
btn21.text_align = TEXT_ALIGN_LEFT
btn_panel.add_control(btn21)
btn22 = BFButton(screen, (320,80,100,40),text=u'居中',click=do_click5)
btn22.text_align = TEXT_ALIGN_MIDDLE
btn_panel.add_control(btn22)
btn23 = BFButton(screen, (440,80,100,40),text=u'靠右',click=do_click6)
btn23.text_align = TEXT_ALIGN_RIGHT
btn_panel.add_control(btn23)

edit1 = BFEdit(screen, (20,140,160,40),text='test1')
btn_panel.add_control(edit1)
edit2 = BFEdit(screen, (200,140,160,40),text='test2')
edit2.text_align = TEXT_ALIGN_LEFT
btn_panel.add_control(edit2)
edit3 = BFEdit(screen, (380,140,160,40),text='test3')
edit3.text_align = TEXT_ALIGN_RIGHT
btn_panel.add_control(edit3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        btn_panel.update(event)

    screen.fill((255,255,255))
    btn_panel.draw()
   
    pygame.display.update() 