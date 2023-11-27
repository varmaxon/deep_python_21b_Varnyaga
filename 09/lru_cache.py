import argparse
import my_logging


class DictElement:
    """Element of dictionary"""

    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.next = None
        self.prev = None

    def get_key(self):
        return self.__key

    def get_val(self):
        return self.__value

    def set_val(self, val):
        self.__value = val


class LRUCache:
    """LRU cache with dictionary"""

    def __init__(self, limit=42):
        self.__limit = limit
        self.__cache_dict = {}
        self.__first = None
        self.__last = None
        logger.debug(
            "Cache %s is created with limit %s",
            self,
            self.__limit
        )

    def get(self, key):
        if key not in self.__cache_dict:
            logger.warning(
                "Command get:\tkey %s not found in cache",
                key
            )
            return None

        logger.info(
            "Command get:\tkey %s is found in cache",
            key
        )
        elem = self.__cache_dict[key]
        self.__set_back(elem)
        return elem.get_val()

    def set(self, key, value):
        if key not in self.__cache_dict:
            if len(self.__cache_dict) == self.__limit:
                if self.__first is None:
                    return

                del self.__cache_dict[self.__first.get_key()]

                if self.__first == self.__last:
                    self.__first = self.__last = None
                else:
                    self.__first = self.__first.next
                    del self.__first.prev
                    self.__first.prev = None

            new_el = DictElement(key, value)
            self.__cache_dict[key] = new_el
            self.__push_back(new_el)
            logger.info(
                "Command set:\tnew key %s with value %s",
                key,
                value
            )

        else:
            elem = self.__cache_dict[key]
            elem.set_val(value)
            logger.info(
                "Command set:\tvalue with key %s was changed to %s",
                key,
                value
            )
            self.__set_back(elem)

    def __set_back(self, elem):
        if self.__last == elem:
            # set the last element
            logger.debug(
                "Element %s is already the last",
                elem
            )
            return

        if self.__first == elem:
            # set the first element
            self.__first = elem.next
            self.__first.prev = None
        else:
            # set the middle element
            elem.next.prev = elem.prev
            elem.prev.next = elem.next
        elem.next = None
        elem.prev = self.__last
        self.__last.next = elem
        self.__last = elem
        logger.debug(
            "Element %s has been successfully moved to the last",
            elem
        )

    def __push_back(self, new_el):
        if self.__last is None:
            self.__last = self.__first = new_el
        else:
            new_el.prev = self.__last
            self.__last.next = new_el
            self.__last = new_el

        logger.debug(
            "Add new element %s to back",
            new_el
        )


def run():
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")

    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse input string')
    parser.add_argument("-s", action="store_true")
    parser.add_argument("-f", action="store_true")
    args = parser.parse_args()

    logger = my_logging.create_logger()

    if args.s:
        logger = my_logging.create_stream_logger(logger)

    if args.f:
        logger = my_logging.create_filter(logger)

    run()
