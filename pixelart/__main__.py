"""Pixel Art Drawing Tool Editor."""

# TODO: Capture signals and graceful shutdown


def main():
    # main controls the order of import. The only important distinction is this
    # project modules vs the rest (Python and libraries). Project modules
    # should sit in main to guarantee the other modules are loaded first. For
    # instance, logging needs proper initialization before Python load other
    # modules. Otherwise, the order of each group should not matter, but Python
    # modules are preferred before libraries.

    from pixelart.configuration import Configuration
    from pixelart.editor import Editor
    from pixelart.palette import Palette

    configuration = Configuration(
        palette=Palette(height=9, width=3, pixel_size=8),
        editor=Editor(height=12, width=12, pixel_size=8),
    )

    from pixelart.ui import UI

    UI(configuration).run()


main()
