import pygame as pg

from enum import Enum


class Color:
    BLACK = (0, 0, 0)
    DARK_GREY = (31, 32, 34)
    DARK_GREY_2 = (46, 48, 51) # lighter
    RED = (255, 123, 114)
    GREEN = (126, 231, 135)
    BLUE = (88, 166, 255)
    YELLOW = (255, 234, 127)
    PURPLE = (210, 168, 255)
    CYAN = (0, 255, 255)
    DARK_CYAN = (0, 204, 204)
    WHITE = (246, 248, 250)


class State(Enum):
    EMPTY = 0
    START = 1
    END = 2
    WALL = 3
    VISITING = 4
    VISITED = 5
    PATH = 6


FPS_LOOKUP = {
    0: "Unlocked",
    60: "Slow",
    90: "Medium",
    120: "Fast"
}

COLOR_LOOKUP = {
    State.EMPTY: Color.WHITE,
    State.START: Color.GREEN,
    State.END: Color.RED,
    State.WALL: Color.DARK_GREY_2,
    State.VISITING: Color.CYAN,
    State.VISITED: Color.DARK_CYAN,
    State.PATH: Color.YELLOW,
}

LEGEND = {
    "Start Vertex": Color.GREEN,
    "End Vertex": Color.RED,
    "Visiting": Color.CYAN,
    "Visited": Color.DARK_CYAN,
    "Wall": Color.DARK_GREY_2,
    "Weight": Color.WHITE,
    "Path": Color.YELLOW,
}
