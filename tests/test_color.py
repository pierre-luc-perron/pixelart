import pytest

from pixelart.color import DEFAULT_COLORS, RGB, Color


def test_color_palette_contains_at_least_one_color():
    assert len(DEFAULT_COLORS) > 0


def test_color_red_in_between_0_and_255():
    assert RGB(red=0, green=0, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=-1, green=0, blue=0)
    assert RGB(red=255, green=0, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=256, green=0, blue=0)


def test_color_green_in_between_0_and_255():
    assert RGB(red=0, green=0, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=0, green=-1, blue=0)
    assert RGB(red=0, green=255, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=0, green=256, blue=0)


def test_color_blue_in_between_0_and_255():
    assert RGB(red=0, green=0, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=0, green=-1, blue=0)
    assert RGB(red=0, green=255, blue=0)
    with pytest.raises(ValueError):
        assert RGB(red=0, green=256, blue=0)


def test_rgb_color_generates_an_equivalent_hexa_color():
    assert "#7f00ff" == Color(RGB(127, 0, 255)).hexa


def test_color_compares_other_color_by_value_of_red_green_blue():
    color = Color(RGB(1, 1, 1))
    assert Color(RGB(0, 0, 0)) < color
    assert Color(RGB(0, 0, 1)) < color
    assert Color(RGB(0, 0, 2)) < color
    assert Color(RGB(0, 1, 0)) < color
    assert Color(RGB(0, 1, 1)) < color
    assert Color(RGB(0, 1, 2)) < color
    assert Color(RGB(1, 0, 0)) < color
    assert Color(RGB(1, 0, 1)) < color
    assert Color(RGB(1, 0, 2)) < color
    assert Color(RGB(1, 0, 2)) < color
    assert Color(RGB(1, 1, 0)) < color
    assert Color(RGB(1, 1, 1)) == color
    assert Color(RGB(1, 1, 2)) > color
    assert Color(RGB(1, 2, 0)) > color
    assert Color(RGB(1, 2, 1)) > color
    assert Color(RGB(1, 2, 2)) > color
    assert Color(RGB(2, 0, 0)) > color
    assert Color(RGB(2, 0, 1)) > color
    assert Color(RGB(2, 0, 2)) > color
    assert Color(RGB(2, 1, 0)) > color
    assert Color(RGB(2, 1, 1)) > color
    assert Color(RGB(2, 1, 2)) > color
    assert Color(RGB(2, 2, 0)) > color
    assert Color(RGB(2, 2, 1)) > color
    assert Color(RGB(2, 2, 2)) > color
