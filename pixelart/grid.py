import dataclasses

from pixelart.pixel import Pixel

X = int
Y = int


@dataclasses.dataclass
class Grid:

    pixel_size: int
    height: int
    width: int
    pixelsXY: dict[tuple[X, Y], Pixel] = dataclasses.field(init=False)

    def __post_init__(self):
        if self.height <= 0:
            raise ValueError(f"Param height must be positive {self.height}")
        if self.width <= 0:
            raise ValueError(f"Param width must be positive {self.width}")
        if self.pixel_size <= 0:
            raise ValueError(f"Param pixel_size must be positive {self.pixel_size}")
        self.pixelsXY = {}

    def __iter__(self):
        yield from self.pixelsXY.items()
