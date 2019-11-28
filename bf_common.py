# -*- coding=utf-8 -*-
import threading
import pygame
from pygame.locals import MOUSEBUTTONDOWN

class BFControlId(object):
    _instance_lock = threading.Lock()
    def __init__(self):
        self.id = 1

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(BFControlId, "_instance"):
            BFControlId._instance = BFControlId(*args, **kwargs)
        return BFControlId._instance

    def get_new_id(self):
        self.id += 1
        return self.id

CLICK_EFFECT_TIME = 100