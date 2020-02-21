# -*- coding=utf-8 -*-
import pygame

pygame.init()
screen = pygame.display.set_mode((600,420))
pygame.scrap.init()

from py_bf_control.bf_panel import BFPanel
from py_bf_control.bf_table import BFTable

screencaption = pygame.display.set_caption('bf control')

btn_panel = BFPanel()

# headers = (u'编号',u'姓名',u'年龄',u'语文成绩',u'数学成绩',u'英语成绩')
headers = (u'周一',u'周二',u'周三',u'周四',u'周五',u'周六',u'周日')
rows = []
# rows.append((1,u'王小明',11,99,95,91))
# rows.append((2,u'李小红',10,97,88,90))
# rows.append((3,u'张小强',11,99,100,100))
# rows.append((4,u'王小明',11,99,95,91))
# rows.append((5,u'李小红',10,97,88,90))
# rows.append((6,u'张小强',11,99,100,100))
# rows.append((7,u'王小明',11,99,95,91))
# rows.append((8,u'李小红',10,97,88,90))
# rows.append((9,u'张小强',11,99,100,100))
# rows.append((10,u'王小明',11,99,95,91))
# rows.append((11,u'李小红',10,97,88,90))
# rows.append((12,u'张小强',11,99,100,100))
rows.append((u'上课','','','','','',''))
rows.append((u'上课',u'考试','','','','',''))
rows.append((u'上课','','','','','',''))
rows.append(('','','','','','',''))
rows.append(('','','','','','',''))
rows.append(('','','','','','',''))
rows.append(('','','','','','',''))
rows.append(('','','','','','',''))
rows.append(('','','','','','',''))
table = BFTable(screen, (20,20,560,300), headers, rows)
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