import pytest

from pixelart.editor import Editor
from pixelart.pixel import Pixel


@pytest.fixture
def editor():
    return Editor(pixel_size=8, width=8, height=8)


def test_editor_draws_on_a_2d_grid_of_pixel(editor):
    positions = [pos2d for pos2d, pixel in editor]
    assert 64 == len(positions)
    assert 0 == min(x for (x, _) in positions)
    assert 7 == max(x for (x, _) in positions)
    assert 0 == min(y for (_, y) in positions)
    assert 7 == max(y for (_, y) in positions)


def test_editor_accesses_any_pixel_by_its_x_y_position(editor):
    px0y0 = editor.pixelsXY[(0, 0)]
    px1y1 = editor.pixelsXY[(1, 1)]
    assert isinstance(px0y0, Pixel)
    assert isinstance(px1y1, Pixel)
    assert px0y0 != px1y1


def test_editor_has_a_white_background_by_default(editor):
    assert {"#ffffff"} == {pixel.color.hexa for pos2d, pixel in editor}
