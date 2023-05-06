from unittest import TestCase
from src.diff_query_api.diff_query_lambda.diff_query_lambda import DiffQueryLambda

class TestDiffQueryLambda(TestCase):
    def setUp(self) -> None:
        self.diff_query_lambda = DiffQueryLambda()
        return super().setUp()


    def test_compare(self):
        # Arrange
        request = {
            "primaryText": "Hellow world. This is cool.\n",
            "secondaryText": "Hellow world. Testing how this works. This is cool.\n"
        }

        # Act
        self.diff_query_lambda.handle(request, None)

        # Assert