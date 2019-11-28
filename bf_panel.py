# -*- coding=utf-8 -*-
import threading
import pygame

class BFPanel(object):
    def __init__(self):
        self.ctl_list = []

    def add_control(self, ctl):
        ctl.panel = self
        self.ctl_list.append(ctl)

    def clear_foucs(self):
        for ctl in self.ctl_list: ctl.clear_foucs()

    def update(self, event):
        for ctl in self.ctl_list: ctl.update(event)

    def draw(self):
        for ctl in self.ctl_list: ctl.draw()
