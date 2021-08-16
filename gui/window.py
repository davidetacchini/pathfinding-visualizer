import pygame as pg

from .button import Button
from consts import *


class Window:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Pathfinding Visualizer")
        self._allowed = (pg.QUIT, pg.MOUSEBUTTONDOWN, pg.MOUSEMOTION)
        pg.event.set_allowed(self._allowed)
        self._flags = pg.DOUBLEBUF
        self.width = 1100
        self.height = 800
        self.screen = pg.display.set_mode((self.width, self.height), self._flags, 16)
        self.screen.set_alpha(None)
        self.screen.fill(Color.DARK_GREY)
        self.font = pg.font.Font("./assets/open-sans.ttf", 15)
        self.clock = pg.time.Clock()
        self.buttons = self.get_buttons()
        self.categorized_buttons = self.get_buttons(categorized=True)
        self.fps = 60
        self.paused = False
        self.executing = False # if executing an algorithm
        self.statistics = (
            "Algorithm:",
            "Execution time:",
            "Visited vertices:",
            "Shortest path:",
        )

    def update(self, grid):
        self.screen.fill(Color.DARK_GREY)
        self.draw_buttons()
        self.draw_statistics()
        self.draw_legend()
        grid.update(self)
        pg.display.update()
        self.clock.tick(self.fps)
    
    def draw_text(self, text, x, y, *, color=Color.WHITE):
        text_render = self.font.render(text, True, color)
        self.screen.blit(text_render, (x, y))

    def get_buttons(self, categorized=False):
        algorithms = {
            "dijkstra": Button("Dijkstra", self.width - 280, 50),
            "astar": Button("A*", self.width - 140, 50),
            "bfs": Button("BFS", self.width - 280, 100),
            "dfs": Button("DFS", self.width - 140, 100),
            "greedy": Button("Greedy", self.width - 280, 150)
        }
        actions = {
            "clear": Button("Clear", self.width - 280, 240),
            "reset": Button("Reset", self.width - 140, 240),
            "pause": Button("Pause", self.width - 280, 290),
            "fps": Button("Slow", self.width - 140, 290)
        }
        maze = {
            "prim": Button("Prim", self.width - 280, 380),
        }
        if categorized:
            return {
                "algorithms": algorithms,
                "actions": actions,
                "maze": maze,
            }
        else:
            return algorithms | actions | maze

    def draw_buttons(self):
        buttons = self.categorized_buttons

        self.draw_text("ALGORITHMS", self.width - 280, 20, color=Color.DARK_CYAN)
        for button in buttons["algorithms"].values():
            button.bg_color = Color.RED if self.executing else Color.WHITE
            button(self.screen, self.font)

        self.draw_text("ACTIONS", self.width - 280, 210, color=Color.DARK_CYAN)
        for key, button in buttons["actions"].items():
            if key in ("clear", "reset"):
                button.bg_color = Color.RED if self.executing else Color.WHITE
            if key == "pause":
                button.text = "Continue" if self.paused else "Pause"
            elif key == "fps":
                button.text = FPS_LOOKUP.get(self.fps)
                # if generating a maze or path, fps are set to 0 and cannot
                # be changed
                button.bg_color = Color.RED if self.fps == 0 else Color.WHITE
            button(self.screen, self.font)

        self.draw_text("MAZE", self.width - 280, 350, color=Color.DARK_CYAN)
        for button in buttons["maze"].values():
            button.bg_color = Color.RED if self.executing else Color.WHITE
            button(self.screen, self.font)
    
    def draw_legend(self):
        self.draw_text("LEGEND", self.width - 280, 600, color=Color.DARK_CYAN)
        for index, (text, color) in enumerate(LEGEND.items()):
            margin = index * 20
            if index % 2 == 0:
                rect_x = self.width - 280
                text_x = self.width - 250
            else:
                rect_x = self.width - 140
                text_x = self.width - 110
                margin -= 20
            pg.draw.rect(self.screen, color, (rect_x, 635 + margin, 25, 25))
            if text == "Weight":
                self.draw_text("5", rect_x + 9, 636 + margin, color=Color.BLACK)
            self.draw_text(text, text_x, 635 + margin)
   
    def draw_statistics(self):
        self.draw_text("STATISTICS", self.width - 280, 460, color=Color.DARK_CYAN)
        for index, text in enumerate(self.statistics):
            index *= 20 # new line
            self.draw_text(text, self.width - 280, 490 + index)
