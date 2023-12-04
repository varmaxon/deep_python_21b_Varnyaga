import unittest
import decorator


class TestDecorator(unittest.TestCase):

    def test_incorrect_type_k(self):
        @decorator.mean("10")
        def new_foo(arg, *args, **kwargs):
            decorator.time.sleep(decorator.SLEEP)
            return arg

        with self.assertRaises(TypeError):
            new_foo("Walter", "Hello", 123)

    def test_valid_type_k(self):
        @decorator.mean(10)
        def new_foo(arg, *args, **kwargs):
            decorator.time.sleep(decorator.SLEEP)
            return arg

        result = new_foo("Walter")
        print("Result", result)


if __name__ == "__main__":
    unittest.main()
