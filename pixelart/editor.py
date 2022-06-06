import dataclasses

from pixelart.color import DEFAULT_COLORS
from pixelart.grid import Grid
from pixelart.pixel import Pixel, Pos2D


@dataclasses.dataclass
class Editor(Grid):
    def __post_init__(self):
        super().__post_init__()
        if self.pixel_size <= 0:
            raise ValueError(f"Param pixel_size must be positive {self.pixel_size}")
        background_color = DEFAULT_COLORS[-1]
        assert background_color.hexa == "#ffffff"  # white
        self.pixelsXY = {}
        for row in range(self.height):
            for col in range(self.width):
                self.pixelsXY[(col, row)] = Pixel(
                    pos2d=Pos2D(col, row), color=background_color
                )

    def __iter__(self):
        yield from self.pixelsXY.items()
