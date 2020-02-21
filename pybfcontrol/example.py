# -*- coding=utf-8 -*-
import pygame

pygame.init()
screen = pygame.display.set_mode((600,420))
pygame.scrap.init()

from pybfcontrol.bf_common import TEXT_ALIGN_LEFT,TEXT_ALIGN_MIDDLE,TEXT_ALIGN_RIGHT
from pybfcontrol.bf_edit import BFEdit
from pybfcontrol.bf_button import BFButton
from pybfcontrol.bf_panel import BFPanel
from pybfcontrol.bf_label import BFLabel
from pybfcontrol.bf_table import BFTable

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
btn_panel.add_control(BFButton(screen, (200,20,160,40),text=u'隐藏',click=do_click2))
btn_panel.add_control(BFButton(screen, (380,20,160,40),text=u'退出',click=do_click3))

bf_lebel = BFLabel(screen, (20,80,160,40),text=u'文字显示')
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

edit1 = BFEdit(screen, (20,140,160,40),text=u'编辑1')
btn_panel.add_control(edit1)
edit2 = BFEdit(screen, (200,140,160,40),text=u'编辑2')
edit2.text_align = TEXT_ALIGN_LEFT
btn_panel.add_control(edit2)
edit3 = BFEdit(screen, (380,140,160,40),text=u'编辑3')
edit3.text_align = TEXT_ALIGN_RIGHT
btn_panel.add_control(edit3)

headers = (u'编号',u'姓名',u'年龄',u'语文成绩',u'数学成绩',u'英语成绩')
rows = []
rows.append((1,u'王小明',11,99,95,91))
rows.append((2,u'李小红',10,97,88,90))
rows.append((3,u'张小强',11,99,100,100))
rows.append((4,u'王小明',11,99,95,91))
rows.append((5,u'李小红',10,97,88,90))
rows.append((6,u'张小强',11,99,100,100))
rows.append((7,u'王小明',11,99,95,91))
rows.append((8,u'李小红',10,97,88,90))
rows.append((9,u'张小强',11,99,100,100))
rows.append((10,u'王小明',11,99,95,91))
rows.append((11,u'李小红',10,97,88,90))
rows.append((12,u'张小强',11,99,100,100))
table = BFTable(screen, (20,200,560,200), headers, rows)
btn_panel.add_control(table)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             exit()
        btn_panel.update(event)

    screen.fill((255,255,255))
    btn_panel.draw()
   
    pygame.display.update() 