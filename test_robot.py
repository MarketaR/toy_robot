import pytest
from robot import Robot

toy_robot = Robot(placed=False, x=None, y=None, facing=None)


@pytest.mark.parametrize(['x', 'y', 'f'], [(2, 8, 'NORTH'), (5, 1, 'EAST'), (0, 0, 'WAST')],)
def test_place(x, y, f):
    toy_robot.place(x, y, f)
    assert toy_robot.placed == False


def test_left():
    toy_robot = Robot(placed=True, x=3, y=3, facing='NORTH')
    toy_robot.left()
    assert toy_robot.facing == 'WEST'


def test_right():
    toy_robot = Robot(placed=True, x=3, y=3, facing='EAST')
    toy_robot.right()
    assert toy_robot.facing == 'SOUTH'


def test_move():
    toy_robot = Robot(placed=True, x=3, y=3, facing='EAST')
    toy_robot.move()
    assert toy_robot.x == 4
