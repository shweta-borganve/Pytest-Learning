import pytest


@pytest.fixture
def numbers():
    return [10, 20, 30]


from calculator import (
    add,
    subtract,
    multiply,
    greet,
    calculate_total,
    get_user_profile,
    find_item,
    divide,
)


class TestCalculator:

    def test_numbers(self, numbers):
        assert numbers == [10, 20, 30]

    def test_user(self, user):
        assert user["name"] == "Shweta"
        assert user["role"] == "developer"
        assert user["active"] is True

    def test_message(self, test_message):
        assert test_message == "Hello, pytest!"

    @pytest.mark.calculator
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 5),
            (1, 3, 4),
            (5, 5, 11),
            (-1, 0, -1),
            (-5, -5, -10),
        ],
    )
    def test_add(self, a, b, expected):
        assert add(a, b) == expected

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_multiply(self):
        assert multiply(5, 5) == 25

    def test_greet(self):
        assert greet("Shweta") == "Hello, Shweta!"

    def test_calculate_total(self):
        assert calculate_total([20, 40, 40]) == 100

    def test_get_user_profile(self):
        profile = get_user_profile("Shweta", "developer", True)

        assert profile["name"] == "Shweta"
        assert profile["role"] == "developer"
        assert profile["active"] is True

    def test_find_item_found(self):
        items = ["apple", "banana", "orange"]

        assert find_item(items, "banana") == "banana"

    def test_find_item_not_found(self):
        items = ["apple", "banana", "orange"]

        assert find_item(items, "grape") is None

    def test_divide_success(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)