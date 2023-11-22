import unittest
import decorator


class TestDecorator(unittest.TestCase):

    def test_incorrect_type_k(self):
        decorator.mean.time = []

        @decorator.mean("10")
        def new_foo(arg1):
            decorator.time.sleep(decorator.SLEEP)
            return arg1

        with self.assertRaises(TypeError):
            new_foo("Walter")

    def test_valid_type_k(self):
        decorator.mean.time = []

        @decorator.mean("10")
        def new_foo(arg1):
            decorator.time.sleep(decorator.SLEEP)
            return arg1

        with self.assertRaises(TypeError):
            new_foo("Walter")


if __name__ == "__main__":
    unittest.main()
