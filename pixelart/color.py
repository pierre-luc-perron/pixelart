import dataclasses
import functools
import itertools

MIN_COLOR = 0
MAX_COLOR = 255
HColor = str


@dataclasses.dataclass(frozen=True)
class RGB:
    """
    >>> RGB(127, 0, 255)
    RGB(red=127, green=0, blue=255)
    """

    red: int
    green: int
    blue: int

    def __post_init__(self):
        if not MIN_COLOR <= self.red <= MAX_COLOR:
            raise ValueError(
                f"Red byte <{self.green}> not in [{MIN_COLOR}..{MAX_COLOR}]"
            )
        if not MIN_COLOR <= self.green <= MAX_COLOR:
            raise ValueError(
                f"Green byte <{self.green}> not in [{MIN_COLOR}..{MAX_COLOR}]"
            )
        if not MIN_COLOR <= self.blue <= MAX_COLOR:
            raise ValueError(
                f"Blue byte <{self.green}> not in [{MIN_COLOR}..{MAX_COLOR}]"
            )


@functools.total_ordering
@dataclasses.dataclass()
class Color:
    """
    >>> Color(RGB(127, 0, 255))
    Color(rgb=RGB(red=127, green=0, blue=255), hexa='#7f00ff')
    """

    rgb: RGB
    hexa: HColor = dataclasses.field(init=False)

    def __post_init__(self):
        r, g, b = self.rgb.red, self.rgb.green, self.rgb.blue
        self.hexa = f"#{r:02x}{g:02x}{b:02x}"

    def __lt__(self, other):
        if not isinstance(other, Color):
            raise ValueError("Cannot compare Color with anyhting else but its own type")
        return self.hexa < other.hexa


DEFAULT_COLORS: tuple[Color, ...] = tuple(
    sorted(Color(RGB(*rgb)) for rgb in itertools.product((0, 127, 255), repeat=3))
)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
