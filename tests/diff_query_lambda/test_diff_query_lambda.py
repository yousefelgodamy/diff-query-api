import pytest
import unittest 
from diff_query_api.diff_query_functions import DiffQueryExecutor
from diff_query_api.diff_query_models import DiffQueryGetDiffRequest, DiffQueryGetDiffResponse
import json

class TestDiffQuery(unittest.TestCase):
    def setUp(self) -> None:
        self.diff_query_executor = DiffQueryExecutor()
        return super().setUp()

    def test_get_diff_insertion(self):
        # Arrange
        request = {
            "primaryText": "Hello world.\n",
            "secondaryText": "Hello world. Test.\n"
        }
        request = DiffQueryGetDiffRequest.parse_obj(request)
        expected_response = {
            "textDiff": [(0, "Hello world."), (1, " Test."), (0, "\n")]
        }
        expected_response_json = json.dumps(expected_response)

        # Act
        output = self.diff_query_executor.get_diff(request)

        # Assert
        self.assertEqual(expected_response_json, output)

    def test_get_diff_deletion(self):
        # Arrange
        request = {
            "primaryText": "Hello world. Test.\n",
            "secondaryText": "Hello world.\n"
        }
        request = DiffQueryGetDiffRequest.parse_obj(request)
        expected_response = {
            "textDiff": [(0, "Hello world."), (-1, " Test."), (0, "\n")]
        }
        expected_response_json = json.dumps(expected_response)

        # Act
        output = self.diff_query_executor.get_diff(request)

        # Assert
        self.assertEqual(expected_response_json, output)

    def test_get_diff_change(self):
        # Arrange
        request = {
            "primaryText": "Hello world. Test the text.\n",
            "secondaryText": "Hello world. Change the text.\n"
        }
        request = DiffQueryGetDiffRequest.parse_obj(request)
        expected_response = {
            "textDiff": [(0, "Hello world. "), (-1, "Test"), (1, "Change"), (0, " the text.\n")]
        }
        expected_response_json = json.dumps(expected_response)

        # Act
        output = self.diff_query_executor.get_diff(request)

        # Assert
        self.assertEqual(expected_response_json, output)
