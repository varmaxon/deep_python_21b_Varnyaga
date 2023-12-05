"""TestModul for meta-class CustomMeta"""

import unittest

from metaclass import CustomMeta


class CustomClass(metaclass=CustomMeta):
    """class inherited from CustomMeta"""

    x = 50

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestCustomList(unittest.TestCase):
    """TestClass"""

    def test_old_attributes(self):
        obj = CustomClass()

        # for class attributes
        self.assertNotIn('x', CustomClass.__dict__)
        self.assertNotIn('line', CustomClass.__dict__)
        self.assertNotIn('val', CustomClass.__dict__)
        self.assertNotIn('yyy', CustomClass.__dict__)

        # for object attributes
        self.assertFalse(hasattr(obj, 'x'))
        self.assertFalse(hasattr(obj, 'line'))
        self.assertFalse(hasattr(obj, 'val'))
        self.assertFalse(hasattr(obj, 'yyy'))

    def test_new_attributes(self):
        obj = CustomClass()

        # for class attributes
        self.assertIn('custom_x', CustomClass.__dict__)
        self.assertEqual(CustomClass.custom_x, 50)

        self.assertIn('custom_line', CustomClass.__dict__)
        self.assertEqual(CustomClass.custom_line(), 100)

        self.assertIn('__str__', CustomClass.__dict__)
        self.assertEqual(str(obj), "Custom_by_metaclass")

        # for object attributes
        self.assertTrue(hasattr(obj, 'custom_x'))
        self.assertEqual(obj.custom_x, 50)

        self.assertTrue(hasattr(obj, 'custom_line'))
        self.assertEqual(obj.custom_line(), 100)

        self.assertTrue(hasattr(obj, 'custom_val'))
        self.assertIn('custom_val', obj.__dict__)
        self.assertEqual(obj.custom_val, 99)

        self.assertEqual(str(obj), "Custom_by_metaclass")

    def test_not_changed_magic_methods(self):
        obj = CustomClass()

        # for class attributes
        self.assertIn('__init__', CustomClass.__dict__)
        self.assertIn('__str__', CustomClass.__dict__)
        self.assertIn('__setattr__', CustomClass.__dict__)
        self.assertIn('__dict__', CustomClass.__dict__)

        # for object attributes
        self.assertTrue(hasattr(obj, '__init__'))
        self.assertTrue(hasattr(obj, '__str__'))
        self.assertTrue(hasattr(obj, '__setattr__'))
        self.assertTrue(hasattr(obj, '__dict__'))

    def test_dynamic_fields(self):
        obj = CustomClass()
        obj.dynamic = "added later"
        self.assertFalse(hasattr(obj, 'dynamic'))
        self.assertTrue(hasattr(obj, 'custom_dynamic'))
        self.assertEqual(obj.custom_dynamic, "added later")

    def test_dynamic_methods(self):
        obj = CustomClass()

        def foo(val):
            return val * 100

        obj.dynamic_method = foo

        self.assertFalse(hasattr(obj, 'dynamic_method'))
        self.assertTrue(hasattr(obj, 'custom_dynamic_method'))
        self.assertEqual(obj.custom_dynamic_method(0.5), 50)

    def test_delete_custom_attributes(self):
        obj = CustomClass()
        self.assertTrue(hasattr(obj, 'custom_val'))
        del obj.custom_val
        self.assertFalse(hasattr(obj, 'custom_val'))


if __name__ == "__main__":
    unittest.main()
