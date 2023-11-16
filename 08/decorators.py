import cProfile
import pstats
import io


def profile_deco(foo):
    pr = cProfile.Profile()

    def wrapper(*args, **kwargs):
        pr.enable()
        res = foo(*args, **kwargs)
        pr.disable()
        return res

    def print_profile():
        s = io.StringIO()
        sort_by = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sort_by)
        ps.print_stats()
        print(s.getvalue())

    wrapper.print_stat = print_profile
    return wrapper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


for i in range(1_000_000):
    add(1, 2)
    add(4, 5)
    sub(4, 5)

add.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции add (всего два вызова)
sub.print_stat()  # выводится результат профилирования суммарно по всем вызовам функции sub (всего один вызов)
