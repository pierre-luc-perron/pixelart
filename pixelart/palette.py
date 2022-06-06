import dataclasses

from pixelart.color import DEFAULT_COLORS
from pixelart.grid import Grid
from pixelart.pixel import Pixel, Pos2D


@dataclasses.dataclass(frozen=False)
class Palette(Grid):
    def __post_init__(self):
        super().__post_init__()
        # TODO: Color ellision. Or, number of colors will exceed palette size
        assert len(DEFAULT_COLORS) <= (self.height * self.width)
        self.pixelsXY = {}
        _colors = iter(DEFAULT_COLORS)
        for row in range(self.height):
            for col in range(self.width):
                _color = next(_colors)
                pixel = Pixel(pos2d=Pos2D(col, row), color=_color)
                self.pixelsXY[(col, row)] = pixel
