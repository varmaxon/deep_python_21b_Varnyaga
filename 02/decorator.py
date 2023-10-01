import time


def mean(k):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(k, int):
                raise TypeError('the parameter K must be of type integer')

            start = time.time()
            func(arg)
            result = time.time() - start
            mean.time.append(result)

            if 0 < len(mean.time) < k:
                return f"[0, {len(mean.time)})",\
                    sum(mean.time) / len(mean.time)

            if len(mean.time) >= k:
                return f"[{len(mean.time) - k}, {len(mean.time)})", \
                    sum(mean.time[len(mean.time) - k: len(mean.time)]) / k

        return wrapper

    return decorator


mean.time = []
SLEEP = 0.25
EPSILON = 0.5


@mean(10)
def foo(arg1):
    time.sleep(SLEEP)
    return arg1


@mean(2)
def boo(arg1):
    time.sleep(SLEEP)
    return arg1
