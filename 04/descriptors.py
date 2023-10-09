"""Modul with class Car containing descriptors"""

from abc import abstractmethod, ABC


class Descriptor(ABC):
    """Abstract base class for descriptors"""

    @abstractmethod
    def check_validation(self, val):
        """abstract method for validation of entering data"""

    def __get__(self, obj, obj_type):
        # print("get", obj.__class__.__name__)
        if obj is None:
            return None

        return getattr(obj, self.name)

    def __set__(self, obj, val):
        # print(f"set '{val}'")
        if obj is None:
            return None

        if self.check_validation(val):
            return setattr(obj, self.name, val)

        raise ValueError(f"incorrect value of {self.name}")

    def __set_name__(self, owner, name):
        self.name = f"int_descr_{name}"
        # print(f"set_name '{name}' of '{owner.__name__}'")


class Brand(Descriptor):
    """Descriptor Brand"""

    def check_validation(self, val):
        if not isinstance(val, str):
            raise TypeError("int required")

        if '-' in val:
            return True

        raise ValueError("incorrect model name")


class Seats(Descriptor):
    """Descriptor Seats"""

    def check_validation(self, val):
        if not isinstance(val, int):
            raise TypeError("int required")

        if 0 < val < 10:
            return True
        raise ValueError("incorrect number of seats")


class GosNumber(Descriptor):
    """Descriptor GosNumber"""

    def check_validation(self, val):
        if not isinstance(val, str):
            raise TypeError("int required")

        if len(val) == 9 and \
                val[0].isalpha() and \
                val[1:4].isdigit() and \
                val[4:6].isalpha() and val[6:-1].isdigit():
            return True

        raise ValueError("incorrect gos number")


class Car:
    """class Car with descriptors-fields"""

    brand = Brand()
    seats = Seats()
    gos_number = GosNumber()

    def __init__(self, brand_, seats_, gos_number_):
        self.brand = brand_
        self.seats = seats_
        self.gos_number = gos_number_

    def __str__(self):
        idx = self.brand.index('-')
        return f"Car {self.brand[:idx]} (model: {self.brand[idx + 1:]}) " \
               f"with {self.gos_number} gos-number " \
               f"has {self.seats} seats"
