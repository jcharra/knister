from .main import eval_group


def test_eval_group_no_score():
    assert eval_group([0, 3, 4, 5, 6]) == 0


def test_eval_group_incomplete():
    assert eval_group([0, 7, 7, 7, 7]) == 0


def test_eval_group_one_double():
    assert eval_group([2, 2, 5, 6, 7]) == 1


def test_eval_group_two_doubles():
    assert eval_group([2, 2, 3, 3, 5]) == 3


def test_eval_group_triple():
    assert eval_group([2, 2, 2, 3, 5]) == 3


def test_eval_group_full_house():
    assert eval_group([2, 2, 3, 3, 3]) == 8


def test_eval_group_street_with_7():
    assert eval_group([7, 5, 6, 4, 3]) == 10


def test_eval_group_street_without_7_higher():
    assert eval_group([8, 9, 10, 11, 12]) == 12


def test_eval_group_street_with_7_lower():
    assert eval_group([2, 3, 4, 5, 6]) == 12


def test_eval_group_fiver():
    assert eval_group([2, 2, 2, 2, 2]) == 10
