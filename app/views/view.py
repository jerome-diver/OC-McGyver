"""
Superclass View embed 
model from MVC design pattern
"""

import pygame


class View:

    def __init__(self, model):
        self._model = model
        self._gameEngine = model.gameEngine()


