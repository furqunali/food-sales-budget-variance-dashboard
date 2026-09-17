from src.variance_engine import calculate


def test_positive_variance():
    result = calculate(100, 120)
    assert result.amount == 20
    assert result.percentage == 20


def test_negative_variance():
    result = calculate(200, 150)
    assert result.amount == -50
    assert result.percentage == -25


def test_zero_budget():
    assert calculate(0, 0).percentage == 0
