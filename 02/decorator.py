import time


def mean(k):
    def decorator(func):
        arr_time = []

        def wrapper(arg, *args, **kwargs):
            if not isinstance(k, int):
                raise TypeError('the parameter K must be of type integer')

            start = time.time()
            func_result = func(arg, *args, **kwargs)
            result = time.time() - start
            arr_time.append(result)

            if 0 < len(arr_time) < k:
                print(sum(arr_time) / len(arr_time))

            if len(arr_time) >= k:
                print(sum(arr_time[len(arr_time) - k: len(arr_time)]) / k)

            return func_result

        return wrapper

    return decorator


SLEEP = 0.25


@mean(10)
def foo(arg1):
    time.sleep(SLEEP)
    return arg1


@mean(2)
def boo(arg1):
    time.sleep(SLEEP)
    return arg1
