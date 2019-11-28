# -*- coding=utf-8 -*-
import time
import threading
import pygame
from pygame.locals import MOUSEBUTTONDOWN,KEYDOWN,SCRAP_TEXT
from bf_common import BFControlId

CLICK_EFFECT_TIME = 100
class BFEdit(object):
    def __init__(self, parent, rect, text='Button', click=None):
        self.x,self.y,self.width,self.height = rect
        self.bg_color = (255,255,255)
        self.parent = parent
        self.panel = None
        self.surface = parent.subsurface(rect)
        self.in_edit = False
        self.in_click = False
        self.click_loss_time = 0
        self.click_event_id = -1
        self.ctl_id = BFControlId().instance().get_new_id()
        self._text = text
        self._visible = True
        self.init_font()

    def clear_foucs(self):
        self.in_edit = False

    def init_font(self):
        font = pygame.font.Font(None, 28)
        white = 100, 100, 100
        self.textImage = font.render(self._text, True, white)
        self.cursorImage = font.render('|', True, (170,205,255))
        w, h = self.textImage.get_size()
        self._tx = (self.width - w) / 2
        self._ty = (self.height - h) / 2
        self._cx = (self.width + w) / 2
        self._cy = (self.height - h) / 2

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.init_font()

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    def update(self, event):
        if self.in_edit and event.type == KEYDOWN:
            if event.key == 8:
                if len(self._text)>0:
                    self.text = self._text[:-1]
            elif event.key == 118 and event.mod>=1024:
                scrap_text = pygame.scrap.get(SCRAP_TEXT)
                if scrap_text:
                    self.text = self._text+scrap_text
            else:
                self.text = self._text+event.unicode
        if self.in_click and event.type == self.click_event_id:
            self.in_edit = True
            self.click_event_id = -1
            return

        x, y = pygame.mouse.get_pos()
        if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if pressed_array[0]:
                    self.in_click = True
                    if self.panel: self.panel.clear_foucs()
                    self.click_loss_time = pygame.time.get_ticks() + CLICK_EFFECT_TIME
                    self.click_event_id = pygame.USEREVENT+self.ctl_id
                    pygame.time.set_timer(self.click_event_id,CLICK_EFFECT_TIME-10)

    def draw(self):
        if not self._visible:
            return
        # if self.in_edit:
        #     r,g,b = self.bg_color
        #     k = 0.95
        #     self.surface.fill((r*k, g*k, b*k))
        # else:
        #     self.surface.fill(self.bg_color)
        if self.in_edit:
            layers = 2
            r_step = (210-170)/layers
            g_step = (225-205)/layers
            for i in range(layers):
                pygame.draw.rect(self.surface, (170+r_step*i, 205+g_step*i, 255), (i, i, self.width - i*2, self.height - i*2), 1)
            pygame.draw.rect(self.surface, (100,100,100), (2,2,self.width-4,self.height-4), 1)
            pygame.draw.rect(self.surface, (225,225,225), (3,3,self.width-6,self.height-6), 1)
        else:
            self.surface.fill(self.bg_color)
            pygame.draw.rect(self.surface, (100,100,100), (1,1,self.width-2,self.height-2), 1)
            pygame.draw.rect(self.surface, (225,225,225), (2,2,self.width-4,self.height-4), 1)
            # pygame.draw.rect(self.surface, (0,0,0), (0,0,self.width,self.height), 1)

        self.surface.blit(self.textImage, (self._tx, self._ty))
        if self.in_edit:
            if int(time.time()*2.5)%3 != 0:
                self.surface.blit(self.cursorImage, (self._cx, self._cy))
