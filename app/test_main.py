from unittest.mock import patch
from app.main import outdated_products
import datetime
import pytest


@pytest.fixture
def test_data() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


class MockedDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 3)


@patch("datetime.date", new=MockedDate)
def test_outdated_products(test_data: list) -> None:
    assert outdated_products(test_data) == ["duck"]
