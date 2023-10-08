"""Modul with class CustomList"""


class CustomList(list):
    """Class CustomList"""

    def __new_custom_list(self, other):
        custom_list = CustomList([0] * max(len(self), len(other)))
        return custom_list

    def __add__(self, other):
        result_list = self.__new_custom_list(other)

        for i, val in enumerate(result_list):
            result_list[i] = self[i] if i < len(self) else val
            result_list[i] += other[i] if i < len(other) else val

        return result_list

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        result_list = self.__new_custom_list(other)

        for i, val in enumerate(result_list):
            result_list[i] = self[i] if i < len(self) else val
            result_list[i] -= other[i] if i < len(other) else val

        return result_list

    def __rsub__(self, other):
        return CustomList(map(lambda x: x * -1, self.__sub__(other)))

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f"CustomList: {super().__str__()}, sum: {sum(self)}"
