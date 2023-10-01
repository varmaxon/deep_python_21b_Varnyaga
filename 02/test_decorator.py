import unittest
import decorator


class TestDecorator(unittest.TestCase):

    def test_foo_from_task(self):
        decorator.mean.time = []
        for _ in range(100):
            self.assertLess(abs(decorator.foo("Walter")[1] -
                                decorator.SLEEP), decorator.EPSILON)

    def test_boo_from_task(self):
        decorator.mean.time = []
        for _ in range(100):
            self.assertLess(abs(decorator.boo("Walter")[1] -
                                decorator.SLEEP), decorator.EPSILON)

    def test_foo_another_sleep_time(self):
        decorator.SLEEP = 1
        decorator.mean.time = []
        for _ in range(30):
            self.assertLess(abs(decorator.boo("Walter")[1] -
                                decorator.SLEEP), decorator.EPSILON)
        decorator.SLEEP = 0.25

    def test_incorrect_type_k(self):
        decorator.mean.time = []

        @decorator.mean("10")
        def new_foo(arg1):
            decorator.time.sleep(decorator.SLEEP)
            return arg1

        with self.assertRaises(TypeError):
            new_foo("Walter")

    def test_check_range_for_foo(self):
        k = 10
        decorator.mean.time = []
        for i in range(12):
            res = decorator.foo("Walter")
            if i < k:
                self.assertEqual(int(res[0][res[0].index(' '): -1]) -
                                 int(res[0][1:res[0].index(',')]), i + 1)
            else:
                self.assertEqual(int(res[0][res[0].index(' '): -1]) -
                                 int(res[0][1:res[0].index(',')]), k)

    def test_check_range_for_boo(self):
        decorator.mean.time = []
        for i in range(12):
            k = 2
            res = decorator.boo("Walter")
            if i < k:
                self.assertEqual(int(res[0][res[0].index(' '): -1]) -
                                 int(res[0][1:res[0].index(',')]), i + 1)
            else:
                self.assertEqual(int(res[0][res[0].index(' '): -1]) -
                                 int(res[0][1:res[0].index(',')]), k)


if __name__ == "__main__":
    unittest.main()
