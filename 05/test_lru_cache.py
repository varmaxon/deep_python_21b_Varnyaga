"""TestModul for class LRUCache"""

import unittest

from lru_cache import LRUCache


class TestCustomList(unittest.TestCase):
    """TestClass"""

    def test_unknown_key(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), None)

    def test_set_get_elements_less_cache_capacity(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        self.assertEqual(cache.get("k1"), "val1")

    def test_set_get_elements_equal_cache_capacity(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), None)

        new_cache = LRUCache(1000)
        for key in range(1000):
            new_cache.set("k" + str(key), "val" + str(key))
        for key in range(1000):
            self.assertEqual(new_cache.get("k" + str(key)), "val" + str(key))

    def test_set_get_elements_more_cache_capacity(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k4"), None)

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k4"), None)

        cache.set("k4", "val4")
        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k4"), "val4")

        new_cache = LRUCache(999)
        for key in range(1000):
            new_cache.set("k" + str(key), "val" + str(key))
        self.assertEqual(new_cache.get("k0"), None)
        self.assertEqual(new_cache.get("k1"), "val1")
        self.assertEqual(new_cache.get("k999"), "val999")

    def test_change_priority_with_get(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        cache.get("k1")

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k3"), "val3")

        new_cache = LRUCache(999)
        for key in range(999):
            new_cache.set("k" + str(key), "val" + str(key))

        new_cache.get("k0")

        new_cache.set("k999", "val999")

        self.assertEqual(new_cache.get("k0"), "val0")
        self.assertEqual(new_cache.get("k1"), None)
        self.assertEqual(new_cache.get("k999"), "val999")

    def test_new_value(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        cache.set("k1", "val10")

        cache.set("k3", "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val10")
        self.assertEqual(cache.get("k3"), "val3")

    def test_add_existing_element(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k2", "val3")
        cache.set("k4", "val4")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val3")
        self.assertEqual(cache.get("k4"), "val4")

    def test_set_first_element(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

    def test_zero_and_one_capacity(self):
        cache = LRUCache(0)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), None)

        cache = LRUCache(1)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")


if __name__ == "__main__":
    unittest.main()
