import unittest
from unittest import mock
from unittest.mock import patch

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    def test_new_custom_list(self):
        list_a = CustomList([1, 2, 3])
        list_b = CustomList([1, 2, 3])
        res = CustomList([0, 0, 0])
        with mock.patch.object(list_a,
                               '_CustomList__new_custom_list',
                               return_value=res) as mock_foo:
            list_a + list_b
            mock_foo.assert_called_once()

    def test_add_less_len(self):

        res1 = CustomList([5, 1]) + CustomList([1, 2, 7])
        res2 = CustomList([1]) + [2, 5]
        res3 = [1] + CustomList([2, 5])

        self.assertEqual(str(res1), "CustomList: [6, 3, 7], sum: 16")
        self.assertEqual(str(res2), "CustomList: [3, 5], sum: 8")
        self.assertEqual(str(res3), "CustomList: [3, 5], sum: 8")

    def test_add_greater_len(self):

        res1 = CustomList([1, 2, 7]) + CustomList([5, 1])
        res2 = CustomList([2, 5]) + [1]
        res3 = [2, 5] + CustomList([1])

        self.assertEqual(str(res1), "CustomList: [6, 3, 7], sum: 16")
        self.assertEqual(str(res2), "CustomList: [3, 5], sum: 8")
        self.assertEqual(str(res3), "CustomList: [3, 5], sum: 8")

    def test_add_equal_len(self):

        res1 = CustomList([1, 2]) + CustomList([5, 1])
        res2 = CustomList([2, 5]) + [1, 2]
        res3 = [2, 5] + CustomList([1, 2])

        self.assertEqual(str(res1), "CustomList: [6, 3], sum: 9")
        self.assertEqual(str(res2), "CustomList: [3, 7], sum: 10")
        self.assertEqual(str(res3), "CustomList: [3, 7], sum: 10")

    def test_saved_items(self):
        list_a = CustomList([5, 1, 3, 7])
        list_b = CustomList([1, 2, 7])
        list_c = [1, 2]

        res11 = list_a + list_b
        res12 = list_c + list_a
        res21 = list_a - list_b
        res22 = list_c - list_b

        self.assertEqual(str(res11), "CustomList: [6, 3, 10, 7], sum: 26")
        self.assertEqual(str(res12), "CustomList: [6, 3, 3, 7], sum: 19")
        self.assertEqual(str(res21), "CustomList: [4, -1, -4, 7], sum: 6")
        self.assertEqual(str(res22), "CustomList: [0, 0, -7], sum: -7")

        """Check that the values of the lists are saved"""
        self.assertEqual(list_a, CustomList([5, 1, 3, 7]))
        self.assertEqual(list_b, CustomList([1, 2, 7]))
        self.assertEqual(list_c, [1, 2])

    def test_sub_less_len(self):

        res1 = CustomList([5, 1]) - CustomList([1, 2, 7])
        res2 = CustomList([1]) - [2, 5]
        res3 = [1] - CustomList([2, 5])

        self.assertEqual(str(res1), "CustomList: [4, -1, -7], sum: -4")
        self.assertEqual(str(res2), "CustomList: [-1, -5], sum: -6")
        self.assertEqual(str(res3), "CustomList: [-1, -5], sum: -6")

    def test_sub_greater_len(self):

        res1 = CustomList([1, 2, 7]) - CustomList([5, 1])
        res2 = CustomList([2, 5]) - [1]
        res3 = [2, 5] - CustomList([1])

        self.assertEqual(str(res1), "CustomList: [-4, 1, 7], sum: 4")
        self.assertEqual(str(res2), "CustomList: [1, 5], sum: 6")
        self.assertEqual(str(res3), "CustomList: [1, 5], sum: 6")

    def test_sub_equal_len(self):

        res1 = CustomList([1, 2]) - CustomList([5, 1])
        res2 = CustomList([2, 5]) - [1, 2]
        res3 = [2, 5] - CustomList([1, 2])

        self.assertEqual(str(res1), "CustomList: [-4, 1], sum: -3")
        self.assertEqual(str(res2), "CustomList: [1, 3], sum: 4")
        self.assertEqual(str(res3), "CustomList: [1, 3], sum: 4")

    @patch.object(CustomList, '__add__')
    def test_add_called(self, mock_foo):

        CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        CustomList([1]) + [2, 5]
        [2, 5] + CustomList([1])

        self.assertEqual(mock_foo.call_count, 3)

    @patch.object(CustomList, '__radd__')
    def test_radd_called(self, mock_foo):
        [2, 5] + CustomList([1])

        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__sub__')
    def test_sub_called(self, mock_foo):
        CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
        CustomList([1]) - [2, 5]
        [2, 5] - CustomList([1])

        self.assertEqual(mock_foo.call_count, 3)

    @patch.object(CustomList, '__rsub__')
    def test_rsub_called(self, mock_foo):
        [2, 5] - CustomList([1])

        self.assertEqual(mock_foo.call_count, 1)

    def test_eq(self):
        self.assertTrue(CustomList([1, 2, 3]) == CustomList([3, 2, 1]))

    def test_ne(self):
        self.assertTrue(CustomList([1, 2, 3]) != CustomList([3, 2, 0]))

    def test_lt(self):
        self.assertTrue(CustomList([1, 2, 3]) < CustomList([3, 2, 2]))

    def test_le(self):
        self.assertTrue(CustomList([1, 2, 3]) <= CustomList([3, 2, 2]))
        self.assertTrue(CustomList([1, 6]) <= CustomList([3, 2, 2]))

    def test_gt(self):
        self.assertTrue(CustomList([5, 2, 1]) > CustomList([3, 2, 2]))

    def test_ge(self):
        self.assertTrue(CustomList([2, 2, 3]) >= CustomList([3, 2, 2]))
        self.assertTrue(CustomList([4, 2, 2]) >= CustomList([3, 2, 2]))

    @patch.object(CustomList, '__eq__')
    def test_eq_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) == CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__ne__')
    def test_ne_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) != CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__lt__')
    def test_lt_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) < CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__le__')
    def test_lg_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) <= CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__gt__')
    def test_gt_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) > CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    @patch.object(CustomList, '__ge__')
    def test_ge_called(self, mock_foo):
        res = CustomList([5, 1, 3, 7]) >= CustomList([1, 2, 7])
        self.assertEqual(mock_foo.call_count, 1)

    def test_str_type(self):
        self.assertTrue(isinstance(str(CustomList([1, 2, 3])), str))

    def test_str_result(self):
        self.assertEqual(str(CustomList([1, 2, 3])),
                         "CustomList: [1, 2, 3], sum: 6")


if __name__ == "__main__":
    unittest.main()
