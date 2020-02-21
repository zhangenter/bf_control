# -*- coding=utf-8 -*-
import sys
import pygame
from py_bf_control.bf_common import BFControlId,BFBase, get_default_font

black = (50,50,50)
class ColInfo(object):
    def __init__(self, surface, name, font_image=None, x=0, y=0):
        self.surface = surface
        self.x = x
        self.y = y
        self.name = name
        self.font_image = font_image

    def draw(self):
        if self.surface: self.surface.blit(self.font_image, (self.x, self.y))

class RowItem(object):
    def __init__(self, surface, val, font_image=None, x=0, y=0):
        self.surface = surface
        self.x = x
        self.y = y
        self.val = val
        self.font_image = font_image

    def draw(self):
        if self.surface: self.surface.blit(self.font_image, (self.x, self.y))

class RowInfo(object):
    def __init__(self):
        self.row_items = []
        self.highlight = False
        self.surface = None

    def draw(self):
        if self.highlight and self.surface:
            self.surface.fill((218,245,255))
        for row_item in self.row_items:
            row_item.draw()

CLICK_EFFECT_TIME = 100
class BFTable(BFBase):
    def __init__(self, parent, rect, columns, rows):
        super(BFTable, self).__init__()
        self.x,self.y,self.width,self.height = rect
        self.bg_color = (255,255,255)
        self.parent = parent
        self.surface = parent.subsurface(rect)
        self.in_click = False
        self.click_loss_time = 0
        self.click_event_id = -1
        self.ctl_id = BFControlId().instance().get_new_id()
        self.header_list = []
        self._header_height = 30
        self._col_width = self.width / len(columns)
        self._row_height = (self.height - self._header_height) / len(rows)
        self._min_row_height = 20
        self._max_row_height = 30
        if self._row_height > self._max_row_height: self._row_height = self._max_row_height
        if self._row_height < self._min_row_height: self._row_height = self._min_row_height
        
        self._col_font = get_default_font(self._header_height * 0.5)
        self._row_font = get_default_font(self._row_height * 0.6) 
        self._columns = []
        for i in range(len(columns)):
            col = columns[i]
            col_info = ColInfo(self.surface.subsurface((self._col_width*i,0,self._col_width,self._header_height)), col)
            header_image=self._col_font.render(col, True, black)
            w, h = header_image.get_size()
            col_info.x = (self._col_width - w) / 2
            col_info.y = (self._header_height - h) / 2
            col_info.font_image = header_image
            self._columns.append(col_info) 

        self._rows = []
        for i in range(len(rows)):
            y = self._header_height + self._row_height * i
            row = rows[i]
            row_info = RowInfo()
            row_info.surface = None if y + self._row_height > self.height else self.surface.subsurface((0,y,self.width,self._row_height))
            if i % 2 == 1: row_info.highlight = True
            for j in range(len(row)):
                v = row[j]
                tmp_rect = (self._col_width*j,y,self._col_width,self._row_height)
                tmp_surface = None if y + self._row_height > self.height else self.surface.subsurface(tmp_rect)
                item = RowItem(tmp_surface,v)
                if sys.version_info >= (3,0) or type(v) is not unicode: v = str(v)
                row_image = self._row_font.render(v,True,black)
                w, h = row_image.get_size()
                item.x = (self._col_width - w) / 2
                item.y = (self._row_height - h) / 2
                item.font_image = row_image
                row_info.row_items.append(item)
            self._rows.append(row_info)

    def clear_foucs(self):
        self.in_edit = False

    def update(self, event):
        return False

    def draw(self):
        if not self._visible:
            return

        grid_color = (100,100,100)
        self.surface.subsurface((0,0,self.width,self._header_height)).fill((200,200,200))
        pygame.draw.rect(self.surface, grid_color, (0,0,self.width,self._header_height+self._row_height*len(self._rows)),1)
        pygame.draw.line(self.surface,grid_color,[0,self._header_height],[self.width,self._header_height], 1)
        for col_info in self._columns:
            col_info.draw()
        for row_info in self._rows:
            row_info.draw()
        for i in range(1, len(self._rows)):
            y = self._header_height + i * self._row_height
            pygame.draw.line(self.surface,grid_color,[0,y],[self.width,y], 1)
        for i in range(1, len(self._columns)):
            x = self._col_width * i
            pygame.draw.line(self.surface,grid_color,[x,0],[x,self._header_height+self._row_height * len(self._rows)], 1)
        
        pygame.draw.rect(self.surface, (200,200,200), (0,0,self.width,self.height),1)