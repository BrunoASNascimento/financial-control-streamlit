# from financial_control.package import example
from financial_control.mongo_services.connect_mongo import MongoServices
import pytest
from pytest import mark
from dotenv import find_dotenv, load_dotenv

from pymongo import database, cursor


class TestExample:

    @mark.test_connection_mongo
    def test_mongo_connection(self):
        load_dotenv(find_dotenv())
        MongoServices.initialize()
        dbname = MongoServices.DATABASE
        assert type(dbname) == database.Database

    @mark.test_read_document
    def test_read_document(self):
        data_read = MongoServices.find("accounts", {})
        assert type(data_read) == cursor.Cursor

    @mark.test_insert_read_delete
    def test_insert_read_delete(self):
        data = {
            "testStr": "test",
            "testNumber": 1234
        }
        id_cod = MongoServices.insert("test", data)
        data_read = MongoServices.find_one("test", id_cod)

        assert data == data_read

        MongoServices.delete("test", {"_id": id_cod})

        data_read = MongoServices.find_one("test", id_cod)

        assert data_read == None


# To execute tests wihr mark
# $ pytest -v -m calcular_bonus
# $ pytest --cov=codigo tests/ --cov-report html
