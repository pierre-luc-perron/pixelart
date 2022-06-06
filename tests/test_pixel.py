import dataclasses

import pytest

from pixelart.color import RGB, Color
from pixelart.pixel import Pixel, Pos2D


@pytest.fixture
def color():
    return Color(RGB(127, 0, 255))


@pytest.fixture
def pixel(color):
    return Pixel(Pos2D(0, 1), color)


def test_pixel_describes_XY_positions(pixel):
    assert Pos2D(0, 1) == pixel.pos2d


def test_pixel_position_are_non_negative_number(color):
    Pixel(Pos2D(0, 0), color)
    with pytest.raises(ValueError):
        Pixel(Pos2D(-1, 0), color)
    with pytest.raises(ValueError):
        Pixel(Pos2D(0, -1), color)


def test_pixel_has_color(pixel):
    assert "#7f00ff" == pixel.color.hexa


def test_pixel_scale_size_is_positive_number(color):
    Pixel.scale(0, 0, px_size=1)
    with pytest.raises(ValueError):
        Pixel.scale(0, 0, px_size=0)
    with pytest.raises(ValueError):
        Pixel.scale(0, 0, px_size=-1)


def test_pixel_scale_up_by_n_expands_previous_pixel():
    assert 1 == Pixel.scale(1, 0, px_size=1).left
    assert 4 == Pixel.scale(2, 0, px_size=2).left
    assert 9 == Pixel.scale(3, 0, px_size=3).left

    assert 1 == Pixel.scale(0, 1, px_size=1).top
    assert 4 == Pixel.scale(0, 2, px_size=2).top
    assert 9 == Pixel.scale(0, 3, px_size=3).top


def test_pixel_scale_up_by_n_refer_to_pixel_length():
    assert 1 == len(Pixel.scale(x=0, y=0, px_size=1))
    for n in range(1, 16):
        assert n == len(Pixel.scale(x=0, y=0, px_size=n))


def test_pixel_scale_result_enum_fields_in_particular_order():
    px_rect = Pixel.scale(0, 2, px_size=3)
    assert (0, 6, 3, 9) == dataclasses.astuple(px_rect)
    assert 0 == px_rect.left
    assert 6 == px_rect.top
    assert 3 == px_rect.right
    assert 9 == px_rect.bottom
