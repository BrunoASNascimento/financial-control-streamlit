"""Unit Test - Package - index"""

from financial_control.package import example
from financial_control.mongo_services.connect_mongo import get_database
import pytest
from pytest import mark
from dotenv import find_dotenv, load_dotenv


class TestExample:

    def test_example(self):
        """Method to test Example"""
        testexample = example()

        # Then
        assert testexample == 10

    @mark.test_connection_mongo
    def test_mongo_connection(self):
        load_dotenv(find_dotenv())
        dbname = get_database()


# To execute tests wihr mark
# $ pytest -v -m calcular_bonus
# $ pytest --cov=codigo tests/ --cov-report html
