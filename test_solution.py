from solution import DogBoarder
import pytest


def test_initial_state():
    boarder = DogBoarder(5, 10)
    assert boarder.total_slots == 5
    assert boarder.daily_rate == 10
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 0


def test_different_initial_state():
    boarder = DogBoarder(3, 15)
    assert boarder.total_slots == 3
    assert boarder.daily_rate == 15
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 0


def test_boarding_until_full():
    boarder = DogBoarder(5, 15)
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 0
    boarder.board("dog1", "breed1", "owner1")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 1
    boarder.board("dog2", "breed2", "owner2")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 2
    boarder.board("dog3", "breed3", "owner3")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 3
    boarder.board("dog4", "breed4", "owner4")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 4
    boarder.board("dog5", "breed5", "owner5")
    assert boarder.is_full() is True
    assert boarder.slots_occupied() == 5


def test_different_boarding_until_full():
    boarder = DogBoarder(3, 15)
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 0
    boarder.board("dog1", "breed1", "owner1")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 1
    boarder.board("dog2", "breed2", "owner2")
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 2
    boarder.board("dog3", "breed3", "owner3")
    assert boarder.is_full() is True
    assert boarder.slots_occupied() == 3


def test_cannot_board_after_full():
    boarder = DogBoarder(1, 30)
    boarder.board("dog1", "breed1", "owner1")
    assert boarder.is_full() is True
    assert boarder.slots_occupied() == 1

    with pytest.raises(ValueError):
        boarder.board("dog2", "breed2", "owner2")

    assert boarder.is_full() is True
    assert boarder.slots_occupied() == 1


def test_board_and_pickup():
    boarder = DogBoarder(3, 15)
    boarder.board("dog1", "breed1", "owner1")
    cost = boarder.pick_up("dog1", "breed1", "owner1", 4)
    assert cost == 60
    assert boarder.slots_occupied() == 0


def test_cannot_double_pickup():
    boarder = DogBoarder(3, 15)
    boarder.board("dog1", "breed1", "owner1")
    boarder.pick_up("dog1", "breed1", "owner1", 4)

    with pytest.raises(ValueError):
        boarder.pick_up("dog1", "breed1", "owner1", 4)


def test_complex_board_and_pickup():
    boarder = DogBoarder(3, 10)
    boarder.board("dog1", "breed1", "owner1")
    boarder.board("dog2", "breed2", "owner2")
    boarder.board("dog3", "breed3", "owner3")

    with pytest.raises(ValueError):
        # This dog doesn't exist
        boarder.pick_up("dog1", "breed2", "owner3", 5)
    assert boarder.is_full() is True
    assert boarder.slots_occupied() == 3

    cost = boarder.pick_up("dog2", "breed2", "owner2", 5)
    assert cost == 50
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 2

    with pytest.raises(ValueError):
        # This dog has already been picked up
        boarder.pick_up("dog2", "breed2", "owner2", 3)
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 2

    cost = boarder.pick_up("dog1", "breed1", "owner1", 3)
    assert cost == 30
    assert boarder.is_full() is False
    assert boarder.slots_occupied() == 1