import unittest

from sentry.api.validators.sentry_apps.schema import validate_component

from .util import invalid_schema


class TestHeaderSchemaValidation(unittest.TestCase):
    def setUp(self):
        self.schema = {"type": "header", "text": "Beep"}

    def test_valid_schema(self):
        validate_component(self.schema)

    @invalid_schema
    def test_missing_text(self):
        del self.schema["text"]
        validate_component(self.schema)

    @invalid_schema
    def test_invalid_text_type(self):
        self.schema["text"] = 1
        validate_component(self.schema)
