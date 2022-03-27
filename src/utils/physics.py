from typing import List
from pygame import Surface
from src.utils.screen import screen, screen_width, screen_height

from utils.binary_tuple import Binary_Tuple

earth_proportion_screen = 0.4
earth_real_size = 1.2742 * 10**7
earth_size = min(screen_width, screen_height) * earth_proportion_screen

Speed = Binary_Tuple
Acceleration = Binary_Tuple
Position = List[int]

def delta_x(pos1: Binary_Tuple, pos2: Binary_Tuple):
  x1 = pos1[0]
  x2 = pos2[0]
  return x2 - x1

def delta_y(pos1: Binary_Tuple, pos2: Binary_Tuple):
  y1 = pos1[1]
  y2 = pos2[1]
  return y2 - y1

def decompose_acceleration(acceleration: float, pos1: Binary_Tuple, pos2: Binary_Tuple):
  x = delta_x(pos1, pos2)
  y = delta_y(pos1, pos2)
  z = distance(pos1, pos2)
  sin = x / z * get_proportion()
  cos = y / z * get_proportion()
  return tuple([acceleration * sin, acceleration * cos])

def distance(pos1: Binary_Tuple, pos2: Binary_Tuple):
  x = delta_x(pos1, pos2)
  y = delta_y(pos1, pos2)
  base = (x)**2 + (y)**2
  return pow(base, 1/2)

def get_proportion():
  return earth_size / earth_real_size