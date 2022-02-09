from re import S

import pygame
from AbstractPlayer import AbstractPlayer


class Necromancer(AbstractPlayer):

  name = ""
  isInGround = True
  gravity = 10

  def __init__(self, image, name):
    super(Necromancer, self).__init__(image)
    AbstractPlayer.life = 50
    AbstractPlayer.defense = 10
    AbstractPlayer.speed = 10
    AbstractPlayer.damage = 10
    self.name = name

  def applyGravity(self):
    if self.rect.bottom >= 1080:
      self.isInGround = True

    if not self.isInGround and self.rect.bottom < 900:
      self.rect.y += self.gravity

  def jump(self):
    if self.isInGround:
      self.rect.bottom -= self.gravity
      self.isInGround = False

