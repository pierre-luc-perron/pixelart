import pytest

from pixelart.grid import Grid


def test_editor_height_is_positive_number():
    Grid(pixel_size=1, width=1, height=1)
    with pytest.raises(ValueError):
        Grid(pixel_size=1, width=1, height=0)
    with pytest.raises(ValueError):
        Grid(pixel_size=1, width=1, height=-1)


def test_editor_width_is_positive_number():
    Grid(pixel_size=1, width=1, height=1)
    with pytest.raises(ValueError):
        Grid(pixel_size=0, width=0, height=1)
    with pytest.raises(ValueError):
        Grid(pixel_size=-1, width=-1, height=1)


def test_editor_pixel_size_is_positive_number():
    Grid(pixel_size=1, width=1, height=1)
    with pytest.raises(ValueError):
        Grid(pixel_size=0, width=1, height=1)
    with pytest.raises(ValueError):
        Grid(pixel_size=-1, width=1, height=1)
