# -*- coding=utf-8 -*-
import threading
import pygame
from pygame.locals import MOUSEBUTTONDOWN

class BFControlId(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        self.id = 1
        self.click_id = -1

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(BFControlId, "_instance"):
            BFControlId._instance = BFControlId(*args, **kwargs)
        return BFControlId._instance

    def get_new_id(self):
        self.id += 1
        return self.id

class BFBase(object):
    def __init__(self):
        self.panel = None
        self._visible = True
        self._text_align = TEXT_ALIGN_MIDDLE
        self.ctl_id = BFControlId().instance().get_new_id()

    def init_font(self):
        pass

    def clear_foucs(self):
        pass

    def clear_hover(self):
        pass

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    @property
    def text_align(self):
        return self._text_align

    @visible.setter
    def text_align(self, value):
        self._text_align = value
        self.init_font()

CLICK_EFFECT_TIME = 100
DEFAULT_FONT = pygame.font.Font(u'syht.otf', 28)

TEXT_ALIGN_LEFT = 1
TEXT_ALIGN_MIDDLE = 2
TEXT_ALIGN_RIGHT = 3