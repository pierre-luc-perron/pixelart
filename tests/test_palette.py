import pytest

from pixelart.palette import Palette
from pixelart.pixel import Pixel


@pytest.fixture
def palette():
    return Palette(pixel_size=8, width=3, height=9)


def test_palette_draws_on_a_2d_grid_of_pixel(palette):
    positions = [pos2d for pos2d, pixel in palette]
    assert 27 == len(positions)
    assert 0 == min(x for (x, _) in positions)
    assert 2 == max(x for (x, _) in positions)
    assert 0 == min(y for (_, y) in positions)
    assert 8 == max(y for (_, y) in positions)


def test_palette_accesses_any_pixel_by_its_x_y_position(palette):
    px0y0 = palette.pixelsXY[(0, 0)]
    px1y1 = palette.pixelsXY[(1, 1)]
    assert isinstance(px0y0, Pixel)
    assert isinstance(px1y1, Pixel)
    assert px0y0 != px1y1


def test_fill_pixels_with_different_colors(palette):
    colors = [pixel.color.hexa for _, pixel in palette]
    unique_colors = {pixel.color.hexa for _, pixel in palette}
    assert 27 == len(unique_colors) == len(colors)
