from .model import Knister


def test_eval_group_no_score():
    assert Knister.eval_group([0, 3, 4, 5, 6]) == 0


def test_eval_group_incomplete():
    assert Knister.eval_group([0, 7, 7, 7, 7]) == 0


def test_eval_group_one_double():
    assert Knister.eval_group([2, 2, 5, 6, 7]) == 1


def test_eval_group_two_doubles():
    assert Knister.eval_group([2, 2, 3, 3, 5]) == 3


def test_eval_group_triple():
    assert Knister.eval_group([2, 2, 2, 3, 5]) == 3


def test_eval_group_full_house():
    assert Knister.eval_group([2, 2, 3, 3, 3]) == 8


def test_eval_group_street_with_7():
    assert Knister.eval_group([7, 5, 6, 4, 3]) == 8


def test_eval_group_street_without_7_higher():
    assert Knister.eval_group([8, 9, 10, 11, 12]) == 12


def test_eval_group_street_with_7_lower():
    assert Knister.eval_group([2, 3, 4, 5, 6]) == 12


def test_eval_group_fiver():
    assert Knister.eval_group([2, 2, 2, 2, 2]) == 10


def test_finished_empty():
    k = Knister()
    k.field = [[0, 0, 0, 0, 0]] * 5
    assert not k.is_finished()


def test_finished_filled():
    k = Knister()
    k.field = [[2, 3, 4, 5, 6]] * 5
    assert k.is_finished()


def test_finished_one_zero():
    k = Knister()
    k.field = [[2, 3, 4, 5, 6]] * 4 + [[2, 3, 4, 5, 0]]
    assert not k.is_finished()
