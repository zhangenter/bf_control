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

    def clear_hover(self):
        for ctl in self.ctl_list: ctl.clear_hover()

    def update(self, event):
        for i in range(len(self.ctl_list)-1, -1, -1):
            ctl = self.ctl_list[i]
            if not ctl.visible: continue
            flag = ctl.update(event)
            if flag:
                break
        # for ctl in self.ctl_list: ctl.update(event)

    def draw(self):
        for ctl in self.ctl_list: ctl.draw()
