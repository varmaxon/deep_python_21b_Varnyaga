import weakref
from time import time
import cProfile
import pstats
import io
from memory_profiler import profile


class Param:
    def __init__(self, value):
        self.value = value


class CarUsually:
    def __init__(self, x_param: Param, y_param: Param, z_param: Param):
        self.x_param = x_param
        self.y_param = y_param
        self.z_param = z_param


class CarSlot:
    __slots__ = ("x_param", "y_param", "z_param")

    def __init__(self, x_param: Param, y_param: Param, z_param: Param):
        self.x_param = x_param
        self.y_param = y_param
        self.z_param = z_param


class CarWeakRef:
    def __init__(self, x_param: Param, y_param: Param, z_param: Param):
        self.x_param = weakref.ref(x_param) if x_param is not None else x_param
        self.y_param = weakref.ref(y_param) if y_param is not None else y_param
        self.z_param = weakref.ref(z_param) if z_param is not None else z_param


def time_of_creating(class_name, size):
    start = time()
    complete_list = [class_name(Param(1), Param(2), Param(3)) for _ in range(size)]
    return round(time() - start, 3), complete_list


def time_of_changing(list_objects):
    start = time()
    for obj in list_objects:
        obj.x_param = Param(4)
        obj.y_param = Param(5)
        obj.z_param = Param(6)
    return round(time() - start, 3)


@profile
def calc_memory_usual():
    time_of_creating(class_name=CarUsually, size=CNT_OBJECTS)


@profile
def calc_memory_slots():
    time_of_creating(class_name=CarSlot, size=CNT_OBJECTS)


@profile
def calc_memory_weak_ref():
    time_of_creating(class_name=CarWeakRef, size=CNT_OBJECTS)


if __name__ == "__main__":
    CNT_OBJECTS = 1_000_000
    pr = cProfile.Profile()

    # Create objects
    print("Time of creating:")
    pr.enable()
    time_create_u_cars, list_usually_cars = time_of_creating(class_name=CarUsually, size=CNT_OBJECTS)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('default attributes')
    print(s.getvalue())
    # print(" - CarUsually", time_create_u_cars)

    pr = cProfile.Profile()
    pr.enable()
    time_create_s_cars, list_slots_cars = time_of_creating(class_name=CarSlot, size=CNT_OBJECTS)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('slots')
    print(s.getvalue())
    # print(" - CarSlot", time_create_s_cars)

    pr = cProfile.Profile()
    pr.enable()
    time_create_w_cars, list_weak_cars = time_of_creating(class_name=CarWeakRef, size=CNT_OBJECTS)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('weak_ref')
    print(s.getvalue())
    # print(" - CarWeakRef", time_create_w_cars)

    # Change attr
    print("\nTime of changing:")
    pr = cProfile.Profile()
    pr.enable()
    time_change_u_cars = time_of_changing(list_usually_cars)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('default attributes')
    print(s.getvalue())
    # print(" - CarUsually", time_change_u_cars)

    pr = cProfile.Profile()
    pr.enable()
    time_change_s_cars = time_of_changing(list_slots_cars)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('slots')
    print(s.getvalue())
    # print(" - CarSlot", time_change_s_cars)

    pr = cProfile.Profile()
    pr.enable()
    time_change_w_cars = time_of_changing(list_weak_cars)
    pr.disable()
    s = io.StringIO()
    SORT_BY = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(SORT_BY)
    ps.print_stats()
    print('weak_ref')
    print(s.getvalue())
    # print(" - CarWeakRef", time_change_w_cars)

    # memory_profile
    calc_memory_usual()
    calc_memory_slots()
    calc_memory_weak_ref()
