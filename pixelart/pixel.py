import dataclasses

from pixelart.color import Color


# TODO: Consider pydantic.
@dataclasses.dataclass(frozen=True)
class Pos2D:
    """
    >>> Pos2D(0, 1)
    Pos(x=0, y=1)
    """

    x: int
    y: int

    def __post_init__(self):
        if self.x < 0:
            raise ValueError(f"Param x value must be positive {self.x}")
        if self.y < 0:
            raise ValueError(f"Param y value must be positive {self.y}")


@dataclasses.dataclass(frozen=True)
class _Square:
    # UI framework requires 4 sides as pairs (left, top), (right, bottom). Hence,
    # the latter form dictates which fields Square dataclass expose.
    left: int
    top: int
    right: int
    bottom: int

    def __len__(self):
        length = self.right - self.left
        assert length == (self.bottom - self.top)
        return length


@dataclasses.dataclass
class Pixel:

    pos2d: Pos2D
    color: Color

    @classmethod
    def scale(cls, /, x: int, y: int, *, px_size: int = 1) -> _Square:
        """Scale a pixel up to `px_size`

        >>> Pixel.scale((0,0), px_size=1)
        _Square(left=0, top=0, right=1, bottom=1)
        """
        if px_size <= 0:
            raise ValueError(f"Param px_size must be positive {px_size}")
        pos2D = Pos2D(x=x, y=y)
        left = pos2D.x * px_size
        top = pos2D.y * px_size
        right = left + px_size
        bottom = top + px_size
        return _Square(left=left, top=top, right=right, bottom=bottom)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
