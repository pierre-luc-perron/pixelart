import dataclasses
import sys

import PySimpleGUI as sg

from pixelart.color import DEFAULT_COLORS, Color
from pixelart.configuration import Configuration
from pixelart.pixel import Pixel


class UI:
    def __init__(self, configuration: Configuration):

        self.c = configuration
        p = self.c.palette
        e = self.c.editor
        self.PALETTE_LAYOUT = [
            [
                sg.Graph(
                    canvas_size=(
                        p.width * p.pixel_size + 2,
                        p.height * p.pixel_size + 2,
                    ),
                    graph_bottom_left=(0, p.height * p.pixel_size + 2),
                    graph_top_right=(p.width * p.pixel_size + 2, 0),
                    key="PALETTE",
                    change_submits=True,
                    drag_submits=False,
                )
            ]
        ]
        self.EDITOR_LAYOUT = [
            [
                sg.Graph(
                    canvas_size=(
                        e.width * e.pixel_size + 2,
                        e.height * e.pixel_size + 2,
                    ),
                    graph_bottom_left=(0, e.height * e.pixel_size + 4),
                    graph_top_right=(e.width * e.pixel_size + 4, 0),
                    key="EDITOR",
                    change_submits=True,
                    drag_submits=False,
                )
            ]
        ]
        self.WINDOW_LAYOUT = [
            [
                sg.Frame(title="", layout=[[sg.Column(layout=self.PALETTE_LAYOUT)]]),
                sg.Column(layout=self.EDITOR_LAYOUT),
            ]
        ]
        self.WINDOW = sg.Window("Pixel Art", self.WINDOW_LAYOUT, finalize=True)
        self._palette = self.WINDOW["PALETTE"]
        self._editor = self.WINDOW["EDITOR"]
        self._selected_color: Color = DEFAULT_COLORS[-1]

        for (col, row), pixel in p:
            left, top, right, bottom = dataclasses.astuple(
                Pixel.scale(col, row, px_size=p.pixel_size)
            )
            color = p.pixelsXY[col, row].color.hexa
            self._palette.draw_rectangle(
                (left, top), (right, bottom), line_color="black", fill_color=color
            )

        for (col, row), pixel in e:
            left, top, right, bottom = dataclasses.astuple(
                Pixel.scale(col, row, px_size=p.pixel_size)
            )
            self._editor.draw_rectangle(
                (left, top),
                (right, bottom),
                line_color="black",
                fill_color=self._selected_color.hexa,
            )

    def run(self) -> None:
        p = self.c.palette
        e = self.c.editor
        while True:
            event, values = self.WINDOW.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            draw_mouse = values["EDITOR"]
            palette_mouse = values["PALETTE"]

            if event == "PALETTE" and palette_mouse != (None, None):
                px = p.pixel_size
                col = int(palette_mouse[0] // px)
                row = int(palette_mouse[1] // px)
                try:
                    color = p.pixelsXY[(col, row)].color
                except KeyError:
                    # Deterministic error: Clicking the palette's right-hand
                    # border triggers a KeyError.
                    print(f"Color Index out of bound {col} {row}", file=sys.stderr)
                else:
                    self._selected_color = color

            if event == "EDITOR" and draw_mouse != (None, None):
                px = e.pixel_size
                col = int(draw_mouse[0] // px)
                row = int(draw_mouse[1] // px)
                fill_left = col * px
                fill_top = row * px
                top_left = (fill_left, fill_top)
                fill_right = fill_left + px
                fill_bottom = fill_top + px
                bottom_right = (fill_right, fill_bottom)
                self._editor.draw_rectangle(
                    top_left,
                    bottom_right,
                    line_color="black",
                    fill_color=self._selected_color.hexa,
                )

        self.WINDOW.close()
