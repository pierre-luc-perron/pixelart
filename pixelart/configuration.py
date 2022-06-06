import dataclasses

from pixelart.editor import Editor
from pixelart.palette import Palette


@dataclasses.dataclass
class Configuration:
    palette: Palette
    editor: Editor
