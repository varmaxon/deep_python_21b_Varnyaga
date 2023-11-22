import unittest
from unittest import mock
from unittest.mock import patch

from custom_list import CustomList


class TestCustomList(unittest.TestCase):

    @staticmethod
    def compare_lists(list_a, list_b) -> bool:
        if len(list_a) != len(list_b):
            return False

        for i in range(len(list_a)):
            if list_a[i] != list_b[i]:
                return False

        return True

    def test_new_custom_list(self):
        list_a = CustomList([1, 2, 3])
        a_cp = list_a.copy()
        list_b = CustomList([1, 2, 3])
        b_cp = list_a.copy()
        res = CustomList([0, 0, 0])
        with mock.patch.object(list_a,
                               '_CustomList__new_custom_list',
                               return_value=res) as mock_foo:
            list_a + list_b
            mock_foo.assert_called_once()

        # проверим неизменность списков после операций
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))

    def test_add_less_len(self):
        list_a, list_b = CustomList([5, 1]), CustomList([1, 2, 7])
        list_c, list_d = CustomList([1]), CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        c_cp, d_cp = list_c.copy(), list_d.copy()

        res1 = list_a + list_b
        res2 = list_c + [2, 5]
        res3 = [1] + list_d

        self.assertTrue(self.compare_lists(res1, [6, 3, 7]))
        self.assertTrue(self.compare_lists(res2, [3, 5]))
        self.assertTrue(self.compare_lists(res3, [3, 5]))

        # проверим неизменность списков после операций
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

    def test_add_greater_len(self):
        list_a, list_b = CustomList([1, 2, 7]), CustomList([5, 1])
        list_c, list_d = CustomList([1]), CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        c_cp, d_cp = list_c.copy(), list_d.copy()

        res1 = list_a + list_b
        res2 = list_d + [1]
        res3 = [2, 5] + list_c

        self.assertTrue(self.compare_lists(res1, [6, 3, 7]))
        self.assertTrue(self.compare_lists(res2, [3, 5]))
        self.assertTrue(self.compare_lists(res3, [3, 5]))

        # проверим неизменность списков после операций
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

    def test_add_equal_len(self):
        list_a, list_b = CustomList([1, 2]), CustomList([5, 1])
        list_c, list_d = CustomList([1, 2]), CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        c_cp, d_cp = list_c.copy(), list_d.copy()

        res1 = list_a + list_b
        res2 = list_d + [1, 2]
        res3 = [2, 5] + list_c

        self.assertTrue(self.compare_lists(res1, [6, 3]))
        self.assertTrue(self.compare_lists(res2, [3, 7]))
        self.assertTrue(self.compare_lists(res3, [3, 7]))

        # проверим неизменность списков после операций
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

    def test_saved_items(self):
        list_a, list_b, list_c = CustomList([5, 1, 3, 7]), CustomList([1, 2, 7]), [1, 2]
        a_cp, b_cp, c_cp = list_a.copy(), list_b.copy(), list_c.copy()

        res1 = list_a + list_b
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))

        res2 = list_c + list_a
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))

        res3 = list_a - list_b
        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))

        res4 = list_c - list_b
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))

        # проверка результатов операций
        self.assertTrue(self.compare_lists(res1, [6, 3, 10, 7]))
        self.assertTrue(self.compare_lists(res2, [6, 3, 3, 7]))
        self.assertTrue(self.compare_lists(res3, [4, -1, -4, 7]))
        self.assertTrue(self.compare_lists(res4, [0, 0, -7]))

    def test_sub_less_len(self):
        list_a, list_b = CustomList([5, 1]), CustomList([1, 2, 7])
        list_c, list_d = CustomList([1]), CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        c_cp, d_cp = list_c.copy(), list_d.copy()

        res1 = list_a - list_b
        res2 = list_c - [2, 5]
        res3 = [1] - list_d

        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

        self.assertTrue(self.compare_lists(res1, [4, -1, -7]))
        self.assertTrue(self.compare_lists(res2, [-1, -5]))
        self.assertTrue(self.compare_lists(res3, [-1, -5]))

    def test_sub_greater_len(self):
        list_a, list_b = CustomList([1, 2, 7]), CustomList([5, 1])
        list_c, list_d = CustomList([1]), CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        c_cp, d_cp = list_c.copy(), list_d.copy()

        res1 = list_a - list_b
        res2 = list_d - [1]
        res3 = [2, 5] - list_c

        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_c, c_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

        self.assertTrue(self.compare_lists(res1, [-4, 1, 7]))
        self.assertTrue(self.compare_lists(res2, [1, 5]))
        self.assertTrue(self.compare_lists(res3, [1, 5]))

    def test_sub_equal_len(self):
        list_a, list_b = CustomList([1, 2]), CustomList([5, 1])
        list_d = CustomList([2, 5])
        a_cp, b_cp = list_a.copy(), list_b.copy()
        d_cp = list_d.copy()

        res1 = list_a - list_b
        res2 = list_d - [1, 2]
        res3 = [2, 5] - list_a

        self.assertTrue(self.compare_lists(list_a, a_cp))
        self.assertTrue(self.compare_lists(list_b, b_cp))
        self.assertTrue(self.compare_lists(list_d, d_cp))

        self.assertTrue(self.compare_lists(res1, [-4, 1]))
        self.assertTrue(self.compare_lists(res2, [1, 3]))
        self.assertTrue(self.compare_lists(res3, [1, 3]))

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
