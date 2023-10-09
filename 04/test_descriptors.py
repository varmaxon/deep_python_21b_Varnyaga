"""TestModul for class Car containing descriptors"""

import unittest

from descriptors import Car


class TestCustomList(unittest.TestCase):
    """TestClass"""

    def test_correct_field(self):
        car1 = Car("BMW-Z4", 2, "A123AA777")
        car2 = Car("VW-passat CC", 5, "A001MP777")

        self.assertEqual(car1.brand, "BMW-Z4")
        self.assertEqual(car1.seats, 2)
        self.assertEqual(car1.gos_number, "A123AA777")

        self.assertEqual(car2.brand, "VW-passat CC")
        self.assertEqual(car2.seats, 5)
        self.assertEqual(car2.gos_number, "A001MP777")

    def test_str_object(self):
        car1 = Car("BMW-Z4", 2, "A123AA777")

        self.assertEqual(str(car1), "Car BMW (model: Z4) "
                                    "with A123AA777 gos-number has 2 seats")

    def test_incorrect_value_of_brand(self):
        with self.assertRaises(ValueError):
            Car("BMWZ4", 2, "A123AA777")

    def test_incorrect_value_of_seats(self):
        with self.assertRaises(ValueError):
            Car("BMW-Z4", 0, "A123AA777")

    def test_incorrect_value_of_gos_number(self):
        with self.assertRaises(ValueError):
            Car("BMW-Z4", 2, "A123AA7770")

    def test_incorrect_type_of_brand(self):
        with self.assertRaises(TypeError):
            Car(1, 2, "A123AA777")

    def test_incorrect_type_of_seats(self):
        with self.assertRaises(TypeError):
            Car("BMW-Z4", "0", "A123AA777")

    def test_incorrect_type_of_gos_number(self):
        with self.assertRaises(TypeError):
            Car("BMW-Z4", 2, 123)

    def test_change_values(self):
        car1 = Car("BMW-Z4", 2, "A123AA777")

        car1.brand = "VW-passat CC"
        car1.seats = 5
        car1.gos_number = "A001MP777"

        self.assertNotEqual(car1.brand, "BMW-Z4")
        self.assertNotEqual(car1.seats, 2)
        self.assertNotEqual(car1.gos_number, "A123AA777")

        self.assertEqual(car1.brand, "VW-passat CC")
        self.assertEqual(car1.seats, 5)
        self.assertEqual(car1.gos_number, "A001MP777")

    def test_change_types(self):
        car1 = Car("BMW-Z4", 2, "A123AA777")

        with self.assertRaises(TypeError):
            car1.brand = list(car1.brand)

        with self.assertRaises(TypeError):
            car1.seats = "5"

        with self.assertRaises(TypeError):
            car1.gos_number = list("A001MP777")

        self.assertEqual(car1.brand, "BMW-Z4")
        self.assertEqual(car1.seats, 2)
        self.assertEqual(car1.gos_number, "A123AA777")


if __name__ == "__main__":
    unittest.main()
