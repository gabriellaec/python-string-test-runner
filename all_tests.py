from strtest import str_test

class TestCase(str_test.TestCaseWrapper):
    TIMEOUT = 1  # In seconds

    def test_1(self):
        result = self.function(1, 2)
        self.assertEqual(3, result, msg=f'Results are not equal. Expected: 3. Got: {result}')

    