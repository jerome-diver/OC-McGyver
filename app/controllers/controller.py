"""
Superclass Controller embed
model from MVC design pattern
"""

import pygame


class Controller:

  def __init__(self, pyGameEngine):
    self._gameEngine = pyGameEngine
