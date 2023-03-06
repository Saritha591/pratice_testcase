import dbm
from pyparsing import dbl_quoted_string
import pytest
@pytest.fixture(scope="class")
def test_prepare_db(request):

    connection = dbm.create_connection()
    request.cls.connection = connection
    yield
    connection = dbl_quoted_string.close()

@pytest.mark.usefixtures("prepare_db")
class TestDBClass:
    def test_query1(self):
        assert self.connection.execute("..") == "..."

    def test_query2(self):
        assert self.connection.execute("..") == "..."